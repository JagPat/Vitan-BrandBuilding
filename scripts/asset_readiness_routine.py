#!/usr/bin/env python3
"""Pre-deadline asset-readiness routine for BB standup visibility.

Reads the submission calendar, checks project photo/checklist readiness for entries
within a configurable horizon, and posts a markdown table to the most recent BB
standup issue in Paperclip.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import os
from pathlib import Path
from typing import Iterable

import requests


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CALENDAR_PATH = REPO_ROOT / "Business development/shared-workspace/references/submission-calendar.md"
DEFAULT_PHOTOS_ROOT = REPO_ROOT / "Business development/PHOTOS FOR SAMPLE PROJECT"
ASSET_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}


@dataclasses.dataclass
class SubmissionEntry:
    submission: str
    deadline: dt.date
    project_folder: str
    checklist_path: str
    notes: str


@dataclasses.dataclass
class ReadinessRow:
    submission: str
    deadline: dt.date
    days_left: int
    project_folder: str
    photo_count: int
    checklist_present: bool
    status: str
    gaps: str


class PaperclipClient:
    def __init__(self, api_url: str, api_key: str, run_id: str):
        self.api_url = api_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {api_key}"})
        self.run_id = run_id

    def get_json(self, path: str, params: dict[str, str] | None = None):
        response = self.session.get(f"{self.api_url}{path}", params=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def patch_issue_comment(self, issue_id: str, comment: str) -> None:
        response = self.session.patch(
            f"{self.api_url}/api/issues/{issue_id}",
            headers={"X-Paperclip-Run-Id": self.run_id, "Content-Type": "application/json"},
            json={"comment": comment},
            timeout=30,
        )
        response.raise_for_status()


def parse_date(value: str) -> dt.date:
    return dt.datetime.strptime(value.strip(), "%Y-%m-%d").date()


def parse_calendar(path: Path) -> list[SubmissionEntry]:
    text = path.read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return []

    entries: list[SubmissionEntry] = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        deadline_raw = cells[1]
        if not deadline_raw:
            continue
        entries.append(
            SubmissionEntry(
                submission=cells[0],
                deadline=parse_date(deadline_raw),
                project_folder=cells[2],
                checklist_path=cells[3],
                notes=cells[4],
            )
        )
    return entries


def collect_photo_count(project_dir: Path) -> int:
    if not project_dir.exists() or not project_dir.is_dir():
        return 0
    count = 0
    for path in project_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in ASSET_EXTENSIONS:
            count += 1
    return count


def evaluate_readiness(
    entries: Iterable[SubmissionEntry],
    photos_root: Path,
    repo_root: Path,
    today: dt.date,
    horizon_days: int,
) -> list[ReadinessRow]:
    horizon = today + dt.timedelta(days=horizon_days)
    rows: list[ReadinessRow] = []

    for entry in entries:
        if not (today <= entry.deadline <= horizon):
            continue

        project_dir = photos_root / entry.project_folder
        checklist_path = repo_root / entry.checklist_path
        photo_count = collect_photo_count(project_dir)
        checklist_present = checklist_path.exists() and checklist_path.is_file()

        gaps: list[str] = []
        if not project_dir.exists():
            gaps.append("project folder missing")
        if photo_count == 0:
            gaps.append("no photos found")
        if not checklist_present:
            gaps.append("ASSET_CHECKLIST missing")

        status = "READY" if not gaps else "GAP"
        rows.append(
            ReadinessRow(
                submission=entry.submission,
                deadline=entry.deadline,
                days_left=(entry.deadline - today).days,
                project_folder=entry.project_folder,
                photo_count=photo_count,
                checklist_present=checklist_present,
                status=status,
                gaps=", ".join(gaps) if gaps else "none",
            )
        )

    rows.sort(key=lambda item: item.deadline)
    return rows


def find_current_bb_standup_issue(client: PaperclipClient, company_id: str) -> dict:
    agents = client.get_json(f"/api/companies/{company_id}/agents")
    bb_agent = next((item for item in agents if (item.get("name") or "").lower() == "business builder"), None)
    if not bb_agent:
        raise RuntimeError("Business Builder agent not found")

    issues = client.get_json(
        f"/api/companies/{company_id}/issues",
        params={"assigneeAgentId": bb_agent["id"], "limit": "300"},
    )

    standups = [
        issue
        for issue in issues
        if "[STANDUP]" in (issue.get("title") or "") and issue.get("status") not in {"cancelled"}
    ]
    if not standups:
        raise RuntimeError("No BB standup issue found")

    standups.sort(key=lambda issue: issue.get("updatedAt") or "", reverse=True)
    return standups[0]


def build_comment(rows: list[ReadinessRow], calendar_path: Path, horizon_days: int, now_utc: dt.datetime) -> str:
    lines = [
        "## Asset Readiness Probe",
        "",
        f"Generated (UTC): `{now_utc.isoformat().replace('+00:00', 'Z')}`",
        f"Source calendar: `{calendar_path}`",
        f"Window: deadlines within next `{horizon_days}` days",
        "",
    ]

    if not rows:
        lines.extend([
            "No submission deadlines are due within the configured window.",
            "",
            "Action: keep `submission-calendar.md` current so the monthly probe can surface gaps early.",
        ])
        return "\n".join(lines)

    ready_count = sum(1 for row in rows if row.status == "READY")
    gap_count = len(rows) - ready_count
    lines.extend(
        [
            f"Summary: `{len(rows)}` upcoming submissions, `{ready_count}` ready, `{gap_count}` with gaps.",
            "",
            "| Submission | Deadline (UTC date) | Days Left | Project Folder | Photo Files | ASSET_CHECKLIST.md | Status | Gaps |",
            "|---|---:|---:|---|---:|---|---|---|",
        ]
    )

    for row in rows:
        lines.append(
            "| {submission} | {deadline} | {days_left} | {folder} | {photos} | {checklist} | {status} | {gaps} |".format(
                submission=row.submission,
                deadline=row.deadline.isoformat(),
                days_left=row.days_left,
                folder=row.project_folder,
                photos=row.photo_count,
                checklist="yes" if row.checklist_present else "no",
                status=row.status,
                gaps=row.gaps,
            )
        )

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Post pre-deadline asset-readiness status to current BB standup.")
    parser.add_argument("--calendar", default=str(DEFAULT_CALENDAR_PATH), help="Path to submission-calendar.md")
    parser.add_argument("--horizon-days", type=int, default=60, help="Future deadline horizon in days")
    parser.add_argument("--dry-run", action="store_true", help="Print markdown instead of posting comment")
    parser.add_argument("--api-url", default=os.getenv("PAPERCLIP_API_URL", ""), help="Paperclip API URL")
    parser.add_argument("--api-key", default=os.getenv("PAPERCLIP_API_KEY", ""), help="Paperclip API key")
    parser.add_argument("--company-id", default=os.getenv("PAPERCLIP_COMPANY_ID", ""), help="Paperclip company id")
    parser.add_argument("--run-id", default=os.getenv("PAPERCLIP_RUN_ID", ""), help="Paperclip run id")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    for name, value in (("api-url", args.api_url), ("api-key", args.api_key), ("company-id", args.company_id), ("run-id", args.run_id)):
        if not value:
            raise SystemExit(f"Missing required value: --{name} or matching PAPERCLIP_* env var")

    calendar_path = Path(args.calendar).resolve()
    if not calendar_path.exists():
        raise SystemExit(f"Calendar file not found: {calendar_path}")

    now_utc = dt.datetime.now(dt.timezone.utc)
    entries = parse_calendar(calendar_path)
    rows = evaluate_readiness(
        entries=entries,
        photos_root=DEFAULT_PHOTOS_ROOT,
        repo_root=REPO_ROOT,
        today=now_utc.date(),
        horizon_days=args.horizon_days,
    )

    comment = build_comment(rows=rows, calendar_path=calendar_path.relative_to(REPO_ROOT), horizon_days=args.horizon_days, now_utc=now_utc)

    if args.dry_run:
        print(comment)
        return 0

    client = PaperclipClient(api_url=args.api_url, api_key=args.api_key, run_id=args.run_id)
    standup_issue = find_current_bb_standup_issue(client, args.company_id)
    client.patch_issue_comment(issue_id=standup_issue["id"], comment=comment)

    print(
        "Posted asset-readiness comment to BB standup: "
        f"{standup_issue.get('identifier')} ({standup_issue.get('id')})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
