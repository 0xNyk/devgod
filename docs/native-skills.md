# Native skill installation

DevGod uses one Agent Skills package: `SKILL.md`, its references, and its helpers.
Each host reads the same checkout through its native skill directory. No plugin,
MCP server, global rule, memory entry, or slash-command wrapper is required.

Agent roles, model selection, and delegation controls follow
[agent setup and model selection](../references/agent-model-selection.md).

## Install a reviewed checkout

Requires Python 3.10+ and Bash on macOS/Linux, or WSL. The installer creates
symlinks; keep the checkout available at its installed path.

```bash
bash scripts/install-all-agents.sh --dry-run
bash scripts/install-all-agents.sh --hosts codex,claude,grok,hermes,cursor
python3 scripts/devgod-doctor.py --hosts codex,claude,grok,hermes,cursor --strict
```

With no `--hosts`, installation selects existing host roots or CLIs found on
`PATH`. Explicit host selection creates missing skill directories. `--hosts all`
selects every supported adapter; it does not install any CLI. Existing directories,
files, and links to other checkouts cause an error before any links are changed.
Inspect and move a conflicting installation yourself, then retry. Repeating an
installation whose links already target this checkout leaves them untouched.

On managed machines, use the existing skill-linking owner when local policy
requires it. If native links already resolve to this checkout, no reinstall is
needed after editing the skill.

## Host discovery

Paths below are user-level defaults. Discovery evidence was checked on 2026-09-05;
installed versions, disabled skills, trust settings, and remote environments can
change what a session sees.

| Host | Native skill location | Load or check |
|---|---|---|
| Codex | `~/.agents/skills/devgod/` | `$devgod audit <target>`; select the skill when completing `$devgod` |
| Claude Code | `~/.claude/skills/devgod/` | `/devgod audit …` |
| Grok CLI | `~/.grok/skills/devgod/` | Inspect `/skills`, then invoke the listed skill |
| Hermes | `~/.hermes/skills/devgod/` | Inspect the skills catalog; load `devgod` with the native skill tool |
| Cursor | `~/.cursor/skills/devgod/` | Select devgod from Skills or the slash picker |
| Gemini CLI | `~/.gemini/skills/devgod/` | `/skills list`, then request devgod |
| OpenCode | `~/.config/opencode/skills/devgod/` | Request devgod through the native `skill` tool |
| Shared Agent Skills | `~/.agents/skills/devgod/` | Available only to hosts that discover this root |

Codex and the `agents` adapter share a destination. The installer does not create
a second Codex copy in `~/.codex/skills`; existing compatibility links are retained.
`agents/openai.yaml` provides optional Codex metadata. Other hosts use `SKILL.md`.

`HERMES_HOME`, `CLAUDE_CONFIG_DIR`, and `XDG_CONFIG_HOME` select the corresponding
Hermes, Claude, and OpenCode roots. Installation and doctor use the same resolver.
An explicit `--home /path` ignores these overrides for isolated fixture checks.

For another host or a project-local skill root, use its documented directory:

```bash
python3 scripts/install-native-skills.py --skills-dir /path/to/native/skills --dry-run
python3 scripts/install-native-skills.py --skills-dir /path/to/native/skills
```

This installs `/path/to/native/skills/devgod/`. A generic path does not establish
that a host supports Agent Skills. On remote hosts, install in the execution
environment. A symlink to a path on another machine will not work. For a portable
repository package, vendor the reviewed skill resources instead of committing
an absolute symlink to a personal checkout.

## Verify a session

If Codex reports `Unrecognized command '/devgod-audit'`, enter
`$devgod audit <target>`. To install the complete alias catalog, run
`bash scripts/install-commands.sh --hosts codex`. Codex aliases use
`/prompts:devgod-audit`; the bare `/devgod-*` form remains unsupported.
Restarting does not change this syntax. See the
[Codex invocation instructions](https://learn.chatgpt.com/docs/build-skills).

Refresh the host's skill catalog or start a new session. Check that `devgod` is
listed, explicitly load it, and ask it to read a bundled reference. Then try a
small engineering task in a disposable project. Confirm the reference resolves
from the skill location while project commands run in the project directory.

Doctor checks installation identity for the selected hosts. It does not spend
model quota or prove that a host loaded the skill. Automatic relevance selection
depends on the host and model. The live evaluation runner currently supports
Codex and Claude; passing installer tests is not a live behavioral result for
every host.

Hosts without a native skill loader can read the entrypoint and referenced files
explicitly. That is a manual fallback, not native discovery. Missing browsers,
subagents, memory, or approval mechanisms must be handled through the capability
contract in `references/coding-agent-hosts.md`.

## Optional legacy adapters

`scripts/install-commands.sh` installs all command aliases separately using each
host's native format. See [slash commands](slash-commands.md) for installation,
profile paths, and Codex's required `prompts:` namespace. The native skill also
accepts `devgod <verb> <task>` without those aliases.

`scripts/install-host-activation.py` remains an opt-in legacy routing helper. It
edits host instruction files, a Cursor rule, and Hermes memory. It is no longer
called by the native installer. Existing routing rules are retained. Doctor's
`--require-activation` checks these legacy locations separately; their presence
does not prove host support for that routing mechanism.

## Discovery sources

- [Agent Skills package specification](https://agentskills.io/specification)
- [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Cursor skill directories](https://cursor.com/docs/skills)
- [Hermes skills system](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [Gemini CLI skills](https://geminicli.com/docs/cli/skills/)
- [OpenCode skills](https://opencode.ai/docs/skills/)

Grok's adapter was checked against its installed CLI README, "Skills / Skill
Locations." The name Grok is also used by other clients; verify their own skill
support before using this adapter.

## Remove native links

From the same checkout used to install:

```bash
bash scripts/install-all-agents.sh --hosts all --uninstall --dry-run
bash scripts/install-all-agents.sh --hosts all --uninstall
```

This removes only symlinks pointing to that checkout. Existing directories, files,
and links to another checkout stop preflight and remain untouched. Command aliases
have a separate uninstall command in [slash-commands.md](slash-commands.md).
Codex and the shared Agent Skills entry use the same link; removing it affects
other hosts that discover that shared directory. Refresh host catalogs afterward.
