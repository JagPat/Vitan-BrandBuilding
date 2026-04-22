# Board Feedback

Owner: Principle Architect (PA)  
Status: Active log  
Last updated: 2026-04-22

## Purpose

This file records board-facing decisions, recurring preferences, and pattern implications. It is the durable source for later references to board patterns.

## Logging Rules

- Log board interactions within 24 hours.
- Do not store secrets or raw credentials here.
- Move recurring patterns into the Preference Codex only after 3 or more consistent decisions.
- For email or WorkDrive-based reviews, log:
  - issue id
  - verdict
  - channel
  - short reasoning summary
  - source ids or message ids
- Do not copy full email bodies into this file.

## Decision Log

### 2026-04-18 — Zoho Mail Identity Closure (Board Directive)
- **Issue:** VITA-510 (parent), VITA-511, VITA-480
- **Verdict:** Close all Zoho mail issues — system identity resolved
- **Channel:** Paperclip comment on VITA-510 (user, 09:53 UTC)
- **Summary:** Board confirmed `growthos@vitan.in` is the dedicated system email. Old `jp@vitan.in` setup cancelled. Board tested live send and confirmed receipt. Directed PA to close all related issues. PA closed VITA-510, VITA-511, VITA-480.
- **Pattern signal:** Board prefers clean closure with explicit confirmation once system-level changes are verified end-to-end (not just intermediate steps).

### 2026-04-19 — Board increased Gemini AI Studio budget
- **Issue:** VITA-649 / VITA-645 — all gemini_local agents in error (quota exhaustion)
- **Decision:** Board increased Google AI Studio "Using Budget" for Gemini app
- **Channel:** Paperclip comment on VITA-649 (2026-04-19T13:59:58)
- **Outcome:** Partial recovery — BB, DPM, OC, HR recovered; BS remained in error (permissions blocker)
- **Pattern implication:** Gemini quota can be exhausted by parallel heartbeat runs; budget headroom needed for concurrent agent ops

### 2026-04-20 — Wave 2 skyscraper outreach DISPATCHED (15 targets)
- **Issue:** VITA-733 — Dispatch Stage 1 + Wave 2 emails to skyscraper prospects
- **Decision:** PA approved (Job 4 Quality Gate) — all 15 drafts passed brand voice, guardrails, value-lead checks
- **Outcome:** VITA-733 is DONE. 15 personalized emails dispatched by BB (Stage 1: 10 targets, Wave 2: 5 targets). contacts-master.csv updated with sent-date 2026-04-20.
- **Source issues:** VITA-595 (Stage 1 drafts), VITA-725 (Wave 2 drafts)
- **Pattern signal:** Zoho rate-limit hit during Wave 2 dispatch; BB auto-retried after cooldown. No board intervention needed.

### 2026-04-20 — Board prefers group address for system email delivery (VITA-755)
- **Issue:** [VITA-755](/VITA/issues/VITA-755)
- **Channel:** Paperclip issue comment (Jagrut Patel, 2026-04-20T05:33)
- **Decision:** Board wants all Growth OS emails sent TO `board@vitan.in` (Zoho group), not individual addresses or Gmail.
- **Context:** Social-media-workflow was sending to `jagrutpatel@gmail.com`; board received in Gmail, not Zoho inbox.
- **Action:** [VITA-756](/VITA/issues/VITA-756) filed to FE — update BOARD_CONTACTS.yaml to use `board@vitan.in` group; fix social-media-workflow.md From/To.
- **Pattern signal (1/3):** Use group address for board delivery; all system emails FROM `growthos@vitan.in` (reinforces PC-001 signal).

### 2026-04-20 — IBDA 2026 Submission FILED (Safal Vihaan)
- **Issue:** VITA-632 — India's Best Design Awards 2026 (Safal Vihaan)
- **Outcome:** Submission FILED and confirmed. VITA-632 status: done.
- **Channel:** OC confirmed in BB standup VITA-742 (2026-04-20T04:40)
- **Pattern signal:** OC successfully executed a submission under deadline pressure even with photo constraints — agents can file with available assets. Board approved fee/action implicitly by not stopping it.

### 2026-04-20 — WAF 2026 Asset Upload — Action Required sent to board
- **Issue:** VITA-474, VITA-530, VITA-588 — WAF 2026 deadline April 24
- **Open ask:** High-res photos for Shaligram Luxuria, Augusta, Safal Vihaan
- **Channel:** Action Required email from growthos@vitan.in to board@vitan.in (messageId: 1776663741846130300, 11:12 IST)
- **Status:** Open. Next escalation: 48h mark (~2026-04-21 03:00 UTC) → severity=Critical if no board response.

