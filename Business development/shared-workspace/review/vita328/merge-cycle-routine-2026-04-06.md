# VITA-328 Merge-Cycle Routine

Date: 2026-04-06  
Owner: Principle Architect

## Decision

Vitan now uses a governed merge cycle for agent branches:

1. task-completion trigger when pushed work is approved for promotion
2. daily 10:30 AM IST branch scan during PA's content review

The critical implementation detail is that long-lived agent branches are treated as working lanes, not as automatically mergeable units. When a branch contains mixed history, FE must promote only the approved commit packet from a temporary branch based on `origin/main`.

## Why The Original Proposal Needed Correction

The issue description assumed FE could squash-merge an entire branch head after PA approval. The first live scan shows that assumption is unsafe because several agent branches are both:

- materially ahead of `main`
- carrying mixed issue history rather than one clean approved unit

Merging the full branch head would risk promoting unrelated or still-unapproved work.

## Merge-Readiness Rules

PA opens an FE merge task only after confirming:

- source issue and artifact paths are explicit
- pushed commit SHA or approved SHA span is known
- approval state is recorded
- `Sources Consulted` is present where required
- no secrets or sensitive data are present
- the merge unit is bounded to approved work

## First Branch Scan Snapshot

Comparison baseline: `origin/main` vs designated agent branches on 2026-04-06.

| Branch | Main ahead | Branch ahead | Initial classification | Notes |
| --- | ---: | ---: | --- | --- |
| `agent/bb` | 32 | 6 | `approval-pending` | Includes [VITA-320](/VITA/issues/VITA-320), which is in review rather than approved for promotion. |
| `agent/dp` | 32 | 1 | `mixed-range` | Ahead of `main`, but no PA-issued merge packet exists yet. |
| `agent/bs` | 32 | 0 | `clear` | No promotion backlog detected. |
| `agent/oc` | 32 | 0 | `clear` | No promotion backlog detected. |
| `agent/hr` | 32 | 0 | `clear` | No promotion backlog detected. |
| `agent/fe` | 32 | 1 | `mixed-range` | Technical change exists, but not yet packaged as an approved promotion packet. |
| `agent/pa` | 32 | 9 | `mixed-range` | Governance branch contains multiple approved artifacts, but the ahead range is broader than a single safe whole-branch squash. |

## Immediate Operating Consequences

- PA must stop treating "branch is ahead of `main`" as synonymous with "merge-ready."
- FE merge requests must carry explicit commit SHAs or commit spans.
- Whole-branch squash should be rare and requires explicit PA sign-off that the entire ahead range is approved.
- Branch-promotion backlog should appear in board digests whenever approved work remains off `main` for more than 24 hours.

## Next FE Follow-Through

FE should receive bounded merge tasks from PA rather than vague "merge branch X" requests. The first follow-through task should validate that FE can execute promotion-branch merges from commit packets on long-lived agent branches.

## Sources Consulted

- `Business development/shared-workspace/references/git-coordination.md`
- `SYSTEM_ARCHITECTURE.md`
- [VITA-320](/VITA/issues/VITA-320)
- [VITA-328](/VITA/issues/VITA-328)
- Git branch scan on 2026-04-06:
  - `git rev-list --left-right --count origin/main...origin/agent/bb`
  - `git rev-list --left-right --count origin/main...origin/agent/dp`
  - `git rev-list --left-right --count origin/main...origin/agent/bs`
  - `git rev-list --left-right --count origin/main...origin/agent/oc`
  - `git rev-list --left-right --count origin/main...origin/agent/hr`
  - `git rev-list --left-right --count origin/main...origin/agent/fe`
  - `git rev-list --left-right --count origin/main...origin/agent/pa`
