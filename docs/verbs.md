# Verbs reference

Text invocations (`devgod plan - …`) and **slash commands** (`/devgod-plan`) are equivalent.
Slash reference: [slash-commands.md](slash-commands.md)

| Text | Slash |
|---|---|
| `devgod <task>` | `/devgod` |
| `devgod plan` | `/devgod-plan` |
| `devgod audit` | `/devgod-audit` |
| `devgod fix` | `/devgod-fix` |
| `devgod refactor` | `/devgod-refactor` |
| `devgod ship` | `/devgod-ship` |
| `devgod enforce` | `/devgod-enforce` |
| `devgod research` | `/devgod-research` |
| `devgod research-deep` | `/devgod-research-deep` |
| `devgod research-report` | `/devgod-research-report` |
| `devgod research-add-items` | `/devgod-research-add-items` |
| `devgod research-add-fields` | `/devgod-research-add-fields` |
| `devgod self-improve` | `/devgod-self-improve` |
| `devgod browser` | `/devgod-browser` |
| `devgod qa` | `/devgod-qa` |
| `devgod assure` | `/devgod-assure` |
| `devgod visual` | `/devgod-visual` |
| `devgod launch` | `/devgod-launch` |
| `devgod business` | `/devgod-business` |
| `devgod kpi` | `/devgod-kpi` |
| `devgod memory` | `/devgod-memory` |
| `devgod mcp-audit` | `/devgod-mcp-audit` |

Combine with a task description after the verb or slash command.

## Build modes

### `devgod <task>` (default)

Plan and build with all operating principles active.

```
devgod - build signup with email/password for Next.js + Supabase
devgod - add filterable project list with URL pagination
devgod - implement GDPR delete account and data export
```

### `devgod plan <task>`

Architecture, file list, migrations, data flow - **no code** until you approve.

```
devgod plan - multi-tenant orgs with role-based project access
devgod plan - Stripe subscription billing with entitlements table
```

Use for: >3 files, schema changes, auth/payment flows, greenfield features.

### `devgod audit <target>`

Score against module rubrics. Report with severity. **No edits.**

```
devgod audit - this dashboard page
devgod audit - full stack including enforcement maturity
devgod audit - coding principles of features/billing/
```

Output format is defined in `SKILL.md` (Critical / Warning / Enforcement gaps).

### `devgod fix <target>`

Audit first, then minimal repair in atomic steps.

```
devgod fix - signup form submits but user not logged in after redirect
devgod fix - hardcoded colors in components/settings/
```

### `devgod refactor <target>`

Structure-only change. Preserve external behavior. Load `references/refactoring.md`.

```
devgod refactor - extract shared Zod schemas from auth actions
devgod refactor - thin this skill SKILL.md; progressive disclosure
devgod refactor - split fat Server Action into use-case + repo
```

Safety loop: green baseline → one structural step → green → commit.

## Domain verbs

| Verb | Routes to | Example |
|---|---|---|
| `devgod schema` | backend-database, backend-auth | `devgod schema - comments with threading and RLS` |
| `devgod page` | conversion-ui, design-system, seo | `devgod page - B2B API product landing` |
| `devgod design` | design-system, design-accessibility, design-patterns | `devgod design - audit this settings UI` |
| `devgod research` | deep-research | `devgod research - background job systems for Next SaaS` |
| `devgod research-deep` | deep-research | After outline confirmed |
| `devgod research-report` | deep-research | After results/*.json validated |
| `devgod api` | backend-api, api-data-flows, typescript | `devgod api - Server Action for project create` |
| `devgod flow` | api-data-flows, system-architecture | `devgod flow - dashboard calling Rust aggregation service` |
| `devgod enforce` | enforcement, templates/ | `devgod enforce - set up CI for this repo` |
| `devgod growth` | growth-funnels, conversion-ui | `devgod growth - improve trial-to-paid conversion` |
| `devgod agent` | ai-agents, skill-authoring | `devgod agent - best prompt for Supabase auth in Cursor` |
| `devgod ship` | deploy-ops, backend-security, enforcement | `devgod ship - production readiness` |
| `devgod browser` | browser-qa, frontend-testing | `devgod browser - test signup on mobile and desktop` |
| `devgod launch` | product-marketing, analytics, GTM, QA | `devgod launch - technical SaaS release` |
| `devgod business` | product-business-engineering | `devgod business - implement hybrid pricing and PQL handoff` |
| `devgod kpi` | product-analytics | `devgod kpi - usage AI product` |
| `devgod prd` | prd-to-evidence | `devgod prd - resumable coding agent` |
| `devgod loop-optimize` | agentic-engineering + prompt-optimization | `devgod loop-optimize - coding agent` |
| `devgod red-team` | agent-red-teaming + ai-security | `devgod red-team - coding agent fixture` |
| `devgod decide` | decision-engineering + domain modules | `devgod decide - monorepo or polyrepo` |
| `devgod memory` | agent-memory + agentic-engineering + ai-security | `devgod memory - user preference store` |
| `devgod mcp-audit` | mcp-security + ai-security | `devgod mcp-audit - remote orders server` |

## Routing disambiguation

| You say | devgod routes to |
|---|---|
| "design a **database schema**" | `backend-database` |
| "design the **dashboard UI**" | `design-patterns` + `frontend` |
| "design **tokens**" | `design-system` |

## End-to-end flows

Multi-module pipelines (from `SKILL.md`):

| Task | Module chain |
|---|---|
| New UI feature | design-system → design-patterns → frontend → frontend-streaming |
| New form / auth | design-patterns → frontend → backend-auth → backend-database |
| Stripe billing | billing-stripe → backend-webhooks → backend-database → cso |
| Ship to production | deploy-ops → backend-security → enforcement → gstack /ship |
| Launch landing | seo-metadata → conversion-ui → growth-funnels |
| Multi-locale | frontend-i18n → seo-metadata → conversion-ui |
| File uploads | backend-storage → backend-api → backend-testing |
| EU privacy | compliance-privacy → backend-security → backend-testing |
| Turbo monorepo | architecture-monorepo → enforcement |
| Greenfield SaaS | system-architecture → architecture → design-system → backend-database → backend-auth → enforcement → growth-funnels → frontend |
| Deep research decision | deep-research outline → deep → report → plan (no code until pick) |

## Composition examples

Stack skills explicitly when needed:

```
devgod page - B2B landing for API product. After build, unmachined audit on hero copy.
```

```
devgod - add Stripe webhook handler. Run gstack /cso before merge.
```

```
devgod audit - performance on /dashboard. Apply react-best-practices after.
```

```
devgod research - compare Inngest vs Trigger.dev vs BullMQ for this SaaS
# then research-deep → research-report → plan chosen option
```

## Verify commands (include in prompts)

Agents should run checks before declaring done:

```bash
npm run typecheck
npm run lint:ci
npm run devgod:scan -- --strict
npm run test:unit
supabase test db # if RLS tests exist
```

See [ai-agents.md](../references/ai-agents.md) for the four-part spec template.

## Loop recipes

See [slash-commands.md](slash-commands.md) and `references/workflows.md`.

| Verb / command | Purpose |
|---|---|
| `/devgod-loop-agent` | Outer loop with budgets + maker/checker |
| `/devgod-loop-verify` | Until typecheck/lint/scan green |
| `/devgod-loop-ci` | Watch GitHub CI |
| `/devgod-loop-ship` | Until ship checklist green |
