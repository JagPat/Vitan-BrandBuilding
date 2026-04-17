#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_SCRIPT="$SCRIPT_DIR/zoho-mail-workflow.py"

if [[ ! -f "$SOURCE_SCRIPT" ]]; then
  echo "ERROR: source script missing: $SOURCE_SCRIPT" >&2
  exit 1
fi

# Durable install target: every temp skill bundle links .claude/skills/paperclip -> /app/skills/paperclip
install -d /app/skills/paperclip/tools
install -m 0755 "$SOURCE_SCRIPT" /app/skills/paperclip/tools/zoho-mail-workflow.py

# Compatibility install target for existing capabilities that call /tmp/paperclip-skills-*/tools/...
for bundle in /tmp/paperclip-skills-*; do
  [[ -d "$bundle" ]] || continue
  install -d "$bundle/tools"
  install -m 0755 "$SOURCE_SCRIPT" "$bundle/tools/zoho-mail-workflow.py"
done

echo "deployed: /app/skills/paperclip/tools/zoho-mail-workflow.py"
echo "deployed: /tmp/paperclip-skills-*/tools/zoho-mail-workflow.py (for currently existing bundles)"