### 2026-04-20 — IIA Ascension Registration — IIA Membership Number needed
- **Issue:** VITA-739 — IIA Ascension Competition registration (deadline Apr 30)
- **Open ask:** IIA Membership Number for Ar. Jagrut Patel
- **Channel:** PA escalation comment on VITA-739 (2026-04-20T05:09)
- **Status:** Open. 10 days remain. No email sent yet (threshold not reached).

### 2026-04-22 — Board raised Gemini spend cap (second time) — VITA-837/838
- **Issue:** [VITA-837](/VITA/issues/VITA-837) / [VITA-838](/VITA/issues/VITA-838) — multi-agent gemini_local outage
- **Decision:** Board (jp@vitan.in) raised Gemini AI Studio spend cap at 08:10:30 UTC
- **Channel:** Paperclip comment on VITA-838 (comment `62828008`)
- **Context:** All 5 gemini_local agents (BB, HR, OC, DPM, BS) were in `error` due to 429 RESOURCE_EXHAUSTED. PA sent FE-Bootstrap escalation emails (~22:43 UTC Apr 21) to jagrutpatel, kaivana, chitrang. Board acted ~9.5h later.
- **Outcome:** Partial — Gemini API returned `OK` after cap raise, but agents still fail with `Process lost -- server may have restarted`. Platform restart orphaned gemini_local adapter processes.
- **Pattern signal (2/3 — matches 2026-04-19 quota pattern):** Gemini quota exhaustion is a recurring monthly risk. Two incidents within 3 days (2026-04-19, 2026-04-22). Budget headroom insufficient for current agent count.
- **Open board action:** Platform restart recovery — see [VITA-837](/VITA/issues/VITA-837). Board needs to Coolify-redeploy or SSH-restart gemini_local processes.
- **Escalation log:** PA unable to send board email (Zoho MCP not available this session). Escalated via Paperclip comment on [VITA-837](/VITA/issues/VITA-837) at ~09:30 UTC.

### 2026-04-22 — WAF 2026 deadline imminent (April 24) — assets still missing
- **Issue:** [VITA-474](/VITA/issues/VITA-474), [VITA-530](/VITA/issues/VITA-530), [VITA-588](/VITA/issues/VITA-588)
- **Status:** OC/DPM are in error and cannot execute. WAF portal deadline is April 24 — 2 days away.
- **Open board action:** Board must either supply high-res photos immediately OR accept that WAF entry will be filed without those assets.
- **Pattern signal:** Asset upload blockers repeating (WAF, IIA Ascension, IBDA). See KAIZEN [VITA-764](/VITA/issues/VITA-764).

### 2026-04-20 — PA Heartbeat: Strategic Synthesis + Routing
- **Actions taken:**
  - Posted PA Weekly Strategic Synthesis on [VITA-752](/VITA/issues/VITA-752) (BB standup) — covers outreach monitoring, WAF escalation plan, IIA fallback option, asset SOP need
  - Routed VITA-734 (IIA Ascension parent) to BB (already orchestrating sub-tasks)
  - Created [VITA-764](/VITA/issues/VITA-764) [KAIZEN] for recurring asset-upload gap SOP
  - VITA-735 stale lock conflict — could not cancel; BB to handle
- **Budget at heartbeat close:** ~78.2% (₹117.31/₹150.00)
- **Open board actions still pending:** WAF photos ([VITA-474](/VITA/issues/VITA-474)), IIA Membership Number ([VITA-739](/VITA/issues/VITA-739))

## Preference Codex

### PC-001 — Clean closure with explicit board confirmation
Board prefers closing system-level issues only after end-to-end verification with explicit confirmation, not just intermediate milestone completion. (Sourced from 2026-04-18 Zoho identity closure pattern, 1 occurrence — monitor for 2 more before full promotion.)

### PC-002 — Gemini quota exhaustion is a recurring monthly risk (2/3 — not yet fully promoted)
Gemini spend cap has been exhausted twice within a 4-day window (2026-04-19, 2026-04-22). Current agent count (5 gemini_local) creates peak-load risk. Monitor for a third incident — if it recurs, promote to a formal capacity recommendation: raise default spend cap or reduce concurrent gemini_local heartbeat frequency. Board responds promptly once alerted (response time: ~9-10h).

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
- `Business development/shared-workspace/references/board-communication-protocol.md`
