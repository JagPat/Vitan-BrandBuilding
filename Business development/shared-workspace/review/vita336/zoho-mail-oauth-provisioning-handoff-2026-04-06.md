# VITA-336 Zoho Mail OAuth Provisioning Handoff

Date: 2026-04-06
Owner: Principle Architect
Related Issues: [VITA-336](/VITA/issues/VITA-336), [VITA-335](/VITA/issues/VITA-335), [VITA-331](/VITA/issues/VITA-331)

## Decision

This is a real credential-provisioning gap, not an FE implementation gap.

- Current company secret inventory contains only `github_pat_vitan` and `social_credentials`
- Current PA runtime already has Zoho SMTP send credentials, but does not have the Zoho Mail read OAuth set
- FE cannot complete live mailbox-read validation until the mailbox-read OAuth material exists in a Paperclip-managed secret source

## Required Secret Material

Create a canonical Paperclip-managed secret source for:

- `ZOHO_CLIENT_ID`
- `ZOHO_CLIENT_SECRET`
- `ZOHO_REFRESH_TOKEN`

These are the only mandatory read-path secrets.

## Optional Runtime Overrides

These values are optional, not mandatory:

- `ZOHO_MAIL_ACCOUNT_ID`
- `ZOHO_MAIL_FOLDER_ID`

The current PA workflow can auto-discover them when the OAuth trio exists:

- account discovery: `GET /api/accounts`
- folder discovery: `GET /api/accounts/{accountId}/folders`
- default folder behavior: use `Inbox` when present, otherwise fall back to the first folder returned

## Board Action Required

The board must provide the mailbox-read OAuth material through a board-authorized Paperclip secret entry path. Do not paste raw secrets into issue comments.

Preferred secure result:

1. Create three company secrets for the OAuth trio
2. Confirm the target mailbox is the board review mailbox
3. Optionally provide explicit account and folder ids if the board wants a non-default folder

## FE Resume Point

Once the secret source exists, FE can resume [VITA-335](/VITA/issues/VITA-335) by:

1. Mounting the new secret refs into the PA runtime
2. Running `scripts/board_communication_workflow.py parse-replies`
3. Recording whether live mailbox-read validation succeeds without fixture mode

## Sources Consulted

- [VITA-336](/VITA/issues/VITA-336)
- [VITA-335](/VITA/issues/VITA-335)
- [VITA-331](/VITA/issues/VITA-331)
- `Business development/shared-workspace/references/board-communication-protocol.md`
- `scripts/board_communication_workflow.py`
- live `company_secrets` metadata state
- live PA runtime configuration state
