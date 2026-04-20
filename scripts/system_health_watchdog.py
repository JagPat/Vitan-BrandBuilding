#!/usr/bin/env python3
"""System health watchdog for Paperclip agent heartbeat monitoring and self-repair.

This script is designed for PA/FE operations to:
1) detect stale agent heartbeats,
2) optionally trigger a guarded self-repair restart,
3) escalate by direct Zoho email after repeated failed repairs,
4) emit board-digest-ready health markdown.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests


DEFAULT_INTERVAL_SEC = 21600
DEFAULT_STALE_MULTIPLIER = 2.0
DEFAULT_RESTART_COOLDOWN_SEC = 3600
DEFAULT_ESCALATE_AFTER_FAILURES = 2


@dataclass
class AgentHealth:
    agent_id: str
    name: str
    status: str
    last_heartbeat_at: str | None
    age_sec: int | None
    interval_sec: int
    stale_after_sec: int
    health: str  # healthy | delayed | stale | unknown


class PaperclipClient:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def get_json(self, path: str) -> Any:
        response = self.session.get(f"{self.api_url}{path}", timeout=60)
        response.raise_for_status()
        return response.json()


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_iso8601(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def classify_health(age_sec: int | None, interval_sec: int, stale_multiplier: float) -> str:
    if age_sec is None:
        return "unknown"
    stale_after = int(interval_sec * stale_multiplier)
    if age_sec > stale_after:
        return "stale"
    if age_sec > interval_sec:
        return "delayed"
    return "healthy"


def evaluate_agent_health(
    agents: list[dict[str, Any]],
    now: dt.datetime,
    default_interval_sec: int,
    stale_multiplier: float,
) -> list[AgentHealth]:
    rows: list[AgentHealth] = []
    for agent in agents:
        runtime_hb = ((agent.get("runtimeConfig") or {}).get("heartbeat") or {})
        interval_sec = int(runtime_hb.get("intervalSec") or default_interval_sec)
        last_hb = parse_iso8601(agent.get("lastHeartbeatAt"))
        age_sec = None if last_hb is None else max(0, int((now - last_hb).total_seconds()))
        stale_after_sec = int(interval_sec * stale_multiplier)
        health = classify_health(age_sec, interval_sec, stale_multiplier)
        rows.append(
            AgentHealth(
                agent_id=str(agent.get("id") or ""),
                name=str(agent.get("name") or "unknown"),
                status=str(agent.get("status") or "unknown"),
                last_heartbeat_at=agent.get("lastHeartbeatAt"),
                age_sec=age_sec,
                interval_sec=interval_sec,
                stale_after_sec=stale_after_sec,
                health=health,
            )
        )
    rows.sort(key=lambda item: (item.health != "stale", item.age_sec is None, -(item.age_sec or 0)))
    return rows


def format_age(age_sec: int | None) -> str:
    if age_sec is None:
        return "n/a"
    hours = age_sec / 3600
    return f"{hours:.2f}h"


def build_markdown(rows: list[AgentHealth], generated_at: str, stale_multiplier: float) -> str:
    total = len(rows)
    stale_count = sum(1 for row in rows if row.health == "stale")
    delayed_count = sum(1 for row in rows if row.health == "delayed")
    unknown_count = sum(1 for row in rows if row.health == "unknown")

    lines = [
        "# Agent Health Snapshot (VITA-374)",
        "",
        f"Generated (UTC): {generated_at}",
        f"Stale threshold: `age > interval * {stale_multiplier:g}`",
        "",
        "## Summary",
        "",
        f"- Total agents checked: **{total}**",
        f"- Stale: **{stale_count}**",
        f"- Delayed: **{delayed_count}**",
        f"- Unknown heartbeat: **{unknown_count}**",
        "",
        "## Board Digest Health Block",
        "",
        f"`Health: {stale_count} stale | {delayed_count} delayed | {unknown_count} unknown ({total} total)`",
        "",
        "## Agent Table",
        "",
        "| Agent | Runtime Status | Health | Last Heartbeat (UTC) | Heartbeat Age | Interval | Stale After |",
        "|---|---|---|---|---:|---:|---:|",
    ]

    for row in rows:
        lines.append(
            "| {name} | {runtime} | {health} | {last} | {age} | {interval} | {stale_after} |".format(
                name=row.name,
                runtime=row.status,
                health=row.health,
                last=row.last_heartbeat_at or "n/a",
                age=format_age(row.age_sec),
                interval=f"{row.interval_sec / 3600:.1f}h",
                stale_after=f"{row.stale_after_sec / 3600:.1f}h",
            )
        )

    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- `stale` agents are candidates for automated self-repair.")
    lines.append("- `delayed` agents are behind one interval but below the stale threshold.")
    return "\n".join(lines) + "\n"


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"failed_self_repair_attempts": 0, "last_restart_at": None, "last_escalation_at": None}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"failed_self_repair_attempts": 0, "last_restart_at": None, "last_escalation_at": None}


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def seconds_since(iso_value: str | None, now: dt.datetime) -> int | None:
    parsed = parse_iso8601(iso_value)
    if parsed is None:
        return None
    return max(0, int((now - parsed).total_seconds()))


def can_attempt_restart(state: dict[str, Any], now: dt.datetime, cooldown_sec: int) -> tuple[bool, str]:
    elapsed = seconds_since(state.get("last_restart_at"), now)
    if elapsed is None:
        return True, "no previous restart"
    if elapsed < cooldown_sec:
        return False, f"restart cooldown active ({elapsed}s < {cooldown_sec}s)"
    return True, f"cooldown elapsed ({elapsed}s >= {cooldown_sec}s)"


def railway_restart(service_hint: str) -> tuple[bool, str]:
    webhook = os.getenv("RAILWAY_REDEPLOY_WEBHOOK_URL", "").strip()
    if webhook:
        response = requests.post(webhook, json={"reason": service_hint}, timeout=60)
        if 200 <= response.status_code < 300:
            return True, "redeploy triggered via RAILWAY_REDEPLOY_WEBHOOK_URL"
        return False, f"webhook restart failed: HTTP {response.status_code}"

    token = os.getenv("RAILWAY_API_TOKEN", "").strip()
    project_id = os.getenv("RAILWAY_PROJECT_ID", "").strip()
    environment_id = os.getenv("RAILWAY_ENVIRONMENT_ID", "").strip()
    service_id = os.getenv("RAILWAY_SERVICE_ID", "").strip()
    endpoint = os.getenv("RAILWAY_GRAPHQL_URL", "https://backboard.railway.app/graphql/v2").strip()

    if not (token and project_id and environment_id and service_id):
        return False, "missing Railway credentials (need webhook or API token+project/environment/service ids)"

    query = (
        "mutation Redeploy($projectId: String!, $environmentId: String!, $serviceId: String!) {"
        " serviceInstanceRedeploy(input: {projectId: $projectId, environmentId: $environmentId, serviceId: $serviceId})"
        " }"
    )
    payload = {
        "query": query,
        "variables": {
            "projectId": project_id,
            "environmentId": environment_id,
            "serviceId": service_id,
        },
    }
    response = requests.post(
        endpoint,
        json=payload,
        headers={"Authorization": f"Bearer {token}"},
        timeout=60,
    )
    if response.status_code >= 300:
        return False, f"Railway GraphQL restart failed: HTTP {response.status_code}"

    body = response.json()
    if body.get("errors"):
        return False, f"Railway GraphQL restart errors: {body['errors']}"

    return True, "redeploy triggered via Railway GraphQL API"


def get_zoho_access_token() -> str:
    required = ["ZOHO_REFRESH_TOKEN", "ZOHO_CLIENT_ID", "ZOHO_CLIENT_SECRET"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise RuntimeError(f"Missing Zoho OAuth env vars: {', '.join(missing)}")

    accounts_url = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2/token")
    response = requests.post(
        accounts_url,
        data={
            "refresh_token": os.environ["ZOHO_REFRESH_TOKEN"],
            "client_id": os.environ["ZOHO_CLIENT_ID"],
            "client_secret": os.environ["ZOHO_CLIENT_SECRET"],
            "grant_type": "refresh_token",
        },
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    token = payload.get("access_token")
    if not token:
        raise RuntimeError(f"Zoho token response missing access_token: {payload}")
    return token


def send_escalation_email(subject: str, body: str) -> tuple[bool, str]:
    account_id = os.getenv("ZOHO_MAIL_ACCOUNT_ID", "").strip()
    send_url = os.getenv("ZOHO_SEND_MAIL_URL", "").strip()

    if not send_url:
        if not account_id:
            return False, "missing ZOHO_MAIL_ACCOUNT_ID or ZOHO_SEND_MAIL_URL for escalation email"
        send_url = f"https://mail.zoho.in/api/accounts/{account_id}/messages"

    token = get_zoho_access_token()
    payload = {
        "fromAddress": os.getenv("ZOHO_ESCALATION_FROM", "board-alerts@vitan.in"),
        "toAddress": os.getenv("ZOHO_ESCALATION_TO", "board@vitan.in"),
        "subject": subject,
        "content": body,
        "mailFormat": "plaintext",
    }
    response = requests.post(
        send_url,
        json=payload,
        headers={"Authorization": f"Zoho-oauthtoken {token}"},
        timeout=60,
    )
    if response.status_code >= 300:
        return False, f"Zoho escalation email failed: HTTP {response.status_code}"
    return True, "escalation email sent via Zoho Mail API"


def run(args: argparse.Namespace) -> int:
    now = utc_now()
    generated_at = now.isoformat().replace("+00:00", "Z")

    client = PaperclipClient(args.api_url, args.api_key)
    agents = client.get_json(f"/api/companies/{args.company_id}/agents")
    rows = evaluate_agent_health(
        agents=agents,
        now=now,
        default_interval_sec=args.default_interval_sec,
        stale_multiplier=args.stale_multiplier,
    )

    markdown = build_markdown(rows, generated_at, args.stale_multiplier)
    args.output_markdown.parent.mkdir(parents=True, exist_ok=True)
    args.output_markdown.write_text(markdown, encoding="utf-8")

    json_output = {
        "generatedAt": generated_at,
        "staleMultiplier": args.stale_multiplier,
        "defaultIntervalSec": args.default_interval_sec,
        "agents": [
            {
                "id": row.agent_id,
                "name": row.name,
                "runtimeStatus": row.status,
                "health": row.health,
                "lastHeartbeatAt": row.last_heartbeat_at,
                "heartbeatAgeSec": row.age_sec,
                "intervalSec": row.interval_sec,
                "staleAfterSec": row.stale_after_sec,
            }
            for row in rows
        ],
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(json_output, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    stale_rows = [row for row in rows if row.health == "stale"]
    state = load_state(args.state_path)
    state.setdefault("failed_self_repair_attempts", 0)
    state.setdefault("last_restart_at", None)
    state.setdefault("last_escalation_at", None)

    actions: list[str] = []

    if stale_rows and args.attempt_self_repair:
        allowed, reason = can_attempt_restart(state, now, args.restart_cooldown_sec)
        actions.append(f"restart-check: {reason}")
        if allowed:
            success, detail = railway_restart(
                service_hint=f"stale agents: {', '.join(row.name for row in stale_rows)}"
            )
            if success:
                state["last_restart_at"] = generated_at
                state["failed_self_repair_attempts"] = 0
                actions.append(f"restart: success ({detail})")
            else:
                state["failed_self_repair_attempts"] = int(state.get("failed_self_repair_attempts", 0)) + 1
                actions.append(f"restart: failed ({detail})")
        else:
            actions.append("restart: skipped due to cooldown")

        failures = int(state.get("failed_self_repair_attempts", 0))
        if failures >= args.escalate_after_failures:
            subject = "[VITA-374] Self-repair failed repeatedly: manual intervention required"
            body = "\n".join(
                [
                    "System self-repair escalation triggered.",
                    f"Generated at (UTC): {generated_at}",
                    f"Failed self-repair attempts: {failures}",
                    "Stale agents:",
                    *[f"- {row.name} (last heartbeat: {row.last_heartbeat_at or 'n/a'})" for row in stale_rows],
                ]
            )
            mail_ok, mail_detail = send_escalation_email(subject, body)
            if mail_ok:
                state["last_escalation_at"] = generated_at
                actions.append(f"escalation-email: success ({mail_detail})")
            else:
                actions.append(f"escalation-email: failed ({mail_detail})")

    elif stale_rows and not args.attempt_self_repair:
        actions.append("stale detected but self-repair disabled (--attempt-self-repair not set)")
    else:
        state["failed_self_repair_attempts"] = 0
        actions.append("no stale agents detected")

    save_state(args.state_path, state)

    summary = {
        "staleCount": len(stale_rows),
        "delayedCount": sum(1 for row in rows if row.health == "delayed"),
        "unknownCount": sum(1 for row in rows if row.health == "unknown"),
        "actions": actions,
        "statePath": str(args.state_path),
        "outputMarkdown": str(args.output_markdown),
        "outputJson": str(args.output_json),
    }
    print(json.dumps(summary, indent=2, ensure_ascii=True))
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Paperclip system health watchdog")
    parser.add_argument("--api-url", default=os.getenv("PAPERCLIP_API_URL", ""), help="Paperclip API base URL")
    parser.add_argument("--api-key", default=os.getenv("PAPERCLIP_API_KEY", ""), help="Paperclip API key")
    parser.add_argument(
        "--company-id", default=os.getenv("PAPERCLIP_COMPANY_ID", ""), help="Paperclip company id"
    )
    parser.add_argument(
        "--output-markdown",
        type=Path,
        default=Path("Business development/shared-workspace/review/vita374/agent-health-status.md"),
        help="Where to write markdown health summary",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("Business development/shared-workspace/review/vita374/agent-health-status.json"),
        help="Where to write machine-readable health summary",
    )
    parser.add_argument(
        "--state-path",
        type=Path,
        default=Path("Business development/shared-workspace/intelligence/system-health-watchdog-state.json"),
        help="State file path for cooldown and failed-attempt tracking",
    )
    parser.add_argument(
        "--default-interval-sec",
        type=int,
        default=DEFAULT_INTERVAL_SEC,
        help="Fallback heartbeat interval when agent runtimeConfig has no interval",
    )
    parser.add_argument(
        "--stale-multiplier",
        type=float,
        default=DEFAULT_STALE_MULTIPLIER,
        help="Mark stale when heartbeat age exceeds interval * multiplier",
    )
    parser.add_argument(
        "--attempt-self-repair",
        action="store_true",
        help="Trigger Railway redeploy attempt when stale agents are detected",
    )
    parser.add_argument(
        "--restart-cooldown-sec",
        type=int,
        default=DEFAULT_RESTART_COOLDOWN_SEC,
        help="Minimum spacing between restart attempts",
    )
    parser.add_argument(
        "--escalate-after-failures",
        type=int,
        default=DEFAULT_ESCALATE_AFTER_FAILURES,
        help="Escalate by direct email after this many failed self-repair attempts",
    )

    args = parser.parse_args(argv)
    missing = [
        label
        for label, value in [
            ("--api-url / PAPERCLIP_API_URL", args.api_url),
            ("--api-key / PAPERCLIP_API_KEY", args.api_key),
            ("--company-id / PAPERCLIP_COMPANY_ID", args.company_id),
        ]
        if not value
    ]
    if missing:
        parser.error("Missing required configuration: " + ", ".join(missing))
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
