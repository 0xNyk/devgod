---
description: Audit then repair — minimal diff fixes for devgod violations in the target scope.
---

# /devgod-fix

Load devgod `SKILL.md` + `references/root-cause-engineering.md`. Mode: **diagnose → audit → fix in atomic steps**.

Target and symptom follow this invocation.

## Execute

1. **Diagnose** — reproduce, state the violated invariant, trace the causal chain to the
   first divergence (`references/root-cause-engineering.md` + system-assurance debug loop).
2. **Mini-audit** — list Critical/Warning for scope only (brief).
3. **Fix** — one issue at a time, minimal diff **at the causal site**, match repo conventions.
4. **Verify** after each batch:
   ```bash
   npm run typecheck
   bash scripts/devgod-scan.sh --strict 2>/dev/null || true
   ```
5. **Report** — what changed, what remains; say "root-cause fixed" or "mitigated" explicitly.

## Rules

- Root cause is a diagnosis obligation, not just a scope limiter — no patch before the first causal divergence is identified
- No silent symptom patches (retry masking a race, null guard hiding a broken invariant, widened timeout hiding an N+1); mitigations ship only declared, with owner + expiry + tracked follow-up
- No drive-by refactors; structural causes route through `references/refactoring.md` first as a separate step
- Do NOT touch files outside stated scope
- Auth bugs → `backend-auth.md`; colors → `design-system.md`; RLS → `backend-database.md`

## Loop

For repeated verify until green: `/devgod-loop-verify` (uses `/loop` skill)
