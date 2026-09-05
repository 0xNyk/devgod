#!/usr/bin/env bash
# Lightweight health score for a target app or the devgod skill package.
# Inspired by gstack health — wraps existing tools, no daemon.
#
# Usage:
#   bash /path/to/devgod/scripts/devgod-health.sh [--profile auto|app|skill] [--json]
set -euo pipefail

JSON=0
PROFILE=auto
while [[ $# -gt 0 ]]; do
  case "$1" in
    --json) JSON=1 ;;
    --profile=*) PROFILE="${1#*=}" ;;
    --profile)
      [[ $# -ge 2 ]] || { echo "--profile requires a value" >&2; exit 2; }
      PROFILE="$2"
      shift
      ;;
    -h|--help)
      echo "Usage: devgod-health.sh [--profile auto|app|skill] [--json]"
      exit 0
      ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

if [[ "$PROFILE" != "auto" && "$PROFILE" != "app" && "$PROFILE" != "skill" ]]; then
  echo "Unknown profile: $PROFILE (expected auto, app, or skill)" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
if [[ "$PROFILE" == "auto" ]]; then
  if [[ -f SKILL.md && -d references && -d commands && -f scripts/validate-repo.sh ]]; then
    PROFILE=skill
  else
    PROFILE=app
  fi
fi

SCORE=0
MAX=0
RESULTS=()

check() {
  local name="$1"
  local weight="$2"
  shift 2
  MAX=$((MAX + weight))
  if "$@" >/dev/null 2>&1; then
    SCORE=$((SCORE + weight))
    RESULTS+=("pass|$name|$weight")
    [[ "$JSON" -eq 0 ]] && echo "  ✓ $name (+$weight)"
  else
    RESULTS+=("fail|$name|$weight")
    [[ "$JSON" -eq 0 ]] && echo "  ✗ $name (0/$weight)"
  fi
  return 0
}

[[ "$JSON" -eq 0 ]] && echo "devgod health — $(pwd) [$PROFILE]" && echo "---"

if [[ "$PROFILE" == "skill" ]]; then
  check "repository integrity" 1 bash "$SCRIPT_DIR/validate-repo.sh"
  check "repository negative fixtures" 1 bash "$SCRIPT_DIR/test-repo-validation.sh"
  check "plan proportionality fixtures" 2 bash "$SCRIPT_DIR/test-plan-complexity.sh"
  check "plan fleet fixtures" 2 bash "$SCRIPT_DIR/test-plan-fleet.sh"
  check "Playwright consumer fixture" 2 bash "$SCRIPT_DIR/test-playwright-template.sh"
  check "scanner fixtures" 2 bash "$SCRIPT_DIR/test-scan.sh"
  check "research fixtures" 2 bash "$SCRIPT_DIR/test-research.sh"
  check "measurement contract fixtures" 2 bash "$SCRIPT_DIR/test-product-metrics.sh"
  check "agentic contract fixtures" 2 bash "$SCRIPT_DIR/test-agentic-contract.sh"
  check "agentic completion fixtures" 2 bash "$SCRIPT_DIR/test-agentic-completion.sh"
  check "optimization run fixtures" 2 bash "$SCRIPT_DIR/test-optimization-run.sh"
  check "security eval fixtures" 2 bash "$SCRIPT_DIR/test-security-eval-catalog.sh"
  check "github signing fixtures" 2 bash "$SCRIPT_DIR/test-github-signing.sh"
  check "csp reporting fixtures" 2 bash "$SCRIPT_DIR/test-csp-reporting.sh"
  check "oss maintainer fixtures" 2 bash "$SCRIPT_DIR/test-oss-maintainer.sh"
  check "oss leak gate fixtures" 2 bash "$SCRIPT_DIR/test-oss-leaks.sh"
  check "GitHub Actions runtime pins" 2 bash "$SCRIPT_DIR/test-action-runtime-pins.sh"
  check "eval bank negative fixtures" 1 bash "$SCRIPT_DIR/test-eval-bank.sh"
  check "live eval runner fixtures" 1 bash "$SCRIPT_DIR/test-live-evals.sh"
  check "behavioral skill eval fixtures" 2 bash "$SCRIPT_DIR/test-skill-eval-run.sh"
  check "skill-eval hash-chain rebind fixtures" 2 bash "$SCRIPT_DIR/test-rebind-skill-eval.sh"
  check "false-done scan fixtures" 2 bash "$SCRIPT_DIR/test-scan-false-done.sh"
  check "host activation fixtures" 2 bash "$SCRIPT_DIR/test-host-activation.sh"
  check "cross-host eval capture fixtures" 2 bash "$SCRIPT_DIR/test-skill-eval-capture.sh"
  check "cross-host capture manifest fixtures" 2 bash "$SCRIPT_DIR/test-skill-eval-capture-manifest.sh"
  check "deterministic skill eval grading fixtures" 2 bash "$SCRIPT_DIR/test-skill-eval-grading.sh"
  check "devgod telemetry fixtures" 2 bash "$SCRIPT_DIR/test-devgod-telemetry.sh"
  check "capability promotion fixtures" 2 bash "$SCRIPT_DIR/test-capability-promotion.sh"
  check "devgod doctor fixtures" 2 bash "$SCRIPT_DIR/test-devgod-doctor.sh"
  check "host capability fixtures" 2 bash "$SCRIPT_DIR/test-host-capabilities.sh"
  check "documentation supply-chain fixtures" 2 bash "$SCRIPT_DIR/test-doc-supply-chain.sh"
  check "skill admission fixtures" 2 bash "$SCRIPT_DIR/test-skill-admission.sh"
  check "agent incident fixtures" 2 bash "$SCRIPT_DIR/test-agent-incident.sh"
  check "orchestration contract fixtures" 2 bash "$SCRIPT_DIR/test-orchestration-contract.sh"
  check "orchestration run fixtures" 2 bash "$SCRIPT_DIR/test-orchestration-run.sh"
  check "browser session fixtures" 2 bash "$SCRIPT_DIR/test-browser-session.sh"
  check "browser lane run fixtures" 2 bash "$SCRIPT_DIR/test-browser-lane-run.sh"
  check "browser lane execution fixtures" 2 bash "$SCRIPT_DIR/test-browser-lane-execution.sh"
  check "agent memory fixtures" 2 bash "$SCRIPT_DIR/test-agent-memory.sh"
  check "coordination envelope fixtures" 2 bash "$SCRIPT_DIR/test-coordination-envelope.sh"
  check "MCP session fixtures" 2 bash "$SCRIPT_DIR/test-mcp-session.sh"
  check "MCP content fixtures" 2 bash "$SCRIPT_DIR/test-mcp-content.sh"
  check "evidence input boundary fixtures" 2 bash "$SCRIPT_DIR/test-evidence-input-boundary.sh"
  check "evidence output boundary fixtures" 2 bash "$SCRIPT_DIR/test-evidence-output-boundary.sh"
  check "MCP transcript fixtures" 2 bash "$SCRIPT_DIR/test-mcp-transcript.sh"
  check "unmachined output gate fixtures" 1 bash "$SCRIPT_DIR/test-output-gate.sh"
  check "eval bank" 2 bash "$SCRIPT_DIR/run-evals.sh" --full
fi

# Typecheck
if [[ "$PROFILE" == "app" && -f tsconfig.json ]]; then
  if command -v pnpm >/dev/null 2>&1 && [[ -f pnpm-lock.yaml ]]; then
    check "tsc (pnpm)" 3 pnpm exec tsc --noEmit
  elif command -v npx >/dev/null 2>&1; then
    check "tsc" 3 npx tsc --noEmit
  fi
fi

# Lint
if [[ "$PROFILE" == "app" ]] && { [[ -f eslint.config.mjs ]] || [[ -f eslint.config.js ]] || [[ -f .eslintrc.json ]]; }; then
  if command -v pnpm >/dev/null 2>&1 && [[ -f pnpm-lock.yaml ]]; then
    check "eslint (pnpm)" 2 pnpm exec eslint . --max-warnings=50
  fi
fi

# Unit tests
if [[ "$PROFILE" == "app" && -f package.json ]] && grep -q '"test"' package.json 2>/dev/null; then
  if command -v pnpm >/dev/null 2>&1; then
    check "pnpm test" 2 pnpm test -- --passWithNoTests 2>/dev/null || check "pnpm test" 2 pnpm test
  fi
fi

# Python
if [[ "$PROFILE" == "app" ]] && { [[ -f pyproject.toml ]] || [[ -f uv.lock ]]; }; then
  if command -v ruff >/dev/null 2>&1; then
    check "ruff" 2 ruff check .
  fi
  if [[ -f uv.lock ]] && command -v uv >/dev/null 2>&1; then
    check "uv.lock present" 1 test -f uv.lock
  fi
fi

# Rust
if [[ "$PROFILE" == "app" && -f Cargo.toml ]]; then
  check "cargo test" 3 cargo test --quiet
  check "cargo build" 1 cargo build --quiet
fi

# devgod scan if script reachable
if [[ "$PROFILE" == "app" && -f "$SCRIPT_DIR/devgod-scan.sh" ]]; then
  check "devgod-scan --backend" 2 bash "$SCRIPT_DIR/devgod-scan.sh" --backend --quiet
fi

# Lockfiles / hygiene
[[ "$PROFILE" == "app" && -f package.json && ! -f pnpm-lock.yaml && ! -f package-lock.json && ! -f yarn.lock ]] && \
  { RESULTS+=("fail|js lockfile|1"); MAX=$((MAX+1)); [[ "$JSON" -eq 0 ]] && echo "  ✗ js lockfile"; } || true

if [[ "$MAX" -eq 0 ]]; then
  [[ "$JSON" -eq 0 ]] && echo "No recognizable project tools found"
  [[ "$JSON" -eq 1 ]] && echo '{"ok":false,"score":0,"max":0,"note":"no tools"}'
  exit 1
fi

# 0–10 scale
TEN=$(python3 -c "print(round(10.0 * $SCORE / $MAX, 1))")

if [[ "$JSON" -eq 1 ]]; then
  python3 -c "
import json
results = '''$(printf '%s\n' "${RESULTS[@]}")'''.strip().splitlines()
items = []
for r in results:
    if not r: continue
    st, name, w = r.split('|', 2)
    items.append({'status': st, 'name': name, 'weight': int(w)})
print(json.dumps({'ok': $SCORE == $MAX, 'score_0_10': $TEN, 'raw': $SCORE, 'max': $MAX, 'checks': items}, indent=2))
"
else
  echo "---"
  echo "score ${TEN}/10  (raw ${SCORE}/${MAX})"
fi

# soft exit: always 0 unless catastrophic — health is advisory
exit 0
