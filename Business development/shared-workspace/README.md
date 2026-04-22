# Shared Working Space

Purpose: keep collaboration artifacts in one shared location for drafting, review, approvals, and feedback.

## Structure
- `drafts/` — working drafts before review
- `review/` — artifacts currently under review
- `approved/` — finalized/approved outputs
- `comments/` — reviewer comments and threaded feedback docs
- `change-notes/` — change logs and revision notes

## Naming Convention
Use date + ticket key + short slug when possible.
Example: `2026-04-03-vita134-swot-competition-rebrand-baseline.md`

## FE Build Tools
- `Business development/shared-workspace/create_email.py`
  - Creates branded HTML outreach email artifacts from `contacts-master.csv`.
  - Example: `Business development/shared-workspace/create_email.py VIT-C-001 --project Privilon`
- `Business development/shared-workspace/create_pdf.py`
  - Creates branded one-page PDF outreach artifacts.
  - Auto-bootstraps a local virtual environment (`.venvs/vitan-content-tools`) for PDF dependencies when needed.
  - Example: `Business development/shared-workspace/create_pdf.py VIT-C-001 Privilon`
- `scripts/asset_readiness_routine.py`
  - Reads `references/submission-calendar.md`, checks project photo/checklist readiness for deadlines within 60 days, and posts a readiness table to the current BB standup issue.
  - Example dry run: `python3 scripts/asset_readiness_routine.py --dry-run`
