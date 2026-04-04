# VITA-163 Sending Mechanism + Response Management SOP

Date: 2026-04-04 (UTC)
Issue: [VITA-163](/VITA/issues/VITA-163)
Related execution: [VITA-133](/VITA/issues/VITA-133)

## Sending Mechanism (Resolved)
Decision for Week-16 first-5: `manual founder send` from `chitrang@vitan.in`.

### Why this path
- Current system does not hold approved delegated mailbox send permissions for `chitrang@vitan.in`.
- Governance already requires final human review before external outreach.
- Manual send gives immediate control over per-recipient final personalization.

### Pre-send workflow (for each row)
1. Business Builder prepares final copy from approved template.
2. Business Builder provides ready-to-send email block (subject + body + attachment references) in board-visible artifact.
3. Chitrang sends manually from `chitrang@vitan.in` during approved UTC window.
4. Immediately after send, Business Builder updates tracker timestamps and next-action fields.

### Ready-to-send template block
- `To:` `<resolved route email>`
- `Subject:` `<approved subject>`
- `Body:` `<finalized personalized body>`
- `Attachments:` `1-2 referenced project visuals`

## Response Management Process (Resolved)

### Ownership
- Inbox monitor: Chitrang (mailbox owner)
- CRM/tracker logger: Business Builder
- Meeting scheduling owner: Business Builder (with Chitrang availability confirmation)

### Monitoring cadence
- Day 0 to Day 2 after send: every 2 hours during business hours (IST) + one end-of-day check.
- Day 3 onward: twice daily until first follow-up decision.

### Logging rules
For every response (or non-response milestone), update:
- `reply_received_at_utc`
- `reply_type` (`positive_interest`, `needs_info`, `not_now`, `no_fit`, `oop`, `none`)
- `reply_latency_hours`
- `last_action_at_utc`
- `next_action`
- `next_touch_due_at_utc`
- `follow_up_sequence_step`

### Follow-up and escalation triggers
- Positive interest: propose 2 meeting slots within 24 hours; set `meeting_offered_at_utc`.
- Needs info: send capability snapshot within 24 hours; keep `follow_up_sequence_step=0`.
- No reply by business day 4: send first bump and set `follow_up_sequence_step=1`.
- No reply after bump window: escalate to hold/dormant reason in tracker.

### Meeting scheduling flow
1. If positive response arrives, Business Builder drafts reply with 2 slot options.
2. Chitrang confirms preferred slot.
3. Business Builder sends confirmation and updates:
   - `meeting_confirmed_at_utc`
   - `meeting_scheduled_for_utc`

## Governance
- No external send executed in this issue.
- This SOP unblocks execution readiness and board review; send still requires approval.
