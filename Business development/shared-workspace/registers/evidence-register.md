# Evidence Register

Internal-only. Phase 0. Markdown is the human source of truth.

One `evidence_id` per project packet. Nest claims under it. Do not add Parijaat Eclat or Palladium-as-lead rows this cycle.

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
| record status | internal evidence / Board permission lock 2026-08-25. Growth Lead cleared reuse 2026-09-07. Already-published cycle may keep circulating Privilon (16). No Distribution row. |
| photographer | none required as a third party (studio still Privilon (16)). Only credit a photographer if the still is later shown not to be ours. Do not invent IOA, Benoy Portfolio, or other photographer names. |
| photo/use permission | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. Not yaml photography_permission. |
| client permission | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. Not yaml photography_permission. |
| architect_credit_public | Lead architect Ar. Jagrut Patel, Vitan Architects |
| architect_credit_internal | Not for public copy. Do not copy yaml collaborators into public columns. |
| packet confidence | identity claims locked; photo/use and client permission Board-verified 2026-08-25; photographer none required as third party for studio still |
| review_date | 2026-10-07 (Asia/Kolkata) |
| expiry_or_hold_notes | Phase 0 row is tight to the four public-yes claims below. No GBA. No other-architect names in public fields. Tranquil is a Board cut. Public completion year is the locked 2019 only. Do not add floors, client, street address, CTA, hashtags, still numbers, or consultant names as public-yes claims in this row. Board permission lock 2026-08-25: studio/architect holds use rights (lock still stands). Photographer third-party credit none required for the studio still Privilon (16). Growth Lead cleared reuse 2026-09-07; next review 2026-10-07. Already-published cycle may keep circulating Privilon (16). Still internal evidence; no Distribution row. |

### Internal asset notes (not public-yes claims; not a Distribution row)

Live still remains `Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (16).jpg` only. Growth Lead approved this path 2026-08-25. Do not use `Privilon (10).jpg` (hash collision with PARIJAAT ECLAT / PAARIJAT ECLAT (1)). Do not invent new stills or credits.

### INTERNAL-ONLY notes (never public claims)

- Board decision 2026-09-28 12:46 IST (relayed by Vitan Growth Lead): Privilon keeps the public line "Lead architect Ar. Jagrut Patel, Vitan Architects" with NO Benoy design credit. The Benoy pairing must not be used publicly or in outreach.
- Third-party public sources seen 2026-09-28 (internal reference only, not approved for any use):
  - https://www.lerchbates.com/projects/safal-privilion/ : 'Architect: Benoy Architects Singapore and Vitan Architects Ahmedabad, India'; client 'Safal Engineers & Realty LLP'.
  - https://enclosures.lerchbates.com/portfolio/safal-privilon/ : lists Benoy Architects (Singapore) and Vitan Architects (Ahmedabad).
  - https://tactileretail.com/portfolio/safal-privilon/ : same two architects.
  - https://avantefacades.com/portfolio/safal-privilon/ : same two architects.
  - https://www.benoy.com/projects/paarijat-eclat-privilon-mixed-use-towers-2/ : Benoy claims the exterior design concept for Paarijat Éclat & Privilon, 80,000 m2; no Vitan mention.
