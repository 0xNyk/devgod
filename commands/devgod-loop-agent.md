---
description: Outer agent loop recipe - plan, act, verify, stop budgets (loop engineering).
---

# /devgod-loop-agent

**Loop command** - load devgod `SKILL.md`, `references/workflows.md` (outer-loop contract), and optionally the active host’s **`loop`** capability when available.

## Purpose

Run a single coding task under an explicit **outer loop**: sense -> plan -> act -> observe -> critique -> stop. Use when the agent would otherwise thrash without budgets or claim done without evidence.

## When invoked

```
/devgod-loop-agent <task>
# or with host loop:
/loop dynamic /devgod-loop-agent <task>
```

## Contract (binding)

| Phase | Action |
|---|---|
| 1. Sense | Goal, scope, stack via project-detect |
| 2. Plan | Multi-file: `.devgod/plan.json` from `templates/plan.sample.json`; validate |
| 3. Act | Minimal diff; 2-4 reference modules max |
| 4. Observe | Tool output, tests, scan |
| 5. Critique | Fix from evidence |
| 6. Stop | Success, hard fail, or escalate |

### Budgets (defaults)

| Budget | Default |
|---|---|
| Outer turns | 15 |
| Verify-fix rounds | 5 without progress -> stop |
| Token/$ | host policy; escalate rather than burn |

### Maker != checker

1. **Maker** implements.
2. **Checker** re-runs verify (prefer `/devgod-loop-verify` bundle).
3. Done only after checker green.

### Risk gates

Follow `workflows.md` risk table. always-ask for prod deploy, migrations, secrets, unaudited MCP/skills.

## Each iteration (when under /loop)

1. State current phase and remaining budget.
2. Act within plan `files_touch`.
3. Run verify:
   ```bash
   npm run typecheck 2>/dev/null || true
   bash scripts/devgod-scan.sh --strict 2>/dev/null || true
   ```
4. If green and acceptance met -> **stop success** with evidence.
5. If same failure as prior turn -> count no-progress; at 5 -> **stop fail**.
6. If always-ask risk appears -> **pause** for human.

## Stop conditions

- Acceptance + verify green
- User abort
- Max turns or no-progress budget hit
- Security / secrets issue (escalate, do not auto-bypass)

## Compose

| Need | Next |
|---|---|
| Pure verify cycle | `/devgod-loop-verify` |
| CI after push | `/devgod-loop-ci` |
| Ship readiness | `/devgod-loop-ship` |
| Provider switch mid-task | portage (composition.md) |
| AI feature | `ai-boundary.md` + `ai-security.md` |

## Do not

- Loop without a stop condition
- Expand scope to "while we are here"
- Mark done without re-running checker after the last edit
