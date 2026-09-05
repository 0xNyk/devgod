#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

check_action() {
  local action="$1" expected="$2" bad
  if command -v rg >/dev/null 2>&1; then
    bad="$(rg -n "uses: ${action}@" .github/workflows templates/github | grep -Fv "$expected" || true)"
  else
    bad="$(grep -R -n --include='*.yml' --include='*.yaml' "uses: ${action}@" .github/workflows templates/github | grep -Fv "$expected" || true)"
  fi
  if [[ -n "$bad" ]]; then
    echo "stale or mutable ${action} reference:" >&2
    echo "$bad" >&2
    exit 1
  fi
}

check_action actions/checkout 'actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0'
check_action actions/setup-python 'actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1 # v6.3.0'
check_action actions/setup-node 'actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7.0.0'

if grep -R -n --include='*.yml' --include='*.yaml' -E 'node-version:[[:space:]]*20([[:space:]]|$)' .github/workflows templates/github; then
  echo "Node 20 app runtime remains in an executable workflow/template" >&2
  exit 1
fi

grep -Fq 'package-manager-cache: false' .github/workflows/validate.yml
grep -Fq 'runner 2.327.1' research/github-actions-node24-2026-07.md
grep -Fq 'Node 24 LTS' research/github-actions-node24-2026-07.md
echo "GitHub Actions runtime pins: ok"