- Public completion year is locked as 2019 on Board + studio (Shailesh, Vitan studio) authority, confirmed 2026-09-28 in the Vitan Growth room. Source label: Board + studio (Shailesh), 2026-09-28. The year is locked on that Board/studio authority, not on Benoy or other third-party pages. 2019 seen earlier on third-party pages was not accepted as evidence and is not the basis of this lock.
- Internal detail (not public): the Ahmedabad Municipal Corporation granted Building Use (BU) permission on 22 Jan 2019. The GujRERA official completion date is 30 Jun 2019, under registration PR/GJ/AHMEDABAD/AHMEDABAD CITY/AUDA/MAA01158/301217, which matches the registration number already referenced in this row. Those dates are not public claims.
- Internal-only references (not the source of record and not a public citation; search-summary text quoting CaseMine and bsafal.com): `Business development/shared-workspace/registers/references/privilon/2026-09-28-privilon-bu-date-screenshot.png` (BU permission granted by AMC on 22 Jan 2019, citing CaseMine); `Business development/shared-workspace/registers/references/privilon/2026-09-28-privilon-rera-completion-screenshot.png` (RERA completion date 30 Jun 2019 plus registration MAA01158/301217, citing Bsafal). developer name in screenshot unverified; promoter to be checked on GujRERA MAA01158/301217.
- Verification (still pending): once the GujRERA registry loads, check the live MAA01158 completion record against 30 Jun 2019 and 22 Jan 2019, and record that it was checked.

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-PRIVILON-001 | Privilon | Project name is Privilon | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | |
| EV-PRIVILON-001 | Privilon | Board credit line: Lead architect Ar. Jagrut Patel, Vitan Architects | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | No other architect or collaboration line in public copy |
| EV-PRIVILON-001 | Privilon | Mixed-use, Ahmedabad | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | Do not expand to street address or extra identity facts in this Phase 0 row |
| EV-PRIVILON-001 | Privilon | Completion year is 2019 | Board + studio (Shailesh), 2026-09-28 | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | Public claim is the year 2019 only. Locked on Board + studio (Shailesh) authority, not on Benoy or other third-party pages. BU date 22 Jan 2019 and GujRERA completion date 30 Jun 2019 stay internal. GujRERA live-registry check against 30 Jun 2019 and 22 Jan 2019 is still pending. |

---

## EV-ARA-001

| Field | Value |
| --- | --- |
| evidence_id | EV-ARA-001 |
| project | ARA (Ahmedabad Racquet Academy) |
| yaml (candidate only, not proof) | `Business development/shared-workspace/intelligence/projects/ara.yaml` |
| record status | internal evidence / Board permission lock 2026-08-25. Board caption mark / live 2 Sep 2026 via Growth Lead (Growth Lead live confirmation 2026-09-07: ARA went live 2 Sep on IG/FB/LI/X + Google Business). File only; no Distribution row. No Urja pack. |
| photographer | none required as a third party (studio still). Do not invent photographer names. |
| photo/use permission | Board-confirmed 2026-08-25 (Vitan-led studio/architect holds use rights). Status Board-verified. Plus Board caption mark / live 2 Sep 2026 via Growth Lead. Not yaml photography_permission. |
| client permission | Board-confirmed 2026-08-25 (Vitan-led studio/architect holds use rights). Status Board-verified. Plus Board caption mark / live 2 Sep 2026 via Growth Lead. Not yaml photography_permission. |
| architect_credit_public | Lead architect Ar. Jagrut Patel, Vitan Architects |
| architect_credit_internal | Not for public copy. Not “& Team”. Do not copy yaml collaborators into public columns. |
| packet confidence | identity claims locked; photo/use and client permission Board-verified 2026-08-25; photographer none required as third party for studio still |
| review_date | 2026-10-07 (Asia/Kolkata) |
| expiry_or_hold_notes | Phase 0 row is tight to the four public-yes claims below. No GBA. No invented years, fees, or other-architect names. Not “& Team”. Tenure file still coming — do not invent numbers. Occupancy/resale may be implied as use; do not say sold. Live Privilon position (add life / occupied and used) continues in notes only; not a new public slogan. Floating gym pavilion is a new building decision for ARA, not a new slogan. Board permission lock 2026-08-25 still stands. Growth Lead cleared this packet 2026-09-07; next review 2026-10-07. No Distribution row. No Urja pack. |

### Internal asset notes (not public-yes claims; not a Distribution row)

