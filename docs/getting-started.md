# Getting started

## 1. Install

Clone once, then symlink so edits update every agent:

```bash
git clone https://github.com/0xNyk/devgod.git
cd devgod
bash scripts/install-all-agents.sh
# optional: bash scripts/install-all-agents.sh --pull # git pull first
```

The installer links the native skill into detected host directories. To select the
five common CLI seats and verify their installations:

```bash
bash scripts/install-all-agents.sh --hosts codex,claude,grok,hermes,cursor --dry-run
bash scripts/install-all-agents.sh --hosts codex,claude,grok,hermes,cursor
python3 scripts/devgod-doctor.py --hosts codex,claude,grok,hermes,cursor --strict
```

It creates missing selected directories and preserves conflicting installations.
It does not install CLIs or change global rules, memory, or slash aliases.
[Native skill support](native-skills.md) lists all supported hosts, profile roots,
custom directories, and session discovery checks.

Refresh the skill catalog or start a new session. Select the native devgod skill
and give it a task: `$devgod audit <target>` in Codex, or
`/devgod audit <target>` in Claude Code. Automatic activation depends on relevance
and host settings. Codex does not register Cursor aliases such as `/devgod-audit`.
Install the full alias catalog with
`bash scripts/install-commands.sh --hosts codex,claude,grok,hermes,cursor`.
Use `/prompts:devgod-audit <target>` in Codex and `/devgod-audit <target>` in the
other listed CLIs. See [slash commands](slash-commands.md) for all hosts.

## 2. Optional companions

Install partner skills only from their canonical repository at a reviewed commit SHA. Audit the
skill package before enabling it; do not execute a floating installer or package runner.

| Skill | When |
|---|---|
| vercel `react-best-practices` | Performance audits, React/Next optimization |
| `unmachined` | Marketing copy, anti-slop UI audits |
| gstack | Optional `/cso` security, exploratory `/qa`, `/ship` deploy runtime |

## 3. First prompts

Start simple - devgod detects your stack from the repo:

```
devgod - add a profile settings page with avatar upload
```

For larger work, plan first:

```
devgod plan - team invitations with role-based access
```

Review-only:

```
devgod audit - app/api and Server Actions
```

Pre-production:

```
devgod ship - production readiness check
```

## 4. Session workflow

Every devgod session follows this order:

```
1. project-detect → read package.json, supabase/, tailwind version
2. route → SKILL.md routing map → 1 router + 2-4 leaf modules
3. build / audit → apply module rules
4. verify → typecheck, devgod-scan, tests
5. compose → unmachined / gstack when needed
```

Agents should **not** bulk-load all of `references/` or `research/` - only modules needed for the task.

## 5. Project-level setup (recommended)

Copy enforcement into your app repo so gates run on every PR:

See [enforcement-setup.md](enforcement-setup.md) for the full checklist.

Minimum:

```bash
mkdir -p your-project/scripts
cp "$DEVGOD/scripts/devgod-scan.sh" your-project/scripts/
cp "$DEVGOD/scripts/check-rls-migration.sh" your-project/scripts/
```

Add to `package.json`:

```json
"devgod:scan": "bash scripts/devgod-scan.sh --strict"
```

## 6. Repo rules

Native skill discovery provides the default entrypoint. Add a repository rule only
when the project needs a narrower stack or verification contract:

```markdown
## Fullstack

Load devgod skill for Next.js + Supabase work.
Security: gstack /cso before payment webhooks ship.
Deploy: devgod ship → gstack /ship
```

Keep `AGENTS.md` short - pointers, not encyclopedias. Details live in devgod modules.

## 7. When devgod is the wrong tool

devgod targets **Next.js App Router + Supabase + TypeScript** (optional Rust).

For other stacks, devgod should detect and scope down - not force patterns. Examples:

- Django/Rails backend → use stack-native patterns
- Pages Router legacy → follow project, flag migration path
- Mobile/Expo → outside core scope; use a dedicated mobile skill

## Next steps

- [Verbs reference](verbs.md) - text invocations (`devgod plan - …`)
- [Slash commands](slash-commands.md) - `/devgod-plan`, loops, pipelines
- [Module map](modules.md) - find the right reference file
- [Enforcement setup](enforcement-setup.md) - CI and pre-commit
