# Evidence Register

Internal-only. Phase 0. Markdown is the human source of truth.

One `evidence_id` per project packet. Nest claims under it. Do not add ARA, Parijaat Eclat, or Palladium-as-lead rows this cycle.

Photographer credit and photo/use permission may be filled only from a named Board/studio source packet. None exists for Privilon in this cycle — both stay **UNKNOWN**. Yaml `photography_permission: true` is not a named source packet. Yaml photographer text is not a named source packet and must not be printed as a credit.

## Schema

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`permission` is photo/use, not publish clearance. `review_date` is ISO date, Asia/Kolkata. `status` is one of: Board-verified | PA-locked | yaml-unverified | PENDING.

## Empty template notes

Copy the header row, then add one packet heading (`EV-…-001`) and only claims that have a Board/PA lock. Leave `permission` and `photographer_credit` as UNKNOWN unless a named Board/studio source packet exists. Do not invent GBA, performance claims, or other-architect public credit.

---

## EV-PRIVILON-001

| Field | Value |
| --- | --- |
| evidence_id | EV-PRIVILON-001 |
| project | Privilon |
| campaign (context, not a claim) | CAMP-2026-09-001 |
| internal id (context, not a claim) | VITA-458 |
| yaml (candidate only, not proof) | `Business development/shared-workspace/intelligence/projects/privilon.yaml` |
| record status | internal / awaiting Growth Lead approval |
| permission | UNKNOWN |
| photographer_credit | UNKNOWN |
| architect_credit_public | Lead architect Ar. Jagrut Patel, Vitan Architects |
| architect_credit_internal | Not for public copy. Do not copy yaml collaborators into public columns. |
| packet confidence | mixed (identity claims below are locked; photographer and permission UNKNOWN) |
| review_date | 2026-09-01 (Asia/Kolkata) |
| expiry_or_hold_notes | Phase 0 row is tight to the three public-yes claims below. No GBA. No other-architect names in public fields. Tranquil is a Board cut. Do not add floors, year, client, street address, CTA, hashtags, still numbers, or consultant names as public-yes claims in this row. |

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-PRIVILON-001 | Privilon | Project name is Privilon | locked CAMP-2026-09-001 / Board credit rule | UNKNOWN | UNKNOWN | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-09-01 | |
| EV-PRIVILON-001 | Privilon | Board credit line: Lead architect Ar. Jagrut Patel, Vitan Architects | locked CAMP-2026-09-001 / Board credit rule | UNKNOWN | UNKNOWN | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-09-01 | No other architect or collaboration line in public copy |
| EV-PRIVILON-001 | Privilon | Mixed-use, Ahmedabad | locked CAMP-2026-09-001 / Board credit rule | UNKNOWN | UNKNOWN | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-09-01 | Do not expand to street address or extra identity facts in this Phase 0 row |
