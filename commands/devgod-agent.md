---
description: Agent setup, model selection, and four-part workflow specs for native coding hosts.
---

# /devgod-agent

Load devgod `SKILL.md`, `references/ai-agents.md`, and `references/agent-model-selection.md`.

User's agent/prompt question follows this invocation.

For setup, inspect the host's actual capabilities, resolve role/model/effort choices,
scope tools and write ownership, and specify acceptance checks. Preserve explicit
model preferences and show unsupported controls. For multiple agents, compile and
validate the orchestration contract before execution. Do not merely return a prompt
when the user requested implementation of agent setup.

## Default response shape

Provide a **four-part spec** they can paste:

```markdown
## Goal
## Scope (touch / do NOT touch)
## Context (@files, modules)
## Acceptance (+ verify commands)
```

## Tool hints

| Tool | Tip |
|---|---|
| Cursor | @files, Agent mode, invoke devgod by name |
| Claude Code | Short prompts, skills in CLAUDE.md, gstack /autoplan |
| Codex | AGENTS.md, explicit verify in acceptance |

## Skill optimization

If user asks about building skills → `references/skill-authoring.md`

## Compose

Stack devgod + gstack + unmachined explicitly in spec when relevant.
