---
description: Set up devgod-scan, RLS gate, CI workflow, pre-commit, and PR template in this repo.
---

# /devgod-enforce

Load devgod `SKILL.md` + `references/enforcement.md` (rule catalog: `references/enforcement-rules.md`).

## Execute

1. Copy into project (adjust `DEVGOD` path):
   ```bash
   # Set DEVGOD to the directory containing the loaded devgod SKILL.md.
   : "${DEVGOD:?Set DEVGOD to the resolved skill directory}"
   mkdir -p scripts supabase/tests .github/workflows .github
   cp "$DEVGOD/scripts/"*.sh scripts/
   cp "$DEVGOD/templates/github/devgod-gates.yml" .github/workflows/
   cp "$DEVGOD/templates/github/pull_request_template.md" .github/
   cp "$DEVGOD/templates/supabase/tests/"*.sql supabase/tests/ 2>/dev/null || true
   chmod +x scripts/*.sh
   ```
2. Merge `templates/package-scripts.snippet.json` into `package.json`.
3. Recommend husky + lint-staged (see `docs/enforcement-setup.md`).
4. Target maturity **L2** unless user specifies otherwise.

## Verify

```bash
npm run devgod:scan 2>/dev/null || bash scripts/devgod-scan.sh --strict
```

## Report

Current maturity level, gaps, and next tier upgrades.
