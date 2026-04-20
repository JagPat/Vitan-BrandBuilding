# VITA-335 Zoho Mail Runtime Alias Verification

Date: 2026-04-06
Owner: Principle Architect
Issue: [VITA-335](/VITA/issues/VITA-335)

## Finding

The mailbox-read blocker is not a missing-secret condition in the active PA runtime. The read-path credentials are already mounted, but under `ZOHO_MAIL_*` names instead of the older `ZOHO_*` names assumed by `scripts/board_communication_workflow.py`.

## Verified Runtime State

- Present in runtime:
  - `ZOHO_MAIL_CLIENT_ID`
  - `ZOHO_MAIL_CLIENT_SECRET`
  - `ZOHO_MAIL_REFRESH_TOKEN`
  - `ZOHO_MAIL_ACCOUNT_ID`
- Also present for send path:
  - `ZOHO_SMTP_HOST`
  - `ZOHO_SMTP_PORT`
  - `ZOHO_SMTP_USER`
  - `ZOHO_SMTP_PASS`
- Not mounted under the older parser names:
  - `ZOHO_CLIENT_ID`
  - `ZOHO_CLIENT_SECRET`
  - `ZOHO_REFRESH_TOKEN`

## Decision

Treat this as an env-name contract defect, not a board-owned secret-provisioning gap.

- The PA workflow now accepts either naming set for the OAuth trio
- FE no longer needs a new secret source to continue live mailbox-read validation
- Optional `ZOHO_MAIL_FOLDER_ID` remains unset, which is acceptable because the workflow already supports folder auto-discovery

## Resume Point

With alias support in place, the next validation step is a live `parse-replies` run against Zoho Mail using the mounted runtime credentials.

## Sources Consulted

- `scripts/board_communication_workflow.py`
- `Business development/shared-workspace/references/board-communication-protocol.md`
- live PA runtime environment
- [VITA-335](/VITA/issues/VITA-335)
- [VITA-336](/VITA/issues/VITA-336)
- [VITA-337](/VITA/issues/VITA-337)
