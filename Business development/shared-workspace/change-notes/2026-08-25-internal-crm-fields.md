# Internal CRM fields on contacts-master / no outbound

Date: 2026-08-25
Owner: Business Builder
Authority: Internal CRM only — sheet schema / no outbound / do not merge

## What changed

- `contacts-master.csv` only. No emails drafted or sent. No Stage-1. Do not send.
- Appended nine empty/mapped columns after existing fields: Last meaningful interaction, Stage-entered date, Stalled reason, Disqualification reason, Estimated decision date, Procurement route, Competing option, Permission / contact restrictions, Pipeline bucket.
- Kept all existing columns and rows VIT-C-001–021. No HOLD rows were present. No existing contact fields were rewritten (emails, stages, notes, dates unchanged).
- Filled **Pipeline bucket** only from existing Relationship Stage / Draft Message Status / Notes / sector:
  - VIT-C-006 The Address, VIT-C-007 DevX → `dormant` (already dormant / sent; notes say mark dormant)
  - VIT-C-008 Karma Workspaces → `hold` (PA hold April draft)
  - VIT-C-017–021 owner-occupier → `nurture`
  - remaining VIT-C-001–016 still cold/enriching → `unverified`
- Left the other eight new fields empty. Did not invent dates, competitors, stalled reasons, or personal emails.
- No row marked `active qualified`. No row marked `stalled` (no stalled reason exists in notes).

## Out of scope

- No outbound. Do not send. Do not merge.
- Did not change Email (Primary/Fallback) or invent personal inboxes.
