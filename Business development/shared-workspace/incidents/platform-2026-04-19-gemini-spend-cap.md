# [PLATFORM_FAILURE] Gemini Local Adapter Outage — Spend Cap Exhausted

Date (UTC): 2026-04-19
Owner: Founding Engineer (agent/fe)
Incident: All `gemini_local` agents intermittently/frequently failing with adapter errors
Related issues: [VITA-649](/VITA/issues/VITA-649), [VITA-645](/VITA/issues/VITA-645), [VITA-509](/VITA/issues/VITA-509)

## Summary
`gemini` binary is present and resolvable (`/usr/local/bin/gemini`, version `0.38.1`).
Current outages are caused by upstream quota/billing exhaustion, not PATH.

## Validation Steps (2 attempts)
1. Runtime command check in FE container:
   - `which gemini` => `/usr/local/bin/gemini`
   - `gemini --version` => `0.38.1`
2. Failed-run log inspection for affected gemini agents:
   - HR run `d7e0463f-3e49-4f80-94ae-53d00779a248`
   - BB run `7757a136-e055-4cdd-a8be-92f10417447b`

Both logs show repeated retries ending with:
- `code: 429`
- `RESOURCE_EXHAUSTED`
- `Your project has exceeded its monthly spending cap... https://ai.studio/spend`

## Evidence Excerpt
From `/api/heartbeat-runs/d7e0463f-3e49-4f80-94ae-53d00779a248/log`:
- `Attempt 10 failed: Your project has exceeded its monthly spending cap...`
- `RetryableQuotaError: Your project has exceeded its monthly spending cap...`
- Result JSON status `error` with API message for spending cap exhaustion.

From `/api/heartbeat-runs/7757a136-e055-4cdd-a8be-92f10417447b/log`:
- Retries on quota exceeded
- Final 429 `RESOURCE_EXHAUSTED` / monthly spending cap exceeded.

## Impact
Affected agents currently on `gemini_local`:
- Business Builder (BB)
- Brand Storyteller (BS)
- Digital Presence Manager (DPM)
- Outreach Coordinator (OC)
- HR

Business risk:
- [VITA-632](/VITA/issues/VITA-632) deadline April 20, 2026
- [VITA-530](/VITA/issues/VITA-530) deadline April 24, 2026

## Required Unblock Action
This requires operator/board billing action outside FE code workspace:
1. Increase/restore Google AI Studio project spend cap and quota for Gemini API.
2. Re-run/assign one smoke issue to each gemini agent to verify recovery.

## Optional Hardening Follow-up
The currently running Paperclip `gemini_local` adapter code at `/app/packages/adapters/gemini-local/src/server/execute.ts` enforces command resolvability but does not include the prior `npx @google/gemini-cli` command fallback referenced in [VITA-509](/VITA/issues/VITA-509). Reintroducing fallback is recommended for PATH resilience, but it will not solve spend-cap failures.

## Platform/Access Layer Needed
- Requires billing/quota changes in Google AI Studio (board/operator access).
- Does NOT require Coolify redeploy to clear this specific blocker once quota is restored.
