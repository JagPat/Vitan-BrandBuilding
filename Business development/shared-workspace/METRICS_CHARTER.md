# Metrics Charter

Owner: Principle Architect (PA)  
Status: Active operating charter  
Last updated: 2026-04-06

## Purpose

This document defines the KPI surface for the 7-agent system. It is the operating interpretation layer for performance management. It does not override `EVALUATION_BASELINES.md`, which remains the scoring source of truth once baselines are set.

## Use Rules

- Update this file when KPI definitions, ownership, or measurement intent changes.
- Do not log weekly results here. Use `evaluation-log.md` and agent scorecards.
- If a KPI is described here but not yet measurable, mark it as `bootstrapping`.
- When board-approved baseline changes are accepted, reflect them here and in `EVALUATION_BASELINES.md`.

## System-Level KPIs

| Metric | Owner | Target | Status |
| --- | --- | --- | --- |
| Strategy-to-publish time | PA | `< 7 days` | active |
| Full cycle time (strategy to feedback) | PA | `< 14 days` | active |
| Cascade completion rate | PA | `100%` | active |
| Relay drop rate | PA | `0` | active |
| PA approval latency | PA | `< 4 hours` | active |

## Agent KPI Surface

### Principle Architect

- Planning-cascade health surfaced accurately
- Approval latency held below target
- Architecture and governance artifacts kept current
- Ratchet, adaptation, and board-feedback routines executed when due

### Business Builder

- Strategy brief delivered on cadence
- Upstream strategy adopted by DPM / BS / OC
- Client-acquisition lanes advanced from research to real market contact
- Sensitivity and authority rules kept execution-safe

### Founding Engineer

- Platform-health signals stay reliable
- Governance tooling and execution helpers reduce manual coordination drag
- Infrastructure blockers are converted into stable workflows or tools

### HR / Workforce Architect

- Capability gaps diagnosed and triaged on time
- Agent-spec proposals grounded in real workload and coordination evidence
- Workforce topology remains aligned with active objectives

### Digital Presence Manager

- Weekly plan delivered on cadence
- Weekly plan traces to current BB strategy
- Performance feedback flows back upstream to BB

### Brand Storyteller

- Long-form outputs align to active strategy and discoverability goals
- Publication and thought-leadership outputs connect to broader relay goals

### Outreach Coordinator

- Awards, speaking, and partnership lanes advance with clear strategic linkage
- External visibility opportunities are fed back into BB / DPM when relevant

## Measurement Notes

- Use `scorecards/` for cycle snapshots.
- Use `evaluation-log.md` for verdict history.
- Use `ratchet-log.md` when proposing or recording target increases.

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
- `SYSTEM_ARCHITECTURE.md`
- `Business development/shared-workspace/references/board-digest-template.md`
