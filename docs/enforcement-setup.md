# Enforcement setup

Copy devgod policy-as-code into your Next.js + Supabase project.

Full module: [references/enforcement.md](../references/enforcement.md) · Rule catalog: [references/enforcement-rules.md](../references/enforcement-rules.md)

## Quick copy

```bash
# Path to your devgod clone (or resolve from skill symlink)
export DEVGOD="${DEVGOD:-$HOME/.claude/skills/devgod}"
# export DEVGOD="$(dirname "$(readlink "$HOME/.cursor/skills/devgod")")"

mkdir -p scripts supabase/tests .github/workflows .github

cp "$DEVGOD/scripts/devgod-scan.sh" scripts/
cp "$DEVGOD/scripts/check-rls-migration.sh" scripts/
cp "$DEVGOD/templates/github/devgod-gates.yml" .github/workflows/
cp "$DEVGOD/templates/github/pull_request_template.md" .github/
cp "$DEVGOD/templates/supabase/tests/"*.sql supabase/tests/

chmod +x scripts/*.sh
```

## Package scripts

Merge from [templates/package-scripts.snippet.json](../templates/package-scripts.snippet.json):

```json
{
  "scripts": {
    "devgod:scan": "bash scripts/devgod-scan.sh --strict",
    "devgod:scan:design": "bash scripts/devgod-scan.sh --design",
    "devgod:scan:backend": "bash scripts/devgod-scan.sh --backend",
    "lint:ci": "eslint . --max-warnings=0",
    "typecheck": "tsc --noEmit",
    "test:unit": "vitest run",
    "test:e2e": "playwright test",
    "test:a11y": "playwright test --grep @a11y",
    "test:rls": "supabase test db"
  }
}
```

## Scanner usage

```bash
bash scripts/devgod-scan.sh              # design + backend baseline
bash scripts/devgod-scan.sh --strict     # pre-merge gate
bash scripts/devgod-scan.sh --design     # tokens, hardcoded colors
bash scripts/devgod-scan.sh --backend    # auth, secrets, getSession warns
bash scripts/devgod-scan.sh --fix-hints  # suggest fixes in output
```

### What devgod-scan checks

| Area | Examples |
|---|---|
| Secrets | `sk_live_`, service role in client paths |
| Design | Hardcoded Tailwind palette (`text-red-500`, `bg-blue-100`) |
| Backend | `getSession()` without `getUser()` warn; `updateTag` in route handlers |
| Layout | `"use client"` on layout files |

### RLS migration gate

Run on every migration PR:

```bash
bash scripts/check-rls-migration.sh supabase/migrations/*.sql
```

Fails if new `public` tables lack `enable row level security`.

## Maturity levels

Target **L2** for production SaaS. See enforcement module for full detail.

| Level | What you have |
|---|---|
| **L0** | PR checklist, manual review |
| **L1** | + local `devgod-scan`, husky pre-commit |
| **L2** | + CI: typecheck, lint `--max-warnings=0`, devgod-scan `--strict`, unit tests |
| **L3** | + Playwright a11y, pgTAP RLS tests, secret scanning, bundle budget |
| **L4** | + production RUM alerts, Sentry paging, auth anomaly monitoring |

## CI workflow

[devgod-gates.yml](../templates/github/devgod-gates.yml) runs:

1. `npm run typecheck`
2. `npm run lint:ci`
3. `devgod-scan.sh --strict --fix-hints`
4. `check-rls-migration.sh` (when migrations change)
5. `npm run test:unit`
6. Playwright a11y (optional job)

Enable pgTAP in CI after local setup:

```bash
supabase start
supabase db reset
supabase test db
```

Uncomment the `rls` job in `devgod-gates.yml` when ready.

## Pre-commit (husky)

```bash
npm install --save-dev --save-exact husky@9.1.7 lint-staged@17.0.8
npm exec --offline -- husky init
```

`.husky/pre-commit`:

```bash
npm exec --offline -- lint-staged
npm run typecheck
npm run devgod:scan
```

`lint-staged` example:

```json
{
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix --max-warnings=0"]
  }
}
```

## PR template

Copy [pull_request_template.md](../templates/github/pull_request_template.md) to `.github/`.

Ensures human gates alongside automated ones: RLS, auth, loading states, semantic tokens.

## Invoke from agent

```
devgod enforce — set up CI and pre-commit for this Next.js + Supabase repo
```

Routes to `enforcement.md` + copies templates with project-specific paths.
