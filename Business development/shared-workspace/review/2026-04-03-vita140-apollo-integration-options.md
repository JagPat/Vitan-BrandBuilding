# VITA-140 Apollo Integration Options for Business Builder

Date: 2026-04-03
Issue: [VITA-140](/VITA/issues/VITA-140)
Parent: [VITA-139](/VITA/issues/VITA-139)
Related execution window: [VITA-133](/VITA/issues/VITA-133) send window begins 2026-04-06 05:00 UTC

## Scope Assessed
Input queue and targeting notes reviewed:
- `Business development/shared-workspace/review/2026-04-03-vita133-apollo-enrichment-queue.csv`
- `Business development/shared-workspace/review/2026-04-03-vita133-deep-target-research-v2.md`

Current queue requires named decision-maker enrichment and direct-work-email validation for 9 target role rows across 5 accounts.

## Option Assessment

### Option 1: Apollo web workflow access only
- Speed to first enriched output: fastest if operator already has Apollo UI login.
- Engineering lift: low (no code changes required).
- Risks:
  - Low repeatability and low auditability (manual exports/imports).
  - Higher process variance between runs.
  - Weak fit for recurring Business Builder execution cadence.
- Fit for deadline: acceptable as emergency fallback to unblock the 2026-04-06 send window.

### Option 2: Apollo API key in runtime secrets + lightweight enrichment script
- Speed to reliable recurring execution: best balance.
- Engineering lift: moderate, but bounded.
- Advantages:
  - Scripted, repeatable enrichment from queue CSV.
  - Deterministic outputs and confidence/state update flow.
  - Reusable for future top-management cycles.
- Risks:
  - Requires one-time secure secret provisioning.
  - Requires API quota monitoring and error handling (rate limits/partial matches).
- Fit for deadline: strong if key is provisioned quickly.

### Option 3: Alternative provider already available in stack
- Current feasibility: not available right now.
- Evidence:
  - Runtime env currently exposes `SOCIAL_CREDENTIALS` and `GITHUB_PAT_VITAN`; no active enrichment-provider secret detected.
  - No existing enrichment module/provider wiring found in current workspace scope.
- Fit for deadline: not recommended for this send window without introducing new service + credential path.

## Recommendation
Recommend **Option 2** as the primary path, with **Option 1 fallback** if API key provisioning is delayed.

Rationale:
- Maintains speed while creating a reusable capability for repeated Business Builder campaigns.
- Avoids introducing a new external provider and associated approval/cost overhead before 2026-04-06.

## Secure Secret Handling
1. Store Apollo credential in Railway service env var (e.g. `APOLLO_API_KEY`) for Paperclip runtime.
2. Do not persist secret values in repo files, issue comments, logs, or artifacts.
3. Inject at runtime only; fail fast with explicit non-secret error when missing.
4. Add token health probe endpoint/script behavior:
   - classify `401/403` as credential-expired/invalid
   - raise `[ESCALATION]` issue with renewal instructions (no token echo)
5. Keep least-privilege usage:
   - use only required Apollo scopes/features
   - document renewal owner and rotation cadence in operational notes.

## Implementation Outline (Option 2)
1. Add enrichment script under Business Builder workspace (`scripts` or equivalent) to:
   - read queue CSV
   - query Apollo by domain + role filters
   - map best candidate(s) with confidence score
   - write enriched CSV/JSON artifact for approval/send routing.
2. Add provider adapter with retry/backoff + explicit status mapping (`ok`, `partial`, `not_found`, `auth_error`, `rate_limited`).
3. Add minimal tests for parser/mapping/merge logic.
4. Document runbook: command, required env, expected output schema, fallback manual path.

## ETA
Assuming Apollo API key is provisioned by board today (2026-04-03):
- 2-3 hours: script + adapter + output artifact generation.
- 1 hour: tests + runbook + dry-run verification on current queue.
- Total: **same-day delivery (~4 hours)**.

If key is not provisioned today:
- execute Option 1 manual web-enrichment fallback for current queue,
- then complete Option 2 implementation next available credential window.

## Decision Gate Needed
- Approve Option 2 and provide `APOLLO_API_KEY` in runtime env.
- Confirm whether first pass should enrich only the current 9 rows or include extended account list for the week.
