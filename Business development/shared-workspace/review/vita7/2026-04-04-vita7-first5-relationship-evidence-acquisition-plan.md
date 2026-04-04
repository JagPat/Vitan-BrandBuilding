# VITA-7 First-5 Relationship Evidence Acquisition Plan

Date: 2026-04-04 (UTC)
Parent: [VITA-7](/VITA/issues/VITA-7)
Dependent execution: [VITA-133](/VITA/issues/VITA-133)
Baseline validation source: `shared-workspace/review/2026-04-03-vita155-first5-final-release-packet.md`

## Objective
Generate verifiable relationship/common-reference evidence for first-5 accounts so at least one row can move from `hold` to approval-ready.

## Problem Snapshot
Current status from latest release packet: `0 ready / 5 hold` because no row has validated relationship/reference support.

## Evidence Standard (row-level pass criteria)
A row can be re-submitted for release only if all are true:
1. Named recipient identity confirmed (name + role).
2. At least one verifiable relationship or common-reference line exists.
3. Evidence source is linkable and attributable (public profile, event roster, company release, or portfolio credit).
4. Personalized opener can cite the evidence without unverifiable claims.

## Priority Queue (by likely evidence accessibility)
1. Arvind SmartSpaces (`OUT-2026-0002`)
2. Shivalik Group (`OUT-2026-0003`)
3. HN Safal (`OUT-2026-0001`)
4. Goyal & Co. (`OUT-2026-0004`)
5. Iscon Group (`OUT-2026-0005`)

## Evidence Source Ladder (use in order)
1. Company leadership/team pages (recipient identity + role).
2. LinkedIn profile + company page overlap signals (shared organizations, collaborations, event intersections).
3. Public event participation pages (conference panels, architecture forums, award juries).
4. Project announcement pages with credited collaborators.
5. Press releases / trade coverage naming cross-firm collaboration or advisor links.

## Execution Packet to Produce
- `first5-evidence-log.csv` with columns:
  - account_id, company, recipient_name, recipient_role, evidence_type, source_url, evidence_quote_or_summary, confidence, usable_in_opener (yes/no)
- `first5-opener-rewrites.md` with one revised opener per row grounded only in validated evidence.
- `first5-readiness-delta.md` showing row movement: hold -> candidate-ready (or reason still blocked).

## Acceptance Criteria
- Minimum 2 rows upgraded from `hold` to `candidate-ready`, or explicit proof why no upgrade is currently possible.
- Every claimed relationship/reference line has a source URL.
- No unverifiable or inferred personal claims in opener copy.

## Governance
No outbound sending in this plan; this is evidence preparation only.
