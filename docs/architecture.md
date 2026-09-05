# Skill architecture

How devgod is structured and why - aligned with Anthropic, Cursor, and agentskills.io best practices.

Research: [research/agent-skills-research.md](../research/agent-skills-research.md)  
Meta module: [references/skill-authoring.md](../references/skill-authoring.md)

## Three-level loading

```
Level 1  YAML description     Always in system prompt (~100 tokens)
         ↓ agent matches user intent
Level 2  SKILL.md body        Loaded on trigger (~200 lines)
         ↓ agent routes to modules
Level 3  references/, scripts/   On demand only
```

**Token rule**: never duplicate Level 3 content in Level 2. The old duplicate module index in `SKILL.md` was removed in v1.2 for this reason.

## File roles

| Path | Role | Loaded by |
|---|---|---|
| `SKILL.md` | Router: principles, verbs, routing map, flows, gates | Agent on trigger |
| `references/*.md` | Domain rules, patterns, checklists | Agent per task |
| `references/MANIFEST.md` | Full module index | Agent when exploring |
| `docs/` | Human guides (this folder) | Humans, not default agent load |
| `research/*.md` | Provenance corpora | Agent via module footers only |
| `scripts/` | Executable policy scanners | Shell, not pasted into chat |
| `templates/` | CI, pgTAP, package.json starters | Copy to projects |
| `evals/evals.json` | Regression prompts + assertions | Skill QA |

## Router pattern

Large domains use a **router module** that points to leaf modules:

```
frontend.md          → frontend-performance.md, frontend-state.md, …
backend-supabase.md  → backend-auth.md, backend-database.md, …
```

Agents load **one router + 2-4 leaf modules** per task - not the full tree.

## Progressive disclosure rules

1. **Description = router** - third person, WHAT + WHEN + trigger verbs
2. **SKILL.md < 500 lines** - workflows and routing only
3. **One-level-deep links** - `references/foo.md`, not nested paths
4. **Research via footers** - `Full research: research/backend-research.md` in modules
5. **Scripts over paste** - run `devgod-scan.sh`; don't dump 222 lines into context
6. **MANIFEST on demand** - not at session start

## Session flow

```
User: "devgod - build avatar upload"
  │
  ├─ L1 description matches "devgod" + "Supabase"
  ├─ L2 SKILL.md loads → routes to backend-storage, backend-api
  ├─ project-detect.md (session start rule)
  └─ L3 leaf modules loaded → build with RLS, getUser(), Zod
```

## Human vs agent docs

| Audience | Read |
|---|---|
| **You** (install, CI, verbs) | `README.md`, `docs/` |
| **Agent** (build rules) | `SKILL.md`, `references/` |
| **Maintainer** (coverage, provenance) | `research/gap-audit.md`, `research/report.md` |

Don't put human onboarding prose in `SKILL.md` - agents pay token cost every trigger.

## Extending devgod

1. Identify gap in [gap-audit.md](../research/gap-audit.md)
2. Add `references/new-module.md` with `Last verified` date
3. Add routing row to `SKILL.md`
4. Add entry to `MANIFEST.md` and [modules.md](modules.md)
5. Add eval in `evals/evals.json`
6. Update gap-audit when filled

Add a module when a gap hits **3+ real projects** or is **ship-blocking**.

## v1.2 optimizations

| Change | Why |
|---|---|
| Removed duplicate index from SKILL.md | ~1.5k token savings per load |
| Added `docs/` | Human docs separated from agent context |
| Added disambiguation table | "design schema" → backend not design-system |
| Audit output template | Consistent `devgod audit` reports |
| 70 evals | Regression coverage for routing and safety contracts |

## Compliance checklist

- [x] SKILL.md under 500 lines (200)
- [x] Third-person description with trigger terms
- [x] Progressive disclosure (references/)
- [x] One-level-deep file references
- [x] Executable enforcement scripts
- [x] Eval suite with assertions
