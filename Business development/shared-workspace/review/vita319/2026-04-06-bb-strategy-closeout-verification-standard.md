# BB Strategy Closeout Verification Standard

## Purpose

Prevent BB strategy work from being marked complete before the relay artifacts that unblock downstream execution are actually visible in tracked git.

This standard applies to:

- strategy refreshes
- strategy restorations
- any BB issue that claims DPM or another downstream agent can now proceed from fresh strategy

## Required Verification Before Closeout

Before moving a relay-critical BB issue to `in_review` or `done`, verify and explicitly reference:

1. the canonical strategy artifact that was expected to land
2. the dated strategy brief in `Business development/shared-workspace/drafts/` when the issue is meant to unblock downstream planning
3. the downstream issue, workflow, or agent the handoff is intended to unblock
4. the exact git commit SHA containing the artifact
5. whether the artifact is only local, present in tracked git, or confirmed on the remote branch

## Minimum Evidence Standard

Use this evidence chain before closeout:

```bash
git ls-files -- "Business development/shared-workspace/drafts/strategy-brief-*.md"
git ls-files -- "SOCIAL_STRATEGY.md"
git log --oneline -1
```

If the issue requires remote confirmation because another agent or board reviewer must consume the artifact, also verify the file exists on `origin/agent/bb` before claiming the relay is complete.

## Closeout Comment Template

Use a closeout block in this format:

```md
## Relay Verification

- Strategy artifact: `[path]` verified in git
- Strategy brief: `[path]` verified in git
- Downstream unblock target: `[issue](/VITA/issues/VITA-XXX)` or named agent/workflow
- Commit: `<sha>`
- Remote status: pushed to `agent/bb` / not yet pushed
- Caveat: none / local-only artifact still needs push / review-only issue, no `SOCIAL_STRATEGY.md` update intended
```

## Failure Conditions

Do not imply relay completion when any of the following is true:

- the artifact exists locally but is not tracked
- the issue references a dated brief that does not exist
- `SOCIAL_STRATEGY.md` is required by the issue outcome but cannot be verified in git
- the branch push failed and downstream consumers cannot access the artifact
- the work is approval-stage only, but the closeout language reads like final delivery

## Language Rules

- If the issue is review-stage only, say that directly.
- If `SOCIAL_STRATEGY.md` was intentionally not changed, say that directly.
- If downstream work is unblocked only after board approval, say that directly.
- If the repo state and local state differ, describe the gap instead of hiding it.

## Why This Fix Exists

The prior relay defect was not just a missing file problem. It was a signaling problem: issue state implied downstream readiness without repo-visible evidence. This standard makes the evidence part of the closeout itself.

## Sources Consulted

- `Business development/shared-workspace/README.md` — canonical shared-workspace structure and artifact naming expectations
- `Business development/shared-workspace/references/git-coordination.md` — branch isolation and push verification expectations
- `Business development/shared-workspace/references/kaizen-protocol.md` — requirement to capture and operationalize learnings
- [VITA-287](/VITA/issues/VITA-287) — prior restoration issue referenced in the defect description
- [VITA-314](/VITA/issues/VITA-314) — immediate relay-break follow-up referenced by the defect description
- [VITA-317](/VITA/issues/VITA-317) — adjacent governance context named in the defect description
- [VITA-319](/VITA/issues/VITA-319) — required improvement and success criteria for this fix
