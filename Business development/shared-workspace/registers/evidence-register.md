# Evidence Register

Internal-only. Phase 0. Markdown is the human source of truth.

One `evidence_id` per project packet. Nest claims under it. Do not add ARA, Parijaat Eclat, or Palladium-as-lead rows this cycle.

Photographer, client permission, and photo permission may be filled only from a named Board/studio source packet. Yaml `photography_permission: true` is not a named source packet. Yaml photographer text is not a named source packet and must not be printed as a credit.

Board lock 2026-08-25 (Vitan Growth Lead / Board): Vitan-led projects — studio already has permission; architect holds project IP. UNKNOWN is the template default until a Board lock exists. After that lock, do not keep client/photographer as UNKNOWN as a publish blocker on Vitan-led studio stills. Photographer third-party credit is none required when the still is studio/Vitan-led. Courtesy rule: if a still is later shown not to be ours, or if we ever use non-studio content, name the source. Do not invent photographer names.

Do not treat a colliding blob as project evidence. Catalog scan is git blob SHA on `main`.

## Schema

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`permission` is photo/use, not publish clearance. `review_date` is ISO date, Asia/Kolkata. `status` is one of: Board-verified | PA-locked | yaml-unverified | PENDING.

## Empty template notes

Copy the header row, then add one packet heading (`EV-…-001`) and only claims that have a Board/PA lock. UNKNOWN is the default for photographer, client permission, and photo permission until a Board lock exists. After Board lock 2026-08-25, do not treat UNKNOWN as a publish blocker on Vitan-led studio stills. Photographer third-party credit is none required for studio stills; courtesy-credit a named source only if the still is not ours. Do not invent GBA, performance claims, or other-architect public credit. Asset paths are internal notes, not public-yes claims.

---

## EV-PRIVILON-001

| Field | Value |
| --- | --- |
| evidence_id | EV-PRIVILON-001 |
| project | Privilon |
| campaign (context, not a claim) | CAMP-2026-09-001 |
| internal id (context, not a claim) | VITA-458 |
| yaml (candidate only, not proof) | `Business development/shared-workspace/intelligence/projects/privilon.yaml` |
| record status | internal evidence / Board permission lock 2026-08-25. 2 Sep proceeds on this permission basis without entering Distribution Mode. |
| photographer | none required as a third party (studio still Privilon (16)). Only credit a photographer if the still is later shown not to be ours. Do not invent IOA, Benoy Portfolio, or other photographer names. |
| photo/use permission | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. Not yaml photography_permission. |
| client permission | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. Not yaml photography_permission. |
| architect_credit_public | Lead architect Ar. Jagrut Patel, Vitan Architects |
| architect_credit_internal | Not for public copy. Do not copy yaml collaborators into public columns. |
| packet confidence | identity claims locked; photo/use and client permission Board-verified 2026-08-25; photographer none required as third party for studio still |
| review_date | 2026-09-01 (Asia/Kolkata) |
| expiry_or_hold_notes | Phase 0 row is tight to the three public-yes claims below. No GBA. No other-architect names in public fields. Tranquil is a Board cut. Do not add floors, year, client, street address, CTA, hashtags, still numbers, or consultant names as public-yes claims in this row. Board permission lock 2026-08-25: studio/architect holds use rights. Photographer third-party credit none required for the 2 Sep studio still. Still internal evidence; no Distribution row. |

### Internal asset notes (not public-yes claims; not a Distribution row)

2 Sep still is `Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (16).jpg`. Growth Lead approved this path 2026-08-25. Do not use `Privilon (10).jpg` (hash collision with PARIJAAT ECLAT / PAARIJAT ECLAT (1)).

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-PRIVILON-001 | Privilon | Project name is Privilon | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-09-01 | |
| EV-PRIVILON-001 | Privilon | Board credit line: Lead architect Ar. Jagrut Patel, Vitan Architects | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-09-01 | No other architect or collaboration line in public copy |
| EV-PRIVILON-001 | Privilon | Mixed-use, Ahmedabad | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-09-01 | Do not expand to street address or extra identity facts in this Phase 0 row |
