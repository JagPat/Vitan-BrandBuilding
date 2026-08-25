# Distribution Register

Internal-only. Phase 0. No live distribution rows.

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

Note (not a row): 2 Sep still is `Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (16).jpg`. Growth Lead approved this path 2026-08-25. Do not use `Privilon (10).jpg` (hash collision with PARIJAAT ECLAT / PAARIJAT ECLAT (1)). Do not add a `distribution_id`.
