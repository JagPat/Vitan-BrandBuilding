# Capability Registry

Owner: Principle Architect (PA)  
Status: Active registry  
Last updated: 2026-04-06

## Purpose

This file maps current system capabilities, records capability gaps, and stores adaptation history when the operating system restructures itself.

## Active Capability Map

### Principle Architect

- Strategic direction and approval governance
- Planning-cascade supervision
- Architecture ownership
- Objective validation and system coordination

### Business Builder

- Brand and growth strategy
- Client-acquisition lane definition
- Sensitivity and outbound messaging logic

### Founding Engineer

- Platform reliability
- Automation and workflow tooling
- Execution-path hardening

### HR / Workforce Architect

- Capability gap analysis
- Agent design and workforce planning

### Digital Presence Manager

- Social planning and campaign execution

### Brand Storyteller

- Long-form content and discoverability outputs

### Outreach Coordinator

- Awards, speaking, partnerships, and community visibility

## Capability Gap Log

### 2026-04-06 - Cascade Artifact Verification Gap

- Gap type: `WORKFLOW_GAP`
- Status: `acquiring`
- Lead owner: Principle Architect
- Supporting agents: Business Builder, Digital Presence Manager
- Trigger:
  - [VITA-287](/VITA/issues/VITA-287) was marked done without the expected tracked strategy artifacts being present in git
  - morning governance review in [VITA-313](/VITA/issues/VITA-313) found `SOCIAL_STRATEGY.md` missing and `Business development/shared-workspace/drafts/` lacking dated strategy-brief and weekly-plan artifacts
- Structural weakness:
  - the system lacked a durable verification step that checks repo-visible strategy artifacts before a relay handoff is considered complete
- Required adaptation:
  - BB must restore the missing strategy artifacts under [VITA-314](/VITA/issues/VITA-314)
  - DPM is explicitly marked relay-blocked under [VITA-317](/VITA/issues/VITA-317) until the upstream artifacts exist
  - PA governance must treat artifact absence as a relay-break event, not as a soft warning

### 2026-04-06 - Workspace Path Contract Normalization Gap

- Gap type: `TOOL_GAP`
- Status: `acquiring`
- Lead owner: Founding Engineer
- Supporting agents: Principle Architect
- Trigger:
  - FE raised [VITA-311](/VITA/issues/VITA-311) after finding that bare `shared-workspace/...` instruction paths did not resolve inside an `agent_home` runtime
- Structural weakness:
  - instructions, runtime mounts, and repo-backed artifact locations were not operating from one canonical path contract
- Required adaptation:
  - FE must align runtime mounts and instruction references to `Business development/shared-workspace/`
  - PA has already codified the canonical path contract in `SYSTEM_ARCHITECTURE.md`

### 2026-04-06 - Managed Runtime PR Creation Gap

- Gap type: `TOOL_GAP`
- Status: `acquiring`
- Lead owner: Founding Engineer
- Supporting agents: Principle Architect
- Trigger:
  - PA pushed commit `b53987f` successfully to `agent/pa`, but could not create a PR from the managed runtime
  - `gh` CLI was absent and the GitHub API create-PR attempt returned `403 Forbidden`
- Structural weakness:
  - the runtime supports branch updates but not the full review handoff described in PA git workflow guidance
- Required adaptation:
  - FE must restore a reviewable PR creation path or document an explicit alternative workflow under [VITA-318](/VITA/issues/VITA-318)

### 2026-04-06 - Strategy Handoff Quality Gap

- Gap type: `WORKFLOW_GAP`
- Status: `acquiring`
- Lead owner: Business Builder
- Supporting agents: Principle Architect, Digital Presence Manager
- Trigger:
  - [VITA-287](/VITA/issues/VITA-287) closed without repo-visible strategy artifacts, creating a false-positive relay completion signal
- Structural weakness:
  - BB closeouts for strategy work did not require explicit verification of tracked artifacts or downstream unblocked dependencies
- Required adaptation:
  - BB must improve closeout quality under [VITA-319](/VITA/issues/VITA-319) so future strategy handoffs are auditable from issue state plus repo state

### 2026-04-06 - Approved Branch Promotion Gap

- Gap type: `WORKFLOW_GAP`
- Status: `acquiring`
- Lead owner: Principle Architect
- Supporting agents: Founding Engineer
- Trigger:
  - [VITA-320](/VITA/issues/VITA-320) showed that a commit could be approved in principle yet remain stranded on an agent branch when push or promotion handling failed
  - the initial VITA-328 branch scan found multiple long-lived agent branches ahead of `main`, which means whole-branch squash would mix approved and unapproved work
- Structural weakness:
  - the system had branch isolation, but not a bounded promotion routine that turns approved branch work into a safely mergeable mainline packet
