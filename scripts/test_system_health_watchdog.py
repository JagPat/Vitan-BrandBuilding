#!/usr/bin/env python3

import datetime as dt
import importlib.util
import sys
import unittest

from pathlib import Path


MODULE_PATH = Path(__file__).with_name("system_health_watchdog.py")
SPEC = importlib.util.spec_from_file_location("system_health_watchdog", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules["system_health_watchdog"] = MODULE
SPEC.loader.exec_module(MODULE)


class HealthClassificationTests(unittest.TestCase):
    def test_classify_healthy(self):
        self.assertEqual(MODULE.classify_health(age_sec=300, interval_sec=21600, stale_multiplier=2.0), "healthy")

    def test_classify_delayed(self):
        self.assertEqual(
            MODULE.classify_health(age_sec=22000, interval_sec=21600, stale_multiplier=2.0),
            "delayed",
        )

    def test_classify_stale(self):
        self.assertEqual(
            MODULE.classify_health(age_sec=50000, interval_sec=21600, stale_multiplier=2.0),
            "stale",
        )

    def test_classify_unknown(self):
        self.assertEqual(MODULE.classify_health(age_sec=None, interval_sec=21600, stale_multiplier=2.0), "unknown")


class CooldownTests(unittest.TestCase):
    def test_can_attempt_with_no_history(self):
        now = dt.datetime(2026, 4, 20, tzinfo=dt.timezone.utc)
        allowed, reason = MODULE.can_attempt_restart({}, now, 3600)
        self.assertTrue(allowed)
        self.assertIn("no previous restart", reason)

    def test_cooldown_blocks(self):
        now = dt.datetime(2026, 4, 20, 6, 0, 0, tzinfo=dt.timezone.utc)
        state = {"last_restart_at": "2026-04-20T05:30:00Z"}
        allowed, reason = MODULE.can_attempt_restart(state, now, 3600)
        self.assertFalse(allowed)
        self.assertIn("cooldown", reason)

    def test_cooldown_allows_after_threshold(self):
        now = dt.datetime(2026, 4, 20, 6, 0, 0, tzinfo=dt.timezone.utc)
        state = {"last_restart_at": "2026-04-20T04:00:00Z"}
        allowed, _reason = MODULE.can_attempt_restart(state, now, 3600)
        self.assertTrue(allowed)


if __name__ == "__main__":
    unittest.main()
