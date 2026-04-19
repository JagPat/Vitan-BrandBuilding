#!/usr/bin/env python3
"""Analyze Paperclip heartbeat token usage and emit a markdown report.

Requires env vars:
- PAPERCLIP_API_URL
- PAPERCLIP_API_KEY
- PAPERCLIP_COMPANY_ID

Example:
  python3 scripts/analyze_paperclip_token_usage.py --limit 1000 \
    --output "Business development/shared-workspace/intelligence/vita678/token-usage-audit-2026-04-19.md"
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any


@dataclass
class AgentAggregate:
    name: str
    runs: int = 0
    raw_input: int = 0
    raw_output: int = 0
    raw_cached: int = 0
    fresh_sessions: int = 0
    reused_sessions: int = 0
    task_reused_sessions: int = 0

    @property
    def total(self) -> int:
        return self.raw_input + self.raw_output + self.raw_cached

    @property
    def cache_pct(self) -> float:
        if self.total == 0:
            return 0.0
        return (self.raw_cached / self.total) * 100.0


class PaperclipClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        query = ""
        if params:
            query = "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(
            self.base_url + path + query,
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"GET {path} failed: HTTP {exc.code} {body[:300]}") from exc


def as_int(value: Any) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return int(value)
    return 0


def iso_date(ts: str | None) -> str:
    if not ts:
        return "n/a"
    try:
        return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return ts[:10]


def build_report(
    company_prefix: str,
    generated_utc: str,
    limit: int,
    runs: list[dict[str, Any]],
    agents: list[dict[str, Any]],
) -> str:
    agent_names = {a["id"]: a.get("name", a["id"]) for a in agents}

    agg: dict[str, AgentAggregate] = {}
    provider_counter: Counter[str] = Counter()
    status_counter: Counter[str] = Counter()

    # (agentId, persistedSessionId) -> list of run entries
    session_runs: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)

    for run in runs:
        usage = run.get("usageJson") or {}
        aid = run.get("agentId", "unknown")
        if aid not in agg:
            agg[aid] = AgentAggregate(name=agent_names.get(aid, aid))
        a = agg[aid]
        a.runs += 1
        a.raw_input += as_int(usage.get("rawInputTokens"))
        a.raw_output += as_int(usage.get("rawOutputTokens"))
        a.raw_cached += as_int(usage.get("rawCachedInputTokens"))
        a.fresh_sessions += 1 if usage.get("freshSession") else 0
        a.reused_sessions += 1 if usage.get("sessionReused") else 0
        a.task_reused_sessions += 1 if usage.get("taskSessionReused") else 0

        provider = usage.get("provider") or "unknown"
        provider_counter[str(provider)] += as_int(usage.get("rawInputTokens")) + as_int(
            usage.get("rawOutputTokens")
        ) + as_int(usage.get("rawCachedInputTokens"))

        status_counter[run.get("status") or "unknown"] += 1

        sid = usage.get("persistedSessionId")
        if sid:
            session_runs[(aid, str(sid))].append(
                {
                    "startedAt": run.get("startedAt"),
                    "rawInputTokens": as_int(usage.get("rawInputTokens")),
                    "rawCachedInputTokens": as_int(usage.get("rawCachedInputTokens")),
                    "runId": run.get("id"),
                }
            )

    by_total = sorted(agg.items(), key=lambda item: item[1].total, reverse=True)
    company_total = sum(a.total for _, a in by_total)

    top_agents_lines = []
    for aid, a in by_total[:7]:
        share = (a.total / company_total * 100.0) if company_total else 0.0
        top_agents_lines.append(
            "| {name} | {runs} | {total} | {raw_in} | {cached} | {share:.1f}% | {cache_pct:.1f}% |".format(
                name=a.name,
                runs=a.runs,
                total=a.total,
                raw_in=a.raw_input,
                cached=a.raw_cached,
                share=share,
                cache_pct=a.cache_pct,
            )
        )

    top_providers_lines = []
    for provider, total in provider_counter.most_common(5):
        pct = (total / company_total * 100.0) if company_total else 0.0
        top_providers_lines.append(f"| {provider} | {total} | {pct:.1f}% |")

    # runaway session heuristic: >=5 runs and max rawInput >= 1,000,000
    runaway = []
    for (aid, sid), items in session_runs.items():
        if len(items) < 5:
            continue
        ordered = sorted(items, key=lambda x: x.get("startedAt") or "")
        raw_inputs = [x["rawInputTokens"] for x in ordered]
        max_in = max(raw_inputs) if raw_inputs else 0
        if max_in < 1_000_000:
            continue
        first = raw_inputs[0]
        last = raw_inputs[-1]
        growth = last - first
        runaway.append(
            {
                "agent": agent_names.get(aid, aid),
                "session_id": sid,
                "runs": len(ordered),
                "first": first,
                "max": max_in,
                "last": last,
                "growth": growth,
                "start": iso_date(ordered[0].get("startedAt")),
            }
        )

    runaway.sort(key=lambda x: x["max"], reverse=True)
    runaway_lines = []
    for item in runaway[:10]:
        runaway_lines.append(
            "| {agent} | {start} | {runs} | {first} | {max} | {last} | {growth} |".format(**item)
        )

    status_bits = ", ".join(f"{k}: {v}" for k, v in status_counter.most_common())

    lines = []
    lines.append("# VITA-678 Token Usage Audit")
    lines.append("")
    lines.append(f"Generated (UTC): {generated_utc}")
    lines.append(f"Sample size: last {limit} heartbeat runs")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total sampled tokens (raw input + raw output + raw cached input): **{company_total}**")
    lines.append(f"- Run statuses in sample: {status_bits}")
    lines.append("- Primary token driver is **context growth in persisted sessions** (high raw input in repeated runs).")
    lines.append("- Cached token share is high, which is useful, but very large sessions still inflate absolute token volume.")
    lines.append("")
    lines.append("## Token Share by Agent")
    lines.append("")
    lines.append("| Agent | Runs | Total Tokens | Raw Input | Raw Cached | Share | Cached % |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    lines.extend(top_agents_lines or ["| n/a | 0 | 0 | 0 | 0 | 0% | 0% |"])
    lines.append("")
    lines.append("## Token Share by Provider")
    lines.append("")
    lines.append("| Provider | Tokens | Share |")
    lines.append("|---|---:|---:|")
    lines.extend(top_providers_lines or ["| n/a | 0 | 0% |"])
    lines.append("")
    lines.append("## Runaway Session Candidates")
    lines.append("")
    if runaway_lines:
        lines.append("| Agent | Start Date | Runs in Session | First Raw Input | Peak Raw Input | Last Raw Input | Growth |")
        lines.append("|---|---|---:|---:|---:|---:|---:|")
        lines.extend(runaway_lines)
    else:
        lines.append("No runaway sessions detected with current threshold.")
    lines.append("")
    lines.append("## Optimization Strategy (Performance-Preserving)")
    lines.append("")
    lines.append("1. **Session budget guardrail**: rotate persisted session when either threshold is hit:")
    lines.append("   - raw input exceeds 250,000 tokens in a run, or")
    lines.append("   - 12 heartbeats on the same persisted session.")
    lines.append("2. **Carry forward compressed context**: before rotation, write a short structured summary (goal, decisions, open blockers, links) and feed only that summary + latest issue context into the new session.")
    lines.append("3. **Keep cold-start detail scoped**: continue using `heartbeat-context` and incremental comments (`after=<id>`) to avoid replaying full threads.")
    lines.append("4. **Weekly audit routine**: run this script every Monday and store report under `Business development/shared-workspace/intelligence/vita678/`.")
    lines.append("")
    lines.append("## Implementation Notes")
    lines.append("")
    lines.append("- This report is generated by `scripts/analyze_paperclip_token_usage.py`.")
    lines.append("- Internal issue link: [{0}-678](/{0}/issues/{0}-678)".format(company_prefix))

    return "\n".join(lines) + "\n"


def derive_company_prefix(issues_identifier: str | None) -> str:
    if not issues_identifier or "-" not in issues_identifier:
        return "VITA"
    return issues_identifier.split("-", 1)[0]


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze Paperclip token usage")
    parser.add_argument("--limit", type=int, default=1000, help="Heartbeat run sample size")
    parser.add_argument("--output", required=True, help="Markdown report output path")
    parser.add_argument(
        "--issue-identifier",
        default=os.getenv("PAPERCLIP_ISSUE_IDENTIFIER", "VITA-678"),
        help="Issue identifier for deep links (default: VITA-678)",
    )
    args = parser.parse_args()

    base_url = os.getenv("PAPERCLIP_API_URL")
    api_key = os.getenv("PAPERCLIP_API_KEY")
    company_id = os.getenv("PAPERCLIP_COMPANY_ID")

    missing = [
        name
        for name, value in (
            ("PAPERCLIP_API_URL", base_url),
            ("PAPERCLIP_API_KEY", api_key),
            ("PAPERCLIP_COMPANY_ID", company_id),
        )
        if not value
    ]
    if missing:
        print(f"Missing env vars: {', '.join(missing)}", file=sys.stderr)
        return 2

    client = PaperclipClient(base_url=base_url, api_key=api_key)
    runs = client.get_json(f"/api/companies/{company_id}/heartbeat-runs", {"limit": args.limit})
    agents = client.get_json(f"/api/companies/{company_id}/agents")

    generated = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    prefix = derive_company_prefix(args.issue_identifier)
    report = build_report(
        company_prefix=prefix,
        generated_utc=generated,
        limit=args.limit,
        runs=runs,
        agents=agents,
    )

    out_path = args.output
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Wrote report: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
