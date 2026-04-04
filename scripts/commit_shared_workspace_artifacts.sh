#!/usr/bin/env bash
set -euo pipefail

repo_root="${PAPERCLIP_WORKSPACE_REPO_ROOT:-}"
if [[ -z "$repo_root" ]]; then
  repo_root="$(git rev-parse --show-toplevel)"
fi

cd "$repo_root"

artifact_root="Business development/shared-workspace"
if [[ ! -d "$artifact_root" ]]; then
  exit 0
fi

has_untracked="false"
if [[ -n "$(git ls-files --others --exclude-standard -- "$artifact_root")" ]]; then
  has_untracked="true"
fi

if git diff --quiet -- "$artifact_root" && git diff --cached --quiet -- "$artifact_root" && [[ "$has_untracked" != "true" ]]; then
  exit 0
fi

git add -- "$artifact_root"

if git diff --cached --quiet -- "$artifact_root"; then
  exit 0
fi

issue_ref="${PAPERCLIP_ISSUE_IDENTIFIER:-${PAPERCLIP_ISSUE_ID:-workspace}}"
current_branch="$(git rev-parse --abbrev-ref HEAD)"
push_ref="$current_branch"

push_shared_workspace_artifacts() {
  local remote_name="$1"
  local refspec="$2"

  if [[ -n "${GITHUB_PAT_VITAN:-}" ]]; then
    git -c credential.helper='!f() { echo username=x-access-token; echo "password=$GITHUB_PAT_VITAN"; }; f' \
      push "$remote_name" "$refspec"
    return
  fi

  git push "$remote_name" "$refspec"
}

if [[ "$current_branch" == "HEAD" ]]; then
  origin_head="$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null || true)"
  target_branch="${PAPERCLIP_WORKSPACE_BRANCH:-}"

  if [[ -z "$target_branch" && -n "$origin_head" ]]; then
    target_branch="${origin_head#origin/}"
  fi

  if [[ -z "$target_branch" ]]; then
    target_branch="main"
  fi

  push_ref="HEAD:refs/heads/$target_branch"
fi

git -c user.name="Paperclip" -c user.email="noreply@paperclip.ing" \
  commit -m "${issue_ref}: commit shared-workspace artifacts" \
  -m "Co-Authored-By: Paperclip <noreply@paperclip.ing>"

if git remote get-url origin >/dev/null 2>&1; then
  echo "INFO: pushing shared-workspace artifacts with refspec $push_ref" >&2

  if ! push_shared_workspace_artifacts origin "$push_ref"; then
    echo "ERROR: git push failed for shared-workspace artifacts (refspec: $push_ref)" >&2
    exit 1
  fi
fi
