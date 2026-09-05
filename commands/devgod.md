---
description: Build a fullstack feature with devgod — plan, code, and verify on Next.js + Supabase stack.
---

# /devgod

Default **build** mode. Load the installed devgod `SKILL.md` through the active host.

The user's task follows this invocation.

## Execute

1. **Detect** — read `references/project-detect.md` before generating code.
2. **Route** — SKILL.md routing map → load 1 router + 2–4 leaf modules (not all references).
3. **Build** — implement with operating principles and hard gates active.
4. **Verify** before done:
   ```bash
   npm run typecheck
   npm run lint:ci 2>/dev/null || npm run lint
   bash scripts/devgod-scan.sh --strict 2>/dev/null || true
   ```

## Do not

- Bulk-load `research/` or all of `references/`
- Commit/push unless user explicitly asked
- Skip auth on mutations or RLS on new tables

## Related

- Plan first: `/devgod-plan`
- Audit only: `/devgod-audit`
- Pipelines: `references/workflows.md`
