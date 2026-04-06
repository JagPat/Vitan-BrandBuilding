# Outbound Authority Normalization

Date: 2026-04-06 (UTC)
Issue: [VITA-299](/VITA/issues/VITA-299)
Related task: [VITA-298](/VITA/issues/VITA-298)
Owner: Business Builder

## Normalized Rule

`PA approved for outbound` now means Business Builder may execute the approved outreach directly on the named task when all of the following are true:

- the approved route is the canonical route recorded in the issue or review artifact
- the contact sensitivity is GREEN or AMBER
- no board comment or approval note explicitly retains board-side sending control
- no material copy, recipient, attachment, or channel change is introduced after approval

Board-side sending remains mandatory when any of the following is true:

- the contact sensitivity is RED
- the board or approval thread explicitly says the board will send
- relationship context, reputation risk, or channel control requires board ownership of the send

## Why This Changed

- [VITA-298](/VITA/issues/VITA-298) was blocked even after approved copy existed because shared references still implied a universal board-side Zoho send rule.
- Principle Architect then granted a task-specific execution exception on [VITA-298](/VITA/issues/VITA-298), proving the workflow needed a durable default instead of repeated one-off exceptions.
- This note normalizes that default so future approved GREEN and AMBER outreach can proceed without guessing.

## Implementation Note

- `Business development/shared-workspace/references/engagement-system.md` now defines the outbound authority split and replaces the blanket board-send workflow.
- `Business development/shared-workspace/references/publishing-protocol.md` now mirrors the same execution rule in the cross-channel publishing system.
- No wording change is required on open task [VITA-298](/VITA/issues/VITA-298); the existing PA exception is already consistent with the normalized rule.

## Sources Consulted

- [VITA-299](/VITA/issues/VITA-299) — scope, success criteria, and required deliverables for this normalization.
- [VITA-298](/VITA/issues/VITA-298) — showed the concrete execution stall and the later PA exception.
- [VITA-296](/VITA/issues/VITA-296) — source issue for the approved first-touch pack referenced by the blocked execution.
- `Business development/shared-workspace/review/vita298/2026-04-06-the-address-send-blocker.md` — documented the exact conflict between approval state and send authority.
- `Business development/shared-workspace/references/engagement-system.md` — contained the blanket board-send rule that caused the ambiguity.
- `Business development/shared-workspace/references/publishing-protocol.md` — repeated the same board-send assumption at the cross-channel workflow layer.
- `Business development/shared-workspace/references/sensitivity-protocol.md` — preserved RED-only mandatory board approval and autonomous-send limits.
