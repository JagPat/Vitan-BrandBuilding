#!/usr/bin/env python3
"""Board email review and digest workflow for the Principle Architect."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import smtplib
import ssl
import sys
from email.message import EmailMessage
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib import error, parse, request


REPO_ROOT = Path(__file__).resolve().parent.parent
CONTACTS_PATH = REPO_ROOT / "BOARD_CONTACTS.yaml"
STATE_PATH = REPO_ROOT / ".sync" / "board_communication_state.json"
BOARD_FEEDBACK_PATH = REPO_ROOT / "Business development" / "shared-workspace" / "BOARD_FEEDBACK.md"
WORKDRIVE_COMMENT_EXPORT_PATH = (
    REPO_ROOT
    / "Business development"
    / "shared-workspace"
    / "review"
    / "board-review-comment-export.json"
)

VERDICT_PRIORITY = {"approved": 1, "revise": 2, "rejected": 3}
VERDICT_ALIASES = {
    "approve": "approved",
    "approved": "approved",
    "pass": "approved",
    "ok": "approved",
    "yes": "approved",
    "revise": "revise",
    "revision": "revise",
    "changes": "revise",
    "change": "revise",
    "needs changes": "revise",
    "rejected": "rejected",
    "reject": "rejected",
    "decline": "rejected",
    "no": "rejected",
}


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing env: {name}")
    return value


def load_contacts(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        raise RuntimeError(f"Missing contacts file: {path}")

    members: List[Dict[str, str]] = []
    current: Dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.strip() == "board_members:":
            continue
        if re.match(r"^\s*-\s+name:\s+", line):
            if current:
                members.append(current)
            current = {"name": line.split(":", 1)[1].strip()}
            continue
        match = re.match(r"^\s+([a-zA-Z_]+):\s+(.+)$", line)
        if match and current:
            current[match.group(1).strip()] = match.group(2).strip()
    if current:
        members.append(current)

    valid = [item for item in members if item.get("email")]
    if not valid:
        raise RuntimeError(f"No board members found in {path}")
    return valid


def load_state(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"pending_reviews": {}, "decisions": [], "processed_message_ids": [], "last_digest_at": None}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"pending_reviews": {}, "decisions": [], "processed_message_ids": [], "last_digest_at": None}
    data.setdefault("pending_reviews", {})
    data.setdefault("decisions", [])
    data.setdefault("processed_message_ids", [])
    data.setdefault("last_digest_at", None)
    return data


def save_state(path: Path, state: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def strip_markdown(text: str) -> str:
    lines: List[str] = []
    for raw_line in (text or "").splitlines():
        cleaned = re.sub(r"`([^`]*)`", r"\1", raw_line)
        cleaned = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", cleaned)
        cleaned = re.sub(r"[*#>_]", " ", cleaned)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        lines.append(cleaned)
    return "\n".join(line for line in lines if line).strip()


def paperclip_api(path: str, method: str = "GET", payload: Optional[dict] = None) -> Any:
    api_url = require_env("PAPERCLIP_API_URL").rstrip("/") + "/api"
    api_key = require_env("PAPERCLIP_API_KEY")
    run_id = os.environ.get("PAPERCLIP_RUN_ID", "").strip()
    data = None
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if method != "GET" and run_id:
        headers["X-Paperclip-Run-Id"] = run_id
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
    req = request.Request(f"{api_url}{path}", data=data, method=method, headers=headers)
    try:
        with request.urlopen(req, timeout=30) as res:
            body = res.read()
            if not body:
                return None
            return json.loads(body.decode("utf-8"))
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {path} failed: {exc.code} {detail}") from exc


def issue_link(identifier: str) -> str:
    prefix = (identifier or "VITA-0").split("-")[0]
    return f"/{prefix}/issues/{identifier}"


def get_company_issues(statuses: Sequence[str], limit: int = 200) -> List[Dict[str, Any]]:
    company_id = require_env("PAPERCLIP_COMPANY_ID")
    status_q = ",".join(statuses)
    return paperclip_api(f"/companies/{company_id}/issues?status={status_q}&limit={limit}")


def get_issue_by_identifier(identifier: str) -> Dict[str, Any]:
    issues = get_company_issues(["todo", "in_progress", "blocked", "in_review", "done"], limit=400)
    for issue in issues:
        if issue.get("identifier") == identifier:
            return issue
    raise RuntimeError(f"Issue not found: {identifier}")


def smtp_settings() -> Dict[str, Any]:
    port_raw = os.environ.get("ZOHO_SMTP_PORT", "465")
    try:
        port = int(port_raw)
    except ValueError:
        port = 465
    return {
        "host": require_env("ZOHO_SMTP_HOST"),
        "port": port,
        "user": require_env("ZOHO_SMTP_USER"),
        "password": require_env("ZOHO_SMTP_PASS"),
        "secure": str(os.environ.get("ZOHO_SMTP_SECURE", "true")).lower() in {"1", "true", "yes", "on"},
    }


def send_email(sender: str, recipients: Sequence[str], subject: str, body: str) -> None:
    smtp_cfg = smtp_settings()
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.set_content(body)

    if smtp_cfg["secure"]:
        with smtplib.SMTP_SSL(
            smtp_cfg["host"], smtp_cfg["port"], context=ssl.create_default_context(), timeout=30
        ) as server:
            server.login(smtp_cfg["user"], smtp_cfg["password"])
            server.send_message(msg)
        return

    with smtplib.SMTP(smtp_cfg["host"], smtp_cfg["port"], timeout=30) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(smtp_cfg["user"], smtp_cfg["password"])
        server.send_message(msg)


def send_email_with_sender_fallback(
    preferred_sender: str, recipients: Sequence[str], subject: str, body: str
) -> str:
    smtp_user = os.environ.get("ZOHO_SMTP_USER", "").strip()
    try:
        send_email(preferred_sender, recipients, subject, body)
        return preferred_sender
    except Exception as exc:
        relay_error = "sender is not allowed to relay emails" in str(exc).lower()
        if relay_error and smtp_user and smtp_user.lower() != preferred_sender.lower():
            send_email(smtp_user, recipients, subject, body)
            return smtp_user
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    review = sub.add_parser("review-request", help="Send a board review request email")
    review.add_argument("--issue-id", required=True, help="Paperclip issue identifier, for example VITA-331")
    review.add_argument("--artifact-title", required=True)
    review.add_argument("--summary", help="Inline summary text")
    review.add_argument("--summary-file", type=Path, help="Path to a markdown or text summary")
    review.add_argument("--artifact-path", help="Repo path of the artifact under review")
    review.add_argument("--workdrive-link", required=True)
    review.add_argument("--content-signoff", default="pending", choices=["pending", "approved", "revise"])
    review.add_argument("--image-signoff", default="pending", choices=["pending", "approved", "revise"])
    review.add_argument("--send", action="store_true", help="Actually send the email. Default is dry-run.")

    digest = sub.add_parser("daily-digest", help="Send the daily board digest email")
    digest.add_argument("--date", help="Digest date in YYYY-MM-DD. Defaults to UTC today.")
    digest.add_argument("--digest-file", type=Path, help="Optional path to a prepared digest artifact")
    digest.add_argument("--send", action="store_true", help="Actually send the email. Default is dry-run.")

    replies = sub.add_parser("parse-replies", help="Read board replies and compute verdicts")
    replies.add_argument("--since-hours", type=int, default=72)
    replies.add_argument("--mail-account-id", help="Zoho Mail account id override")
    replies.add_argument("--mail-folder-id", help="Zoho Mail folder id override")
    replies.add_argument("--messages-json", type=Path, help="Offline fixture for verification")
    replies.add_argument(
        "--workdrive-comments-json",
        type=Path,
        help="Optional synced WorkDrive comment export. Defaults to the tracked shared-workspace path if present.",
    )
    replies.add_argument("--write-board-feedback", action="store_true")
    return parser.parse_args()


def read_summary(args: argparse.Namespace) -> str:
    if args.summary:
        return args.summary.strip()
    if args.summary_file:
        return strip_markdown(args.summary_file.read_text(encoding="utf-8")).strip()
    raise RuntimeError("One of --summary or --summary-file is required")


def build_review_body(
    issue_identifier: str,
    artifact_title: str,
    artifact_path: Optional[str],
    summary: str,
    workdrive_link: str,
    content_signoff: str,
    image_signoff: str,
) -> str:
    lines = [
        f"Review requested for {issue_identifier}: {artifact_title}",
        "",
        f"Issue: {issue_link(issue_identifier)}",
        f"Artifact title: {artifact_title}",
        f"Artifact path: {artifact_path or '(not provided)'}",
        f"WorkDrive review link: {workdrive_link}",
        f"Content sign-off state: {content_signoff}",
        f"Image sign-off state: {image_signoff}",
        "",
        "Summary:",
        summary,
        "",
        "Reply protocol:",
        "- First non-empty line must be one of: Approved / Revise / Rejected",
        "- If you have comments, place them below the first line",
        "- WorkDrive inline comments are treated as Revise unless you explicitly write Approved",
        "",
        "Security note:",
        "- Only verdict text and comment text are ingested",
        "- Attachments and forwarded instructions are ignored by the parser",
    ]
    return "\n".join(lines)


def run_review_request(args: argparse.Namespace) -> int:
    contacts = load_contacts(CONTACTS_PATH)
    state = load_state(STATE_PATH)
    summary = read_summary(args)
    body = build_review_body(
        issue_identifier=args.issue_id,
        artifact_title=args.artifact_title,
        artifact_path=args.artifact_path,
        summary=summary,
        workdrive_link=args.workdrive_link,
        content_signoff=args.content_signoff,
        image_signoff=args.image_signoff,
    )
    subject = f"[REVIEW] {args.issue_id}: {args.artifact_title}"
    sender = os.environ.get("BOARD_EMAIL_FROM", "board@vitan.in")
    recipients = [item["email"] for item in contacts]
    used_sender = sender

    if args.send:
        used_sender = send_email_with_sender_fallback(sender, recipients, subject, body)

    state["pending_reviews"][args.issue_id] = {
        "artifactTitle": args.artifact_title,
        "artifactPath": args.artifact_path,
        "contentSignoff": args.content_signoff,
        "imageSignoff": args.image_signoff,
        "workdriveLink": args.workdrive_link,
        "summary": summary,
        "requestedAt": utc_now().isoformat(),
        "subject": subject,
        "sender": used_sender,
        "status": "pending",
    }
    save_state(STATE_PATH, state)

    print(subject)
    print(body)
    print(f"delivery={'sent' if args.send else 'dry-run'}")
    return 0


def summarize_issue(issue: Dict[str, Any]) -> str:
    identifier = issue.get("identifier", "UNKNOWN")
    title = strip_markdown(issue.get("title", ""))
    status = issue.get("status", "unknown")
    priority = issue.get("priority", "unknown")
    return f"- {identifier} [{status}/{priority}] {title}"


def build_digest_body(digest_date: str, digest_text: str, state: Dict[str, Any], issues: List[Dict[str, Any]]) -> str:
    pending_reviews = [
        f"- {issue_id}: {data.get('artifactTitle', 'Untitled')} ({data.get('status', 'pending')})"
        for issue_id, data in sorted(state.get("pending_reviews", {}).items())
        if data.get("status") == "pending"
    ]
    recent_decisions = []
    for decision in state.get("decisions", [])[-5:]:
        recent_decisions.append(
            f"- {decision.get('issueId')}: {decision.get('verdict')} from {decision.get('sources', [])}"
        )

    active_issues = [summarize_issue(issue) for issue in issues[:8]]
    escalations = [
        summarize_issue(issue)
        for issue in issues
        if (issue.get("priority") or "").lower() in {"high", "urgent", "critical"}
        and (issue.get("status") or "").lower() in {"blocked", "in_progress", "todo"}
    ][:6]

    lines = [
        f"Vitan Growth OS Board Digest - {digest_date}",
        "",
        "Prepared by: Principle Architect",
        "",
        "Pending reviews:",
        *(pending_reviews or ["- none"]),
        "",
        "Recent approvals / verdicts:",
        *(recent_decisions or ["- none logged yet"]),
        "",
        "Agent activity summary:",
        *(active_issues or ["- no open issue activity found"]),
        "",
        "Escalations:",
        *(escalations or ["- none"]),
        "",
        "Digest artifact summary:",
        digest_text or "(no digest artifact provided)",
    ]
    return "\n".join(lines)


def run_daily_digest(args: argparse.Namespace) -> int:
    contacts = load_contacts(CONTACTS_PATH)
    state = load_state(STATE_PATH)
    digest_date = args.date or utc_now().date().isoformat()
    digest_text = ""
    if args.digest_file and args.digest_file.exists():
        digest_text = strip_markdown(args.digest_file.read_text(encoding="utf-8"))
    issues = get_company_issues(["todo", "in_progress", "blocked", "in_review"], limit=200)
    body = build_digest_body(digest_date, digest_text, state, issues)
    subject = f"[DIGEST] Vitan Growth OS - {digest_date}"
    sender = os.environ.get("BOARD_EMAIL_FROM", "board@vitan.in")
    recipients = [item["email"] for item in contacts]
    used_sender = sender
    if args.send:
        used_sender = send_email_with_sender_fallback(sender, recipients, subject, body)
    state["last_digest_at"] = utc_now().isoformat()
    state["last_digest_sender"] = used_sender
    save_state(STATE_PATH, state)
    print(subject)
    print(body)
    print(f"delivery={'sent' if args.send else 'dry-run'}")
    return 0


def refresh_zoho_token() -> str:
    token_url = os.environ.get("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2/token")
    payload = parse.urlencode(
        {
            "refresh_token": require_env("ZOHO_REFRESH_TOKEN"),
            "client_id": require_env("ZOHO_CLIENT_ID"),
            "client_secret": require_env("ZOHO_CLIENT_SECRET"),
            "grant_type": "refresh_token",
        }
    ).encode("utf-8")
    req = request.Request(token_url, data=payload, method="POST")
    with request.urlopen(req, timeout=30) as res:
        body = json.loads(res.read().decode("utf-8"))
    token = body.get("access_token")
    if not token:
        raise RuntimeError(f"Zoho token refresh failed: {body}")
    return token


def zoho_mail_request(path: str, token: str, query: Optional[Dict[str, Any]] = None) -> Any:
    base = os.environ.get("ZOHO_MAIL_BASE_URL", "https://mail.zoho.in").rstrip("/")
    qs = ""
    if query:
        qs = "?" + parse.urlencode(query)
    req = request.Request(
        f"{base}{path}{qs}",
        headers={
            "Authorization": f"Zoho-oauthtoken {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    with request.urlopen(req, timeout=30) as res:
        return json.loads(res.read().decode("utf-8"))


def first_account_id(token: str) -> str:
    if os.environ.get("ZOHO_MAIL_ACCOUNT_ID"):
        return os.environ["ZOHO_MAIL_ACCOUNT_ID"]
    payload = zoho_mail_request("/api/accounts", token)
    accounts = payload.get("data", [])
    if not accounts:
        raise RuntimeError("No Zoho Mail accounts returned")
    return str(accounts[0].get("accountId") or accounts[0].get("id") or "")


def inbox_folder_id(token: str, account_id: str) -> str:
    if os.environ.get("ZOHO_MAIL_FOLDER_ID"):
        return os.environ["ZOHO_MAIL_FOLDER_ID"]
    payload = zoho_mail_request(f"/api/accounts/{account_id}/folders", token)
    folders = payload.get("data", [])
    for folder in folders:
        name = str(folder.get("folderName") or folder.get("name") or "").lower()
        if name == "inbox":
            return str(folder.get("folderId") or folder.get("id") or "")
    if folders:
        return str(folders[0].get("folderId") or folders[0].get("id") or "")
    raise RuntimeError("No Zoho Mail folders returned")


def normalize_sender(raw: str) -> str:
    text = raw or ""
    match = re.search(r"<([^>]+)>", text)
    if match:
        return match.group(1).strip().lower()
    return text.strip().lower()


def verdict_from_text(text: str) -> Optional[str]:
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        key = re.sub(r"[^a-z ]", "", line.lower()).strip()
        return VERDICT_ALIASES.get(key)
    return None


def extract_issue_identifier(subject: str, text: str) -> Optional[str]:
    for source in (subject or "", text or ""):
        match = re.search(r"\b([A-Z]+-\d+)\b", source)
        if match:
            return match.group(1)
    return None


def conservative_verdict(verdicts: Iterable[str]) -> Optional[str]:
    selected: Optional[str] = None
    score = 0
    for verdict in verdicts:
        current_score = VERDICT_PRIORITY.get(verdict, 0)
        if current_score > score:
            selected = verdict
            score = current_score
    return selected


def fetch_recent_messages(
    token: str, account_id: str, folder_id: str, since_hours: int
) -> List[Dict[str, Any]]:
    payload = zoho_mail_request(
        f"/api/accounts/{account_id}/messages/view",
        token,
        query={"folderId": folder_id, "start": 1, "limit": 50},
    )
    cutoff = utc_now() - dt.timedelta(hours=since_hours)
    recent: List[Dict[str, Any]] = []
    for item in payload.get("data", []):
        received_raw = item.get("receivedTime") or item.get("date") or item.get("receivedTimeInGMT")
        received_dt = cutoff
        if isinstance(received_raw, (int, float)):
            received_dt = dt.datetime.fromtimestamp(received_raw / 1000, tz=dt.timezone.utc)
        message = {
            "messageId": str(item.get("messageId") or item.get("mailId") or item.get("id") or ""),
            "folderId": str(item.get("folderId") or folder_id),
            "subject": item.get("subject", ""),
            "fromAddress": item.get("fromAddress") or item.get("senderAddress") or item.get("from", ""),
            "receivedAt": received_dt.isoformat(),
        }
        if received_dt >= cutoff and message["messageId"]:
            recent.append(message)
    return recent


def fetch_message_content(token: str, account_id: str, folder_id: str, message_id: str) -> str:
    payload = zoho_mail_request(
        f"/api/accounts/{account_id}/folders/{folder_id}/messages/{message_id}/content",
        token,
    )
    data = payload.get("data") or {}
    if isinstance(data, list):
        data = data[0] if data else {}
    content = data.get("content") or data.get("textContent") or data.get("htmlContent") or ""
    return strip_markdown(str(content))


def load_messages_from_fixture(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return data.get("messages", [])
    return data


def load_workdrive_comment_verdicts(path: Optional[Path]) -> List[Dict[str, Any]]:
    if path is None:
        path = WORKDRIVE_COMMENT_EXPORT_PATH if WORKDRIVE_COMMENT_EXPORT_PATH.exists() else None
    if path is None or not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    items = data.get("comments", data if isinstance(data, list) else [])
    results: List[Dict[str, Any]] = []
    for item in items:
        issue_id = item.get("issueId") or item.get("issueIdentifier")
        text = str(item.get("text") or item.get("comment") or "")
        if not issue_id or not text.strip():
            continue
        verdict = verdict_from_text(text) or "revise"
        results.append(
            {
                "issueId": issue_id,
                "source": f"workdrive:{item.get('commentId') or item.get('id') or 'unknown'}",
                "author": item.get("author") or "unknown",
                "verdict": verdict,
                "detail": text.strip(),
            }
        )
    return results


def append_board_feedback_entries(path: Path, entries: List[Dict[str, Any]]) -> None:
    if not entries:
        return
    text = path.read_text(encoding="utf-8")
    marker = "\n## Preference Codex\n"
    if marker not in text:
        raise RuntimeError(f"Could not find insertion marker in {path}")

    blocks = []
    for entry in entries:
        blocks.append(
            "\n".join(
                [
                    f"### {entry['loggedAt']} - {entry['issueId']} - {entry['verdict'].title()}",
                    f"- Channel: {entry['channel']}",
                    f"- Reasoning summary: {entry['detail']}",
                    f"- Sources: {', '.join(entry['sources'])}",
                    "- Pattern implication: board communication workflow logged a new review outcome; durable preference not promoted automatically.",
                ]
            )
        )
    updated = text.replace(marker, "\n" + "\n\n".join(blocks) + marker, 1)
    path.write_text(updated, encoding="utf-8")


def run_parse_replies(args: argparse.Namespace) -> int:
    contacts = load_contacts(CONTACTS_PATH)
    allowed_senders = {normalize_sender(item["email"]) for item in contacts}
    state = load_state(STATE_PATH)
    processed = set(state.get("processed_message_ids", []))

    board_inputs: List[Dict[str, Any]] = []
    if args.messages_json:
        messages = load_messages_from_fixture(args.messages_json)
        for item in messages:
            sender = normalize_sender(str(item.get("fromAddress") or item.get("from") or ""))
            if sender not in allowed_senders:
                continue
            body = strip_markdown(str(item.get("content") or item.get("body") or item.get("text") or ""))
            issue_id = extract_issue_identifier(str(item.get("subject") or ""), body)
            verdict = verdict_from_text(body)
            if not issue_id or not verdict:
                continue
            board_inputs.append(
                {
                    "issueId": issue_id,
                    "source": f"mail-fixture:{item.get('messageId') or item.get('id') or 'unknown'}",
                    "author": sender,
                    "verdict": verdict,
                    "detail": body,
                }
            )
    else:
        token = refresh_zoho_token()
        account_id = args.mail_account_id or first_account_id(token)
        folder_id = args.mail_folder_id or inbox_folder_id(token, account_id)
        for item in fetch_recent_messages(token, account_id, folder_id, args.since_hours):
            message_id = item["messageId"]
            if message_id in processed:
                continue
            sender = normalize_sender(item["fromAddress"])
            if sender not in allowed_senders:
                continue
            body = fetch_message_content(token, account_id, item["folderId"], message_id)
            issue_id = extract_issue_identifier(item["subject"], body)
            verdict = verdict_from_text(body)
            if not issue_id or not verdict:
                continue
            processed.add(message_id)
            board_inputs.append(
                {
                    "issueId": issue_id,
                    "source": f"mail:{message_id}",
                    "author": sender,
                    "verdict": verdict,
                    "detail": body,
                }
            )

    board_inputs.extend(load_workdrive_comment_verdicts(args.workdrive_comments_json))

    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for item in board_inputs:
        grouped.setdefault(item["issueId"], []).append(item)

    decisions: List[Dict[str, Any]] = []
    feedback_entries: List[Dict[str, Any]] = []
    for issue_id, items in sorted(grouped.items()):
        verdict = conservative_verdict(item["verdict"] for item in items)
        if not verdict:
            continue
        decision = {
            "issueId": issue_id,
            "verdict": verdict,
            "sources": [item["source"] for item in items],
            "authors": sorted({item["author"] for item in items}),
            "loggedAt": utc_now().isoformat(),
            "detail": " | ".join(strip_markdown(item["detail"])[:180] for item in items[:3]),
        }
        decisions.append(decision)
        feedback_entries.append(
            {
                "issueId": issue_id,
                "verdict": verdict,
                "sources": decision["sources"],
                "detail": decision["detail"],
                "channel": "email+workdrive" if any(src.startswith("workdrive:") for src in decision["sources"]) else "email",
                "loggedAt": utc_now().date().isoformat(),
            }
        )
        if issue_id in state["pending_reviews"]:
            state["pending_reviews"][issue_id]["status"] = verdict
            state["pending_reviews"][issue_id]["resolvedAt"] = utc_now().isoformat()

    if decisions:
        state["decisions"].extend(decisions)
        state["processed_message_ids"] = sorted(processed)
        save_state(STATE_PATH, state)
    if args.write_board_feedback and feedback_entries:
        append_board_feedback_entries(BOARD_FEEDBACK_PATH, feedback_entries)

    print(json.dumps({"decisions": decisions}, indent=2))
    return 0


def main() -> int:
    args = parse_args()
    try:
        if args.command == "review-request":
            return run_review_request(args)
        if args.command == "daily-digest":
            return run_daily_digest(args)
        if args.command == "parse-replies":
            return run_parse_replies(args)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    raise RuntimeError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
