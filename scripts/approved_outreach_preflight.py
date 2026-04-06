#!/usr/bin/env python3
"""Validate the minimum prerequisites for an approved BB outreach send."""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path

CANONICAL_SENDER_ROUTE = "jp@vitan.in"
CANONICAL_REPLY_ROUTE = "connect@vitan.in"
DEFAULT_CONTACTS_CSV = Path("Business development/shared-workspace/contacts-master.csv")


@dataclass(frozen=True)
class CheckResult:
    status: str
    label: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contact-id", required=True, help="Contact identifier from contacts-master.csv")
    parser.add_argument("--issue", required=True, help="Issue identifier for the live send, for example VITA-298")
    parser.add_argument(
        "--approved-artifact",
        required=True,
        type=Path,
        help="Approved review pack or note that authorizes the send",
    )
    parser.add_argument(
        "--execution-artifact",
        required=True,
        type=Path,
        help="Planned execution log path that will be updated after the send",
    )
    parser.add_argument("--recipient-route", required=True, help="Email address that will receive this send")
    parser.add_argument(
        "--sensitivity",
        required=True,
        choices=("green", "amber", "red"),
        help="Normalized sensitivity level for the contact",
    )
    parser.add_argument(
        "--discovery-status",
        default="complete",
        choices=("complete", "partial", "undiscovered"),
        help="Discovery status from the sensitivity protocol",
    )
    parser.add_argument(
        "--approved-for-outbound",
        action="store_true",
        help="Set when the issue or approval thread explicitly approved outbound execution",
    )
    parser.add_argument(
        "--board-retains-control",
        action="store_true",
        help="Set when the board explicitly kept send ownership on this task",
    )
    parser.add_argument(
        "--material-change",
        default="none",
        choices=("none", "copy", "recipient", "attachment", "channel", "multiple"),
        help="Whether anything material changed after approval",
    )
    parser.add_argument(
        "--sender-route",
        default=CANONICAL_SENDER_ROUTE,
        help="Authenticated sender route expected by the canonical path",
    )
    parser.add_argument(
        "--reply-route",
        default=CANONICAL_REPLY_ROUTE,
        help="Reply handling route expected by the canonical path",
    )
    parser.add_argument(
        "--contacts-csv",
        type=Path,
        default=DEFAULT_CONTACTS_CSV,
        help="Path to contacts-master.csv",
    )
    parser.add_argument("--output", type=Path, help="Optional markdown output path for the preflight report")
    return parser.parse_args()


