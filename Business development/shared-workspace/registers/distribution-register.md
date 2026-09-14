# Distribution Register

Internal-only. Phase 0. Live published rows are recorded below. Do not invent IDs, queues, or captions. Do not publish new posts from this file.

A row may be added only for an **approved** Evidence Register entry. Do not invent IDs, queues, or captions here.

## Schema

| distribution_id | evidence_id | derived_content | channel | approval | publication_status | scheduled_window_ist | asset_path | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

`evidence_id` must be an approved Evidence entry; otherwise do not add a row.

`derived_content` is a packet/caption id, not a live post.

`publication_status`: not-entered | queued | approved | published | held.

## Rows

| distribution_id | evidence_id | derived_content | channel | approval | publication_status | scheduled_window_ist | asset_path | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DIST-MERLIN-IG-001 | EV-MERLIN-001 | Merlin live IG pack (Urja Approve; Growth Lead posted) | Instagram | Urja Approve + Growth Lead post | published | 2026-09-09 (live) | Business development/PHOTOS FOR SAMPLE PROJECT/MERLIN PENTAGON/Pentagon (1).jpg | Live URL https://www.instagram.com/vitanarchitects/p/DdEZawXlAZr/ |
| DIST-MERLIN-FB-001 | EV-MERLIN-001 | Merlin live FB pack | Facebook | Urja Approve + Growth Lead post | published | 2026-09-09 (live) | Business development/PHOTOS FOR SAMPLE PROJECT/MERLIN PENTAGON/Pentagon (1).jpg | Live post id 290161881095312_1683065920488319 |
| DIST-MERLIN-LI-001 | EV-MERLIN-001 | Merlin live LI pack | LinkedIn | Urja Approve + Growth Lead post | published | 2026-09-09 (live) | Business development/PHOTOS FOR SAMPLE PROJECT/MERLIN PENTAGON/Pentagon (1).jpg | Live urn:li:activity:7503444465852928000 |
| DIST-MERLIN-GBP-001 | EV-MERLIN-001 | Merlin live GBP / Maps pack | Google Business Profile | Urja Approve + Growth Lead post | published | 2026-09-11 ~07:12 IST (Manage Published) | Business development/PHOTOS FOR SAMPLE PROJECT/MERLIN PENTAGON/Pentagon (1).jpg | Vitan Architects listing 702 HetDiv Square; no public permalink exposed in Manage |

Note (not a row): Privilon still, if referenced, remains `Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (16).jpg` (Growth Lead approved 2026-08-25). Do not use `Privilon (10).jpg` (hash collision with PARIJAAT ECLAT / PAARIJAT ECLAT (1)). No Privilon Distribution row this cycle. Live Merlin Distribution rows are DIST-MERLIN-IG-001, DIST-MERLIN-FB-001, DIST-MERLIN-LI-001, DIST-MERLIN-GBP-001 above.
