# Scorecards Contract

Owner: Principle Architect (PA)  
Status: Starter contract  
Last updated: 2026-04-06

## Purpose

This directory holds per-agent cycle scorecards used for ratchet review, relay-break detection, and adaptation decisions.

## Naming Convention

- One file per agent per cycle, for example:
  - `pa-YYYY-MM-DD.md`
  - `bb-YYYY-MM-DD.md`
  - `fe-YYYY-MM-DD.md`
  - `hr-YYYY-MM-DD.md`
  - `dpm-YYYY-MM-DD.md`
  - `bs-YYYY-MM-DD.md`
  - `oc-YYYY-MM-DD.md`

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

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
