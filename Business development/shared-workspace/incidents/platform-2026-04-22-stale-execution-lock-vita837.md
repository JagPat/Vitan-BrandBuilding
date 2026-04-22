# [PLATFORM_FAILURE] Stale `executionRunId` lock on VITA-837 despite terminal run

Date (UTC): 2026-04-22
Owner: Founding Engineer (agent/fe)
Related issues: [VITA-838](/VITA/issues/VITA-838), [VITA-837](/VITA/issues/VITA-837)

## Summary

Issue [VITA-837](/VITA/issues/VITA-837) has `executionRunId=a250a497-2baf-44df-b798-ab6ddad0183f` set, while that heartbeat run is terminal (`status=succeeded`, `finishedAt=2026-04-21T03:13:45.101Z`).

This stale execution lock causes checkout conflicts for other agents (PA and FE), blocking normal issue ownership flow.

## Evidence

- `GET /api/issues/1fa56b3f-6d3f-4af8-ba49-79d150145d6a`
  - `status=todo`
  - `assigneeAgentId=null`
  - `checkoutRunId=null`
  - `executionRunId=a250a497-2baf-44df-b798-ab6ddad0183f` (stale)
- `GET /api/heartbeat-runs/a250a497-2baf-44df-b798-ab6ddad0183f`
  - `status=succeeded`
  - `startedAt=2026-04-21T03:11:22.559Z`
  - `finishedAt=2026-04-21T03:13:45.101Z`

## Attempts

1. **Checkout attempt** on VITA-837:
   - `POST /api/issues/{id}/checkout`
   - Result: `409 Issue checkout conflict`
   - Conflict details include stale `executionRunId`.
2. **Release attempt** on VITA-837:
   - `POST /api/issues/{id}/release`
   - Result: `200 OK`, but `executionRunId` remains unchanged.
3. **Patch attempt** with `executionRunId=null` field:
   - `PATCH /api/issues/{id}`
   - Result: request accepted, comment added, but execution lock unchanged.

## Root Cause Classification

Platform-level issue in issue-lock lifecycle/reconciliation. FE cannot clear this stale `executionRunId` via normal agent API pathways.

## Required Unblock Action (PA/Board)

1. Clear stale `executionRunId` for VITA-837 at platform/admin level.
2. Verify lock cleanup behavior after terminal runs (`succeeded`/`failed`) for unassigned `todo` issues.
3. Re-run PA checkout on VITA-837 after lock clear.

## Impact

- PA watchdog/orchestration on VITA-837 is blocked by stale execution lock.
- FE cannot fully close VITA-838 handoff path tied to VITA-837 ownership flow.
