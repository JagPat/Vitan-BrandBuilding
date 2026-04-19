#!/usr/bin/env python3

import importlib.util
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("zoho-mail-workflow.py")
SPEC = importlib.util.spec_from_file_location("zoho_mail_workflow", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules["zoho_mail_workflow"] = MODULE
SPEC.loader.exec_module(MODULE)
is_board_bypass = MODULE.is_board_bypass
list_sent_messages = MODULE.list_sent_messages


class BoardBypassClassifierTests(unittest.TestCase):
    def test_board_sender_hr_only_pa_absent(self):
        result = is_board_bypass(
            sender="jp@vitan.in",
            recipients=["growthos+hr@vitan.in"],
            thread_root_recipients=[],
        )
        self.assertEqual(result, (True, ["HR"]))

    def test_board_sender_hr_and_pa(self):
        result = is_board_bypass(
            sender="jp@vitan.in",
            recipients=["growthos+hr@vitan.in", "growthos+pa@vitan.in"],
            thread_root_recipients=[],
        )
        self.assertEqual(result, (False, []))

    def test_board_sender_hr_only_but_root_has_pa(self):
        result = is_board_bypass(
            sender="jp@vitan.in",
            recipients=["growthos+hr@vitan.in"],
            thread_root_recipients=["pa@vitan.in"],
        )
        self.assertEqual(result, (False, []))

    def test_non_board_sender(self):
        result = is_board_bypass(
            sender="someone@example.com",
            recipients=["growthos+hr@vitan.in"],
            thread_root_recipients=[],
        )
        self.assertEqual(result, (False, []))

    def test_board_group_sender(self):
        result = is_board_bypass(
            sender="board@vitan.in",
            recipients=["growthos+hr@vitan.in"],
            thread_root_recipients=[],
        )
        self.assertEqual(result, (True, ["HR"]))


class ListSentMessagesTests(unittest.TestCase):
    def setUp(self):
        self.previous_fixture = os.environ.get("ZOHO_SENT_MESSAGES_FILE")
        self.tmp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        now = datetime.now(timezone.utc)
        fixture = [
            {
                "from": "growthos@vitan.in",
                "subject": "Recent message",
                "timestamp": int((now - timedelta(hours=2)).timestamp()),
                "snippet": "  hello\nworld  ",
            },
            {
                "from": "growthos@vitan.in",
                "subject": "Old message",
                "timestamp": int((now - timedelta(hours=30)).timestamp()),
                "snippet": "ignore me",
            },
        ]
        json.dump(fixture, self.tmp_file)
        self.tmp_file.close()
        os.environ["ZOHO_SENT_MESSAGES_FILE"] = self.tmp_file.name

    def tearDown(self):
        if self.previous_fixture is None:
            os.environ.pop("ZOHO_SENT_MESSAGES_FILE", None)
        else:
            os.environ["ZOHO_SENT_MESSAGES_FILE"] = self.previous_fixture
        Path(self.tmp_file.name).unlink(missing_ok=True)

    def test_list_sent_filters_by_hours(self):
        rows = list_sent_messages(24)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["subject"], "Recent message")
        self.assertEqual(rows[0]["from"], "growthos@vitan.in")
        self.assertEqual(rows[0]["body_snippet"], "hello world")


if __name__ == "__main__":
    unittest.main()
