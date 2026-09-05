---
description: Loop until typecheck, lint, and devgod-scan pass - uses /loop dynamic mode.
---

# /devgod-loop-verify

**Loop command** - load devgod `SKILL.md`, `references/workflows.md`, and the active host’s **`loop`** capability when available.

## Purpose

Repeat fix + verify until clean or stop condition. This is the default **maker → checker** cycle for product code.

## When invoked via /loop

User runs: `/loop dynamic /devgod-loop-verify`

## Roles each iteration

| Role | Action |
|---|---|
| **Maker** | Apply minimal fix to failing scope only |
| **Checker** | Re-run full verify bundle; only checker pass ends the loop |

## Each iteration

1. **Checker** runs verify bundle (adapt to detected stack):
 ```bash
 # Node/Next (common)
 npm run typecheck
 npm run lint:ci 2>/dev/null || npm run lint 2>/dev/null || true
 bash scripts/devgod-scan.sh --strict 2>/dev/null || true
 # Python service (if present)
 # uv run ruff check . && uv run basedpyright && uv run pytest -q
 # Rust (if present)
 # cargo test
 ```
2. **All pass** → evaluate acceptance criteria. When an execution contract exists, capture the
   verification artifact and validate `completion-receipt.json`; only then stop successfully.
3. **Any fail** → **Maker**: parse output, `/devgod-fix` on failing scope only (minimal diff)
4. Re-arm dynamic wake (loop skill) - lean long if no changes possible

## Stop conditions

- User says stop
- 5 iterations with same failure → report blocker, stop (no-progress)
- Critical security issue → stop and escalate (no auto-fix secrets)
- Outer-loop max turns from workflows.md if session is already long

## Do not

- Force push, amend commits, or `--no-verify` unless user explicitly asked
- Claim green without re-running the checker bundle after the last edit
- Treat green commands or `verification_passed: true` as proof that behavioral acceptance passed
- Expand scope beyond the failing files while inside this loop
