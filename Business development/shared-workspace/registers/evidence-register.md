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
- Internal-only references (not the source of record and not a public citation; search-summary text quoting CaseMine and bsafal.com): `Business development/shared-workspace/registers/references/privilon/2026-09-28-privilon-bu-date-screenshot.png` (BU permission granted by AMC on 22 Jan 2019, citing CaseMine); `Business development/shared-workspace/registers/references/privilon/2026-09-28-privilon-rera-completion-screenshot.png` (RERA completion date 30 Jun 2019 plus registration MAA01158/301217, citing Bsafal). developer name in screenshot unverified at capture; the promoter check against GujRERA MAA01158/301217 is closed in the live check note below (internal only).
- GujRERA live check 2026-09-29 IST (https://gujrera.gujarat.gov.in/, regId 788): completionDateStr 30-06-2019 matches the internal GujRERA completion date; projRegNo PR/GJ/AHMEDABAD/AHMEDABAD CITY/AUDA/MAA01158/301217 matches; registered project type Mixed Development; registered promoter name SKZ DEVELOPERS LLP; registered project name PAARIJAT ECLAT AND PRIVILON. AMC BU 22 Jan 2019 is not a GujRERA field and was not re-checked on the registry. Verification pending item closed for GujRERA completion/regNo/promoter/type. INTERNAL-ONLY. Public-yes claims are unchanged.

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-PRIVILON-001 | Privilon | Project name is Privilon | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | |
| EV-PRIVILON-001 | Privilon | Board credit line: Lead architect Ar. Jagrut Patel, Vitan Architects | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | No other architect or collaboration line in public copy |
| EV-PRIVILON-001 | Privilon | Mixed-use, Ahmedabad | locked CAMP-2026-09-001 / Board credit rule | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | PA-locked | yes | high | 2026-10-07 | Do not expand to street address or extra identity facts in this Phase 0 row |
| EV-PRIVILON-001 | Privilon | Completion year is 2019 | Board + studio (Shailesh), 2026-09-28 | Board-confirmed 2026-08-25 (studio/architect holds use rights). Status Board-verified. | none required as a third party (studio still Privilon (16)) | Lead architect Ar. Jagrut Patel, Vitan Architects | not public | Board-verified | yes | high | 2026-10-07 | Public claim is the year 2019 only. Locked on Board + studio (Shailesh) authority, not on Benoy or other third-party pages. BU date 22 Jan 2019 and GujRERA completion date 30 Jun 2019 stay internal. GujRERA live check 2026-09-29 (regId 788) matched completionDateStr 30-06-2019 and registration MAA01158/301217. AMC BU 22 Jan 2019 is not a GujRERA field and was not re-checked on the registry. |

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

---

## EV-PAARIJAT-EROS-001

| Field | Value |
| --- | --- |
| evidence_id | EV-PAARIJAT-EROS-001 |
| project | PAARIJAT EROS / Paarijat Eros |
| record status | internal evidence; registry read 2026-09-29; no Board lock; no Distribution row. Not Parijaat Eclat. |
| photographer | UNKNOWN (waiting on studio). Photos: none. |
| photo/use permission | UNKNOWN (waiting on studio) |
| client permission | UNKNOWN (no studio clearance on file) |
| architect_credit_public | not suggested |
| architect_credit_internal | Not for public copy. Professionals row filed from GujRERA 2026-09-29 (regId 31655): name JAGRUT RAMANLAL PATEL; licence CA/1999/24504; address VITAN HOUSE OPP RANGKUNJ SOCIETY; email jagrutpatel@gmail.com. The architect row does not print a firm name. Do not invent Vitan Architects as a public claim. Do not publish "Architect: Ar. Jagrut Patel, Vitan Architects" from this packet. |
| packet confidence | Registry facts read 2026-09-29 from GujRERA regId 31655; internal only; not Board-locked. Photo/use and photographer UNKNOWN (waiting on studio). |
| review_date | 2026-10-12 (Asia/Kolkata) |
| expiry_or_hold_notes | GujRERA (https://gujrera.gujarat.gov.in/) live read 2026-09-29, regId 31655 (alldatabyprojectid and project details). The 2026-09-28 unread state is closed for the registry fields below. Filled registry claims use status `registry-read`: the row was read, and that status is not Board-verified and not PA-locked. public_yes_no stays no until Growth Lead/Board clear any public use. Public architect line is not suggested: the architect row names JAGRUT RAMANLAL PATEL and licence CA/1999/24504 and does not print a firm name. Do not invent Vitan Architects as a public claim. Photos and permissions stay UNKNOWN. No GBA. No fees. No prices. No Distribution row. Parijaat Eclat stays held and is not this packet. Do not use Eclat stills. |

### Internal asset notes (not public-yes claims; not a Distribution row)

No still for Paarijat Eros. Do not use `Business development/PHOTOS FOR SAMPLE PROJECT/PARIJAAT/` (those files are Parijaat/Paarijat Eclat). Do not pull any image from the web. Not a public-yes claim. Not a Distribution row.

### Repo spelling (internal; not a Paarijat Eros project fact)

On main, `Parijaat` and `Paarijat` name Parijaat Eclat. There is no path for Paarijat Eros, Parijaat Eros, or Eros. Safal strings elsewhere on main are other records and are not a promoter legal name for this packet.

### Claims

| evidence_id | project | claim | source | permission | photographer_credit | architect_credit_public | architect_credit_internal | status | public_yes_no | confidence | review_date | expiry_or_hold_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Registered project name: PAARIJAT EROS | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. Registered name filed. public-yes no until Growth Lead/Board clear any public use. Medium means the official registry row was read; not publish confidence; not a Board/PA lock. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | RERA registration number: PR/GJ/AHMEDABAD/SANAND/Ahmedabad Urban Development Authority/RAA17189/270726/300931 | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. public-yes no. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Promoter/developer legal name: SAFAL CONSTRUCTIONS(INDIA) PRIVATE LIMITED | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. Taken from the GujRERA promoter name on regId 31655. Not filled from other Safal records in the repo. public-yes no. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Approval/registration date: 27-07-2026 | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. Registry approvedDate. public-yes no. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Project type: Residential/Group Housing | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. public-yes no. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Location as registered: Ahmedabad / Sanand / Godhavi; TPS No. 429 (Godhavi-Manipur), Survey No. 915/4/P, FP No 140; pin 382115; approving authority Ahmedabad Urban Development Authority | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. public-yes no. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Number of towers/units: Flat inventory 88 (towers not separately stated on the registry inventory row) | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. Inventory type Flat, count 88. Not a tower count. public-yes no. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Carpet area as registered: 14985.52 (registry carpet; not GBA) | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. Registry carpet 14985.52. Not GBA. public-yes no. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Proposed completion date: 30-09-2031 (start 24-02-2026) | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Internal. completionDateStr 30-09-2031; startDateStr 24-02-2026. public-yes no. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Architect named in the professionals section (name, firm, registration no.): name JAGRUT RAMANLAL PATEL; licence CA/1999/24504; address VITAN HOUSE OPP RANGKUNJ SOCIETY; email jagrutpatel@gmail.com. Registry does not print a firm name in the architect row. | https://gujrera.gujarat.gov.in/ live 2026-09-29 (regId 31655) | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | registry-read | no | medium | 2026-10-12 | Public line not suggested. Registry names JAGRUT RAMANLAL PATEL and licence CA/1999/24504. It does not name a firm. Do not invent Vitan Architects as a public claim. public-yes only after Growth Lead/Board clear it. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Photos: none. Photo/use permission UNKNOWN (waiting on studio). Photographer UNKNOWN (waiting on studio). Client permission UNKNOWN (no studio clearance on file). | No Paarijat Eros image on main. Eclat stills are not this packet: `.sync/workdrive_state.json`; `Business development/shared-workspace/registers/evidence-register.md` | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | PENDING | no | unknown | 2026-10-12 | No image pulled from the web. |
| EV-PAARIJAT-EROS-001 | PAARIJAT EROS / Paarijat Eros | Repo text on main: Parijaat/Paarijat strings name Parijaat Eclat (held). No path names Paarijat Eros, Parijaat Eros, or Eros. Safal strings elsewhere on main are other records and are not this promoter legal name. | `scripts/branded_content_utils.py`; `scripts/sync_from_workdrive.py`; `scripts/sync_to_workdrive.py`; `Business development/shared-workspace/registers/distribution-register.md`; `Business development/shared-workspace/registers/evidence-register.md`; `Business development/shared-workspace/registers/evidence-register.yaml`; `Business development/shared-workspace/registers/README.md`; `Business development/shared-workspace/drafts/strategy-brief-2026-08-24.md`; `.sync/workdrive_state.json` | UNKNOWN (waiting on studio) | UNKNOWN (waiting on studio) | not suggested | not public | PENDING | no | high | 2026-10-12 | Internal. High means those paths were read on main. Not publish confidence. Not a Board/PA lock. Not a Paarijat Eros project fact. Eclat stays held. |
