# Agent setup and model selection

**Last verified**: 2026-09-05 · **Review cadence**: monthly and after host/model changes

Apply this policy when configuring agents, selecting models, or delegating work.
For a small task, keep the decision in the session. An actual multi-agent run uses
the contract and runtime gates in `multi-agent-orchestration.md`.

## Choose the work split first

Keep one coordinator responsible for scope, integration, and verification. Delegate
only a bounded task that can proceed independently while useful work continues in
the parent, or when a separate context materially improves review. Follow host and
user restrictions on delegation; this policy never enables a disabled capability.
Use native roles before adding persistent definitions. A small coupled fix stays
with one agent. Start with the smallest useful team and expand only for measured need.

Each worker briefing includes its goal, owned files/resources, inputs, relevant
DevGod modules, allowed tools, acceptance checks, output destination, limits, and
stop conditions. State that other workers share the codebase: preserve their edits.
Pass bounded evidence references rather than an entire transcript. Do not assume
that a child inherits the parent's loaded skill instructions. Reviewers receive
read access; writers use disjoint paths or isolated worktrees. The coordinator
integrates only after writers finish. Leaf workers have zero descendants.

## Select models against the task

Honor managed constraints, then explicit user choices and project policy. Otherwise
choose from the host's observed catalog. Resolve provider, model, supported effort,
context capacity, modalities, tool support, data restrictions, and cost/latency limits.
Read safe model metadata; do not dump credentials or full host configuration.

| Role | Selection rule |
|---|---|
| Coordinator, architecture, uncertain debugging | Prefer demonstrated reasoning and tool reliability; increase supported effort when complexity warrants it. |
| Bounded search, extraction, repetitive edits | Use a faster or cheaper available model when it meets the same acceptance checks. |
| Implementation | Match language/tool competence and context capacity to the owned change; escalate after a diagnosed capability failure. |
| Security or high-impact review | Prioritize reasoning and evidence quality; use a separate context with read access and independent checks. |
| Browser or visual verification | Require the modalities and browser tools the task needs. A larger text model cannot substitute for missing visual evidence. |

"Optimal" means the best measured tradeoff under the user's constraints. Compare
representative tasks using acceptance pass rate, retries, total cost, and latency.
Without comparable measurements, label the choice provisional. Do not rank models
by name, release date, price alone, or a fixed vendor leaderboard. More agents and
maximum reasoning on every worker are not default improvements.

Record each agent's resolved `model_selection`, catalog evidence reference, task-fit
rationale, and required versus available capabilities. `selection_basis: inherit`
still records the effective model ID. Use `not_configurable` for effort only when
the host exposes no effort control; never invent a setting. Catalog and runtime
evidence should identify the host version and capture time. Refresh after changes.
An explicitly requested unavailable model is a blocked choice, not permission to
silently substitute. Diagnose transient failures within the retry budget; model or
effort changes require a revised contract before relaunch. Do not rewrite an old
receipt to disguise a fallback. Keep automatic provider fallback off for strict runs.

## Bind to the actual host

Codex supports custom agent configuration and model/effort inheritance. Effective
settings can differ from spawn arguments because role configuration participates
in resolution. Check the installed tool schema and runtime metadata. See the
[official Codex subagent guide](https://developers.openai.com/codex/multi-agent).

Claude supports subagent model declarations and invocation overrides; managed
allowlists and forced defaults can change the effective result. Verify the model
actually running. See [Claude subagent configuration](https://code.claude.com/docs/en/sub-agents#choose-a-model).

Hermes currently uses `delegation.model` for the whole child batch; `delegate_task`
has no per-task model argument. Inherit a suitable model or use a supported separate
task surface when different models are required. See [Hermes delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation/).

For Cursor, Grok, Gemini, OpenCode, and other hosts, inspect the installed version's
native tools and official documentation before generating configuration. Do not
copy another host's fields or assume identical inheritance and isolation behavior.
If delegation is absent, execute the roles sequentially and disclose that no
independent worker ran. Never spawn another CLI to bypass a host restriction.

## Enforcement and evidence

Before launch, validate the graph and map its tool/lane/budget limits to effective
host controls or a reviewed execution runner. Normalize concurrency to include the parent;
some hosts advertise only child slots. Use the lower host/user limit and reserve
capacity for coordination. A worker may not raise its own limits or spawn outside
the declared graph. Serial execution is the fallback for unsafe writer overlap.

Skill instructions guide behavior; they cannot install a sandbox or intercept every
host tool. A contract validator checks declarations. Host permissions and runner
checks enforce operations. Record which controls are actually active; if a required
boundary is unavailable, stop that delegated operation. Do not report prompt-only
restrictions as enforced isolation. Persistent host configuration changes need the
user's authorization and a reviewable diff; session setup does not imply global edits.

At joins, verify returned artifacts and the integrated state, release workers, and
report missing results. Validate schema-v2 runtime receipts against the exact
contract, including observed host/model/effort and concurrency. Unknown identity or
a silent substitution cannot pass. Evidence references must come from captured host
metadata, not the worker's guess. Validators do not authenticate a provider's model
identity or prove that the declared catalog and telemetry are complete.
