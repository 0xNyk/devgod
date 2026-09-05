# Releasing DevGod

Publish a reviewed commit with evidence from a fresh checkout. A green local test
run covers the working tree; it does not establish that older commits or hosted
logs are suitable for public access.

## Release checks

1. Review the complete candidate diff, including staged files and new files.
   Confirm source attribution and retain license notices for copied material.
2. Run `python3 scripts/rebind-skill-eval.py --check`. If runtime files changed,
   run it without `--check`, review the sample changes, and repeat validation.
3. Run `bash scripts/validate-repo.sh`, the installer tests below, and the repository
   leak gate with the documented fixture exceptions in the validation workflow.
   The leak gate scans tracked working files; include every candidate file in the
   reviewed snapshot before relying on that result.
4. Run the pinned prose gate and require all validation jobs on the exact candidate
   commit, including clean-install jobs on Linux and macOS.
5. Test native command discovery and representative workflows in the hosts you
   claim to support. Record version, platform, invocation, result, and evidence.
6. Verify Issues, license, installation links, and release notes. GitHub private
   vulnerability reporting is available for public repositories. After the clean
   destination is public, enable it and verify the form before announcing the release.
   See [GitHub reporting configuration](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).

```bash
python3 scripts/test-native-skills.py
python3 scripts/test-command-aliases.py
python3 scripts/test-clean-install.py
```

The clean-install test exports the installer files into a temporary directory,
installs into an isolated home from a consumer project, relocates the export,
checks conflict handling and refresh, then uninstalls. It uses no installed host,
model account, network service, or profile override. CI runs it on Python 3.10 and
3.13 with Linux and macOS. The default installers require only Python and Bash.

## Host evidence

Keep three claims separate when recording a release result:

| Level | Evidence required |
|---|---|
| Adapter format | Generated files parse, cover the catalog, preserve arguments, and pass lifecycle tests |
| Native discovery | The named host version lists and expands the command in an isolated profile |
| Workflow execution | The host completes a disposable audit, fix, and plan task with checked results |

The automated installer suite covers formats and filesystem behavior for Codex,
Claude Code, Cursor, Grok, Hermes, Gemini CLI, and OpenCode. It does not prove that
all host versions discover or execute these commands. Gemini and OpenCode adapters
need host testing before claiming verified workflow support. Codex custom prompts
use `/prompts:devgod-*`; the host does not register bare `/devgod-*` aliases.
Its custom-prompt interface is deprecated; `$devgod` is the native skill entrypoint.

For a manual host smoke test, create a disposable project with a function that
incorrectly adds one to a total and a failing test. Invoke `devgod-audit` to locate
the defect without edits, `devgod-fix` to repair it and pass the test, then
`devgod-plan` for a small extension. Use the host's actual command spelling.
Check the diff after each invocation, preserve quoted task arguments, and verify
that the plan does not claim unrun tests. Keep transcripts private until reviewed.

## Git history and hosted state

Review every branch and tag intended for publication, commit messages, historical
blobs, releases, attachments, and Actions logs. Removing a file at the branch tip
does not remove its old content. A visibility change can expose Actions history
and logs; see [GitHub's visibility documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).
Pattern scans identify candidates for review; a clean scan does not establish
that content is safe to publish.

When history contains private session state, prepare a clean export from the
reviewed candidate. Include only the explicitly reviewed file list, inspect the
export for ignored or untracked material, and run validation there. Start a new
history for that export, retain required attribution, and keep the original
repository private. Creating or publishing the destination is a separate
maintainer action. Rewriting existing history also needs an explicit decision;
neither operation is part of the installer.

CI checks out the public unmachined prose scanner at an immutable commit. Review
changes to the scanner before updating that pin. `requirements-dev.txt` pins the
Python fixture dependency and gives Dependabot a manifest it can update.

## Dependency updates

Dependabot updates executable workflows. Its PR may leave consumer templates and
the expected pins in `scripts/test-action-runtime-pins.sh` unchanged. A pin mismatch
fails CI until a maintainer reviews and synchronizes the whole change.

1. Update the candidate branch from the default branch so existing fixes are included.
2. Inspect the upstream release, resolved commit and signature, source diff, action
   runtime, removed inputs, and minimum runner version. A verified signature alone
   does not establish that the change is compatible or safe.
3. Update every matching pin in `.github/workflows/`, `templates/github/`, and
   `scripts/test-action-runtime-pins.sh`. Record the reviewed versions and evidence
   in `research/github-actions-node24-2026-07.md`.
4. Rebind the skill-eval samples, run the pin and documentation supply-chain checks,
   and require hosted CI on the resulting commit before merge.

```bash
python3 scripts/rebind-skill-eval.py
bash scripts/test-action-runtime-pins.sh
python3 scripts/scan-doc-supply-chain.py
bash scripts/validate-repo.sh
```

Retain exact SHA pins and the synchronization gate. Do not bypass a failed check to
merge a bot proposal or mark the hosted checks green based on local results.
