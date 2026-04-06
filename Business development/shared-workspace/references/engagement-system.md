# Vitan Architects — Client Engagement System

## Overview

This document defines the complete client-engagement journey for Vitan Architects, from cold outreach through active collaboration. Every communication must be stage-appropriate, recipient-aware, and tied to a measurable outcome.

## Engagement Stages

### Stage 1: FIRST OUTREACH (cold → warm)
**Goal**: Open a conversation, not sell. Make THEM the subject.
**Trigger**: New contact added to contacts-master with stage=cold

**Recipient-type messaging**:
- Founder/MD/Owner: "We'd love to understand your upcoming projects" — peer-to-peer
- Director/VP: "Your recent project caught our attention" — professional admiration
- Project Manager: "We've worked on similar projects" — practical, collaborative
- Existing Client: "It's been a while — we'd love to catch up" — warm, familiar
- Referral: "{{Referrer}} suggested we connect" — warm, referenced

**Rules**: Subject never salesy. Body 2-3 short paragraphs (about THEM first). CTA: "Schedule a Meeting"/"Visit Our Studio". Fallback: "or call directly: +91 99250 11639". Hero image matched to sector.

### Stage 2: FOLLOW-UP 1 (5 business days, no response)
Do NOT repeat Stage 1. Share relevant project detail or publication. Shorter than Stage 1 (<100 words). Different hero image. Warm, not pushy.

### Stage 3: FOLLOW-UP 2 (10 more business days, no response)
Different angle: share case study PDF. Frame as "thought you might find this useful". If no response → mark dormant, set re-engage date +90 days. Max 3 emails to cold contact.

### Stage 4: VISIT COMMUNICATION
4a. Confirmation (1 day before): date/time/location, agenda, portfolio PDF
4b. Day-of reminder: brief logistics only, Jagrut mobile for changes

### Stage 5: POST-VISIT FOLLOW-UP (within 24 hours)
Thank + reference ONE specific discussion point (board provides via VITA comment). Propose next step. Must feel hand-crafted, not templated.

### Stage 6: PROPOSAL / COLLABORATION
Board-directed. BB prepares materials (approach doc, fee proposal cover, capability statement). Track: proposal_sent → won/lost.

### Stage 7: RE-ENGAGEMENT (dormant, 90 days)
Fresh angle (new project, award, publication). Max 2 re-engagement attempts/year. If no response → lost.

## Follow-Up Trigger Rules
- cold + 5 biz days no response → Follow-up 1
- Follow-up 1 + 10 biz days no response → Follow-up 2  
- Follow-up 2 + 10 biz days no response → dormant, re-engage +90 days
- dormant + follow-up date reached → re-engagement email
- positive response/meeting scheduled → visit prep
- visit completed (board confirms) → post-visit follow-up

## Loop Closure
- Won: board confirms → stop outreach
- Lost: board confirms → stop outreach, log reason
- Dormant: 3 unanswered → dormant, re-engage 90 days
- Dead: 2 re-engagements no response → lost, stop all
- Declined: explicit decline → lost/declined, never contact again

## Outbound Authority Rule

- `PA approved for outbound` means the content, route, and guardrails are approved for execution on the named task.
- After that approval, BB may execute Stage-1, Stage-2, Stage-3, and Stage-7 outreach directly using the canonical approved sending route when the contact sensitivity is GREEN or AMBER.
- RED sensitivity outreach still requires explicit board approval before any send, and the board may still require board-side sending on a task when relationship context or channel control matters.
- If the board wants to retain direct sending control on a specific task, that exception must be stated explicitly in the issue or approval thread. Do not infer it from the general workflow.
- BB must not improvise a new channel, new recipient, or materially revised copy after approval. Any such change returns the task to board review.

## Email Delivery Workflow
1. BB drafts HTML → shared-workspace/review/vita{NNN}/
2. BB updates contacts-master Draft Message Status = "drafted"
3. Board reviews → approves/changes/rejects
4. If approved for outbound and sensitivity is GREEN/AMBER, BB sends via the canonical approved route and logs the send
5. If sensitivity is RED or the board explicitly retains send ownership, board sends via the named route and records that choice in the issue
6. BB updates contacts-master: "sent", Last Contacted = date, route used, and execution note reference
7. BB monitors follow-up triggers
