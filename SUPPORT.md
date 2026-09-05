# Support

devgod is a volunteer-maintained skill package. Use the right channel so questions are seen.

## Where to ask

| You want to | Go to |
|---|---|
| Ask how a verb, module, or scanner works | [Issues](https://github.com/0xNyk/devgod/issues/new/choose) |
| Share a workflow, composition, or host adapter | Issues |
| Report reproducible incorrect behavior | [Issues](https://github.com/0xNyk/devgod/issues/new/choose) using the bug template |
| Propose a module, verb, or gate | Issues using the feature template |
| Report a vulnerability | [SECURITY.md](SECURITY.md), never a public issue |

Before opening an issue, run `bash scripts/validate-repo.sh` and include the output, your agent host (Cursor, Claude Code, Codex, other), and the commit SHA you installed from.

## What maintainers promise

- Issues and vulnerability reports get an acknowledgement, usually within 7 days.
- Bugs in first-party scripts, scanners, and templates are fixed on a best-effort basis.
- Every release is noted in [CHANGELOG.md](CHANGELOG.md).

## What maintainers do not promise

- No response-time SLA for questions or feature requests.
- No support for third-party skills, hosts, or stacks outside TypeScript, Python, and Rust web products; report those upstream.
- No help debugging a consumer app that disabled a module hard gate.
- No private consulting through the issue tracker.

Start with [docs/getting-started.md](docs/getting-started.md) and [docs/verbs.md](docs/verbs.md); most questions are answered there.
