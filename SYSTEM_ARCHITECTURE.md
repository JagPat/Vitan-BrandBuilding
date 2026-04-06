# Vitan Autonomous Operating System

Owner: Principle Architect (PA)  
Status: Canonical system blueprint  
Last updated: 2026-04-06

## Purpose

This document defines how Vitan's 7-agent operating system is structured, how work flows from strategy to execution, and which artifacts are required for governance. If any required artifact is missing or stale, the planning cascade is considered degraded and must be surfaced explicitly in board communications.

## Agent Topology

### Core Layer

- Principle Architect (PA): system brain, strategic direction, architecture ownership, final approval authority
- Business Builder (BB): brand and growth strategy owner, upstream signal source for execution agents
- Founding Engineer (FE): infrastructure, deployment, automation, tooling, and platform reliability
- HR / Workforce Architect (HR): capability planning, hiring design, workforce architecture, readiness assessment

### Execution Layer

- Digital Presence Manager (DPM): social media planning and execution across Dimensions 3, 4, and 12
- Brand Storyteller (BS): long-form content, portal submissions, and discoverability across Dimensions 2, 8, and 9
- Outreach Coordinator (OC): awards, speaking, partnerships, and community visibility across Dimensions 5, 6, 10, and 11

## Ownership Model

- PA owns `SYSTEM_ARCHITECTURE.md` and the planning-cascade governance model.
- BB owns `SOCIAL_STRATEGY.md` and the strategy-refresh outputs that drive execution-layer work.
- DPM owns weekly social planning artifacts and daily campaign packs for review.
- BS owns long-form and publication artifacts.
- OC owns awards, speaking, and partnership visibility artifacts.
- FE owns technical infrastructure, automation, and environment reliability.
- HR owns capability planning, agent design proposals, and workforce readiness outputs.

## Planning Cascade

The planning cascade is the primary operating rhythm for content and visibility work.

### 1. Strategy Refresh

Cadence: Tuesday, 7:00 PM IST  
Primary owner: BB  
Required outputs:

- `SOCIAL_STRATEGY.md`
- `Business development/shared-workspace/drafts/strategy-brief-YYYY-MM-DD.md`
- downstream Paperclip issues for DPM, BS, and OC when execution work is required

### 2. Weekly Social Media Plan

Cadence: Thursday, 7:00 PM IST  
Primary owner: DPM  
Required outputs:

- `Business development/shared-workspace/drafts/weekly-plan-YYYY-MM-DD.md`
- linked execution issues for campaign production and review

Inputs:

- current `SOCIAL_STRATEGY.md`
- latest BB strategy brief
- active BS and OC dependencies
- board preference references and sensitivity guardrails

### 3. Daily Content Review

Cadence: Daily, 10:30 AM IST  
Primary owner: PA  
Required actions:

- review campaign artifacts against strategy, brand, sensitivity, and upstream issue links
- provide explicit approval or revision guidance
- preserve two-level sign-off: content approval and image approval

### 4. Board Digests

Cadence: Daily morning and evening  
Primary owner: PA  
Required content:

- planning-cascade health
- active blockers
- major agent progress
- governance risks

### Strategy-Readiness Evidence

Default evidence source:

- Use the platform-health signal `planningCascade.strategy` as the default indicator for strategy-layer readiness when it is available.

Fallback evidence path:

- If the signal is unavailable or suspected stale, PA may fall back to direct repo inspection of:
  - `SOCIAL_STRATEGY.md`
  - the latest `Business development/shared-workspace/drafts/strategy-brief-*.md`

## Required Artifact Paths

- Repo root: `SYSTEM_ARCHITECTURE.md`
- Repo root: `SOCIAL_STRATEGY.md`
- Drafts: `Business development/shared-workspace/drafts/`
- Working review artifacts: `Business development/shared-workspace/review/vita{NNN}/`
- Approved artifacts: `Business development/shared-workspace/approved/vita{NNN}/`
- Governance references: `Business development/shared-workspace/references/`

## Workspace Path Contract

The canonical shared-artifact root for this system is:

- `Business development/shared-workspace/`

This path contract applies to governance files, drafts, review artifacts, approved artifacts, deliverables, scorecards, and reference documents whenever agents are operating inside the tracked repository.

Compatibility rule:

- bare `shared-workspace/...` references in older instructions are deprecated shorthand, not guaranteed runtime paths
- agents must not assume a sibling `shared-workspace/` directory exists at `$AGENT_HOME` unless FE has explicitly provisioned it
- when an agent is mounted with `PAPERCLIP_WORKSPACE_SOURCE=agent_home`, instruction paths must still resolve to the canonical repo-backed location or the runtime must provide a verified mirror

