# Technical Operating Model and Delivery System v1

Original target date: 2026-03-24
Reconstructed in repo: 2026-04-04
Source issues: VITA-3, VITA-66, VITA-178

## Purpose

Define the first durable operating model for Vitan's architecture practice so work moves through a repeatable system instead of ad hoc coordination.

## Operating Model

- Use one canonical project workspace per active initiative.
- Convert meaningful work into Paperclip issues with clear ownership and closure evidence.
- Keep one weekly delivery review to inspect priorities, blockers, and shipped outputs.
- Require one QA gate before release or external publication.
- Maintain one decision and risk log per project so tradeoffs stay visible.

## Delivery Backbone

### 1. Intake and Framing

- The Principle Architect defines the desired outcome and assigns work through Paperclip.
- Every task should specify the owner, expected artifact, and success condition.

### 2. Execution

- The assigned agent checks out the issue before doing work.
- Work happens inside the shared repository and linked workspace, not in private scratch space.
- Durable outputs are stored in repo paths that other operators can inspect.

### 3. Review

- Weekly delivery review inspects progress, open blockers, and quality gaps.
- QA confirms the artifact exists, the path is valid, and the stated evidence is real.

### 4. Closure

- `done` requires objective evidence: a committed artifact, proof link, or other verifiable output.
- `blocked` requires blocker type, unblock owner, and next event.
- Strategy redirects must link the replacement issue or artifact.

## Shared Artifacts

- `plans/` stores shared plans and operating documents.
- `Business development/reports/` stores execution evidence and delivery proofs.
- `Business development/shared-workspace/` stores drafts, reviews, approvals, and change notes.

## Cadence

- Daily: heartbeat execution against assigned Paperclip issues.
- Weekly: delivery review with status, risks, and next actions.
- As needed: QA review before release and whenever closure evidence is challenged.

## Throughput Controls

- Limit active work to issues with explicit ownership.
- Prefer continuation issues over silent closure when evidence is missing.
- Use repo artifacts and comments to keep handoffs auditable.

## Staffing Trigger

The next full-time delivery hire should be a Project Architect / Delivery Lead once a live pursuit or signed project creates a sustained daily coordination gap that the Principle Architect should no longer absorb directly.

## Version Note

This file is a repo reconstruction of the operating model referenced in earlier issue comments. It reflects the surviving system rules now codified in `SYSTEM_ARCHITECTURE.md` and the related continuation issues.
