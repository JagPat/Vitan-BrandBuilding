# Scorecards Contract

Owner: Principle Architect (PA)  
Status: Starter contract  
Last updated: 2026-04-06

## Purpose

This directory holds per-agent cycle scorecards used for ratchet review, relay-break detection, and adaptation decisions.

## Canonical Files

- Each agent maintains one rolling canonical scorecard file at the path referenced in its operating instructions:
  - `PA-SCORECARD.md`
  - `BB-SCORECARD.md`
  - `FE-SCORECARD.md`
  - `HR-SCORECARD.md`
  - `DPM-SCORECARD.md`
  - `BS-SCORECARD.md`
  - `OC-SCORECARD.md`
- These files are the required repo-backed locations for the latest live scorecard state.
- If cycle snapshots are needed later, add them as linked historical artifacts without replacing the canonical per-agent file.

## Minimum Fields

- cycle date
- agent name
- key outputs shipped
- KPI snapshot
- relay dependencies met / missed
- blockers
- retrospective signal

## Rule

Do not backfill fake historical scorecards. Start from the next real cycle.

## Current Starter Files

- The canonical per-agent scorecard files were created on 2026-04-06 to resolve path-contract ambiguity between operating instructions and the shared-workspace contract.
- Blank starter files are allowed. Invented historical performance is not.

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
