# Board Feedback

Owner: Principle Architect (PA)  
Status: Active log  
Last updated: 2026-04-20

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

### 2026-04-20 — PA approved Wave 2 skyscraper outreach drafts
- **Issue:** VITA-595 / VITA-725 — Wave 2 drafts for 5 skyscraper targets (VIT-C-025 to VIT-C-029 range)
- **Decision:** PA approved (Job 4 Quality Gate) — all 5 drafts pass brand voice, guardrails, and value-lead checks
- **Drafts location:** `shared-workspace/review/VITA-725/` (commit f4d52f0 on agent/bb branch)
- **Status:** Ready for board review and dispatch decision; VITA-733 created for BB to send

### 2026-04-20 — Board prefers group address for system email delivery (VITA-755)
- **Issue:** [VITA-755](/VITA/issues/VITA-755)
- **Channel:** Paperclip issue comment (Jagrut Patel, 2026-04-20T05:33)
- **Decision:** Board wants all Growth OS emails sent TO `board@vitan.in` (Zoho group), not individual addresses or Gmail.
- **Context:** Social-media-workflow was sending to `jagrutpatel@gmail.com`; board received in Gmail, not Zoho inbox.
- **Action:** [VITA-756](/VITA/issues/VITA-756) filed to FE — update BOARD_CONTACTS.yaml to use `board@vitan.in` group; fix social-media-workflow.md From/To.
- **Pattern signal (1/3):** Use group address for board delivery; all system emails FROM `growthos@vitan.in` (reinforces PC-001 signal).

### 2026-04-20 — Board needs to decide on IBDA entry fee (deadline today)
- **Issue:** VITA-632 — India's Best Design Awards 2026 (Safal Vihaan), deadline April 20
- **Open ask:** ₹35,000 entry fee approval; high-res Safal Vihaan photos
- **Channel:** VITA-645 board alert and VITA-632 PA comment (2026-04-20T03:56)
- **Status:** OC actively running VITA-632 but cannot file without fee approval and photos

## Preference Codex

### PC-001 — Clean closure with explicit board confirmation
Board prefers closing system-level issues only after end-to-end verification with explicit confirmation, not just intermediate milestone completion. (Sourced from 2026-04-18 Zoho identity closure pattern, 1 occurrence — monitor for 2 more before full promotion.)

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
- `Business development/shared-workspace/references/board-communication-protocol.md`
