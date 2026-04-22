#!/usr/bin/env python3

import datetime as dt
import importlib.util
import sys
import tempfile
import unittest

from pathlib import Path


MODULE_PATH = Path(__file__).with_name("asset_readiness_routine.py")
SPEC = importlib.util.spec_from_file_location("asset_readiness_routine", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules["asset_readiness_routine"] = MODULE
SPEC.loader.exec_module(MODULE)


class CalendarParseTests(unittest.TestCase):
    def test_parse_calendar_table(self):
        content = """# Submission Calendar\n\n| Submission | Deadline (UTC date) | Project Folder | Checklist Path | Notes |\n|---|---|---|---|---|\n| ArchDaily | 2026-05-10 | PRIVILON | Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/ASSET_CHECKLIST.md | sample |\n"""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "calendar.md"
            path.write_text(content, encoding="utf-8")
            entries = MODULE.parse_calendar(path)

        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].submission, "ArchDaily")
        self.assertEqual(entries[0].project_folder, "PRIVILON")
        self.assertEqual(entries[0].deadline, dt.date(2026, 5, 10))


class ReadinessEvalTests(unittest.TestCase):
    def test_evaluate_readiness_reports_gaps(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            photos_root = repo_root / "Business development/PHOTOS FOR SAMPLE PROJECT"
            project_dir = photos_root / "SEVENTY"
            project_dir.mkdir(parents=True)
            (project_dir / "sample.jpg").write_bytes(b"x")

            entries = [
                MODULE.SubmissionEntry(
                    submission="WAF",
                    deadline=dt.date(2026, 5, 1),
                    project_folder="SEVENTY",
                    checklist_path="Business development/PHOTOS FOR SAMPLE PROJECT/SEVENTY/ASSET_CHECKLIST.md",
                    notes="",
                )
            ]
            rows = MODULE.evaluate_readiness(
                entries=entries,
                photos_root=photos_root,
                repo_root=repo_root,
                today=dt.date(2026, 4, 20),
                horizon_days=60,
            )

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].photo_count, 1)
        self.assertFalse(rows[0].checklist_present)
        self.assertEqual(rows[0].status, "GAP")


if __name__ == "__main__":
    unittest.main()
