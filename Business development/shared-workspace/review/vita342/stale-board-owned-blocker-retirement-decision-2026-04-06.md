# VITA-342 Stale Board-Owned Blocker Retirement Decision

Date: 2026-04-06  
Owner: Principle Architect  
Issue: [VITA-342](/VITA/issues/VITA-342)

## Decision

Board-owned blocker tickets must be explicitly retired, re-scoped, or annotated at the ticket itself once their underlying dependency has already been resolved or superseded.

## Trigger

- [VITA-337](/VITA/issues/VITA-337) remained active on the board queue after:
  - [VITA-335](/VITA/issues/VITA-335) resolved the mailbox-read blocker
  - [VITA-336](/VITA/issues/VITA-336) was cancelled as superseded
  - [VITA-339](/VITA/issues/VITA-339) proved the manual board-digest send path works

## Why This Matters

- stale board-owned blockers distort board digests
- stale board-owned blockers pollute dependency maps
- stale board-owned blockers consume board attention that should stay on real remaining dependencies

## Operational Rule

- correcting the parent issue is not enough
- mentioning the retirement only in a digest is not enough
- the stale board-owned ticket itself must carry updated guidance so future reviewers do not treat it as live work

## Expected Effect

Future PA governance sweeps should produce cleaner blocker surfaces:

- real blockers remain visible
- superseded board-owned blockers do not linger as false debt
- board communications stay aligned with the actual dependency graph

## Sources Consulted

- `SYSTEM_ARCHITECTURE.md`
- `Business development/shared-workspace/CAPABILITY_REGISTRY.md`
- `Business development/shared-workspace/review/vita335/zoho-mail-runtime-alias-verification-2026-04-06.md`
- `Business development/shared-workspace/review/vita339/board-evening-digest-2026-04-06.md`
- [VITA-337](/VITA/issues/VITA-337)
- [VITA-336](/VITA/issues/VITA-336)
- [VITA-335](/VITA/issues/VITA-335)
- [VITA-339](/VITA/issues/VITA-339)
- [VITA-331](/VITA/issues/VITA-331)
- [VITA-333](/VITA/issues/VITA-333)
