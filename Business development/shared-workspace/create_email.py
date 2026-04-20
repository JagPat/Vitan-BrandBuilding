#!/usr/bin/env python3
"""Compatibility wrapper for branded HTML email generation."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _resolve_paths() -> tuple[Path, Path]:
    this_file = Path(__file__).resolve()
    workspace_dir = this_file.parent
    repo_root = workspace_dir.parent.parent
    scripts_dir = repo_root / "scripts"
    return repo_root, scripts_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a branded outreach email HTML artifact for a contact."
    )
    parser.add_argument("contact_id", help="VIT contact identifier, for example VIT-C-001")
    parser.add_argument("--project", help="Optional explicit project name override")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Optional output directory. Defaults to shared-workspace/review/vita189",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    _, scripts_dir = _resolve_paths()
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))

    from branded_content_utils import artifact_name, ensure_output_dir, load_contact
    from generate_branded_email import build_email_html

    contact = load_contact(args.contact_id)
    output_dir = ensure_output_dir(args.output_dir)
    subject, email_html = build_email_html(args.contact_id, args.project)
    output_path = output_dir / artifact_name(contact, "branded-email", "html")
    output_path.write_text(email_html, encoding="utf-8")
    print(f"Generated {output_path}")
    print(f"Subject: {subject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
