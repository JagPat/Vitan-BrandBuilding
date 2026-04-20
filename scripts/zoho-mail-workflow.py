#!/usr/bin/env python3
"""Layer-1 Zoho mail workflow with board-bypass awareness detection.

This script intentionally separates message ingestion from classification so it can
run against either a live Zoho source or a local fixture file.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import getaddresses, parsedate_to_datetime
from pathlib import Path
from typing import Iterable, Sequence

import requests


BOARD_BYPASS_DETECTION_ENABLED = os.getenv("BOARD_BYPASS_DETECTION_ENABLED", "1") == "1"

BOARD_SENDERS = {
    "jp@vitan.in",
    "kaivana@vitan.in",
    "chitrang@vitan.in",
}
BOARD_GROUP_ADDRESSES = {"board@vitan.in"}
PA_EMAIL_ALIASES = {"growthos+pa@vitan.in", "pa@vitan.in"}
AGENT_EMAIL_MAP = {
    "growthos+pa@vitan.in": "PA",
    "growthos+hr@vitan.in": "HR",
    "growthos+fe@vitan.in": "FE",
    "growthos+bb@vitan.in": "BB",
    "growthos+bs@vitan.in": "BS",
    "growthos+dpm@vitan.in": "DPM",
    "growthos+oc@vitan.in": "OC",
}

LOG_PATH = Path(os.getenv("BOARD_BYPASS_LOG_PATH", "/app/shared-workspace/board-bypass-log.jsonl"))

ZOHO_ACCOUNTS_URL = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2/token")
ZOHO_MAIL_MESSAGES_URL = os.getenv("ZOHO_MAIL_MESSAGES_URL", "")
ZOHO_SENT_FOLDER_URL = os.getenv("ZOHO_SENT_FOLDER_URL", "")
ZOHO_MAIL_API_BASE_URL = os.getenv("ZOHO_MAIL_API_BASE_URL", "https://mail.zoho.in/api")
ZOHO_MAIL_MESSAGES_LIMIT = os.getenv("ZOHO_MAIL_MESSAGES_LIMIT", "20")
ZOHO_THREAD_ROOT_URL_TEMPLATE = os.getenv("ZOHO_THREAD_ROOT_URL_TEMPLATE", "")

PAPERCLIP_API_URL = os.getenv("PAPERCLIP_API_URL", "")
PAPERCLIP_API_KEY = os.getenv("PAPERCLIP_API_KEY", "")
PAPERCLIP_COMPANY_ID = os.getenv("PAPERCLIP_COMPANY_ID", "")
PA_AGENT_ID = os.getenv("PA_AGENT_ID", "")


@dataclass
class Message:
    message_id: str
    thread_id: str
    sender: str
    to: list[str]
    cc: list[str]
    bcc: list[str]
    subject: str
    snippet: str
    zoho_thread_link: str


def canonical_email(value: str) -> str:
    return value.strip().lower()


def normalize_recipients(values: Sequence[str]) -> list[str]:
    addresses = [addr for _, addr in getaddresses(values) if addr]
    return sorted({canonical_email(addr) for addr in addresses})


def all_recipients(message: Message) -> list[str]:
    return sorted(set(message.to + message.cc + message.bcc))


def sender_is_board(sender: str) -> bool:
    normalized = canonical_email(sender)
    return normalized in BOARD_SENDERS or normalized in BOARD_GROUP_ADDRESSES


def targeted_agents(recipients: Iterable[str]) -> list[str]:
    found = sorted({AGENT_EMAIL_MAP[r] for r in recipients if r in AGENT_EMAIL_MAP and AGENT_EMAIL_MAP[r] != "PA"})
    return found


def is_board_bypass(
    sender: str,
    recipients: Sequence[str],
    thread_root_recipients: Sequence[str],
) -> tuple[bool, list[str]]:
    """Return (is_bypass, targeted_agents)."""
    normalized_recipients = {canonical_email(r) for r in recipients}
    normalized_root = {canonical_email(r) for r in thread_root_recipients}

    if not sender_is_board(sender):
        return False, []

    agents = targeted_agents(normalized_recipients)
    if not agents:
        return False, []

    if PA_EMAIL_ALIASES.intersection(normalized_recipients):
        return False, []

    if PA_EMAIL_ALIASES.intersection(normalized_root):
        return False, []

    return True, agents


def get_access_token() -> str:
    required = ["ZOHO_REFRESH_TOKEN", "ZOHO_CLIENT_ID", "ZOHO_CLIENT_SECRET"]
    missing = [var for var in required if not os.getenv(var)]
    if missing:
        raise RuntimeError(f"Missing required env vars: {', '.join(missing)}")

    resp = requests.post(
        ZOHO_ACCOUNTS_URL,
        data={
            "refresh_token": os.environ["ZOHO_REFRESH_TOKEN"],
            "client_id": os.environ["ZOHO_CLIENT_ID"],
            "client_secret": os.environ["ZOHO_CLIENT_SECRET"],
            "grant_type": "refresh_token",
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    token = data.get("access_token")
    if not token:
        raise RuntimeError(f"Zoho token response missing access_token: {data}")
    return token


def resolve_messages_url() -> str:
    if ZOHO_MAIL_MESSAGES_URL:
        return ZOHO_MAIL_MESSAGES_URL

    account_id = os.getenv("ZOHO_MAIL_ACCOUNT_ID", "").strip()
    folder_id = os.getenv("ZOHO_MAIL_INBOX_FOLDER_ID", "").strip()
    if not account_id or not folder_id:
        return ""

    return (
        f"{ZOHO_MAIL_API_BASE_URL.rstrip('/')}/accounts/{account_id}/messages/view"
        f"?folderId={folder_id}&limit={ZOHO_MAIL_MESSAGES_LIMIT}"
    )


def fetch_messages() -> list[Message]:
    fixture_path = os.getenv("ZOHO_MESSAGES_FILE", "")
    if fixture_path:
        raw = json.loads(Path(fixture_path).read_text(encoding="utf-8"))
        return [message_from_dict(item) for item in raw]

    messages_url = resolve_messages_url()
    if not messages_url:
        return []

    token = get_access_token()
    resp = requests.get(
        messages_url,
        headers={"Authorization": f"Zoho-oauthtoken {token}"},
        timeout=60,
    )
    resp.raise_for_status()
    payload = resp.json()
    if isinstance(payload, dict):
        items = payload.get("messages") or payload.get("data") or []
    else:
        items = payload if isinstance(payload, list) else []
    return [message_from_dict(item) for item in items]


def parse_timestamp(value: object) -> datetime | None:
    if value in (None, ""):
        return None

    if isinstance(value, datetime):
        dt = value
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    if isinstance(value, (int, float)):
        ts = float(value)
        if ts > 1e12:
            ts = ts / 1000.0
        return datetime.fromtimestamp(ts, tz=timezone.utc)

    if isinstance(value, str):
        raw = value.strip()
        if not raw:
            return None
        if raw.isdigit():
            return parse_timestamp(int(raw))
        try:
            return datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(timezone.utc)
        except ValueError:
            pass
        try:
            return parsedate_to_datetime(raw).astimezone(timezone.utc)
        except (TypeError, ValueError):
            return None

    return None


def extract_sent_timestamp(item: dict) -> datetime | None:
    for key in (
        "timestamp",
        "sent_at",
        "sentAt",
        "sent_time",
        "sentTime",
        "date",
        "created_time",
        "createdTime",
        "time",
    ):
        parsed = parse_timestamp(item.get(key))
        if parsed:
            return parsed
    return None


def normalize_snippet(raw: object, limit: int = 200) -> str:
    text = re.sub(r"\s+", " ", str(raw or "")).strip()
    return text[:limit]


def fetch_sent_items() -> list[dict]:
    fixture_path = os.getenv("ZOHO_SENT_MESSAGES_FILE", "") or os.getenv("ZOHO_MESSAGES_FILE", "")
    if fixture_path:
        payload = json.loads(Path(fixture_path).read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            return payload.get("messages", payload.get("data", []))
        return payload if isinstance(payload, list) else []

    sent_url = os.getenv("ZOHO_SENT_FOLDER_URL", ZOHO_SENT_FOLDER_URL)
    if not sent_url:
        return []

    token = get_access_token()
    resp = requests.get(
        sent_url,
        headers={"Authorization": f"Zoho-oauthtoken {token}"},
        timeout=60,
    )
    resp.raise_for_status()
    payload = resp.json()
    if isinstance(payload, dict):
        return payload.get("messages", payload.get("data", []))
    return payload if isinstance(payload, list) else []


def list_sent_messages(hours: int) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=max(hours, 0))
    items = fetch_sent_items()
    rows: list[dict] = []

    for item in items:
        if not isinstance(item, dict):
            continue
        sent_at = extract_sent_timestamp(item)
        if sent_at and sent_at < cutoff:
            continue
        rows.append(
            {
                "from": canonical_email(item.get("from") or item.get("sender") or item.get("fromAddress") or ""),
                "subject": (item.get("subject") or "(no subject)").strip(),
                "timestamp": sent_at.isoformat() if sent_at else "",
                "body_snippet": normalize_snippet(
                    item.get("body_snippet")
                    or item.get("snippet")
                    or item.get("preview")
                    or item.get("content")
                    or item.get("body")
                ),
            }
        )

    rows.sort(key=lambda row: row.get("timestamp") or "", reverse=True)
    return rows


def fetch_thread_root_recipients(message: Message) -> list[str]:
    if message.thread_id and ZOHO_THREAD_ROOT_URL_TEMPLATE:
        token = get_access_token()
        url = ZOHO_THREAD_ROOT_URL_TEMPLATE.format(thread_id=message.thread_id)
        resp = requests.get(
            url,
            headers={"Authorization": f"Zoho-oauthtoken {token}"},
            timeout=60,
        )
        resp.raise_for_status()
        payload = resp.json()
        root = payload.get("root", payload)
        return normalize_recipients(root.get("to", []) + root.get("cc", []) + root.get("bcc", []))
    return []


def message_from_dict(item: dict) -> Message:
    sender = item.get("from") or item.get("sender") or ""
    to = normalize_recipients(item.get("to", []))
    cc = normalize_recipients(item.get("cc", []))
    bcc = normalize_recipients(item.get("bcc", []))

    return Message(
        message_id=item.get("message_id") or item.get("messageId") or "",
        thread_id=item.get("thread_id") or item.get("threadId") or "",
        sender=canonical_email(sender),
        to=to,
        cc=cc,
        bcc=bcc,
        subject=(item.get("subject") or "(no subject)").strip(),
        snippet=(item.get("snippet") or item.get("preview") or "").strip(),
        zoho_thread_link=item.get("thread_link") or item.get("zoho_thread_link") or "",
    )


def already_logged(message_id: str) -> bool:
    if not message_id or not LOG_PATH.exists():
        return False

    with LOG_PATH.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("message_id") == message_id:
                return True
    return False


def log_bypass(entry: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=True) + "\n")


def build_issue_body(message: Message, agents: Sequence[str]) -> str:
    preview = re.sub(r"\s+", " ", message.snippet).strip()[:500]
    recipients = ", ".join(all_recipients(message))
    agent_list = ", ".join(agents)
    return "\n".join(
        [
            "## BOARD AWARENESS (Layer 1)",
            "",
            "Board-origin email reached an agent route without PA on recipients.",
            "",
            f"- Sender: `{message.sender}`",
            f"- Subject: `{message.subject}`",
            f"- Targeted Agents: `{agent_list}`",
            f"- Recipients: `{recipients}`",
            f"- Message-ID: `{message.message_id}`",
            f"- Thread Link: {message.zoho_thread_link or '(unavailable)' }",
            "",
            "### Preview",
            "",
            preview or "(no preview)",
        ]
    )


def create_paperclip_board_awareness_issue(message: Message, agents: Sequence[str]) -> str:
    required = {
        "PAPERCLIP_API_URL": PAPERCLIP_API_URL,
        "PAPERCLIP_API_KEY": PAPERCLIP_API_KEY,
        "PAPERCLIP_COMPANY_ID": PAPERCLIP_COMPANY_ID,
        "PA_AGENT_ID": PA_AGENT_ID,
    }
    missing = [k for k, v in required.items() if not v]
    if missing:
        raise RuntimeError(f"Missing Paperclip configuration: {', '.join(missing)}")

    title = f"[BOARD AWARENESS] Board-bypass email -> {', '.join(agents)} - {message.subject}"
    payload = {
        "title": title,
        "description": build_issue_body(message, agents),
        "priority": "high",
        "status": "todo",
        "assigneeAgentId": PA_AGENT_ID,
        "labels": ["board-bypass", "layer-1", "auto"],
    }

    resp = requests.post(
        f"{PAPERCLIP_API_URL}/api/companies/{PAPERCLIP_COMPANY_ID}/issues",
        headers={
            "Authorization": f"Bearer {PAPERCLIP_API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return str(data.get("identifier") or data.get("id") or "")


def process_incoming_message(message: Message) -> bool:
    if not BOARD_BYPASS_DETECTION_ENABLED:
        return False

    if not message.message_id:
        return False

    if already_logged(message.message_id):
        return False

    recipients = all_recipients(message)
    root_recipients = fetch_thread_root_recipients(message)
    bypass, agents = is_board_bypass(message.sender, recipients, root_recipients)
    if not bypass:
        return False

    issue_id = create_paperclip_board_awareness_issue(message, agents)
    print(f"board-bypass detected: {message.sender} -> {agents} (issue={issue_id})")

    log_bypass(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "message_id": message.message_id,
            "thread_id": message.thread_id,
            "sender": message.sender,
            "subject": message.subject,
            "targeted_agents": agents,
            "issue": issue_id,
            "recipients": recipients,
            "root_recipients": root_recipients,
            "thread_link": message.zoho_thread_link,
        }
    )
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Zoho mail workflow")
    subparsers = parser.add_subparsers(dest="command")

    list_sent_parser = subparsers.add_parser("list-sent", help="List sent messages as JSON")
    list_sent_parser.add_argument("--hours", type=int, default=24, help="Lookback window in hours (default: 24)")
    subparsers.add_parser("detect-board-bypass", help="Run board bypass detection")
    subparsers.add_parser("process-inbox", help="Backward-compatible alias for detect-board-bypass")
    args = parser.parse_args()

    try:
        if args.command == "list-sent":
            print(json.dumps(list_sent_messages(args.hours), ensure_ascii=True))
            return 0

        messages = fetch_messages()
        if not messages:
            print("No messages to process")
            return 0

        created = 0
        for message in messages:
            if process_incoming_message(message):
                created += 1

        print(f"Processed {len(messages)} messages; created {created} board-awareness issues")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
