# Evidence Register

Internal-only. Phase 0. Markdown is the human source of truth.

One `evidence_id` per project packet. Nest claims under it. Do not add ARA, Parijaat Eclat, or Palladium-as-lead rows this cycle.

Photographer, client permission, and photo permission may be filled only from a named Board/studio source packet. None exists for Privilon in this cycle — all three stay **UNKNOWN**. Do not invent a yes. Yaml `photography_permission: true` is not a named source packet. Yaml photographer text is not a named source packet and must not be printed as a credit.

Do not treat a colliding blob as project evidence. Catalog scan is git blob SHA on `main`.

## Schema

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`permission` is photo/use, not publish clearance. `review_date` is ISO date, Asia/Kolkata. `status` is one of: Board-verified | PA-locked | yaml-unverified | PENDING.

## Empty template notes

Copy the header row, then add one packet heading (`EV-…-001`) and only claims that have a Board/PA lock. Leave photographer, client permission, and photo permission as UNKNOWN unless a named Board/studio source packet exists. Do not invent GBA, performance claims, or other-architect public credit. Asset paths are internal notes, not public-yes claims.

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
| photographer | UNKNOWN |
| client permission | UNKNOWN |
| photo permission | UNKNOWN |
| architect_credit_public | Lead architect Ar. Jagrut Patel, Vitan Architects |
| architect_credit_internal | Not for public copy. Do not copy yaml collaborators into public columns. |
| packet confidence | mixed (identity claims below are locked; photographer, client permission, and photo permission UNKNOWN) |
| review_date | 2026-09-01 (Asia/Kolkata) |
| expiry_or_hold_notes | Phase 0 row is tight to the three public-yes claims below. No GBA. No other-architect names in public fields. Tranquil is a Board cut. Do not add floors, year, client, street address, CTA, hashtags, still numbers, or consultant names as public-yes claims in this row. Do not invent a yes for photographer or permissions. |

### Internal asset notes (not public-yes claims)

2 Sep already-approved still, path only: `Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (16).jpg` (git blob SHA `aa243aca071854bf01a1ca43eaab72aae6acc91d` on `main`). Same blob also at `PRIVILON/FOR BOOK/Privilon (16).jpg` (same project, not a cross-project collision). It does not match any PARIJAAT / PARIJAAT ECLAT blob. Keep as the 2 Sep asset. Do not invent a Distribution row.

Do not use `PRIVILON/Privilon (10).jpg` as the 2 Sep still. Do not treat that file as Privilon evidence. Blob SHA `4adf8154b3cced5a32dc42d748522f05a8ace107` is identical to `PARIJAAT ECLAT/Privilon (10).jpg` and `PARIJAAT/PAARIJAT ECLAT (1).jpg`.

Other `PRIVILON/` files on `main` that do not collide with Parijaat: (2)(6)(12)(13)(14)(15)(16)(17)(23)(26)(29)(54). Only (10) collides. Non-collision is not photo clearance and is not a public-yes claim.

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-PRIVILON-001 | Privilon | Project name is Privilon | locked CAMP-2026-09-001 / Board credit rule | UNKNOWN | UNKNOWN | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-09-01 | |
| EV-PRIVILON-001 | Privilon | Board credit line: Lead architect Ar. Jagrut Patel, Vitan Architects | locked CAMP-2026-09-001 / Board credit rule | UNKNOWN | UNKNOWN | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-09-01 | No other architect or collaboration line in public copy |
| EV-PRIVILON-001 | Privilon | Mixed-use, Ahmedabad | locked CAMP-2026-09-001 / Board credit rule | UNKNOWN | UNKNOWN | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-09-01 | Do not expand to street address or extra identity facts in this Phase 0 row |
