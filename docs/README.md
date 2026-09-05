# devgod documentation

Human-readable guides for installing, using, and extending devgod.

**Agents** should load `SKILL.md` and `references/` - not this folder - unless a task explicitly involves documentation.

**Current skill version:** 1.90.0

## Guides

| Guide | Description |
|---|---|
| [Getting started](getting-started.md) | Install, first prompts, session workflow |
| [Verbs](verbs.md) | All `devgod` verbs with example prompts |
| [Slash commands](slash-commands.md) | `/devgod-*` commands, pipelines, loops |
| [Enforcement setup](enforcement-setup.md) | Scripts, CI, pre-commit, maturity levels |
| [Architecture](architecture.md) | Skill structure, progressive disclosure, file roles |
| [Module map](modules.md) | All reference modules by domain |

## Reference (agents)

| Path | Audience |
|---|---|
| [SKILL.md](../SKILL.md) | Agent router - verbs, routing, flows, gates |
| [references/MANIFEST.md](../references/MANIFEST.md) | Full module index for agents |
| [references/skill-authoring.md](../references/skill-authoring.md) | Meta: build agent skills |
| [COMPAT.md](../COMPAT.md) | Stack pins and security pins |

## Research & audit

| Path | Description |
|---|---|
| [research/gap-audit.md](../research/gap-audit.md) | Coverage matrix + roadmap |
| [research/report.md](../research/report.md) | Provenance and source notes |
| [research/agent-skills-research.md](../research/agent-skills-research.md) | Agent skill best practices |

## Templates & scripts

| Path | Copy to project |
|---|---|
| [scripts/devgod-scan.sh](../scripts/devgod-scan.sh) | `your-project/scripts/` |
| [scripts/check-rls-migration.sh](../scripts/check-rls-migration.sh) | `your-project/scripts/` |
| [scripts/run-evals.sh](../scripts/run-evals.sh) | Skill-package eval bank |
| [scripts/run-live-evals.py](../scripts/run-live-evals.py) | Live routing smoke via `claude -p` with skills-off baseline (opt-in, costs tokens) |
| [scripts/capture-host-capabilities.py](../scripts/capture-host-capabilities.py) | Secret-safe local coding-agent host inventory |
| [scripts/test-playwright-template.sh](../scripts/test-playwright-template.sh) | Playwright consumer contract |
| [scripts/plan-fleet-status.sh](../scripts/plan-fleet-status.sh) | Read-only active-plan fleet overview across canonical repos (`--json`, `--snapshot`) |
| [templates/github/devgod-gates.yml](../templates/github/devgod-gates.yml) | `.github/workflows/` |
| [templates/github/pull_request_template.md](../templates/github/pull_request_template.md) | `.github/` |
| [templates/playwright/](../templates/playwright/) | Parallel-safe desktop/mobile/auth/quality E2E |
| [templates/lib/](../templates/lib/) | rate-limit, instrumentation, cache-tags |
| [templates/eslint.config.mjs](../templates/eslint.config.mjs) | Next flat ESLint CI |
| [templates/plan.sample.json](../templates/plan.sample.json) | Multi-file plan artifact |
| [templates/supabase/tests/](../templates/supabase/tests/) | `supabase/tests/` |
| [templates/package-scripts.snippet.json](../templates/package-scripts.snippet.json) | merge into `package.json` |
| [scripts/install-commands.sh](../scripts/install-commands.sh) | Install slash commands |
| [commands/](../commands/) | Canonical command definitions |
| [references/workflows.md](../references/workflows.md) | Pipelines + loop recipes |

## Evals

[evals/evals.json](../evals/evals.json) - Prompt scenarios with assertions for skill routing and behavior. CI: `bash scripts/run-evals.sh --smoke`.

[evals/live-smoke.json](../evals/live-smoke.json) - curated live subset for the model-in-the-loop runner. Opt-in only (costs tokens, never in default CI): `bash scripts/run-evals.sh --live --compare --model haiku` proves real activation via the sealed routing probe and reports with-skill vs skills-disabled baseline lift.

Release maintainers: [releasing.md](releasing.md) covers clean installs, host evidence, and publication checks.
