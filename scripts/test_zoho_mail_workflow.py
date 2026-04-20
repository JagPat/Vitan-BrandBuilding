#!/usr/bin/env python3

import importlib.util
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock


MODULE_PATH = Path(__file__).with_name("zoho-mail-workflow.py")
SPEC = importlib.util.spec_from_file_location("zoho_mail_workflow", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules["zoho_mail_workflow"] = MODULE
SPEC.loader.exec_module(MODULE)
is_board_bypass = MODULE.is_board_bypass
list_sent_messages = MODULE.list_sent_messages
fetch_messages = MODULE.fetch_messages
resolve_messages_url = MODULE.resolve_messages_url


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


class FetchMessagesTests(unittest.TestCase):
    def test_resolve_messages_url_from_account_and_folder(self):
        with mock.patch.dict(
            os.environ,
            {
                "ZOHO_MAIL_ACCOUNT_ID": "acct-123",
                "ZOHO_MAIL_INBOX_FOLDER_ID": "folder-456",
            },
            clear=False,
        ):
            with mock.patch.object(MODULE, "ZOHO_MAIL_MESSAGES_URL", ""):
                with mock.patch.object(MODULE, "ZOHO_MAIL_MESSAGES_LIMIT", "20"):
                    url = resolve_messages_url()
        self.assertEqual(
            url,
            "https://mail.zoho.in/api/accounts/acct-123/messages/view?folderId=folder-456&limit=20",
        )

    def test_fetch_messages_uses_resolved_url_when_explicit_url_missing(self):
        payload = {
            "messages": [
                {
                    "messageId": "mid-1",
                    "threadId": "tid-1",
                    "from": "jp@vitan.in",
                    "to": ["growthos+pa@vitan.in"],
                    "subject": "hello",
                }
            ]
        }
        fake_response = mock.Mock()
        fake_response.json.return_value = payload
        fake_response.raise_for_status.return_value = None

        with mock.patch.object(MODULE, "ZOHO_MAIL_MESSAGES_URL", ""):
            with mock.patch.dict(
                os.environ,
                {
                    "ZOHO_MAIL_ACCOUNT_ID": "acct-123",
                    "ZOHO_MAIL_INBOX_FOLDER_ID": "folder-456",
                },
                clear=False,
            ):
                with mock.patch.object(MODULE, "get_access_token", return_value="token-1"):
                    with mock.patch.object(MODULE.requests, "get", return_value=fake_response) as get_mock:
                        messages = fetch_messages()

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message_id, "mid-1")
        self.assertIn("accounts/acct-123/messages/view?folderId=folder-456", get_mock.call_args[0][0])

    def test_fetch_messages_accepts_data_key_payload(self):
        payload = {
            "data": [
                {
                    "message_id": "mid-2",
                    "thread_id": "tid-2",
                    "from": "jp@vitan.in",
                    "to": ["growthos+pa@vitan.in"],
                    "subject": "hello-2",
                }
            ]
        }
        fake_response = mock.Mock()
        fake_response.json.return_value = payload
        fake_response.raise_for_status.return_value = None

        with mock.patch.object(MODULE, "ZOHO_MAIL_MESSAGES_URL", "https://mail.zoho.in/api/custom"):
            with mock.patch.object(MODULE, "get_access_token", return_value="token-1"):
                with mock.patch.object(MODULE.requests, "get", return_value=fake_response):
                    messages = fetch_messages()

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message_id, "mid-2")


if __name__ == "__main__":
    unittest.main()