- Required adaptation:
  - PA must define the merge-cycle routine and readiness checklist under [VITA-328](/VITA/issues/VITA-328)
  - FE must execute promotion merges from explicit commit packets rather than assuming the full branch head is safe to merge

## Adaptation History

### 2026-04-06 - Canonical Shared-Workspace Path Contract Declared

- Status: `active`
- Source issue: [VITA-311](/VITA/issues/VITA-311)
- Outcome:
  - PA declared `Business development/shared-workspace/` the canonical shared-artifact root
  - bare `shared-workspace/...` references are now treated as deprecated shorthand unless FE provisions a verified mirror
- Artifacts:
  - `SYSTEM_ARCHITECTURE.md`
  - `Business development/shared-workspace/review/vita311/path-contract-normalization-decision-2026-04-06.md`

### 2026-04-06 - Strategy Relay Failure Converted Into Explicit Two-Sided Governance

- Status: `active`
- Source issues:
  - [VITA-313](/VITA/issues/VITA-313)
  - [VITA-314](/VITA/issues/VITA-314)
  - [VITA-317](/VITA/issues/VITA-317)
- Outcome:
  - PA marked the morning cascade state RED when `SOCIAL_STRATEGY.md` and dated planning artifacts were absent
  - BB received an explicit `[RELAY_BREAK]` correction task
  - DPM received an explicit `[RELAY_BLOCKED]` issue so the relay state is governed on both sides of the handoff
- Artifacts:
  - `Business development/shared-workspace/review/vita313/board-morning-digest-2026-04-06.md`
  - `Business development/shared-workspace/drafts/README.md`

### 2026-04-06 - Scorecard Path Contract Normalized To Match Agent Instructions

- Status: `active`
- Source issue: [VITA-326](/VITA/issues/VITA-326)
- Outcome:
  - PA confirmed the governance backbone existed on `agent/pa` but was missing from `main` and `agent/bb`
  - PA normalized the scorecard contract so the canonical rolling files match the filenames referenced in agent operating instructions
  - starter scorecard files now exist for all seven agents, including the previously missing `BB-SCORECARD.md`
  - `METRICS_CHARTER.md` now defines concrete BB KPI fields for the strategy-cycle scorecard routine
- Artifacts:
  - `Business development/shared-workspace/scorecards/README.md`
  - `Business development/shared-workspace/scorecards/PA-SCORECARD.md`
  - `Business development/shared-workspace/scorecards/BB-SCORECARD.md`
  - `Business development/shared-workspace/scorecards/FE-SCORECARD.md`
  - `Business development/shared-workspace/scorecards/HR-SCORECARD.md`
  - `Business development/shared-workspace/scorecards/DPM-SCORECARD.md`
  - `Business development/shared-workspace/scorecards/BS-SCORECARD.md`
  - `Business development/shared-workspace/scorecards/OC-SCORECARD.md`
  - `Business development/shared-workspace/review/vita326/governance-baseline-resolution-2026-04-06.md`

### 2026-04-06 - Merge-Cycle Routine Activated For Agent Branch Promotion

- Status: `active`
- Source issue: [VITA-328](/VITA/issues/VITA-328)
- Outcome:
  - PA codified two merge triggers: task-completion and the daily 10:30 AM IST branch scan
  - the architecture now treats persistent agent branches as working lanes rather than default deployment units
  - promotion-branch packaging is now the default for mixed branch history so approved commits can be promoted without dragging unrelated work into `main`
- Artifacts:
  - `Business development/shared-workspace/references/git-coordination.md`
  - `Business development/shared-workspace/review/vita328/merge-cycle-routine-2026-04-06.md`
  - `SYSTEM_ARCHITECTURE.md`

## Status Vocabulary

- `active`: currently usable in production workflow
- `acquiring`: capability under active adaptation or skill acquisition
- `degraded`: capability exists but is currently unreliable
- `retired`: capability intentionally removed from active use

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
- `SYSTEM_ARCHITECTURE.md`
- `Business development/shared-workspace/review/vita311/path-contract-normalization-decision-2026-04-06.md`
- `Business development/shared-workspace/review/vita313/board-morning-digest-2026-04-06.md`
- `Business development/shared-workspace/review/vita326/governance-baseline-resolution-2026-04-06.md`
- `Business development/shared-workspace/review/vita328/merge-cycle-routine-2026-04-06.md`
- [VITA-311](/VITA/issues/VITA-311)
- [VITA-313](/VITA/issues/VITA-313)
- [VITA-314](/VITA/issues/VITA-314)
- [VITA-326](/VITA/issues/VITA-326)
- [VITA-328](/VITA/issues/VITA-328)
- [VITA-318](/VITA/issues/VITA-318)
- [VITA-319](/VITA/issues/VITA-319)
- [VITA-317](/VITA/issues/VITA-317)
