# VITA-333 Workflow Token Provisioning Brief

Owner: Principle Architect (PA)  
Status: Blocked pending board credential provisioning  
Date: 2026-04-06

## Executive Summary

Managed runtimes can currently push normal branch updates with `GITHUB_PAT_VITAN`, but they cannot push changes under `.github/workflows/*`.

The blocker is now verified from this PA runtime in two ways:

1. Paperclip company secrets are board-gated from agent context.
2. A disposable workflow-file push probe was rejected by GitHub because the mounted PAT lacks workflow authority.

## Evidence

### 1. Secret provisioning is not agent-self-service

- `GET /api/companies/{companyId}/secrets` returned `403` with `Board access required`
- implication: PA cannot mount a new workflow-capable GitHub token directly from this heartbeat identity

### 2. Live workflow-file push probe failed from this runtime

- probe base: `origin/agent/pa`
- disposable branch: `probe/vita333-workflow-scope-123254`
- disposable file: `.github/workflows/vita333-scope-probe.yml`
- result:

```text
remote rejected ... refusing to allow a Personal Access Token to create or update workflow `.github/workflows/vita333-scope-probe.yml` without `workflow` scope
```

## Architectural Ruling

This is a real platform gap, not a local FE implementation mistake.

- Existing managed-runtime GitHub credentials are sufficient for normal branch pushes.
- They are insufficient for repo automation files under `.github/workflows/`.
- Agents cannot close that gap autonomously because secret provisioning is board-gated.

## Required Next Action

### Board

Provision `GITHUB_WORKFLOW_PAT_VITAN` into the managed runtime secret store with authority to update workflow files for `JagPat/Vitan-BrandBuilding`.

Minimum practical requirement:

- normal repo push authority for the repository
- workflow-file update authority for `.github/workflows/*`

### Founding Engineer

After the board mounts the secret:

1. expose `GITHUB_WORKFLOW_PAT_VITAN` to the runtime(s) that perform automation pushes
2. rerun the workflow-file push validation path for [VITA-332](/VITA/issues/VITA-332)
3. confirm the durable helper and audit artifact are pushed on the FE lane before closing the issue

### Principle Architect

After FE confirms the credential path works:

1. reopen the workflow-backed scheduling lane for [VITA-331](/VITA/issues/VITA-331)
2. move the board email review loop from degraded-ready to scheduled execution

## Validation Checklist After Provisioning

- the runtime environment contains `GITHUB_WORKFLOW_PAT_VITAN`
- a disposable workflow-file branch push succeeds
- FE confirms the approved helper-based push path in [VITA-332](/VITA/issues/VITA-332)
- PA can promote `.github/workflows/board-communication.yml` without hitting the same rejection

## Sources Consulted

- `Business development/shared-workspace/references/git-coordination.md`
- `Business development/shared-workspace/CAPABILITY_REGISTRY.md`
- `Business development/shared-workspace/review/vita331/board-email-review-workflow-2026-04-06.md`
- [VITA-331](/VITA/issues/VITA-331)
- [VITA-332](/VITA/issues/VITA-332)
- [VITA-333](/VITA/issues/VITA-333)
- Paperclip API response: `GET /api/companies/{companyId}/secrets` -> `403 Board access required`
- Live git probe from 2026-04-06 UTC against `JagPat/Vitan-BrandBuilding`
