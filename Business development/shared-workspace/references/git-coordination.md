# Git Coordination Protocol — Vitan Growth OS

Owner: Principle Architect (PA)  
Status: Active coordination protocol  
Last updated: 2026-04-06

## Branch Isolation (7 Agents)

| Agent | Branch | Primary Dimensions |
|-------|--------|-------------------|
| Business Builder (BB) | `agent/bb` | Dim 1: Client Acquisition, Dim 11: Strategic Partnerships |
| Founding Engineer (FE) | `agent/fe` | Dim 4: Website & SEO (technical), Infrastructure |
| Principle Architect (PA) | `agent/pa` | Strategic Oversight, Quality Gate, Vision |
| HR | `agent/hr` | Dim 7: Academic Engagement, Talent Pipeline |
| Brand Storyteller (BS) | `agent/bs` | Dim 2: Industry Portals, Dim 8: Publications, Dim 9: Media/PR |
| Outreach Coordinator (OC) | `agent/oc` | Dim 5: Awards, Dim 6: Speaking, Dim 10: Associations |
| Digital Presence Manager (DP) | `agent/dp` | Dim 3: Social Media, Dim 4: Website (content), Dim 12: Reputation |

## Protected Main Branch

- Direct push to `main` is **blocked** for all agents
- All changes go through PRs: `agent/{name}` → `main`
- PA agent or board merges approved PRs
- After merge, agents sync their branches from latest main

## Merge-Cycle Ownership

- PA owns merge readiness, approval gating, and the daily branch scan.
- FE owns the technical execution that promotes approved changes into `main`.
- Source agents own keeping their designated branch pushable, rebased, and traceable to issue artifacts.

## Merge Triggers

### 1. Task-Completion Trigger

Run when an agent closes or submits work for approval and confirms the pushed commit exists on its designated branch.

PA actions:

1. validate the issue linkage, artifact path, approval state, and `Sources Consulted` block
2. decide the merge unit:
   - single approved commit
   - contiguous approved commit span
   - full branch head only if the entire ahead range is approved
3. create a `[TASK]` issue for FE with the merge packet

### 2. Daily Scan Trigger

Run during PA's 10:30 AM IST Daily Content Review.

PA actions:

1. compare `origin/main` against every `origin/agent/*` branch
2. identify branches that are ahead of `main`
3. classify each ahead range as:
   - `merge-ready`
   - `approval-pending`
   - `mixed-range`
   - `blocked`
4. create FE execution tasks only for `merge-ready` units
5. surface stale merge-ready backlog in the board digest

## Merge Readiness Checklist

PA must confirm all of the following before opening an FE merge task:

- pushed commit SHA or approved commit span is known
- artifact paths exist in the tracked repo on the source branch
- parent issue and downstream trace are explicit
- external-facing content has PA approval recorded
- internal governance changes have a clear owning issue and review artifact
- `Sources Consulted` section is present where required
- no secrets or sensitive data are exposed
- merge unit is bounded to approved work rather than implied by full branch divergence

## Merge Unit Rules

- Agent branches are persistent working lanes, not automatic deployment units.
- FE must **not** merge a whole branch head by default when the branch contains unrelated or unapproved commits.
- Default mode is a bounded promotion merge:
  1. create a temporary promotion branch from `origin/main`
  2. cherry-pick the approved commit set or contiguous approved span
  3. validate the resulting tree
  4. merge that promotion branch into `main` using the repo's supported review path
- Whole-branch squash is allowed only when PA explicitly states that the full ahead range is approved for promotion.
- If PA cannot isolate an approved commit set cleanly, the work is `mixed-range` and FE should not merge until PA resolves scope.

## FE Merge Packet Format

Every PA -> FE merge task must include:

- source issue link
- source branch
- approved commit SHA or SHA range
- artifact paths being promoted
- merge mode: `promotion-branch` or `whole-branch`
- approval basis
- conflict notes, if any

## Conflict Handling

- Trivial non-semantic conflicts: FE may resolve directly and document what changed.
- Content overlap or approval ambiguity: FE opens a `[COORDINATION_GAP]` issue for PA arbitration.
- Structural or tool failure: FE marks the merge task `blocked` and escalates with the exact failing command or platform condition.

## Post-Merge Requirements

- FE comments the `main` commit SHA and promoted artifact paths on both the merge task and the source issue.
- PA updates branch-scan status on the next review cycle.
- The source agent rebases or syncs its branch from `main` before new delivery work proceeds.

## File Ownership (Advisory)

| Path | Primary Owner | Secondary |
|------|--------------|-----------|
| shared-workspace/references/ | PA | All agents |
| shared-workspace/contacts-master.csv | BB | PA |
| shared-workspace/review/{issue-id}/ | Assigned agent | PA |
| shared-workspace/deliverables/content/ | BS | PA |
| shared-workspace/deliverables/outreach/ | OC | PA |
| shared-workspace/deliverables/social/ | DP | HR |
| shared-workspace/deliverables/analytics/ | DP | PA |
| shared-workspace/references/awards-calendar.md | OC | PA |
| shared-workspace/references/publishing-protocol.md | DP | BS, BB |
| shared-workspace/references/sensitivity-protocol.md | BB | PA |
| shared-workspace/references/brand-ecosystem.md | PA | All |

## Cross-Agent Coordination Rules

1. Never modify files another agent is actively working on
2. Use shared-workspace/references/ for inter-agent communication
3. If you need content from another agent's domain, create an issue requesting it
4. PA agent is the merge authority — tag PA in your PR description
5. All deliverables must go through shared-workspace/review/ before final

## Sources Consulted

- `SYSTEM_ARCHITECTURE.md`
- `Business development/shared-workspace/review/vita313/board-morning-digest-2026-04-06.md`
- `Business development/shared-workspace/review/vita328/merge-cycle-routine-2026-04-06.md`
- [VITA-318](/VITA/issues/VITA-318)
- [VITA-320](/VITA/issues/VITA-320)
- [VITA-328](/VITA/issues/VITA-328)
