# Slash commands

All 51 commands in `commands/` can be installed as native command aliases.
The command instructions stay in this checkout; generated adapters load them
when invoked.

```bash
bash scripts/install-commands.sh --hosts codex,claude,cursor,grok,hermes --dry-run
bash scripts/install-commands.sh --hosts codex,claude,cursor,grok,hermes
bash scripts/install-commands.sh --hosts codex,claude,cursor,grok,hermes --check
```

| CLI | Audit alias | User directory |
|---|---|---|
| Codex | `/prompts:devgod-audit <target>` | `$CODEX_HOME/prompts/` or `~/.codex/prompts/` |
| Claude Code | `/devgod-audit <target>` | `~/.claude/commands/` |
| Cursor | `/devgod-audit <target>` | `~/.cursor/commands/` |
| Grok | `/devgod-audit <target>` | `~/.grok/commands/` |
| Hermes | `/devgod-audit <target>` | `~/.hermes/skills/devgod-audit/SKILL.md` |
| Gemini CLI | `/devgod-audit <target>` | `~/.gemini/commands/` (TOML) |
| OpenCode | `/devgod-audit <target>` | `~/.config/opencode/commands/` |

Codex requires the `prompts:` namespace for every command in the table below;
its bare `/devgod-*` spelling remains unsupported. The custom-prompt interface
is deprecated upstream, so `$devgod audit <target>` remains the native skill
fallback. [Codex custom prompts](https://learn.chatgpt.com/docs/custom-prompts).

With no arguments, the installer selects detected hosts. `--hosts all` generates
adapters for every listed host without installing any CLI. `--user` retains the
old Cursor-only default; `--project` does the same for the current project.
Project scope also supports Claude, Grok, Gemini, and OpenCode via `--hosts`.
Codex custom prompts and Hermes aliases use user/profile scope.

The installer respects `CODEX_HOME`, `CLAUDE_CONFIG_DIR`, `HERMES_HOME`, and
`XDG_CONFIG_HOME`. `--home /path` creates an isolated installation for testing.
Unmanaged files and edited generated aliases block installation before any host
is changed. Existing symlinks to this checkout's command files can be migrated;
their source files stay untouched. Each destination records file hashes in
`.devgod-command-aliases.json` so subsequent updates preserve local edits.

Start new sessions after installing. Hermes can also reload its skill catalog;
Gemini has `/commands reload`. A successful `--check` proves generated files
match the catalog, not that a running session has refreshed or executed them.
Aliases preserve arguments as prompt text and add no hooks or shell execution.
The original command's permissions, audit-only behavior, and required tools
still apply. Missing loop, browser, or delegation capabilities remain host limits.

Discovery formats: [Claude](https://code.claude.com/docs/en/skills),
[Gemini](https://geminicli.com/docs/cli/custom-commands/),
[OpenCode](https://opencode.ai/docs/commands/), and
[Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/).
Grok's legacy command format was checked against its installed skills guide.

## Core verbs

| Command | Mode |
|---|---|
| `/devgod` | Build with all rules (default) |
| `/devgod-plan` | Architecture plan - no code |
| `/devgod-audit` | Report only, severity findings |
| `/devgod-refactor` | Structure-only refactor (preserve behavior) |
| `/devgod-fix` | Audit → minimal repair |
| `/devgod-schema` | Migrations + RLS plan |
| `/devgod-page` | Landing / conversion page |
| `/devgod-design` | Design system + a11y audit |
| `/devgod-api` | Server Actions / handlers |
| `/devgod-flow` | Data flow diagram |
| `/devgod-enforce` | Copy scanners + CI setup |
| `/devgod-growth` | PLG funnel plan |
| `/devgod-agent` | Prompt/spec help |
| `/devgod-ship` | Production pre-flight |
| `/devgod-research` | Deep-research outline (items + fields) |
| `/devgod-research-deep` | Parallel deep agents → validated JSON |
| `/devgod-research-review` | Claims → captured evidence → independent semantic review |
| `/devgod-research-report` | Results → report.md |
| `/devgod-research-add-items` | Extend outline items |
| `/devgod-research-add-fields` | Extend research dimensions and revalidate |
| `/devgod-self-improve` | Optimize devgod itself with regression gates |
| `/devgod-browser` | Browser coverage, isolated lanes, evidence |
| `/devgod-qa` | Systematic product QA and optional repair |
| `/devgod-assure` | Goal-to-runtime business-logic and full-stack assurance |
| `/devgod-visual` | Infographics, editorial-technical assets, thumbnails, identity, and banners |
| `/devgod-launch` | Launch surfaces through activation and QA |
| `/devgod-business` | Product/business goal to software architecture |
| `/devgod-kpi` | KPI tree, events, dashboards, data quality |
| `/devgod-prd` | Requirements to acceptance, plan, tests, and evidence |
| `/devgod-loop-optimize` | Prompt, context, tool, loop, and grader optimization |
| `/devgod-orchestrate` | Bounded multi-agent graph, delegation, lanes, joins, and synthesis contract |
| `/devgod-red-team` | Authorized, isolated defensive agent security evaluation |
| `/devgod-skill-audit` | Quarantine, inventory, sandbox, and decide trust for a third-party skill |
| `/devgod-capability-promote` | Decide whether recurring work belongs in code, instructions, DevGod, an existing skill, or a new skill |
| `/devgod-mcp-audit` | Audit MCP authorization, capabilities, tools, roots, and captured calls |
| `/devgod-incident` | Preserve evidence, contain, revoke, eradicate, and recover an agent compromise |
| `/devgod-memory` | Review durable memory admission, retrieval, retention, and deletion |
| `/devgod-decide` | Bounded evidence-based engineering deliberation |
| `/devgod-doctor` | Cross-host installation identity and evaluation readiness |
| `/devgod-oss` | Automatic proportional OSS maintainer audit and repository baseline |

## Workflow pipelines

Multi-module sequences. Full checklists: [references/workflows.md](../references/workflows.md).

| Command | Pipeline |
|---|---|
| `/devgod-greenfield` | Architecture → design → backend → enforcement → growth |
| `/devgod-landing` | SEO → design-taste → conversion → growth → perf → unmachined |
| `/devgod-billing` | Stripe Checkout → webhooks → RLS → cso |
| `/devgod-auth` | Forms → frontend → auth → database |
| `/devgod-locale` | i18n → SEO → conversion UI |
| `/devgod-upload` | Storage → API → pgTAP |
| `/devgod-privacy` | GDPR export/delete → security |
| `/devgod-launch` | Brief → conversion → analytics/GTM → browser QA |
| `/devgod-qa` | Coverage matrix → evidence → repair → regression |
| `/devgod-assure` | Goals/rules → boundaries → layered tests → runtime evidence → residual risk |

## Loops (with `/loop` skill)

Compose with Cursor **`/loop`** skill for until-green automation.

| Command | Loop invocation | Purpose |
|---|---|---|
| `/devgod-loop-agent` | `/loop dynamic /devgod-loop-agent` | Outer loop with budgets + maker/checker |
| `/devgod-loop-verify` | `/loop dynamic /devgod-loop-verify` | Until typecheck + lint + devgod-scan pass |
| `/devgod-loop-ship` | `/loop dynamic /devgod-loop-ship` | Until ship checklist green |
| `/devgod-loop-ci` | `/loop 2m /devgod-loop-ci` | Watch GitHub CI until green |

### Example sessions

**Plan → build:**

```
/devgod-plan - team invitations with roles
# review plan, then:
/devgod - implement approved plan
```

**Deep research → plan:**

```
/devgod-research - background job systems for Next SaaS
/devgod-research-deep
/devgod-research-review
/devgod-research-report
# pick a winner, then:
/devgod-plan - integrate chosen queue into the app
```

**Audit → fix loop:**

```
/devgod-audit - features/billing/
/devgod-fix - features/billing/
/loop dynamic /devgod-loop-verify
```

**Landing launch:**

```
/devgod-landing - B2B API product page
# then unmachined on copy
```

**Pre-production:**

```
/devgod-enforce
/devgod-ship
/loop dynamic /devgod-loop-ship
```

---

## Native skill fallback

If command aliases are not installed, load the native skill (`$devgod` in Codex,
`/devgod` in Claude) or use the equivalent plain-text requests:

```
devgod plan - ...
devgod audit - ...
Load devgod. Run devgod ship - ...
```

Or load gstack-style: `Load gstack. Run /ship` composed with devgod modules.

---

## File location

Commands live in `commands/*.md` in the devgod repo. Filename = slash name:

```
commands/devgod-plan.md  →  /devgod-plan
commands/devgod-loop-verify.md  →  /devgod-loop-verify
```

Add new commands: create `commands/devgod-{name}.md`, add routing to `references/workflows.md`, run install script.

## Update and uninstall

Rerun the installer after updating the checkout. It refreshes unchanged managed
aliases and removes unchanged aliases for commands no longer in the catalog.
`--check` reports drift without writing. A changed managed file, invalid receipt,
or conflicting symlink stops the whole selected-host preflight before any writes.
Move a customized alias to a different name before retrying; keep a copy of your edits.

```bash
bash scripts/install-commands.sh --hosts all --uninstall --dry-run
bash scripts/install-commands.sh --hosts all --uninstall
```

Uninstall removes only receipt-owned files whose hashes still match. It preserves
unrelated commands, edited files, and native skill links. Empty Hermes alias
directories are removed; directories containing other files remain. Do not edit
or discard `.devgod-command-aliases.json`: it records ownership for safe cleanup.
A filesystem failure during application can leave a partial update; resolve the
failure and rerun the installer. The preflight is not a filesystem transaction.