Live item still is `Business development/PHOTOS FOR SAMPLE PROJECT/ARA (AHMEDABAD RACQUET ACADEMY)/ARA Sports Complex (3).jpg` only. Chitrang first-still pick 2026-08-31 (`ARA-Sports-complex-3.jpg`). Next stills 4, 6, 26 are not this post. Omit 13. Do not invent new stills or credits.

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-ARA-001 | ARA (Ahmedabad Racquet Academy) | Project name is ARA (Ahmedabad Racquet Academy) | Board lock 2026-08-25; Board queue/caption mark 2026-08-31; Growth Lead live confirmation 2026-09-07 (ARA went live 2 Sep); Chitrang first-still pick 2026-08-31 (ARA-Sports-complex-3.jpg) | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | |
| EV-ARA-001 | ARA (Ahmedabad Racquet Academy) | Board credit line: Lead architect Ar. Jagrut Patel, Vitan Architects | Board lock 2026-08-25; Board queue/caption mark 2026-08-31; Growth Lead live confirmation 2026-09-07 (ARA went live 2 Sep); Chitrang first-still pick 2026-08-31 (ARA-Sports-complex-3.jpg) | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | Not “& Team”. No other architect or collaboration line in public copy |
| EV-ARA-001 | ARA (Ahmedabad Racquet Academy) | Institutional / sports campus, Ahmedabad | Board lock 2026-08-25; Board queue/caption mark 2026-08-31; Growth Lead live confirmation 2026-09-07 (ARA went live 2 Sep); Chitrang first-still pick 2026-08-31 (ARA-Sports-complex-3.jpg) | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | Do not expand to street address, year, GBA, or fees |
| EV-ARA-001 | ARA (Ahmedabad Racquet Academy) | Building decision (studio/Chitrang via Growth Lead): floating gym pavilion; people exercising can see the football field (energy exchange / motivation) | Board lock 2026-08-25; Board queue/caption mark 2026-08-31; Growth Lead live confirmation 2026-09-07 (ARA went live 2 Sep); Chitrang first-still pick 2026-08-31 (ARA-Sports-complex-3.jpg) | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | New building decision for ARA, not a new public slogan. Occupancy/resale may be implied as use; do not say sold. Tenure file still coming — do not invent numbers |

---

## EV-MERLIN-001

| Field | Value |
| --- | --- |
| evidence_id | EV-MERLIN-001 |
| project | Merlin Pentagon |
| record status | internal evidence / Board permission lock 2026-08-25. Board queue mark. Chitrang first-still pick 2026-08-31. Growth Lead unlock 2026-09-07. DIST-MERLIN-IG-001 + DIST-MERLIN-FB-001 + DIST-MERLIN-LI-001 + DIST-MERLIN-GBP-001 filed. |
| photographer | none required as a third party (studio still). Do not invent photographer names. |
| photo/use permission | Board-confirmed 2026-08-25 (Vitan-led studio/architect holds use rights). Status Board-verified. Not yaml photography_permission. |
| client permission | Board-confirmed 2026-08-25 (Vitan-led studio/architect holds use rights). Status Board-verified. Not yaml photography_permission. |
| architect_credit_public | Lead architect Ar. Jagrut Patel, Vitan Architects |
| architect_credit_internal | Not for public copy. Not “& Team”. Do not copy yaml collaborators into public columns. |
| packet confidence | identity claims locked; photo/use and client permission Board-verified 2026-08-25; photographer none required as third party for studio still |
| review_date | 2026-10-07 (Asia/Kolkata) |
| expiry_or_hold_notes | Phase 0 row is tight to the four public-yes claims below. No GBA. No invented years, fees, client, or other-architect names. Not “& Team”. Tenure file still coming — do not invent numbers. Do not say sold. Live Privilon/ARA position (add life / occupied and used) continues in notes only; new building decision for Merlin, not a new public slogan. Board permission lock 2026-08-25 still stands. Growth Lead unlock 2026-09-07; next review 2026-10-07. Thin still set (two unique stills); hero is (1) only. DIST-MERLIN-IG-001 + DIST-MERLIN-FB-001 + DIST-MERLIN-LI-001 + DIST-MERLIN-GBP-001 filed. |

### Internal asset notes (not public-yes claims; not a Distribution row)