def load_contact_row(path: Path, contact_id: str) -> dict[str, str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("Contact ID", "").strip() == contact_id:
                return {key: (value or "").strip() for key, value in row.items()}
    raise KeyError(contact_id)


def build_results(args: argparse.Namespace, contact: dict[str, str]) -> list[CheckResult]:
    results: list[CheckResult] = []

    if args.approved_for_outbound:
        results.append(CheckResult("PASS", "Approval state", "Outbound approval was explicitly confirmed."))
    else:
        results.append(
            CheckResult(
                "FAIL",
                "Approval state",
                "Missing `--approved-for-outbound`; do not send until the issue or approval thread says so.",
            )
        )

    if args.board_retains_control:
        results.append(
            CheckResult(
                "FAIL",
                "Authority split",
                "Board-side send ownership is still active for this task.",
            )
        )
    else:
        results.append(
            CheckResult(
                "PASS",
                "Authority split",
                "Board-side send ownership is not retained on this task.",
            )
        )

    if args.sensitivity == "red":
        results.append(
            CheckResult(
                "FAIL",
                "Sensitivity",
                "RED sensitivity requires board-side approval and send control.",
            )
        )
    else:
        results.append(
            CheckResult(
                "PASS",
                "Sensitivity",
                f"{args.sensitivity.upper()} sensitivity is eligible for BB execution under the normalized rule.",
            )
        )

    if args.discovery_status == "complete":
        results.append(CheckResult("PASS", "Discovery status", "Discovery is marked complete."))
    else:
        results.append(
            CheckResult(
                "WARN",
                "Discovery status",
                f"Discovery is `{args.discovery_status}`; confirm the board is comfortable with the current context.",
            )
        )

    if args.approved_artifact.is_file():
        results.append(
            CheckResult(
                "PASS",
                "Approved artifact",
                f"Found `{args.approved_artifact}`.",
            )
        )
    else:
        results.append(
            CheckResult(
                "FAIL",
                "Approved artifact",
                f"Missing `{args.approved_artifact}`.",
            )
        )

    execution_parent = args.execution_artifact.parent
    if execution_parent.exists():
        detail = f"Execution artifact parent exists at `{execution_parent}`."
        if args.execution_artifact.exists():
            detail += " The file already exists, so update it carefully instead of overwriting blindly."
            results.append(CheckResult("WARN", "Execution log path", detail))
        else:
            results.append(CheckResult("PASS", "Execution log path", detail))
    else:
        results.append(
            CheckResult(
                "FAIL",
                "Execution log path",
                f"Parent folder `{execution_parent}` does not exist.",
            )
        )

    allowed_routes = {
        contact.get("Email (Primary)", "").strip(),
        contact.get("Email (Fallback)", "").strip(),
    }
    allowed_routes.discard("")
    if args.recipient_route in allowed_routes:
        results.append(
            CheckResult(
                "PASS",
                "Recipient route",
                f"`{args.recipient_route}` matches the contact record for `{contact.get('Company', args.contact_id)}`.",
            )
        )
    else:
        results.append(
            CheckResult(
                "FAIL",
                "Recipient route",
                f"`{args.recipient_route}` is not in contacts-master for `{args.contact_id}`.",
            )
        )

    if args.sender_route == CANONICAL_SENDER_ROUTE and args.reply_route == CANONICAL_REPLY_ROUTE:
        results.append(
            CheckResult(
                "PASS",
                "Canonical routes",
                f"Sender `{args.sender_route}` and reply route `{args.reply_route}` match the canonical path.",
            )
        )
    else:
        results.append(
            CheckResult(
                "FAIL",
                "Canonical routes",
                "The send is not using the expected canonical sender/reply route pair.",
            )
        )

    if args.material_change == "none":
        results.append(
            CheckResult(
                "PASS",
                "Material change",
                "No material copy, recipient, attachment, or channel change was introduced after approval.",
            )
        )
    else:
        results.append(
            CheckResult(
                "FAIL",
                "Material change",
                f"`{args.material_change}` changed after approval; return this send to board review first.",
            )
        )

    recorded_issue = contact.get("VITA Issue", "")
    if recorded_issue and recorded_issue != args.issue:
        results.append(
            CheckResult(
                "WARN",
                "Contact linkage",
                f"contacts-master currently points to `{recorded_issue}` instead of `{args.issue}`.",
            )
        )
    else:
        results.append(
            CheckResult(
                "PASS",
                "Contact linkage",
                "Issue linkage in contacts-master is aligned or not yet recorded.",
            )
        )

    return results


def render_report(args: argparse.Namespace, contact: dict[str, str], results: list[CheckResult]) -> str:
    status_order = {"FAIL": 0, "WARN": 1, "PASS": 2}
    overall = min(results, key=lambda item: status_order[item.status]).status

    lines = [
        "# Approved Outbound Preflight",
        "",
        f"- Overall: **{overall}**",
        f"- Issue: `{args.issue}`",
        f"- Contact: `{args.contact_id}` ({contact.get('Company', 'Unknown company')})",
        f"- Recipient route: `{args.recipient_route}`",
        f"- Approved artifact: `{args.approved_artifact}`",
        f"- Planned execution log: `{args.execution_artifact}`",
        "",
        "## Check Results",
    ]

    for result in results:
        lines.append(f"- {result.status}: **{result.label}** — {result.detail}")

    lines.extend(
        [
            "",
            "## Post-Send Logging Requirements",
            "- Record `Sent at`, `Authenticated sender route`, `Reply handling route`, `Message-ID`, and attachment state in the execution note.",
            "- Update `Business development/shared-workspace/contacts-master.csv` with `Last Contacted`, `Response Status`, `Follow-up Date`, and `Draft Message Status`.",
            "- Link the approved pack and the live execution issue in the execution artifact so the next send does not rely on issue-thread archaeology.",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()

    try:
        contact = load_contact_row(args.contacts_csv, args.contact_id)
    except FileNotFoundError:
        print(f"ERROR: contacts file not found: {args.contacts_csv}", file=sys.stderr)
        return 2
    except KeyError:
        print(f"ERROR: contact `{args.contact_id}` not found in {args.contacts_csv}", file=sys.stderr)
        return 2

    results = build_results(args, contact)
    report = render_report(args, contact, results)
    print(report, end="")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")

    if any(result.status == "FAIL" for result in results):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
