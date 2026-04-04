# VITA-7 First-5 Named Recipient Resolution Sprint Plan

Date: 2026-04-04 (UTC)
Parent: [VITA-7](/VITA/issues/VITA-7)
Execution issue: [VITA-161](/VITA/issues/VITA-161)

## Objective
Resolve named recipient identity and route confidence for first-5 hold rows, then refresh readiness scoring without executing outbound sends.

## Working Targets
1. HN Safal (`OUT-2026-0001`)
2. Goyal & Co. (`OUT-2026-0004`)
3. Iscon Group (`OUT-2026-0005`)

## Method
1. Reuse VITA-160 evidence baseline and QA blockers.
2. Validate named leaders from first-party public pages where possible.
3. Map each account to primary + fallback route with ownership confidence.
4. Rewrite hold-row openers only with verifiable evidence.
5. Publish updated delta (`candidate-ready` vs `hold`) for release-gate use in [VITA-133](/VITA/issues/VITA-133).

## Deliverables
- `Business development/shared-workspace/review/2026-04-04-vita161-first5-recipient-candidate-log.csv`
- `Business development/shared-workspace/review/2026-04-04-vita161-first5-recipient-route-validation.md`
- `Business development/shared-workspace/review/2026-04-04-vita161-first5-hold-row-opener-rewrites.md`
- `Business development/shared-workspace/review/2026-04-04-vita161-first5-readiness-delta-v2.md`

## Governance
No outbound send execution in this sprint.