Normalization requirement:

- FE owns the technical fix for aligning runtime mounts and agent instructions with this contract
- PA treats any instruction set that points to nonexistent bare `shared-workspace/...` paths as a structural coordination defect, not an agent execution failure

## Governance Backbone

The system's measurement, adaptation, and board-intelligence layer is tracked in shared-workspace, not in agent-local memory.

- `Business development/shared-workspace/METRICS_CHARTER.md`
  Defines which KPIs exist, who owns them, and how they are interpreted at an operating level.
- `Business development/shared-workspace/EVALUATION_BASELINES.md`
  Read-only scoring function and thresholds. Board-controlled after publication.
- `Business development/shared-workspace/BOARD_FEEDBACK.md`
  Decision log and Preference Codex source for recurring board patterns.
- `Business development/shared-workspace/CAPABILITY_REGISTRY.md`
  Capability map, gap log, and adaptation history for the 7-agent system.
- `Business development/shared-workspace/ratchet-log.md`
  History of ratchet proposals and accepted target increases.
- `Business development/shared-workspace/evaluation-log.md`
  Weekly measurement ledger for PASS / REVERT / RATCHET / UNMEASURED verdicts.
- `Business development/shared-workspace/scorecards/`
  Per-agent rolling scorecards at canonical filenames such as `PA-SCORECARD.md`, `BB-SCORECARD.md`, and their peer agent equivalents.

These artifacts must exist in git if PA is expected to run the Performance Ratchet, Adaptation Engine, Relay Race Protocol, or board-preference extraction without relying on unstored session context.

## Failure Conditions

The system is considered degraded when any of the following are true:

- `SYSTEM_ARCHITECTURE.md` is missing or materially out of date
- `SOCIAL_STRATEGY.md` is missing, stale, or agent-local only
- the drafts directory is missing from git
- a weekly plan exists without a current strategy brief
- daily review is happening without explicit upstream strategic linkage
- execution agents are producing work that does not trace back to strategy or issue dependencies

When degradation is detected, PA must surface it in board communications and create corrective work rather than relying on implicit recovery.

## Cross-Agent Coordination Rules

- Execution-layer agents derive campaign direction from BB strategy and PA directives, not from isolated local interpretation.
- DPM, BS, and OC should reference upstream VITA issues when they produce downstream deliverables.
- FE is engaged when tooling or repository structure prevents the cascade from operating reliably.
- HR is engaged when expansion priorities create capability gaps or when agent topology needs revision.

## Architecture Review Triggers

PA updates this document when:

- a new agent is added or removed
- ownership boundaries materially change
- the planning-cascade timing changes
- recurring coordination failure reveals a structural flaw
- a new workstream becomes part of the operating model

## Current Known Gaps

As of 2026-04-06:

- publication-source blockers remain open in [VITA-233](/VITA/issues/VITA-233), [VITA-226](/VITA/issues/VITA-226), and [VITA-211](/VITA/issues/VITA-211)
- strategy-relay restoration remains open in [VITA-314](/VITA/issues/VITA-314), [VITA-317](/VITA/issues/VITA-317), and [VITA-319](/VITA/issues/VITA-319)
- managed-runtime branch or worktree isolation remains open in [VITA-309](/VITA/issues/VITA-309)
- managed-runtime PR creation remains open in [VITA-318](/VITA/issues/VITA-318)

## Sources Consulted

- `Business development/shared-workspace/references/growth-os.md`
- `Business development/shared-workspace/references/engagement-system.md`
- `Business development/shared-workspace/review/vita311/path-contract-normalization-decision-2026-04-06.md`
- `Business development/shared-workspace/review/vita313/board-morning-digest-2026-04-06.md`
- `Business development/shared-workspace/review/vita326/governance-baseline-resolution-2026-04-06.md`
- Principle Architect operating instructions loaded for 2026-04-06
- Open issue state: [VITA-211](/VITA/issues/VITA-211), [VITA-226](/VITA/issues/VITA-226), [VITA-233](/VITA/issues/VITA-233), [VITA-309](/VITA/issues/VITA-309), [VITA-314](/VITA/issues/VITA-314), [VITA-317](/VITA/issues/VITA-317), [VITA-318](/VITA/issues/VITA-318), [VITA-319](/VITA/issues/VITA-319), [VITA-326](/VITA/issues/VITA-326)
