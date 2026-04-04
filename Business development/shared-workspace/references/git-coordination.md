# Git Coordination Protocol — Vitan Growth OS

## Problem
Multiple AI agents (BB, FE, PA, HR) operate on the same repository simultaneously.
Direct pushes to `main` from different agents cause race conditions where one agent's
commit overwrites another's work.

## Solution: Per-Agent Branch Isolation

### Architecture
```
main (protected)
  ├── agent/bb   ← Business Builder works here
  ├── agent/fe   ← Founding Engineer works here
  ├── agent/pa   ← Product Architect works here
  └── agent/hr   ← HR works here
```

### Rules

1. **NEVER push directly to `main`.**
   - `main` is branch-protected. Direct pushes will be rejected.
   - All changes reach `main` only through Pull Requests.

2. **Each agent works ONLY on its own branch.**
   - BB → `agent/bb`
   - FE → `agent/fe`
   - PA → `agent/pa`
   - HR → `agent/hr`

3. **Workflow for every task:**
   ```
   git fetch origin
   git checkout agent/<your-agent>
   git pull origin agent/<your-agent>
   # ... do work, commit ...
   git push origin agent/<your-agent>
   # Then create a PR: agent/<your-agent> → main
   ```

4. **Pull Request merge process:**
   - Agent creates PR from its branch to `main`
   - If merge conflicts exist, the agent must rebase its branch on `main` first
   - PRs use squash merge to keep `main` history clean

5. **Sync with main regularly:**
   ```
   git fetch origin main
   git rebase origin/main
   ```

6. **Conflict resolution:**
   - If two agents need to modify the same file, the second agent must rebase after the first agent's PR is merged
   - Never force-push to `main`
   - Agents should check `git log origin/main` before starting work to see recent changes

### File Ownership (Advisory)
To minimize conflicts, each agent should primarily work in designated areas:

| Agent | Primary directories |
|-------|-------------------|
| BB    | `shared-workspace/review/`, `shared-workspace/change-notes/`, `shared-workspace/contacts-master.csv` |
| FE    | `scripts/`, `SHORTLISTED TREES & LANDSCAPE/`, `Business development/PHOTOS FOR SAMPLE PROJECT/` |
| PA    | `shared-workspace/references/`, `shared-workspace/intelligence/` |
| HR    | `shared-workspace/approved/`, `Business development/Brand Guide/` |

### Emergency: Resolving Conflicts
If an agent's push to its own branch fails:
1. `git fetch origin`
2. `git rebase origin/agent/<your-agent>`
3. Resolve any conflicts
4. `git push origin agent/<your-agent>`

If a PR to main has conflicts:
1. `git fetch origin main`
2. `git rebase origin/main`
3. Resolve conflicts
4. `git push origin agent/<your-agent> --force-with-lease`
5. PR will auto-update

## Enforcement
- Branch protection on `main`: PRs required, linear history, no force push
- Each agent's capability instructions include these rules
- Violations will cause push rejections (not silent overwrites)
