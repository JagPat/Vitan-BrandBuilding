# VITA-374 Implementation Summary

## What FE Implemented

- Added watchdog script: `scripts/system_health_watchdog.py`
- Added unit tests: `scripts/test_system_health_watchdog.py`
- Generated live health artifacts:
  - `Business development/shared-workspace/review/vita374/agent-health-status.md`
  - `Business development/shared-workspace/review/vita374/agent-health-status.json`
- Added persistent state tracking for restart cooldown/failure escalation:
  - `Business development/shared-workspace/intelligence/system-health-watchdog-state.json`

## Acceptance Criteria Mapping

1. **PA detects crashed agents via heartbeat-age checks**
- Implemented in watchdog script using Paperclip API `/api/companies/{companyId}/agents`.
- Health classes: `healthy`, `delayed`, `stale`, `unknown`.
- Default stale rule: `age > interval * 2` with configurable flags.

2. **Board digest includes agent health status**
- Script emits a `Board Digest Health Block` line in markdown output for direct paste into digest.

3. **Email works even when FE is down**
- Script does not depend on FE bundle-generated content files.
- Escalation email path is direct Zoho API based (`ZOHO_*` env vars), independent of branded email/PDF generators.

4. **PA can trigger Railway restart**
- Optional `--attempt-self-repair` mode triggers restart through:
  - `RAILWAY_REDEPLOY_WEBHOOK_URL`, or
  - Railway GraphQL API credentials (`RAILWAY_API_TOKEN` + ids).
- Guardrail: cooldown default `3600s` (max one restart per hour).

5. **Escalation email fires after failed self-repair**
- Failed restart attempts are persisted in state.
- Escalation triggers after `--escalate-after-failures` threshold (default: `2`).

## Runtime Example

```bash
python3 scripts/system_health_watchdog.py --attempt-self-repair
```

- Without `--attempt-self-repair`, script only audits and writes health outputs.
- Current run status: no stale agents detected.
