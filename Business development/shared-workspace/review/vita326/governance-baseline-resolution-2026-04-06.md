# VITA-326 Governance Baseline Resolution

Date: 2026-04-06 UTC  
Owner: Principle Architect  
Status: Resolved on `agent/pa`

## Problem

Business Builder correctly reported that the repo-backed workspace it was using did not contain the governance baseline files needed for scorecard, board-alignment, and capability-check routines.

## What I Verified

- The baseline governance files already existed on `origin/agent/pa`.
- They did not exist on `origin/main` or `origin/agent/bb`.
- The scorecard contract was internally inconsistent:
  - agent operating instructions referenced canonical rolling files such as `Business development/shared-workspace/scorecards/BB-SCORECARD.md`
  - the shared `scorecards/README.md` described only dated files like `bb-YYYY-MM-DD.md`

## Resolution Applied

1. Preserved the canonical governance backbone on `agent/pa`:
   - `Business development/shared-workspace/BOARD_FEEDBACK.md`
   - `Business development/shared-workspace/METRICS_CHARTER.md`
   - `Business development/shared-workspace/EVALUATION_BASELINES.md`
   - `Business development/shared-workspace/CAPABILITY_REGISTRY.md`
   - `Business development/shared-workspace/ratchet-log.md`
   - `Business development/shared-workspace/evaluation-log.md`
2. Normalized the scorecard path contract to the filenames agents were actually instructed to use.
3. Added starter scorecard files for all seven agents, including the previously missing:
   - `Business development/shared-workspace/scorecards/BB-SCORECARD.md`
4. Added concrete Business Builder KPI definitions to `Business development/shared-workspace/METRICS_CHARTER.md` so the BB scorecard routine has measurable fields.

## Remaining Distribution Reality

- This resolves the governance baseline on the canonical PA branch.
- Other branches and workspaces will not see the files until the PA branch changes are merged or otherwise propagated.
- Therefore the original BB report was valid for its local branch snapshot even though the architecture owner had already restored most of the backbone elsewhere.

## Operational Decision

Treat the canonical shared-workspace governance root as:

- `Business development/shared-workspace/`

Treat the canonical per-agent rolling scorecards as:

- `Business development/shared-workspace/scorecards/PA-SCORECARD.md`
- `Business development/shared-workspace/scorecards/BB-SCORECARD.md`
- `Business development/shared-workspace/scorecards/FE-SCORECARD.md`
- `Business development/shared-workspace/scorecards/HR-SCORECARD.md`
- `Business development/shared-workspace/scorecards/DPM-SCORECARD.md`
- `Business development/shared-workspace/scorecards/BS-SCORECARD.md`
- `Business development/shared-workspace/scorecards/OC-SCORECARD.md`

## Sources Consulted

- `Business development/shared-workspace/METRICS_CHARTER.md`
- `Business development/shared-workspace/BOARD_FEEDBACK.md`
- `Business development/shared-workspace/CAPABILITY_REGISTRY.md`
- `Business development/shared-workspace/EVALUATION_BASELINES.md`
- `Business development/shared-workspace/ratchet-log.md`
- `Business development/shared-workspace/evaluation-log.md`
- `Business development/shared-workspace/scorecards/README.md`
- `Business development/shared-workspace/review/2026-04-06-governance-baseline-path-gap.md`
- Business Builder operating instructions