Live still is `Business development/PHOTOS FOR SAMPLE PROJECT/MERLIN PENTAGON/Pentagon (1).jpg` only. Chitrang first-still pick 2026-08-31 (`Merlin-Pentagon-1.jpg`; twisted facade / shuttering). Do not use `Pentagon (3).jpg` as the live hero unless Board says. Thin still set: two unique stills; hero is (1) only. Do not invent new stills or credits.

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-MERLIN-001 | Merlin Pentagon | Project name is Merlin Pentagon | Board lock 2026-08-25; Board queue mark; Chitrang first-still pick 2026-08-31 (Merlin-Pentagon-1.jpg); Growth Lead unlock 2026-09-07 | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | |
| EV-MERLIN-001 | Merlin Pentagon | Board credit line: Lead architect Ar. Jagrut Patel, Vitan Architects | Board lock 2026-08-25; Board queue mark; Chitrang first-still pick 2026-08-31 (Merlin-Pentagon-1.jpg); Growth Lead unlock 2026-09-07 | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | Not “& Team”. No other architect or collaboration line in public copy |
| EV-MERLIN-001 | Merlin Pentagon | Ahmedabad | Board lock 2026-08-25; Board queue mark; Chitrang first-still pick 2026-08-31 (Merlin-Pentagon-1.jpg); Growth Lead unlock 2026-09-07 | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | Chitrang / Growth Lead. Do not expand to street address, year, GBA, fees, or yaml location invent |
| EV-MERLIN-001 | Merlin Pentagon | Building decision (Chitrang via Growth Lead): five-road intersection; small triangular plot; two basements without losing FSI; facade executed as designed (twisted facade / shuttering) | Board lock 2026-08-25; Board queue mark; Chitrang first-still pick 2026-08-31 (Merlin-Pentagon-1.jpg); Growth Lead unlock 2026-09-07 | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | New building decision for Merlin, not a new public slogan. Occupancy/resale may be implied as use; do not say sold. Tenure file still coming — do not invent numbers |

---

## EV-SEVENTY-001

