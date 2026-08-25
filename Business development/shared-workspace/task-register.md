# Shared Task Register

This CSV plus this note is the **only work-order system** for Vitan Agent Operating Architecture (Board sign-off 25 Aug 2026). A SendToAgent ping is a **nudge**, not an assignment. Work starts only when a Shared Task Register (STR) row exists.

Schema file: `task-register.csv`. Do not invent columns. Do not send email or publish from this register.

## Lifecycle

Happy path:

Created → Assigned → Inputs Verified → Running → Quality Check → Awaiting Approval → Released → Outcome Recorded → Closed

Terminal / exception statuses (not on the happy path):

- **Blocked** — missing input, approval, or evidence; fill `blocked_reason`
- **Failed** — execution failed; fill `failure_reason`; `retry_count` may increment (max 2)
- **Rejected** — reviewer or Board declined; fill `rejection_reason`
- **Cancelled** — withdrawn before release

**Released** is the only status that may touch the outside world (send, publish, post, or otherwise contact a prospect or the public).

Phase 0 / shadow: **no row may enter Released for send/publish**, except the already-unlocked **2 Sep Privilon Instagram**. That exception is owned by **Proof**, not this send path. This register does not execute that post.

## owner_bot

One of: `GL` | `BB` | `Proof` | `OC` | `CC` | `FE`

The bot named in `owner_bot` is accountable for the row. `created_by` may be Board or another agent; ownership is still `owner_bot`.

## permission_level

One of: `GREEN` | `AMBER` | `RED` | `INTERNAL`

- `INTERNAL` — no outbound; fixtures, schema, and shadow work stay here
- `GREEN` / `AMBER` / `RED` — follow the operating architecture; RED does not self-release

## Identifiers and uniqueness

- `task_id` format: `STR-YYYYMMDD-NNN` (example: `STR-20260825-001`)
- IDs are unique. Do not reuse a closed ID.
- **One open STR** per (`related_contact_ids` + `skill_id`). Close or cancel the open row before opening another for the same pair.
- Empty `related_contact_ids` is allowed for internal / fixture work that is not contact-scoped.

## Retries and money language

- `retry_count` starts at `0`. Maximum **2**. A third failure stays Failed; do not auto-retry.
- Do **not** report pipeline value as earned revenue. Pipeline is not cash. Outcome notes may record status, sent/published flags, and qualitative result only.

## Columns

| Column | Role |
| --- | --- |
| task_id | Unique STR id |
| created_at | ISO-8601 with offset |
| created_by | Who opened the row |
| owner_bot | Accountable bot |
| business_objective | Why this row exists |
| source_links | Repo, issue, or brief URLs |
| skill_id | Skill being executed |
| skill_version | Skill version |
| permission_level | GREEN / AMBER / RED / INTERNAL |
| deadline | Date the work is due |
| reviewer | Named reviewer |
| retry_count | Integer 0–2 |
| result | Outcome text (no pipeline-as-revenue) |
| cost_tokens | Token cost if known; else `unknown` |
| failure_reason | Required when Failed |
| rejection_reason | Required when Rejected |
| blocked_reason | Required when Blocked |
| related_contact_ids | Contact IDs from contacts-master, if any |
| evidence_ids | Evidence packet ids (pointers only; facts live in the Evidence Register when present) |
| next_action_date | Next review or follow-up date |
| status | Lifecycle status |

`evidence_ids` on a row (for example `EV-PRIVILON-001`) is a pointer. This register does not store project facts and must not scrape the web to fill them.

## Seed row

`STR-20260825-001` records Phase 1 fixture tests for eleven v0.1 skills. Status **Closed**. `sent=no` `published=no`. No outbound.
