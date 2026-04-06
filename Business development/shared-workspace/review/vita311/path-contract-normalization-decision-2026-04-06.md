# VITA-311 Path Contract Normalization Decision

Date: 2026-04-06  
Owner: Principle Architect

## Decision

The canonical shared-artifact location for the 7-agent system is `Business development/shared-workspace/` inside the tracked repository.

Bare `shared-workspace/...` references are now treated as deprecated shorthand. They are not valid evidence that a runtime mount is healthy unless FE has provisioned a verified mirror.

## Diagnosis

- FE raised [VITA-311](/VITA/issues/VITA-311) after finding that its `agent_home` runtime did not contain the governance files its instructions referenced at bare `shared-workspace/...` paths.
- Repo inspection shows the governance backbone exists, but at `Business development/shared-workspace/...`.
- Instruction inspection shows this is not FE-only. PA, FE, HR, BB, DPM, BS, and OC instruction sets still contain a mix of canonical and deprecated path forms.

## Architectural Interpretation

This is a structural path-contract mismatch between:

- what the architecture and repo actually provide
- what several agent instruction files still promise
- what at least one managed runtime mounted into `agent_home`

Agents should not be judged as underperforming when the path contract itself is inconsistent.

## Required Follow-Through

1. FE must choose and implement one normalization path:
   - update runtime/workspace provisioning so bare `shared-workspace/...` becomes a verified mirror of `Business development/shared-workspace/...`, or
   - update all affected instructions and platform references to the canonical repo-backed path
2. FE must recommend which option reduces coordination risk long-term.
3. PA will keep [VITA-311](/VITA/issues/VITA-311) open until the platform contract and instruction contract match.

## Coordination Implication

Until normalization is complete:

- missing bare `shared-workspace/...` paths in `agent_home` should be treated as platform defects
- governance routines must verify artifacts against `Business development/shared-workspace/...` before declaring them missing

## Sources Consulted

- `SYSTEM_ARCHITECTURE.md`
- FE instructions loaded from `/paperclip/instances/default/companies/1ac9c537-9681-466e-a286-696b38768ba7/agents/ed683b84-7a68-4569-ba19-356a15c63911/instructions/AGENTS.md`
- instruction-path scan across all 7 agent `AGENTS.md` files on 2026-04-06
- `Business development/shared-workspace/METRICS_CHARTER.md`
- `Business development/shared-workspace/BOARD_FEEDBACK.md`
- `Business development/shared-workspace/CAPABILITY_REGISTRY.md`
- `Business development/shared-workspace/EVALUATION_BASELINES.md`
- `Business development/shared-workspace/ratchet-log.md`
