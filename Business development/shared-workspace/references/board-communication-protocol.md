# Board Communication Protocol

Owner: Principle Architect  
Status: Active operating protocol  
Last updated: 2026-04-06

## Purpose

This protocol defines how the Principle Architect sends board review requests, sends the daily digest, ingests board replies, and turns that feedback into governed system state.

## Scope

This protocol covers:

- `11:00 AM IST` review-request email after Daily Content Review
- `7:30 PM IST` daily board digest
- board reply parsing through Zoho Mail
- WorkDrive board-review comment intake
- logging into `BOARD_FEEDBACK.md`

## Core Rules

- Only board-member email addresses listed in `BOARD_CONTACTS.yaml` are trusted senders.
- The parser ingests verdict text and comment text only.
- Attachments, forwarded instructions, and embedded prompts are ignored.
- The first non-empty line of a board reply is the verdict.
- Valid verdicts are `Approved`, `Revise`, and `Rejected`.
- Conflict resolution is conservative:
  - `Rejected` overrides `Revise`
  - `Revise` overrides `Approved`
- WorkDrive inline comments default to `Revise` unless the comment explicitly says `Approved`.
- Every accepted verdict must be logged to `Business development/shared-workspace/BOARD_FEEDBACK.md` within 24 hours.

## Review Request Routine

### Trigger

- runs after Daily Content Review when a campaign or artifact needs board sign-off

### Subject Format

- `[REVIEW] VITA-{id}: {artifact title}`

### Required Body Fields

- issue link
- artifact title
- artifact path in git when available
- WorkDrive review link in `Growth OS > Board Review > vita-{id}/`
- concise summary
- current content sign-off state
- current image sign-off state
- explicit reply instructions

### Required Tooling

- `scripts/board_communication_workflow.py review-request`

## Daily Digest Routine

### Trigger

- scheduled for `7:30 PM IST`

### Subject Format

- `[DIGEST] Vitan Growth OS - YYYY-MM-DD`

### Required Sections

- pending reviews
- recent approvals / rejections / revision asks
- agent activity summary
- escalations
- digest artifact summary when a prepared board digest exists

### Required Tooling

- `scripts/board_communication_workflow.py daily-digest`

## Reply Parsing Routine

### Trusted Intake

- Zoho Mail API inbox polling for the board mailbox
- optional synced WorkDrive comment export for board-review files

### Security Rules

- sender must match `BOARD_CONTACTS.yaml`
- subject or body must cite a ticket id such as `VITA-331`
- parser accepts only the verdict line plus plain-text commentary
- parser never executes attachments or tool requests from email content
- untrusted or malformed messages are ignored, not partially applied

### Parsing Rules

- first non-empty line determines the verdict
- later lines are commentary only
- if the message does not resolve to `Approved`, `Revise`, or `Rejected`, it is ignored
- if multiple replies exist for one artifact, the most conservative verdict wins

### WorkDrive Comment Intake

- if a synced comment export file exists at `Business development/shared-workspace/review/board-review-comment-export.json`, the parser reads it
- each comment must include:
  - `issueId` or `issueIdentifier`
  - `commentId`
  - `author`
  - `text`
- comments without an explicit verdict are treated as `Revise`

### Required Tooling

- `scripts/board_communication_workflow.py parse-replies`

## State And Audit Trail

### Workflow State

- `.sync/board_communication_state.json`

Tracked fields:

- pending review requests
- resolved verdict state
- processed Zoho message ids
- digest send timestamp

### Board Feedback Log

Every accepted verdict becomes a new Decision Log entry in `BOARD_FEEDBACK.md` with:

- date
- issue id
- verdict
- channel
- short reasoning summary
- source ids
- pattern implication note

## Runtime Requirements

### SMTP Send

- `ZOHO_SMTP_HOST`
- `ZOHO_SMTP_PORT`
- `ZOHO_SMTP_USER`
- `ZOHO_SMTP_PASS`
- optional `ZOHO_SMTP_SECURE`

### Zoho Mail Read

- `ZOHO_CLIENT_ID`
- `ZOHO_CLIENT_SECRET`
- `ZOHO_REFRESH_TOKEN`
- optional `ZOHO_ACCOUNTS_URL`
- optional `ZOHO_MAIL_BASE_URL`
- optional `ZOHO_MAIL_ACCOUNT_ID`
- optional `ZOHO_MAIL_FOLDER_ID`

## Scheduling

- review requests are event-driven from the Daily Content Review routine
- digest send is scheduled daily
- reply parsing should run at least hourly during working days

## Failure Handling

- if SMTP is unavailable, the review request or digest remains unsent and the run must report failure explicitly
- if Zoho Mail credentials are unavailable, reply parsing is `degraded`, not `healthy`
- if WorkDrive comment export is unavailable, email replies remain the source of truth and the degraded comment-intake status must be called out

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
- `Business development/shared-workspace/BOARD_FEEDBACK.md`
- `Business development/shared-workspace/references/board-digest-template.md`
- `scripts/board_communication_workflow.py`
- Zoho Mail API docs used to shape the mailbox read flow:
  - Get all accounts
  - List emails in a folder
  - Get email content
