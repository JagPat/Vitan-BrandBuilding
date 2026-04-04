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

git -c user.name="Paperclip" -c user.email="noreply@paperclip.ing" \
  commit -m "${issue_ref}: commit shared-workspace artifacts" \
  -m "Co-Authored-By: Paperclip <noreply@paperclip.ing>"

if git remote get-url origin >/dev/null 2>&1 && [[ "$current_branch" != "HEAD" ]]; then
  git push origin "$current_branch"
fi
