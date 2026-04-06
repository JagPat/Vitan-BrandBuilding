# VITA-331 Board Email Review Workflow

Date: 2026-04-06  
Owner: Principle Architect  
Issue: [VITA-331](/VITA/issues/VITA-331)

## Delivered

1. Operating protocol for board communication:
   - `Business development/shared-workspace/references/board-communication-protocol.md`
2. Automation entrypoint:
   - `scripts/board_communication_workflow.py`
3. Tracked board sender registry:
   - `BOARD_CONTACTS.yaml`
4. Governance updates:
   - `Business development/shared-workspace/BOARD_FEEDBACK.md`
   - `Business development/shared-workspace/METRICS_CHARTER.md`
   - `Business development/shared-workspace/CAPABILITY_REGISTRY.md`
5. Scheduling and trigger contract documented in protocol for later platform wiring

## Workflow Modes

### Review Request

- Sends `[REVIEW] VITA-{id}: {artifact title}`
- Stores pending review metadata in `.sync/board_communication_state.json`
- Requires issue id, artifact title, summary, and WorkDrive link

### Daily Digest

- Sends `[DIGEST] Vitan Growth OS - YYYY-MM-DD`
- Aggregates pending board reviews, recent decisions, active issue activity, and escalations
- Can include a prepared digest artifact summary

### Reply Parsing

- Reads trusted board replies from Zoho Mail
- Accepts only board-member senders from `BOARD_CONTACTS.yaml`
- Extracts verdict from the first non-empty line
- Applies conservative conflict resolution across multiple replies
- Ingests synced WorkDrive comment export when present
- Can append accepted verdicts into `BOARD_FEEDBACK.md`

## Security Decisions

- Board replies are treated as untrusted input until sender allowlist checks pass.
- The parser never executes instructions from email content.
- Attachments and forwarded content are ignored.
- WorkDrive comments default to `Revise` unless explicitly marked `Approved`.

## Known Runtime Constraint

- This PA runtime currently has SMTP credentials but not the Zoho OAuth env needed to verify live mailbox reads.
- The parser supports offline message fixtures for verification and live Zoho Mail polling once credentials are mounted.
- WorkDrive inline comments remain dependent on either a synced export file or a future FE-provided fetch layer.
- GitHub rejected the automation-workflow file push because the available PAT lacks `workflow` scope, so the schedule remains documented but not committed from this runtime.

## Verification

- `python3 -m py_compile scripts/board_communication_workflow.py`
- dry-run `review-request` generated the expected `[REVIEW]` subject/body and created pending review state
- dry-run `daily-digest` generated pending-review, agent-activity, and escalation sections
- fixture-driven `parse-replies` resolved mixed board replies to `Revise`, proving the conservative conflict rule

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
- `BOARD_CONTACTS.yaml`
- `Business development/shared-workspace/BOARD_FEEDBACK.md`
- `Business development/shared-workspace/CAPABILITY_REGISTRY.md`
- `Business development/shared-workspace/METRICS_CHARTER.md`
- `Business development/shared-workspace/references/board-digest-template.md`
- Zoho Mail API docs used to shape the mailbox read flow:
  - Get all accounts
  - List emails in a folder
  - Get email content
