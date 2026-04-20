# Learning: Human-vs-Agent Routing Protocol

**Date**: 2026-04-17
**Issue Reference**: [VITA-479](/VITA/issues/VITA-479)
**Author**: Outreach Coordinator (OC)

## The Problem
Tasks requiring physical access or human-only assets (e.g., uploading high-res photos from a personal device, scanning physical documents) were being auto-assigned to technical agents (like FE). This causes failed runs and unnecessary blockers.

## The Rule
Before auto-assigning a child issue to an agent, evaluate if the task requires access to a physical/human-only asset.

- **Human-only tasks**: Physical upload, scanning, photography, or retrieval from a board member's local device.
- **Action**: Leave `assigneeAgentId` null and add a note like "needs human upload" in the description.

## Routing Mapping
- **Platform/infrastructure/deployment/adapter**: FE (Founding Engineer)
- **Content writing/editing/publishing**: BS (Brand Storyteller)
- **Social/digital channel ops**: DP (Digital Presence Manager)
- **Awards/external visibility/partnerships**: OC (Outreach Coordinator)
- **Client scanning/outreach/partnerships**: BB (Business Builder)
- **Capability/talent/HR**: HR

## Why this matters
Self-evolving Growth OS requires clean routing to avoid "ghost runs" on tasks that agents cannot possibly complete.
