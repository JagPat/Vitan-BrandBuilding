# Approved Outbound Send Runbook

Date: 2026-04-06 (UTC)  
Owner: Founding Engineer  
Primary user: Business Builder

## When To Use This

Use this runbook after a board or PA thread says a specific email task is **approved for outbound** and before Business Builder executes the live send.

This is for GREEN and AMBER email outreach that already has:

- approved copy
- a named recipient route
- a live execution issue
- a planned execution note path in `Business development/shared-workspace/review/vita{NNN}/`

## What This Does Not Automate

- It does not approve outreach.
- It does not send email for you.
- It does not override RED-sensitivity or board-owned sends.
- It does not mutate `contacts-master.csv` automatically.

## Normalized Authority Rule

Business Builder may execute the approved outreach directly only when all of the following are true:

- the task is explicitly approved for outbound
- the contact sensitivity is GREEN or AMBER
- the board did not explicitly retain send ownership
- no material copy, recipient, attachment, or channel change was introduced after approval

If any of those are false, return the task to board review instead of sending.

## Canonical Send Expectations

- Authenticated sender route: `jp@vitan.in`
- Reply handling route: `connect@vitan.in`
- Recipient route: must match `Email (Primary)` or `Email (Fallback)` in `Business development/shared-workspace/contacts-master.csv`
- Execution log: write a send execution note in the live issue folder under `Business development/shared-workspace/review/vita{NNN}/`

## Preflight Command

Run this from the repo root before sending:

```bash
python3 scripts/approved_outreach_preflight.py \
  --contact-id VIT-C-006 \
  --issue VITA-298 \
  --approved-artifact "Business development/shared-workspace/review/vita296/2026-04-06-flex-first-wave-send-ready-pack.md" \
  --execution-artifact "Business development/shared-workspace/review/vita298/2026-04-06-the-address-send-execution.md" \
  --recipient-route raj@gototheaddress.com \
  --sensitivity amber \
  --discovery-status complete \
  --approved-for-outbound
```

If the helper returns `FAIL`, do not send. Fix the mismatch or return the task to board review.

If the helper returns only `PASS` and `WARN`, read the warnings, confirm they are understood, then continue.

## Execution Checklist

1. Confirm the approved artifact still matches the exact copy and route you intend to use.
2. Run the preflight helper.
3. Send through the canonical mail path using `jp@vitan.in` authentication and `connect@vitan.in` reply handling.
4. Capture the SMTP acceptance details immediately after send.
5. Write the execution note with:
   - recipient
   - route used
   - subject
   - sent timestamp
   - authenticated sender route
   - reply handling route
   - `Message-ID`
   - attachment state
   - follow-up recommendation
6. Update `Business development/shared-workspace/contacts-master.csv` with:
   - `Last Contacted`
   - `Response Status`
   - `Follow-up Date`
   - `Draft Message Status`
   - `Outreach Channel`
7. Comment on the live issue with the execution summary and the execution note path.

## Sources Consulted

- `Business development/shared-workspace/references/engagement-system.md`
- `Business development/shared-workspace/references/publishing-protocol.md`
- `Business development/shared-workspace/references/sensitivity-protocol.md`
