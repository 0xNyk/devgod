#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/.claude" "$TMP/.grok" "$TMP/.hermes/memories"
printf '%s\n' '# existing Claude rule' > "$TMP/.claude/CLAUDE.md"
printf '%s\n' '# existing Grok rule' > "$TMP/.grok/AGENTS.md"
printf '%s\n' '# existing Hermes memory' > "$TMP/.hermes/memories/MEMORY.md"

python3 "$ROOT/scripts/install-host-activation.py" --home "$TMP" --hosts all >/dev/null
python3 "$ROOT/scripts/install-host-activation.py" --home "$TMP" --hosts all >/dev/null
python3 "$ROOT/scripts/install-host-activation.py" --home "$TMP" --hosts all --check >/dev/null

[[ "$(grep -c '<!-- devgod-auto:begin -->' "$TMP/.claude/CLAUDE.md")" -eq 1 ]]
grep -q '# existing Claude rule' "$TMP/.claude/CLAUDE.md"
grep -q '# existing Grok rule' "$TMP/.grok/AGENTS.md"
grep -q '^alwaysApply: true$' "$TMP/.cursor/rules/devgod-auto.mdc"

python3 "$ROOT/scripts/install-host-activation.py" --home "$TMP" --hosts all --remove >/dev/null
grep -q '# existing Claude rule' "$TMP/.claude/CLAUDE.md"
! grep -q 'devgod-auto:begin' "$TMP/.claude/CLAUDE.md"
[[ ! -e "$TMP/.cursor/rules/devgod-auto.mdc" ]]

echo "OK host activation install/check/remove is idempotent and preserves existing content"