| Field | Value |
| --- | --- |
| evidence_id | EV-SEVENTY-001 |
| project | Seventy |
| record status | internal evidence / Board permission lock 2026-08-25. Board MARKED Approve 2026-09-16: Executive Architecture / Executive Architect credit chrome. Growth Lead unlock to file 2026-09-16. Collaborative — Vitan is not Lead/Principal. DIST-SEVENTY-IG-001 + DIST-SEVENTY-FB-001 + DIST-SEVENTY-GBP-001 filed; LI post is live (DIST-SEVENTY-LI-001, urn:li:share:7508485082270208000); X is live (DIST-SEVENTY-X-001). |
| photographer | none required as a third party unless still shown not ours. Do not invent photographer names. |
| photo/use permission | Board-confirmed 2026-08-25 (studio/architect holds use rights for Vitan studio stills) + Board credit chrome Approve 2026-09-16. Status Board-verified for credit line. Not yaml photography_permission. |
| client permission | Board-confirmed 2026-08-25 (studio/architect holds use rights for Vitan studio stills) + Board credit chrome Approve 2026-09-16. Status Board-verified for credit line. Not yaml photography_permission. |
| architect_credit_public | Executive Architect: Ar. Jagrut Patel, Vitan Architects |
| design_credit_public | Design: SCDA Architects (Board allowed after verify; https://seventy.co/team-architect.html 2026-09-16) |
| architect_credit_internal | Not for public copy as Lead or Principal. Not “& Team”. Service framing Executive Architecture is Board-marked chrome. Do not copy yaml collaborators into public columns. |
| packet confidence | identity claims locked; photo/use and client permission Board-verified 2026-08-25; credit chrome Board-verified 2026-09-16; Design SCDA medium–high (first-party project site; Board allowed after verify); photographer none required as third party for studio still |
| review_date | 2026-10-07 (Asia/Kolkata) |
| expiry_or_hold_notes | Phase 0 row is tight to the five public-yes claims below. No GBA. No client. No yaml year. No tenure invent. Not Lead architect. Not Principal. Not “& Team”. Live Privilon/ARA/Merlin position (add life / occupied and used) continues in notes only; new building decision for Seventy, not a new public slogan. Board permission lock 2026-08-25 still stands. Board Approve Executive Architecture 2026-09-16; Growth Lead unlock to file 2026-09-16; next review 2026-10-07. DIST-SEVENTY-IG-001 + DIST-SEVENTY-FB-001 + DIST-SEVENTY-GBP-001 filed; LI post is live (DIST-SEVENTY-LI-001, urn:li:share:7508485082270208000); X is live (DIST-SEVENTY-X-001). |

### Internal asset notes (not public-yes claims; not a Distribution row)

Hero still (internal note only) is `Business development/PHOTOS FOR SAMPLE PROJECT/SEVENTY/DSC_9372.jpg` (Chitrang Seventy-dsc_9372.jpg). Next stills on file: `DSC_8768-HDR.jpg`, `DSC_8455-HDR.jpg`. Do not invent DSC_9896 (disk has `DSC_8996-HDR.jpg` unmatched). Do not invent new stills or credits.

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-SEVENTY-001 | Seventy | Project name is Seventy | Board lock 2026-08-25; Board Approve Executive Architecture 2026-09-16; Chitrang first-still pick 2026-08-31; Growth Lead unlock to file 2026-09-16; seventy.co verify | Board-confirmed 2026-08-25 (studio/architect holds use rights for Vitan studio stills) + Board credit chrome Approve 2026-09-16. Status Board-verified for credit line. | none required as a third party unless still shown not ours | Executive Architect: Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | |
| EV-SEVENTY-001 | Seventy | Executive Architect: Ar. Jagrut Patel, Vitan Architects (Board Approve 2026-09-16 Executive Architecture chrome) | Board lock 2026-08-25; Board Approve Executive Architecture 2026-09-16; Chitrang first-still pick 2026-08-31; Growth Lead unlock to file 2026-09-16; seventy.co verify | Board-confirmed 2026-08-25 (studio/architect holds use rights for Vitan studio stills) + Board credit chrome Approve 2026-09-16. Status Board-verified for credit line. | none required as a third party unless still shown not ours | Executive Architect: Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | Not Lead architect. Not Principal. Not “& Team”. Collaborative — Vitan is not Lead/Principal. Service framing Executive Architecture is Board-marked chrome. |
| EV-SEVENTY-001 | Seventy | Design: SCDA Architects (verified seventy.co/team-architect.html 2026-09-16) | Board lock 2026-08-25; Board Approve Executive Architecture 2026-09-16; Board allowed Design credit after verify; https://seventy.co/team-architect.html verified 2026-09-16 (RIBA award-winning architecture firm SCDA is the artist behind Seventy); Growth Lead unlock to file 2026-09-16 | Board-confirmed 2026-08-25 (studio/architect holds use rights for Vitan studio stills) + Board credit chrome Approve 2026-09-16. Status Board-verified for credit line. | none required as a third party unless still shown not ours | Executive Architect: Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | medium–high | 2026-10-07 | First-party project site; Board allowed Design credit after verify. Design architect only — not Vitan Lead/Principal. |
| EV-SEVENTY-001 | Seventy | Ahmedabad (Chitrang / Growth Lead) | Board lock 2026-08-25; Board Approve Executive Architecture 2026-09-16; Chitrang first-still pick 2026-08-31; Growth Lead unlock to file 2026-09-16; seventy.co verify | Board-confirmed 2026-08-25 (studio/architect holds use rights for Vitan studio stills) + Board credit chrome Approve 2026-09-16. Status Board-verified for credit line. | none required as a third party unless still shown not ours | Executive Architect: Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | Chitrang / Growth Lead. Do not expand to street address, year, GBA, fees, client, or yaml location invent |
| EV-SEVENTY-001 | Seventy | Building decision (Chitrang 31 Aug via Growth Lead): two towers to 70 m (23 storeys) connected by an infinity pool; glass facade and double-height balconies | Board lock 2026-08-25; Board Approve Executive Architecture 2026-09-16; Chitrang first-still pick 2026-08-31; Growth Lead unlock to file 2026-09-16; seventy.co verify | Board-confirmed 2026-08-25 (studio/architect holds use rights for Vitan studio stills) + Board credit chrome Approve 2026-09-16. Status Board-verified for credit line. | none required as a third party unless still shown not ours | Executive Architect: Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | New building decision for Seventy, not a new public slogan. Continue live Privilon/ARA/Merlin position (add life / occupied and used) in notes only. Tenure file still coming — do not invent numbers. No GBA. No client. No yaml year. |
