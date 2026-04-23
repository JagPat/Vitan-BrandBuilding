#!/usr/bin/env python3

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("zoho-mail-workflow.py")
SPEC = importlib.util.spec_from_file_location("zoho_mail_workflow", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules["zoho_mail_workflow"] = MODULE
SPEC.loader.exec_module(MODULE)
is_board_bypass = MODULE.is_board_bypass


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


if __name__ == "__main__":
    unittest.main()
