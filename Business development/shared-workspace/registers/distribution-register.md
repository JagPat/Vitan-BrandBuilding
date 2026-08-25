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

Note (not a row): 2 Sep Instagram stays unlocked outside this register as CAMP-2026-09-001. Asset path is an internal note on EV-PRIVILON-001 only (`PRIVILON/Privilon (16).jpg`). Do not add a `distribution_id`. Do not use `Privilon (10).jpg`. Do not publish from this folder.
