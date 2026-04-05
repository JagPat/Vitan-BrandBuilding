# Vitan Autonomous Operating System

Owner: Principle Architect (PA)  
Status: Canonical system blueprint  
Last updated: 2026-04-05

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

As of 2026-04-05:

- `SOCIAL_STRATEGY.md` is missing from the tracked repo and has been delegated for restoration in [VITA-287](/VITA/issues/VITA-287)
- publication-source blockers remain open in [VITA-211](/VITA/issues/VITA-211) and [VITA-226](/VITA/issues/VITA-226)

## Sources Consulted

- `Business development/shared-workspace/references/growth-os.md`
- `Business development/shared-workspace/references/engagement-system.md`
- Open issue state: [VITA-211](/VITA/issues/VITA-211), [VITA-226](/VITA/issues/VITA-226), [VITA-285](/VITA/issues/VITA-285), [VITA-286](/VITA/issues/VITA-286), [VITA-287](/VITA/issues/VITA-287)
