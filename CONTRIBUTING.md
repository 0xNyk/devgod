# Contributing to devgod

Thanks for improving the agent OS. This repo is a **skill package** (markdown modules + shell gates), not an application runtime.

## Principles

1. **Progressive disclosure** - keep `SKILL.md` thin (~200-300 lines). Put depth in `references/`.
2. **Project truth first** - modules advise; they never invent a stack the target repo does not use.
3. **Machine-checkable when possible** - new hard rules should land in `scripts/devgod-scan.sh` or templates, not only prose.
4. **Add modules sparingly** - gap must appear in **3+ real projects** or be **ship-blocking** (see `research/gap-audit.md`).
5. **Own the contribution** - human and AI-assisted changes have the same provenance, license, review, test, and clarity requirements. Do not submit generated material you cannot explain or maintain.

## Setup

```bash
git clone https://github.com/0xNyk/devgod.git
cd devgod
bash scripts/install-all-agents.sh
```

Symlinks point agent skill dirs at this clone so edits are live.

## Layout

| Path | Purpose |
|---|---|
| `SKILL.md` | Router only - load on trigger |
| `references/` | Agent modules (on demand) |
| `commands/` | Portable command instructions used by host alias adapters |
| `docs/` | Human docs (not bulk-loaded by agents) |
| `scripts/` | Scanners and installers |
| `templates/` | CI, pgTAP, package.json snippets |
| `evals/evals.json` | Regression scenarios |
| `research/` | Provenance - load via module footers only |

## Making changes

### New module

1. Add `references/<name>.md` with clear load conditions, rules, anti-patterns, and a short checklist.
2. Register in `references/MANIFEST.md` and `SKILL.md` routing map.
3. Add or extend an eval in `evals/evals.json`.
4. If agents need a verb shortcut, add `commands/devgod-<verb>.md` and document in `docs/slash-commands.md` + `docs/verbs.md`.

### Scanner / CI

1. Extend `scripts/devgod-scan.sh` or `check-rls-migration.sh` with low false-positive checks.
2. Mirror docs in `references/enforcement.md` / `references/enforcement-rules.md` and `docs/enforcement-setup.md`.
3. Keep templates in `templates/` copy-paste ready.

For Action upgrades, follow [dependency update checks](docs/releasing.md#dependency-updates).
Workflow pins, consumer templates, and pin regression checks must change together.

### Docs

- Human install/verbs → `docs/`
- Agent-facing rules → `references/`
- Brand assets → `assets/BRAND.md`

## Validation

```bash
bash scripts/devgod-health.sh --profile skill
```

Checks include repository structure, executable fixtures, eval integrity, supply-chain rules, and package contracts. Run the focused test for changed modules before the full profile.

Edits to `SKILL.md`, `references/`, `scripts/`, `templates/`, `commands/`, or `evals/` change the runtime package digest. Before claiming green, run:

```bash
python3 scripts/rebind-skill-eval.py --check
# if it reports drift:
python3 scripts/rebind-skill-eval.py
```

`validate-repo.sh` and `devgod-health.sh` fail closed on unbound skill-eval samples.

## Pull requests

- Prefer small, reviewable PRs (one module or one concern).
- Add a versioned `CHANGELOG.md` entry for the release (append-only; do not rewrite old entries).
- Do not commit secrets, personal absolute paths, or large binary dumps.
- Keep research corpora out of agent hot paths.

### Anti-slop output gate

Run `bash scripts/devgod-output-gate.sh <file>` on every human-facing doc you touch; changed
files must not regress their HEAD score and new modules must pass outright. Documented
exemption: `CHANGELOG.md` is append-only and released entries are immutable history, so the
gate applies to the **new entry text only** (scan the entry in isolation before committing).
The whole-file scan carries a standing baseline from pre-gate entries (score 56, em/en dash
critical as of 1.76.0); do not rewrite old entries to clear it, and do not add to it.

## Scope boundaries

Out of scope unless gap-audit promotes them: mobile/Expo, pgvector product features, brand-new stacks outside TypeScript, Python, and Rust web products.

## License

By contributing, you agree your contributions are licensed under the MIT License (see `LICENSE`).
