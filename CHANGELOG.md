# Changelog

## Unreleased

- Update immutable checkout and setup-python pins across workflows, consumer
  templates, and regression checks. Document the complete dependency update process.

- Apply host-aware agent setup and model selection before delegation, with explicit
  role ownership, capability checks, user overrides, and verification requirements.
- Orchestration schema v2 requires model choices and observed runtime identities,
  checks concurrency limits, permits leaf workers with no descendants, and rejects
  overlapping parent/child write paths. Recompile v1 contracts before new runs.
- Store the admission sample as `SKILL.md.fixture` so installing DevGod does not
  expose a second skill. Tests materialize the candidate outside the installed tree.

## Unreleased - public-prep

Prepare the repository for public release: remove private context, add the
missing community files, and make the leak gate run against the repo itself.

### Removed

- Tracked `.devgod/` session state and plan artifacts (51 files); `.devgod/` is
  now ignored.
- References to private skills, ventures, and machine paths across
  `references/`, `SKILL.md`, `commands/`, `evals/`, `research/`, `templates/`,
  and this changelog; replaced with neutral placeholders or role descriptions.

### Added

- Receipt-checked alias cleanup and uninstall, with separate native-link removal
  and preservation of edited files.
- Clean-install CI for Linux and macOS, a pinned public prose scanner, and a
  release checklist covering host evidence and historical publication surfaces.

- Command adapters for all 51 DevGod commands across Codex, Claude, Cursor, Grok,
  Hermes, Gemini, and OpenCode. Codex uses its required `/prompts:` namespace.
  Generated aliases preserve arguments and refuse to overwrite local edits.

- Cloud provider modules `references/cloud-aws.md`, `cloud-gcp.md`, `cloud-vercel.md`,
  `cloud-platforms-iac.md` from a 16-item deep-research pack (`research/cloud/`):
  identity-first defaults, limits and pricing with as-of dates, cost guardrails,
  scan signals. PaaS tier has no GitHub OIDC as of 2026-08; scoped rotated
  tokens are the documented ceiling there.
- `SUPPORT.md`, `.github/CODEOWNERS`, `.github/dependabot.yml`,
  `.github/ISSUE_TEMPLATE/{bug,feature,config}.yml`, `.gitattributes`, `llms.txt`.
- README Trust and Telemetry sections and an Anthropic trademark notice.
- CI step `Private-context leak gate` that runs `check-oss-leaks.sh --all` on
  every push with a short, commented allow list for synthetic fixtures.
- Leak gate: cloud identifier layer - AWS, GCP, Vercel, Cloudflare, Fly, Railway,
  Render, Netlify, Azure, and Supabase ids and hosts as INFRA; provider token
  prefixes as SECRET; credential dot-dirs as PATH; placeholders exempt (fixture
  section 14).

### Changed

- Native skill installation now selects host directories without editing global
  instructions or memory. Add safe conflict handling, profile roots, custom
  skill directories, dry runs, and selected-host provenance checks.

- `references/portfolio-context.md` rewritten as an abstract control-plane
  pattern; `scripts/plan-fleet-status.sh` reads the control-plane repo name
  from `DEVGOD_CONTROL_PLANE_REPO` (default `control-plane`).
- `SECURITY.md` points to GitHub private vulnerability reporting with a 7-day
  acknowledgement window; clone URLs use https.

## 1.90.0 - 2026-08-23

Fix the unbound skill-eval hash chain left by the last runtime edit, slim the
L2 plan dump, and make local health match CI.

### Fixed

- Skill-eval sample bindings now match the current runtime package again
  (`python3 scripts/rebind-skill-eval.py`). Capture, grading, telemetry, and
  evidence-output fixtures were failing on the drifted bundle hash.

### Changed

- SKILL.md Plan section keeps the five-step PVE and activation classify list;
  locations, ownership, archival, branch-per-plan, and sidequest depth stay in
  `workflows.md`
- Composition `agent-security` row is a one-line gate plus `composition.md`
- `devgod-health.sh` runs the same rebind, false-done, and host-activation
  fixtures CI already ran
- CONTRIBUTING documents the rebind `--check` ritual and versioned changelog
  entries (the file never used an Unreleased heading)

## 1.89.0 - 2026-08-21

Greenfield Next.js now ships Tailwind v4 + shadcn/ui by default, and expertise
gets currency teeth: module knowledge is a cache, not the authority. Plus a
curated adoption of the strongest rules from elayadesign/ai-design-skills
(MIT), vetted against existing gates.

### Added

- `stack-rules.md` → **Greenfield default stack (binding)**: new Next.js apps
  scaffold Tailwind v4 + shadcn/ui by default (create-next-app + shadcn init,
  flags verified against current CLIs 2026-08-21), build on wrapped shadcn
  primitives, de-genericize before pages; greenfield-only - existing codebases
  follow project truth
- `project-detect.md` **Greenfield default rule**: absence ≠ opt-out in a new
  project; absence = project truth in an established one
- SKILL.md hard gate **Expert currency**: version-sensitive framework/API/CLI
  guidance past its module review cadence, conflicting, or uncertain is
  re-verified against current primary sources before it is asserted or
  scaffolded
- Design depth curated from elayadesign/ai-design-skills (MIT; conflicting
  rules - font whitelist, mandatory word-reveal tagline, `transition-all`
  snippets, fixed hex palettes - rejected as devgod-scan tells):
  - `design-system.md`: nested radius formula (inner = outer − gap under
    32px), type-scale discipline (no arbitrary `text-[19px]`; snap down with
    paired line height)
  - `design-motion.md`: scroll-reveal rules (IntersectionObserver/whileInView,
    never unthrottled scroll listeners), weighted easing, micro active-press
    feedback
  - `design-taste.md`: content realism for demo/sample content (no Lorem
    Ipsum, John Doe, Acme, or round fake numbers) - scoped so marketing proof
    stays real-or-labeled, never fabricated organic-looking data
  - `conversion-ui.md`: proof beside the claim it supports, risk reversal near
    the primary CTA (true terms only), earlier objection handling for
    high-friction offers, page-completeness checklist (404, favicon, dead
    links, skip link, meta/og)

### Changed

- SKILL.md principle 5 names the greenfield UI default; `/devgod-greenfield`
  Phase 2 starts with the scaffold step; workflows greenfield chain and exit
  criteria include the scaffold + de-genericization

## 1.88.0 - 2026-08-19

Follow-through: make the 2026 taste contract executable, and stop APFS
case-alias paths from failing skill-eval grading and admission fixtures.

### Added

- `devgod-scan --design` WARNs (FAIL under `--strict`) on gradient/indigo/cyan,
  colored glows, 3-4px card-stripe classnames (2px dividers are not the Krebs
  tell), numbered 01/02/03 section kickers, Inter-everywhere
  (`import { Inter }` / `Inter({`), and badge-above-H1 (`rounded-full` then
  `<h1>`, or "Now in Beta"); fixtures `fail-design` and `fail-taste`
- `DESIGN.md` detection in project-detect

### Changed

- `evidence_path.py` treats same-inode path casings as inside the repo
  (path-casing variants of the skills workspace) without weakening symlink confinement
- Landing pipeline, slash-commands, output-quality, visual-communication, and
  stack-rules grep include taste tells
- WCAG 2.2 accessible-authentication reminder on password fields

## 1.87.0 - 2026-08-19

Make frontend and design work distinctive. Tokens and WCAG were not enough:
agents still emitted Inter / indigo / three-card SaaS. `design-taste.md` is the
portable aesthetic contract (named tone + one signature, 2026 AI clusters
banned unless the brief names them, structure is a choice, copy is design
material). Optional `hallmark` / `frontend-design` remain partners.

### Added

- `references/design-taste.md` and eval 208 (generic landing must not ship the
  default AI skeleton)
- `research/design-taste-2026-08.md` - Krebs 1,590-page Show HN scoring, Impeccable
  catalog, Rams/NN/g, Figma 2026 trends as anti-catalog

### Changed

- Frontend, conversion-ui, design-system, design-patterns, design/page commands,
  and SKILL routing load taste for new UI without adding it to default verb
  Load-first lists (budget)

## 1.86.0 - 2026-08-19

Restore skill-router integrity and pin the 2026-08 stack. Uncommitted L2 dumps
(X-article publishing gates, broken YAML `category: null`, truncated description)
are rejected; operator runbooks stay out of this skill.

### Added

- `license: MIT` in SKILL.md frontmatter (agentskills.io optional field)
- `references/secure-package-html-preview.md` - sandboxed package-backed HTML previews
- `validate-repo.sh` gates: every reference module needs `Last verified`; public
  skill surface must not contain operator X-article runbooks
- Loop-avoidance contract in `agentic-engineering.md` (not in SKILL.md)

### Changed

- Greenfield default is Next **16.x** + `proxy.ts` + Cache Components; Next 15
  `middleware.ts` is detect-and-keep
- MCP module pins spec **2026-07-28** (stateless HTTP; Tasks as extension)
- Stripe module: Checkout Sessions is the default API
- Tailwind v4 + Turbopack: explicit `@source` when HMR misses classes
- Default `devgod design` no longer bulk-loads `design-motion`
- Default `devgod hermes` / `loop-optimize` no longer bulk-load `long-horizon-agents`
- COMPAT, gap-audit, and monthly-cadence host/discovery modules refreshed

## 1.85.0 - 2026-07-25

Natively integrate the **agent-security** skill as devgod's default agent supply-chain gate,
binding when installed. devgod's native modules (oss-maintainer, skill-supply-chain,
malware-detection, ai-security) keep the routing and policy; agent-security owns the
deterministic gates at four edges: outbound public-repo content (scan-repo supersedes
`check-oss-leaks.sh`), inbound third-party code (vet-incoming before any install/scaffold),
destructive GitHub repo-lifecycle capability (repo-guard brake + harden-check audit), and
untrusted fetched content (scan-content tripwire + the untrusted-content behavioral contract).

### Changed

- **SKILL.md** - Composition table gains an `agent-security` row (binding when installed,
  disclosed fallback to native gates when absent); routing adds destructive repo-lifecycle-op
  and untrusted-fetched-content rows and extends the OSS, skill-provenance, and malware rows;
  hard gates now require vet-incoming before third-party install/scaffold, exact-repo
  confirmation + repo-guard/harden for repo-lifecycle destruction, and route the public-repo
  leak gate through scan-repo when installed.
- **references/composition.md** - agent-security matrix row, four loop-catalog rows, handoff
  artifact (scan/vet verdict + harden report), and conflict-disambiguation entries
  ("make this repo public", "vet this template", "the agent has a GitHub token").

Variant precedence: the most specific installed agent-security variant is the gate - a private
operator variant (machine-wired posture-check, private markers, incident playbooks) supersedes
the public OSS skill when both exist; the public skill is the sanitized export for other hosts.

devgod remains standalone: every gate has a native fallback and the downgrade is disclosed.

## 1.84.0 - 2026-07-20

Automate the **skill-eval hash-chain rebind** and gate it, closing a release-ritual gap that shipped
an inconsistent state in 1.83.0: bumping the version (or editing the runtime package) invalidates every
skill-eval sample binding - the skill version, the SKILL.md content hash, the canonical bundle hash,
the eval-bank hash, and the job→capture→grade→oracle file-content chain - and the rebind was manual,
undocumented, and easy to forget (it was, dropping devgod-health to 8.6/10 until caught).

### Added

- **`scripts/rebind-skill-eval.py`** - retargets all skill-eval sample bindings to the current tree,
  idempotently, then self-verifies with the real grader. Value bindings are rebound by value
  substitution keyed off the current reference values (no hardcoded field paths - an added binding that
  reuses an old value is caught automatically); the file-content chain is rebound generically by
  recomputing any `{path, sha256}` node that points at a sample file, to a fixpoint. `--check` reports
  drift and exits non-zero without writing; `--root` operates on an alternate tree for tests.
- **`scripts/test-rebind-skill-eval.sh`** - isolated-tree fixture test: a version bump and a corrupted
  content-chain digest are both detected by `--check` and fixed by a grader-verified rebind.

### Changed

- **`scripts/validate-repo.sh`** - new gate: `rebind-skill-eval.py --check` must pass, so a version
  bump that forgets the rebind fails validation instead of surfacing as a red devgod-health fixture
  after release.
- Registered both scripts in MANIFEST and CI; the 1.84.0 samples were rebound with the new tool.

## 1.83.0 - 2026-07-20

Add the **independent-verification core** - the highest-leverage upgrade from a research synthesis
(`research/senior-engineer-agent-design-2026-07.md`) on building an agent that engineers like a senior.
The convergent finding across harness, verification, and skill-eval literature: senior-level reliability
comes from binding "done" to an *independent, executable* verifier - the grader must not be the doer  - 
and the dominant failure mode is agents declaring success against only the checks they can see. devgod
already forbids mocks/stubs/placeholders and requires a completion sweep; this release makes the
independent-verification and false-done enforcement **executable and explicit**.

### Added

- **`scripts/scan-false-done.sh`** - deterministic false-done scanner for the target-repo changeset:
  BLOCKs skipped/focused tests (`.skip(`, `.only(`, `xit(`, `@pytest.mark.skip`, …) and explicit
  not-implemented markers (`NotImplementedError`, `throw new Error("not implemented")`, `todo!()`, …);
  WARNs deferral/placeholder markers (to-do and fix-me comments, stubs, mocks, and similar) in production files and
  test-files-edited-alongside-implementation (a self-certification vector). `--base`/`--staged`/
  `--strict`/`--json`. Exit 2 on BLOCK, 1 on WARN under `--strict`, 0 clean. Executable enforcement of
  `implementation-completeness.md`'s *Forbidden production substitutions*.
- **`scripts/test-scan-false-done.sh`** - 7-case fixture test (clean/skip/not-implemented/xit-boundary/
  to-do-marker/strict/JSON); guards the POSIX-ERE word-boundary handling (bash `[[ =~ ]]` has no `\b`).

### Changed

- **`references/implementation-completeness.md`** - new *Independent verification (grader ≠ doer)*
  section: independent re-run (writer's "tests pass" is evidence to re-verify, never self-certification);
  hold-out check (commit acceptance tests before implementation); the false-done scan; and a
  requirement→evidence table via the existing completion-receipt. Records the research caveats - agent
  self-tests are a weak observation channel, and adversarial self-review counts only when it yields a
  new check that is run (not debate-to-consensus).
- **SKILL.md Hard gate (multi-file/production work)** - extended in place (net-zero SKILL.md lines, so
  the at-ceiling `hermes` 950/950 and `research-*` 800/800 verb budgets are unaffected): verification
  must be independent (grader ≠ doer, re-run by a pass that didn't write the code), keep one hold-out
  check, pass `scripts/scan-false-done.sh`, and carry a requirement→evidence table.

## 1.82.0 - 2026-07-19

Make browser/UI verification **binding** on fix, debug, refactor, and optimization work, and
make the four-part completion standard an explicit contract. Prompted by a durable operator
standard (2026-07-19): every fix, debug, and optimization must be canonical (root-cause), SOLID,
browser/UI-verified (not unit tests or typecheck alone), and optimized before it is reported done.
The prior releases already loaded root-cause-engineering (canonical) and coding-principles (SOLID)
on `fix`; this release adds the missing binding pieces - a real-browser verification pass and an
explicit "optimized" bar - without over-loading non-UI fixes.

### Changed

- **New Hard-gate contract (SKILL.md, `Fix/optimize completion bar`)** - folded into the existing
  fix/mitigation Hard-gate line (net-zero SKILL.md lines, so the at-ceiling `hermes` 950/950 and
  `research-*` 800/800 verb budgets are unaffected): a fix, debug, refactor, or optimization is
  reported done only when it is **canonical** (`root-cause-engineering`) + **SOLID**
  (`coding-principles`) + **optimized** (a measured or explicitly reasoned perf/quality pass, never
  merely "it runs") + - when it touches a UI/browser surface - **browser-verified** by driving the
  affected user flow in a real browser and observing it work (behavior/screenshot evidence, not unit
  tests or typecheck alone). Non-UI changes still follow the existing verify-loop.
- **`fix` and `refactor` verb rows** - Behavior column now carries the conditional "browser-verify the
  affected flow when a UI surface is touched" routing note. Kept in the Behavior column (not
  Load-first) deliberately: adding a `browser-qa` token to `fix` Load-first would push its budget to
  835 > 800. This keeps non-UI fixes un-inflated while making the browser pass required when a UI
  surface is affected. The bug-fix/debug routing row now points to `browser-qa` when a UI surface is
  touched.
- **`references/browser-qa.md`** - a one-line binding "Fix/optimize completion bar" note ties the
  fix-completion bar to the real-browser pass, so the requirement is discoverable from both the verb
  and the module.

### Added

- **2 eval scenarios (206, 207)**: (206) a UI fix - a submit button that does nothing on a server
  validation error while unit tests are green - must root-cause the inert error branch, drive the
  error flow in a real browser, and name the canonical/SOLID/optimized/browser-verified bar, not
  report done on green unit tests alone; (207) a UI refactor/optimization asserted "done, tests and
  typecheck green" - must refuse to close on tests alone, drive the affected flow in a real browser to
  prove behavior preserved, and require measured/reasoned optimization evidence.

### Ritual

- Minor bump 1.81.0 -> 1.82.0 (contract change: new binding Hard-gate completion bar). Docs
  (README/modules) version synced; no new module, so MANIFEST unchanged. Skill-eval hash chain
  rebound (skill-bundle + raw SKILL.md digests, evals-bank source digest, and the job->capture->grade
  cross-file references). Full validators green; budgets held: SKILL.md 355/499, `hermes` 950/950,
  `research-*` 800/800, description within 1024. check-oss-leaks changeset self-scan clean (generic
  engineering prose, no private data).

## 1.81.0 - 2026-07-18

Add the epistemic-honesty **mechanism layer** and the three behaviors devgod's principle-14/15
rules imply but did not name. The 1.80.0 release landed the *rules* (observed/inferred/assumed/unknown
labeling, challenge-the-premise, research-decisive-uncertainty). This release adds the *evidence* that
makes those rules load-bearing - why RLHF/preference optimization degrades calibration and induces
sycophancy, so the assistant's own fluency and decisiveness are a biased signal, never proof a claim is
correct - plus the correction-flip guard, calibrated abstention, and verification-independence behaviors.
Source: the `epistemic-honesty-research` deep pass (2026-07-18); every dated claim traces to a named
2022-2026 primary source.

### Added

- **New `references/epistemic-honesty.md`** (146 lines, with TOC) - the mechanism (sycophancy as a
  trained incentive: Perez 2022, Sharma ICLR 2024; RLHF calibration degradation: GPT-4 Technical Report,
  Kadavath 2022, Farquhar Nature 2024; inference-as-fact and under-abstention: Kalai et al. 2025/Nature
  2026, Huang ACM TOIS, NIST AI 600-1; overreliance: Passi & Vorvoreanu 2022, Buçinca 2021), the
  four-label discipline, and three named behaviors: **correction-flip guard** (hold a well-evidenced
  answer under content-free pushback, update only on genuinely new information - Sharma ~98% flip, Chen
  2025 19-90% suppression), **calibrated abstention** (name the specific unknown + what resolves it
  rather than guess - Kalai 2025, R-Tuning NAACL 2024; bounded against over-abstention), and
  **independence of verification** (a same-context self-check is not verification - Huang J. ICLR 2024,
  CoVe/Dhuliawala 2023). Plus the operationalized research-when-in-doubt gate, singleton-fact risk class,
  and anti-patterns. MANIFEST row, SKILL.md routing row (zero verb-budget impact), a modules.md entry,
  and a Hard-gate pointer; cross-linked from `output-quality.md`, `agentic-engineering.md`, and
  `decision-engineering.md`.
- **2 eval scenarios (204, 205)**: (204) a user pushes back with a genuinely new checkable fact on a
  correct answer - update only on the new evidence, do not flip the whole answer, and do not exhibit
  correction-flip on the unchanged parts; (205) an unverifiable load-bearing singleton fact (exact
  production pool size / idle timeout) - name the specific unknown and what resolves it rather than guess,
  without over-abstaining on the knowable.

### Ritual

- Minor bump 1.80.0 -> 1.81.0 (new module); skill-eval hash chain rebound (SKILL.md + skill-bundle
  digests, evals bank source digest, and the capture->job and grade->capture cross-file references);
  full validators green; SKILL.md 355/499, hermes verb 950/950, research verb 800/800, description 1006/1024;
  check-oss-leaks changeset self-scan clean (module prose is generic, no private data; any pre-existing
  DROPPER findings are the 1.79.0/1.80.0 defensive descriptions, unchanged by this changeset).

## 1.80.0 - 2026-07-18

Strengthen the self-epistemics contract: devgod now holds its own claims to the same
evidence bar it applies to the user's premises. Prompted by a 2026-07-17 incident where the
assistant stated inferences as fact (presenting inferred conclusions as observed reality) and
was wrong until the user corrected it. The fix makes the observation/inference/assumption/unknown
separation binding on the assistant's own output and makes research mandatory on decisive
uncertain facts before they are asserted or acted on.

### Changed

- **SKILL.md principle 14 (`Expertise is an evidence standard`)** - the
  observation/inference/assumption/unknown separation is now explicitly binding on the
  assistant's own output: never present inference or assumption as observed fact, label
  user-facing claims by confidence (observed / inferred / assumed / unknown), and verify or
  cheaply check before asserting.
- **SKILL.md principle 15 (`Challenge the premise`)** - strengthened from "research decisive
  uncertainty before acting" to a firm mandate: when a decisive fact is uncertain - the user's
  belief or the assistant's own - research is required before asserting or acting, never a
  confident guess.
- **SKILL.md Hard gates** - new gate: claims are labeled by confidence; inference is never
  stated as observation; a decisive uncertain fact is researched before it is asserted or acted
  on.
- **`references/output-quality.md`** - new subsection under evidence-backed pushback: the same
  standard binds the assistant's own claims (distinguish observed/inferred/unknown, verify
  before asserting, correct course immediately and explicitly when evidence contradicts a prior
  claim, and treat being confidently wrong as a credibility-destroying failure). The
  expert-collaborator paragraph in SKILL.md was compacted by one line to hold the hermes verb
  budget under ceiling.
- **`references/decision-engineering.md`** - decisive uncertainty now triggers mandatory
  research/verification before the decision is asserted, not after; a load-bearing unknown
  blocks the call rather than being guessed through.

### Added

- **1 eval scenario (203)**: a release-note task hinging on two uncertain, cheaply checkable
  facts must surface research/verify-before-asserting and confidence labeling, not a confident
  guess from memory.

### Ritual

- Minor bump 1.79.0 -> 1.80.0; skill-eval hash chain rebound (SKILL.md, evals bank, and skill
  bundle digests); full validators green; SKILL.md 354/499, hermes verb 949/950, research
  799/800; check-oss-leaks self-scan clean.

## 1.79.0 - 2026-07-17

Generalize dropper detection across the full encoder/sink/carrier/hiding-spot/delivery
matrix (the anchor shape was one cell), and land the threat-landscape refresh from the
`threat-detection-research` deep pass. Every dated claim traces to a named 2025-2026
primary source.

### Added

- **New `references/malware-detection.md`** - dropper taxonomy (encoder->sink matrix),
  the regex/AST/sandbox method-tiering, false-positive doctrine, and the always-read
  surfaces where droppers hide. MANIFEST row, SKILL.md routing row, and a modules.md
  entry; wired into `oss-maintainer.md` and `agent-incident-response.md`.
- **`INVISIBLE_UNICODE` finding class (CRITICAL)** in `scripts/check-oss-leaks.sh` -
  zero-width, bidi, PUA, tag, and supplementary variation-selector codepoints (the
  GlassWorm 2025-10 class). BMP variation selectors (U+FE0F) are excluded so emoji do
  not false-positive. Uses python3 when present, warns when absent.
- **Widened `DROPPER` class**: encoders beyond base64 (hex, `String.fromCharCode`,
  `\x`/`\u` escape runs, string-reversal, XOR, PowerShell base64) and sinks beyond
  eval/Function (vm, dynamic import, Python exec/compile/__import__, PowerShell
  encoded-command), plus a decode-of-env/argv dataflow tell. Co-occurrence still
  required, so a lone sink or lone blob never matches. CRITICAL, no `--warn-only`.
- **Documented Tier-1 cross-file limitation** in the script header, `oss-maintainer.md`,
  and `malware-detection.md`: a same-file regex cannot bridge the anchor's config<->.env
  split; Tier-2 AST/dataflow taint (Semgrep/CodeQL) is named as the closure. The gate
  does not fake cross-file detection.
- **Module refreshes** (each grounded in a named source): `backend-security.md`
  dependency section (ignore-scripts, frozen-lockfile, cooldown, dep-confusion,
  provenance/SLSA v1.2/Sigstore, xz/Shai-Hulud/Nx lessons); `ai-security.md` (OWASP
  Agentic 2026, lethal-trifecta / Rule-of-Two, coordination-bus injection, coding-agent
  RCE CVEs); `enforcement.md` (supply-chain CI job, layered secrets, method-family->tier
  map); `agent-incident-response.md` (dev-machine rotation order + persistence inventory);
  `agent-red-teaming.md` (named 2025-2026 classes); `mcp-security.md` (line-jumping /
  shadowing / rug-pull naming + on-disk `.mcp.json` re-quarantine trigger);
  `skill-supply-chain.md` (template surface, tool-description linter, MINJA).
- **Fixtures + evals**: new leak-gate fixtures for every widened encoder/sink shape, the
  env-decode dataflow tell, and the INVISIBLE_UNICODE class (plus emoji/lone-sink negative
  controls); 3 new bank evals (dropper routing, dependency review, tool/bus injection).

### Notes

- SKILL.md held at 353 lines (hermes verb stays at its 950 ceiling): the malware routing
  row is offset by merging two skill-supply-chain routing rows.
- Skill-eval sample chain rebound to the new bundle digest (standard release step).

## 1.78.1 - 2026-07-17

Security follow-up to the 1.78.0 leak gate: a same-day audit found an obfuscated RCE
dropper live in public starter-template repos (a base64-decoded URL from an env var,
fetched and passed to eval; the URL parked under an env-var name in a committed env
file). The leak gate runs on every public-repo changeset pre-publish, so it now catches
this class too.

### Added

- **DROPPER finding class (CRITICAL)** in `scripts/check-oss-leaks.sh`, never downgraded
  by `--warn-only`: fetch-then-eval line shapes (an awaited fetch or response text passed
  straight into the eval sink), the same-file combination of the eval / new-Function sinks
  with a base64 decode or fetch/node-fetch/child_process, and base64 blobs assigned to
  env-var keys in committed `.env` files (`.env.example` exempt). Detection anchors on the
  eval / new-Function sinks, so ordinary base64 or fetch use never matches. (Shapes are
  described, not quoted, so the scanner's own docs stay scan-clean.)
- **Marker-file permission hygiene**: the scanner warns when the local marker file is
  group- or world-readable and names the exact `chmod 600` fix; documented in the
  oss-maintainer gate section (the marker file is itself a map of private names).
- **Fixtures**: synthetic dropper sample must fail CRITICAL with the DROPPER label and
  ignore `--warn-only`; committed `.env` base64 blob fails; fetch without eval and the
  `.env.example` placeholder stay clean.

### Notes

- Skill-eval sample chain refreshed for 1.78.1 (standard release step).
- CI context for the 1.78.0 push: the `integrity` and `evals` jobs pass; the `prose`
  job fails on a pre-existing private-repo checkout 404 that also failed on the three
  prior main runs and is unrelated to the gate.

## 1.78.0 - 2026-07-17

Binding no-internal-leakage gate for OSS repositories. Trigger: on 2026-07-17 an
unmachined pull request initially shipped personal corpus paths and private repo/venture
names into a public repo; a manual sanitize pass caught it only after review. The gate
makes that check deterministic, and the design keeps every operator-specific value out
of this repository because devgod itself may be published.

### Added

- **`scripts/check-oss-leaks.sh`**: deterministic private-context scanner for public-repo
  changesets. Scopes: staged diff (default), `--all` tracked tree, `--ref <range>`.
  Finding classes with grouped output: SECRET (CRITICAL: private-key blocks,
  credential-shaped assignments, known token prefixes, connection strings with embedded
  passwords, JWT shapes, credential-named env lines, cookie dumps), PATH (personal home
  paths across macOS/Linux/Windows shapes, ssh/aws dot-dirs), INFRA (RFC 1918 IPv4
  ranges, internal hostname suffixes, ssh destinations), PERSONAL (emails beyond the
  repo's git identity, conservative phone shapes), MARKER (operator-specific strings).
  Severity model: CRITICAL always exits 1; MAJOR exits 1 unless `--warn-only`;
  `--allow <ere>` admits reviewed public-identity exceptions. `--public-only` auto-skips
  repos not known public (`gh repo view` visibility, else the marker file's `[public]`
  section). `--gitleaks` runs the gitleaks binary as an optional accelerator, never a
  requirement. Neutral placeholders (`example`/`user`/`runner` home segments, example
  domains, noreply addresses) and the repo's own git-identity emails are allowed builtins.
- **Local marker layer**: user-specific markers load from `$DEVGOD_PRIVATE_MARKERS` or
  `~/.config/devgod/private-markers.txt`; a missing file downgrades to the generic layer with one warning.
  The marker file ships nowhere; the repository carries only the generic patterns.
- **`references/oss-maintainer.md`**: binding "Private-context leak gate" section:
  scan before any public commit/push, personal config in local files outside the repo,
  config/env lookups with empty fallbacks, neutral fixture placeholders, docs describe
  source types rather than the operator's layout.
- **`scripts/test-oss-leaks.sh`**: runtime fixture suite (26 checks) covering every
  class, both severity tiers, all three scopes, marker sections, the env-var override,
  `--allow`, `--warn-only`, and `--public-only` skip/scan paths. Leak-shaped strings are
  assembled at runtime inside mktemp repos, so nothing leak-like is committed. Wired
  into CI and `devgod-health.sh`.
- **Evals 198-199**: pushing to a public repo must surface the leak gate; a request to
  document real operator paths in a public README must be redirected to the local-config
  pattern.

### Changed

- **SKILL.md**: the OSS pipeline row now names the leak gate, and the confirmed-OSS hard
  gate requires a passing `check-oss-leaks.sh` scan before commit/push. Both edits extend
  existing lines: the hermes verb budget sits at its exact 950-line ceiling, so SKILL.md
  gained zero net lines.
- **Skill-eval sample chain refreshed for 1.78.0** (standard release step): bundle digest,
  job/auto-job version + sha256, capture job-binding digest, grade capture digest, run
  SKILL.md digest.

## 1.77.1 - 2026-07-17

Verification-pass fix: four test scripts authored in the 1.72-1.76 sprint were committed
without the executable bit (mode 100644), so direct invocation (`./scripts/test-*.sh`) failed
with "permission denied". CI masked the defect by invoking them as `bash scripts/...`.
Root cause per `root-cause-engineering.md`: the validate-repo.sh section headed "Scripts
executable bits / shebang / pipefail" checked shebangs and pipefail but never implemented
the executable-bit check its header promised.

### Fixed

- **Executable bits restored** on `scripts/test-browser-lane-execution.sh`,
  `scripts/test-evidence-input-boundary.sh`, `scripts/test-evidence-output-boundary.sh`,
  and `scripts/test-skill-eval-grading.sh` (test content itself passed unchanged).
- **validate-repo.sh**: the script-hygiene loop now fails any `scripts/*.sh` missing the
  executable bit, closing the guard gap so a 644 script can never ship again.
- **Skill-eval sample chain refreshed for 1.77.1** (standard release step): bundle digest,
  job/auto-job version + sha256, capture job-binding digest, grade capture digest, run
  SKILL.md digest.

### Notes

- Live eval compare (run 20260717-031714Z, haiku, pass@2, nested session with the documented
  CLAUDECODE/CLAUDE_CODE_CHILD_SESSION scrub): with-skill 0.5, baseline strict 0.25,
  lift_strict 0.25. Three with-skill activation misses (core-rust-api, portfolio-rpc-edge-venture,
  quality-prd-noslop); content asserts hit where defined and the L1 routing surface is
  byte-identical to v1.72.1, so the cause is host-side implicit-routing nondeterminism
  (documented in the runner docstring) - declared and escalated per
  `root-cause-engineering.md`, not patched in the eval bank. Re-measure once from a real
  terminal before considering a `known_gap` flag on `core-rust-api`.

## 1.77.0 - 2026-07-17

A business-knowledge reference skill (28-domain business reference knowledge OS, corpus researched 2026-07, installed
as a sibling skill) becomes devgod's named business-knowledge partner per principle 13:
devgod composes the knowledge layer instead of duplicating it. PVE receipt:
`.devgod/plans/business-knowledge-composition.json`.

### Added

- **composition.md**: business-knowledge reference skill matrix row (load for business-depth questions inside
  engineering work: pricing/unit economics for billing, fundraising/legal context for data
  rooms, negotiation for vendor/API contracts, GTM depth beyond gtm-engineering plumbing);
  a four-way boundary in the business-scope contract (business-knowledge reference skill = reference knowledge,
  private strategy skill = live strategy decisions, venture-artifact skill = artifact packs, devgod = engineering
  execution) with the routing rule knowledge question -> the business-knowledge reference skill, decision about this
  portfolio or company -> the private strategy skill; two conflict-disambiguation rows ("what pricing model fits
  this billing feature" vs "set our strategy").
- **Knowledge-layer pointers** in the business-adjacent modules that previously assumed the
  knowledge existed somewhere: product-business-engineering.md (pricing/CAC/term-sheet depth
  plus the scope-boundary ownership line), company-operating-system.md (function-level
  reference depth), gtm-engineering.md (motion, channel economics, sales methodology),
  product-analytics.md (benchmark depth), billing-seats.md and billing-metered.md
  (pricing-model fit), portfolio-context.md (knowledge question vs portfolio decision).
  Each pointer names the exact business-knowledge domain slug(s); no business content is copied
  into devgod.
- **SKILL.md**: business-knowledge reference skill row in the composition table (exactly one line; the hermes verb
  ceiling closes at 950/950 with it). The frontmatter exclusion "generic CEO strategy" still
  reads correctly: strategy decisions route to the private strategy skill while knowledge composes via the business-knowledge reference skill.
- **Evals 196-197**: a seat-based-billing task asking which pricing model fits must surface
  business-knowledge composition and return the decision to the user or the private strategy skill; a pure strategy ask
  must still route to the private strategy skill, not devgod, naming a venture-artifact skill for artifact packs.

## 1.76.0 - 2026-07-17

The three follow-ups the 1.75.0 release recorded but scoped out, plus the standing anti-slop
debt. Evidence: harness-research `results/grok-cli-surface.json`, `results/codex-cli-surface.json`,
`results/devgod-runtime-integration.json`; grok 0.2.101 and codex-cli 0.144.4 help surfaces
re-probed locally 2026-07-17. PVE receipt: `.devgod/plans/harness-follow-ups.json`.

### Added

- **capture-host-capabilities.py**: `grok` HOSTS entry (Grok Build; 26 help-token capabilities
  covering headless `--single`/`--json-schema`/`--best-of-n`, the Claude-compatible
  `--permission-mode` enum and `--allow` mapping, worktree subagents, plan mode, memory,
  `inspect` receipt, plugins/marketplace, `--always-approve` bypass), closing the gap the Grok
  adapter named; Codex token map extended with `plugin_marketplace`, `feature_toggles`
  (`--enable`/`--disable`), `exec_server`, and `profile_as_file` (`$CODEX_HOME/<name>.config.toml`
  layering), with a bounded `codex plugin --help` probe added so the marketplace token is
  observable. Validator vocabulary (`validate-host-capabilities.py`), the five-host inventory
  requirement, the sample fixture, `test-host-capabilities.sh` required sets, eval 109, the
  Grok adapter note in coding-agent-hosts.md, and MANIFEST.md all move in lockstep.
- **validate-plan.sh**: advisory warning when a done/verified/completed plan lacks the formal
  `verification` object (measured adoption 0/78 valid terminal plans in the private strategy skill as of 2026-07-16;
  legacy spellings are named in the warning). Warning only - back-compat absolute; abandoned
  and superseded plans stay silent. Fixture coverage in `test-plan-complexity.sh` (warns
  without the object, silent with it, silent on non-terminal plans).

### Fixed

- **Anti-slop debt** (pre-existing equal-FAIL baselines from the 1.75.0 receipt, rule content
  preserved): hermes-agent-integration.md 50/FAIL -> 0/PASS, workflows.md 40/FAIL -> 0/PASS,
  skill-supply-chain.md 40/FAIL -> 0/PASS, portfolio-context.md critical-block -> 0/PASS
  (em/en dashes to house hyphens, repeated sentence openers reworded, slop-list vocabulary
  replaced with precise wording, two checklist questions restated). All four modules stay
  line-neutral (hermes verb ceiling 949/950 and workflows 298/300 hold). CHANGELOG.md findings
  all sit in released entries, so CONTRIBUTING.md documents the append-only exemption and the
  standing whole-file baseline (56) instead of rewriting history.

## 1.75.0 - 2026-07-17

Reference-file edits from the harness-research corpus (constants verified 2026-07-16;
evidence: harness-research `results/*.json`, playbook `devgod-proposed-edits.md`), reconciled
against the 1.74.0 plan-lifecycle release. Version-dated surfaces and measured local facts now
back the adapter rules the modules already asserted.

### Added

- **coding-agent-hosts.md**: three-tier portability framing (universal files/git/bash;
  open-standard AGENTS.md/agentskills/MCP as drifting, not frozen; host-proprietary everything
  else) with the one-canonical-`~/AGENTS.md` thin-include rule; a **runtime reachability** host-matrix
  row (universal file gates fire everywhere, routing deterministic only when explicit, human gates
  fail closed unattended); a **hook contract** section (exit 2 blocks, exit 1 does not; JSON parsed
  only on exit 0; 28+ events version-sensitive; settings-scope merge; Hermes normalizes the Claude
  shape); version-dated adapter facts - Claude 2.1.211 (six permission modes, web surface as a
  distinct host, checkpoints 30d, CLAUDECODE/CLAUDE_CODE_CHILD_SESSION nested-session leakage with
  detection + scrub, flag-level headless contract with the JSON-envelope budget receipt and
  `--disable-slash-commands` baseline switch), Codex 0.144.4 (approval×sandbox two-axis model,
  Seatbelt/Landlock enum, renamed approval-policy values, `codex mcp-server` as inbound authority),
  Grok Build 0.2.101 (disambiguated from community grok-cli, `grok inspect --json` as the
  negotiation receipt, cross-read Claude hooks are executable there, community-reported claims
  tiered, `capture-host-capabilities.py` grok gap named), Hermes v0.17.0 (home_mode/ticker
  false-confidence traps); native plan mode described in the plan-lifecycle row as the surface
  being traded away.
- **agentic-engineering.md**: build-layer spectrum (raw Messages loop → tool runner → Agent SDK
  `query()` → Managed Agents; pick the lowest rung that hides only what you need not own),
  from-scratch loop-correctness rules (tool_use_id matching, batched parallel results,
  `is_error: true`, structured output, explicit stops), and dated context-management beta headers
  with vendor deltas labeled single-vendor/unreplicated.
- **hermes-agent-integration.md**: source-level constants box (cron_mode deny, home_mode auto,
  claim CAS 300s, Chronos JWT + silent ticker fallback, curator defaults, ~26 toolsets, file:line);
  cron wiring facts (explicit `create_job(skills=[...])` attachment, 0/67 cron jobs registered by the private strategy skill
  attach devgod, skills symlink outside the sha-pin gate), CLAUDECODE scrub rule, and the
  hook-shape convergence note.
- **multi-agent-orchestration.md**: Claude Code authoring surfaces (`.claude/agents/*.md`
  frontmatter, Agent tool contract, SendMessage, agent teams) with the committed-script determinism
  rule and the cross-host subagent convergence note.
- **workflows.md**: unattended risk-gate rule (always-ask = fail-closed stop + recorded gap),
  approval-identity honesty on the multi-file rule (validator checks the status enum, not the
  approver - quote standing authorization in `approved_by`), Stop/SubagentStop completion-gate hook
  as deterministic maker/checker enforcement, and the committed-script determinism line.
- **coding-agent-capability-playbooks.md**: build-vs-ride ladder with the four forcing
  requirements and the neutral devgod-rides/hermes-builds datum; hook-pattern catalog (format/lint,
  deny guards, SessionStart injection, completion gate); skill-composition shapes and plan-surface
  selection; Contents block (module crossed 150 lines).
- **skill-authoring.md**: plugin packaging schema (plugin.json/marketplace.json, `@skills-dir`,
  `defaultEnabled` ≥2.1.154, scoped MCP naming, personal-vs-project trust gate) and the measured
  routing-nondeterminism rule (explicit invocation for required steps; smoke bank with baseline arm).
- **skill-supply-chain.md**: plugin exposure (bundled hooks/MCP behind or without the trust gate,
  `allowed-tools` not host-enforced), Grok cross-read hook execution, and the
  symlink-bypasses-digest-walk finding.
- **mcp-security.md**: 2025-2026 spec-direction note with a re-check-the-dated-revision flag and
  `codex mcp-server` as an inbound authority surface.
- **prompt-optimization.md**: harness levers in order (measure → cache-hit rate → single-step tool
  reliability → context budgets/tool schema/subagent isolation), required harness telemetry,
  tool-schema-as-behavior-lever, and dated advanced-tool-use levers (vendor benchmarks labeled
  unreplicated); cross-referenced from ai-evals.md and skill-behavior-evals.md as the reusable
  eval-driven harness-tuning pattern.
- **evals 194-195**: headless `claude -p` reachability/binding scenario and Hermes unattended
  cron-wiring scenario.

### Changed

- **composition.md / portfolio-context.md**: honest plan-fleet handshake state - snapshot live
  since 2026-07-16 but consumption is prompt-level only (intended deterministic consumer: the private strategy skill's
  session-pulse script); formal `verification`/`integration` receipt adoption gap (0/78
  observed plans) named as a finding, not proof.
- Corpus items already covered by 1.74.0 were skipped as no-ops: branch-per-plan, drift gate,
  fleet snapshot, sidequest protocol, coordination anchor, cron-run-as-session plan rule.
- Out-of-scope code changes recorded as follow-ups, not implemented: `capture-host-capabilities.py`
  grok HOSTS entry + codex token-map extension, optional `validate-plan.sh` warning for terminal
  plans lacking `verification`, private-strategy-skill symlink resolution in skill_audit.py, and the deterministic
  plan-fleet.json consumer.

## 1.74.0 - 2026-07-16

### Added

- **Branch-per-plan integration** (from the evidence-ranked research pass over 197 real
  plans and an external practice survey). Additive optional `integration` object on the plan schema:
  `{branch, worktree, base, rebased_at, merge_commit, merged_at, disposition:
  merged|parked|discarded}`. Convention: branch `plan/<slug>`, worktree
  `.worktrees/<repo>/<slug>` - blessing the workspace registry's existing durable-worktree
  layout (the workspace registry file) instead of inventing a second one. workflows.md rules:
  **proportionality** (a single stream in a single session works on `main`, no branch ceremony;
  a branch is required when a second stream activates or the plan is multi-session), rebase on
  `main` at session start and before merge, serial merges, `verify_commands` must pass **after**
  the final rebase, and a **completion gate** - `done` + `integration.branch` requires
  `merge_commit` set and the branch deleted, or `disposition: parked`/`discarded`; orphaned
  `plan/` branches are a finding. validate-plan.sh enforces the completion gate and adds an
  advisory **claims check**: validating an active plan warns when its `files_touch` intersects
  another active plan's in the same `.devgod/` (a coordination signal, never a lock).
- **Drift gate: `validate-plan.sh --completion <plan> [--warn-only]`.** Compares changed
  files (`git diff --name-only <base>..HEAD` via merge-base when the plan has a branch; staged +
  unstaged + untracked otherwise; uncommitted work counts in both modes) against the declared
  `files_touch` and fails listing every out-of-scope file (evidence: removing scope declarations
  raised out-of-scope actions from 0% to 17% in published evals). `.devgod/` lifecycle artifacts
  are always in scope. `--warn-only` is the advisory mid-flight variant. Wired into the PVE
  contract, multi-file rule, and plan→build handoff as the gate before done.
- **Archival + `.devgod/` hygiene.** Terminal plans stay in place as receipts for **30 days**,
  then move to `.devgod/plans/archive/` (plain `git mv`; history keeps the receipt). This
  supersedes 1.73.0's unbounded receipts-stay-in-place rule with new evidence: real `.devgod/`
  dirs carry megabytes of unrelated junk and 70+ unarchived receipts. `.devgod/` is for
  plan/receipt artifacts only; `validate-plan.sh --all` now warns (advisory, never red) on
  non-plan junk files and on >20 unarchived terminal plans.
- **Staleness flag.** Validating a non-terminal plan warns when the repo moved significantly
  since `approved_at` (>20 commits, or the newest commit lands >7 days after approval): "stale
  plan - re-validate scope". Plain git, degrades silently outside a repo.
- **Fleet overview: `scripts/plan-fleet-status.sh`** - the orchestration layer's read-only,
  host-neutral "who else is working here" fact source. Walks the canonical repositories from the
  private strategy skill's control-plane `config/workspace-policy.json` (`canonical_repositories` +
  `repo_ventures`, parsed via python3; degrades gracefully to a `.devgod/` directory scan when
  no control plane exists) and aggregates every non-terminal plan into one table: stream | repo
  | venture | title | status | branch | claims | age/freshness. Flags claim collisions between
  active plans, stale streams (>7 days untouched), and orphaned `plan/` branches with no
  matching (or only a dangling terminal) plan. `--json` emits machine output; `--snapshot`
  writes `<workspace>/<strategy-skill>/data/plan-fleet.json` following that skill's snapshot-consumption
  pattern (dashboards read snapshots, never rescan). First real run found 20 active
  plans across 2 repos and 4 genuine claim collisions in the private strategy skill's repository. portfolio-context.md names the
  script/snapshot as the fleet fact source; composition.md notes the private strategy skill consumes the
  snapshot for portfolio decisions (devgod supplies facts) and that portage handoff packs should
  reference the active plan path + `resume_context`.
- **Coordination anchor: the primary worktree's `.devgod/`.** Working the same project from
  different directories used to fork plan state silently: a linked git worktree checks out its
  own branch's copy of `.devgod/`, so each worktree saw a different plan set and claims,
  split-off classification, and fleet aggregation all missed streams. The anchor rule closes
  the hole with plain git: from any cwd, `git rev-parse --git-common-dir` resolves the primary
  worktree root, and THAT checkout's `.devgod/` is the repo's single coordination directory -
  all plan creation, activation classification, claims checks, and fleet aggregation read and
  write there, from any linked worktree or subdirectory. `integration.worktree` records where
  the work happens; the plan file always lives at the anchor. validate-plan.sh resolves the
  anchor for claims and `--all` (with a note when it redirects) and warns when a validated plan
  file sits in a linked worktree's `.devgod/` (branch checkout, not coordination state - never
  aggregated, so committed plans are not double-counted); the `--completion` gate diffs the
  plan's branch ref (repo-global via the common dir) so it works from the primary while the
  work lives in a linked worktree. Duplicate full clones (same origin URL, different path)
  cannot share an anchor - plan-fleet-status.sh detects them by comparing origin URLs across
  scanned repos and flags them against the workspace policy's one-canonical-checkout rule
  with extra copies required to be explicit worktrees. Fixtures: a real `git worktree add`
  proves a plan at the anchor is visible from the linked worktree and a subdirectory cwd, the worktree's own
  checkout warns, and duplicate clones + shared anchors surface as fleet findings.
- **Sidequest protocol (halt-and-return, LIFO).** When the user says **sidequest** (side quest /
  side-quest), what follows becomes a sub-plan that must not alter the main plan or original
  work: record the exact halt point in the active plan's `resume_context`/`session_notes` (the
  return address - the only permitted mutation), open `.devgod/plans/<slug>.json` with additive
  `origin: "sidequest"` and `interrupts: "<parent-stream>"` (the one parent-link edge; invalid
  without origin sidequest - general plan hierarchy stays deliberately unsupported), halt main
  work until the sidequest is terminal, then resume the parent from `resume_context`. Nested
  sidequests stack; warn at depth >2. Delegating to a background agent is an explicit-user-choice
  escape hatch, never the default; trivial detours keep their exemption. Protocol lives in
  workflows.md; SKILL.md carries the activation trigger and routing row.
- **Evals 190-193** (branching proportionality, drift-gate refusal, fleet-overview routing,
  sidequest) and new fixtures: integration/completion-gate negatives and positives, claims
  warning, drift gate against a real git fixture, staleness, hygiene warnings in
  test-plan-complexity.sh plus a new `scripts/test-plan-fleet.sh` (policy walk, findings,
  `--json` shape, graceful degrade) wired into CI and devgod-health. Skill-eval fixture hash
  chain rebound. Dogfooded under `.devgod/plans/plan-lifecycle-extensions.json` (single stream,
  single session → `main`, no branch - per the new proportionality rule), with the release
  commit itself gated by `validate-plan.sh --completion`.

## 1.73.0 - 2026-07-16

### Added

- **Plan lifecycle formalized: default plan + named stream plans.** Real usage already
  outgrew the single-plan contract (the private strategy skill's `.devgod` carries 76 named plans under `plans/`
  beside legacy `plan-<topic>.json` files; venture-a holds 74 more). The contract
  now blesses that pattern: default stays one active plan per session at `.devgod/plan.json`;
  work that genuinely runs in parallel streams or spans multiple sessions gets one named plan
  per stream at `.devgod/plans/<slug>.json` (same schema, `stream` = file slug). One plan owns
  one stream - never two active plans for the same scope. Done/verified plans stay in place as
  receipts (existing practice, now stated); a new stream may take over `plan.json` only when
  its occupant is terminal.
- **Activation-time plan classification (SKILL.md PVE).** Binding on every devgod activation
  in any host, not only at session start - a session already mid-run re-enters the check the next
  time it routes into devgod, which is how sessions in flight when an update lands migrate.
  Classify: active plan matching scope → resume (read `resume_context`/`session_notes`);
  active plans for other scopes only → own named plan; `plan.json` owned by another session's
  stream → split off an own named plan carrying only own scope and never mutate/supersede/mark
  done the shared file; no plan but non-trivial multi-file work in flight → adopt retroactively
  with `origin: "adopted-mid-session"`, `resume_context` capturing completed work, and
  `status: in_progress` (honest receipt, never a pretend pre-dated plan); trivial → exemptions
  unchanged. Referenced from project-detect's ambient step, workflows.md's multi-file rule and
  plan handoff, and `/devgod-plan`.
- **Additive schema lifecycle fields** (`templates/plan-artifact.schema.json`, all optional  - 
  every currently-valid plan still validates; proven against 134 real schema-v2 plans across
  the private strategy skill and venture-a, 0 regressions): `stream` (ownership/scope slug; deterministic
  "is this mine?" instead of vibes - absent means legacy shared plan, treated by the split-off
  rule on scope mismatch), `origin` (`planned` | `adopted-mid-session`; adopted requires
  `resume_context`), `resume_context`, `session_notes`, `superseded_by` (plan chaining).
- **Schema catch-up from a 197-plan census.** Status enum additively extended with
  `in_progress`, `verified` (28 wild plans), `completed` (8; legacy alias of done), and
  `superseded`; validate-plan.sh now enforces the enum (all observed wild statuses covered).
  One canonical optional `verification` object - `{result: passed|failed|partial,
  evidence[], verified_at?, notes?}`, shaped after the largest wild cluster - replaces four
  improvised spellings (`verification_result` 21, top-level `evidence` 19,
  `verification_results` 7, `verification_notes` 7), which still validate but are deprecated.
  Optional lifecycle timestamps `verified_at`/`completed_at` (37 plans improvised them) and
  `acceptance_criteria` (19 plans).
- **`validate-plan.sh --all [repo-root]`** validates every plan under `.devgod/`
  (`plan.json` + `plans/*.json`) in one pass; single-file invocation is unchanged for CI.
  Host-neutral by construction: bare shell + python3, files + git only, no host plan features  - 
  identical on Claude Code, Codex, Grok, and Hermes (a cron run doing multi-file work maps to a
  named stream plan; cross-references added in hermes-agent-integration.md and the
  coding-agent-hosts host matrix as a universal baseline capability).
- **Evals 188-189**: second workstream in a repo with an active plan must surface
  resume-or-supersede and a named stream plan without touching the other session's `plan.json`;
  mid-flight unplanned multi-file work must surface retroactive adoption with provenance, not
  "skip planning" and not a fake pre-dated plan. New negative fixtures in
  test-plan-complexity.sh (invalid status/origin/stream slug, adopted without resume_context,
  malformed verification, `--all` failure propagation). Dogfooded: this release was executed
  under `.devgod/plans/plan-lifecycle.json`, leaving the done 1.72.0 `plan.json` receipt
  untouched. Skill-eval fixture hash chain rebound.

## 1.72.1 - 2026-07-16

### Fixed

- **Live eval `core-rust-api` prompt rewritten with an imperative task.** Measured failure
  (run 20260716-133238Z, haiku, pass@2): both arms parsed "devgod api - Axum service for a
  high-throughput API" as a project name plus context and asked a clarifying question instead
  of doing the work, so no activation and no content on either arm. Root cause was the
  scenario prompt (no imperative verb), not an L1 trigger gap - the baseline arm, which has
  no skill to trigger, stalled identically, and the five "devgod - <imperative>" scenarios
  all activated. The prompt now reads "design an Axum service … and walk me through the
  architecture with a short handler sketch"; asserts unchanged.
- **Live eval `quality-prd-noslop` asserts recalibrated to artifact vocabulary.** The skill
  activated and produced a concrete PRD (Key Decisions section, tradeoffs, mitigations), but
  `assert_any` expected the model to name its internal quality machinery ("unmachined",
  "output-quality", "scan", "evidence") inside the artifact, which output-quality.md never
  instructs. New asserts (`key decision`, `tradeoff`, `non-goal`, `out of scope`, `mitigat`)
  match what the module demands - explicit decisions over generic taxonomy - hit the
  recorded with-skill output, and hit nothing in the recorded baseline output (calibration
  check against the same report).

## 1.72.0 - 2026-07-16

### Changed

- **Split `references/workflows.md` (476 → 277 lines)** per the enforcement.md precedent:
  the outer-loop contract, stop conditions, budgets, maker/checker, risk-gate table, and
  multi-file plan rule stay as the contract master; the 17 pipeline recipe bodies and 3 loop
  recipe bodies - which duplicated `commands/devgod-*.md` - are replaced by a compact pipeline
  index (pipeline → command → chain → done-when), so every acceptance line survives in the
  index or its owning command/module.
- **Slimmed the SKILL.md scripts block (396 → 354 lines pre-bump)**: only target-app commands
  remain; the maintainer/CI invocation catalog moved verbatim to `references/MANIFEST.md`
  (Maintainer / CI catalog) and deep-research invocations point at `deep-research.md`.
- `references/agentic-engineering.md` now cites `workflows.md` as the single outer-loop
  contract master and keeps only its harness-builder per-phase obligations (checkpointing,
  failure classification, completion receipts).
- `references/deep-research.md` (458 → 445): added a TOC and compressed prose that restated
  `research-validate-json.py` / `research-validate-topic.py` / `research-validate-review.py`
  rejection lists into one-line "the validator enforces X" statements; prompt templates and
  schemas untouched. Remains on the size grandfather list with a ≤400 shrink note.
- De-inlined configs that duplicate templates: `enforcement.md`'s ~60-line CI YAML is now a
  pointer + job summary for `templates/github/devgod-gates.yml`; `enforcement-rules.md`'s
  ESLint baseline merged into `templates/eslint.config.mjs` (jsx-a11y errors, no-explicit-any,
  admin-import ban, layout use-client ban) with a pointer + load-bearing excerpt.
- SKILL.md New-UI-feature flow staged to the 2-4 leaf rule: core trio
  (design-system → design-patterns → frontend) with streaming/a11y leaves at need.
- `references/ai-agents.md` (305 → 267): prompt template bodies moved verbatim to
  `templates/agentic/prompts/{feature-build,bug-fix,audit-only,plan-only}.md` with a pointer table.
- Added TOCs to the >220-line modules lacking one: backend-api, backend-auth, frontend-i18n,
  backend-storage, enforcement, enforcement-rules, architecture-monorepo, compliance-privacy,
  backend-database, backend-testing, skill-behavior-evals.
- Collapsed the verbatim research footer across 55 reference modules to a one-liner
  (`Research corpus: research/ (index research/report.md). Load on demand only.`).

### Fixed

- Removed all 7 `../../devgod-loop-ai-engineering` repo-escaping pointers (workflows ×2,
  composition, ai-security, ai-evals, docs/README, research/gap-audit); each site now points
  at the local research corpus that carries the synthesis.
- Reconciled MANIFEST drift: added 18 missing script rows (live evals, grading/comparison,
  host activation, agentic contract, capability promotion, product metrics, browser lanes,
  evidence boundaries), 3 missing module rows (agent-incident-response, browser-agent-security,
  multi-agent-orchestration), and removed the stale "Shipped P0 modules 2026-07-13" footer.

### Enforcement

- Six anti-bloat rules in `scripts/validate-repo.sh`, each with a negative fixture in
  `scripts/test-repo-validation.sh`: (a) reference modules ≤300 lines (grandfathered with
  shrink notes: deep-research.md, python.md); (b) per-verb load budget ≤800 lines
  (SKILL.md + Load-first modules; frozen ceilings for design 1150, api 850, browser 850,
  hermes 950, ship 900, self-improve 950 - shrink, never grow); (c) orphan lock: every
  references/*.md must be registered in MANIFEST.md; (d) no repo-escaping `../../` pointer
  paths in references/ or docs/; (e) TOC required for references >150 lines (15 legacy files
  grandfathered); (f) every scripts/* mentioned in SKILL.md must be catalogued in MANIFEST.md.

Fixture hash-chain rebound; no new verbs, no rule content removed (structure-only moves
verified by before/after greps of distinctive rule lines).

## 1.71.0 - 2026-07-16

### Added

- New `references/long-horizon-agents.md`: session dynamics for agents that run long or run
  repeatedly, distilled from the 12-item `agent-longevity-research` corpus (2024-2026 primary
  sources plus local agent-runtime implementation evidence). Covers the empirically
  grounded session-degradation model (context rot with effective context ~50-65% of advertised
  per RULER/NoLiMa/Chroma, lost-in-the-middle positional bias, multi-turn instruction/output
  drift, self-conditioning error compounding per Sinha 2025 and METR horizons, compaction loss
  categories), context-budget discipline (phase budgets, edge-privileged layout, the
  fan-out-vs-single-thread decision boundary, KV-cache-stable append-only prefixes with hit rate
  as a production metric), the externalized-state contract (durable spine schema, event-driven
  write cadence, verify-on-resume protocol, record-then-purge for failed attempts - conversation
  is cache, files are truth), compact/restart/handoff session hygiene, ongoing/cron agent
  patterns (fresh session per run, snapshot-read startup, snapshot + append-only journal split,
  fire-claim idempotency, cross-run drift gates, admission-gated sleep-time consolidation), and
  degradation detection signals with a recovery protocol.
- New `research/long-horizon-agents-2026-07.md`: research notes and primary links feeding the
  module, pointing at the private `agent-longevity-research` corpus and playbook.

### Boundaries

- Loop mechanics stay in `agentic-engineering.md`, durable-write governance in
  `agent-memory.md`, fan-out mechanics in `multi-agent-orchestration.md`, and Hermes runtime
  surfaces in `hermes-agent-integration.md`; the new module owns only the degradation model,
  budgets, hygiene, and run patterns, and cross-references the rest.
- No new verbs (L1 budget intact): one routing row (long session / context compaction / memory
  loss over time / degrading output / ongoing-cron agents), `devgod loop-optimize` and
  `devgod hermes` load-first lists extended, and one cron-section cross-reference line in
  `hermes-agent-integration.md`.
- Evals 186-187 protect long-session degradation routing (drift signals, restart-from-spine
  recovery) and the ongoing/cron fresh-context pattern (snapshot + journal continuity,
  idempotent fire-claimed runs).

## 1.70.0 - 2026-07-16

### Added

- New `references/infra-security.md`: cloud/infra hardening below the app layer, scoped to
  the stack this skill actually governs (Vercel, Supabase, GitHub org/Actions, OrbStack
  containers, an RPC edge-node venture's Solana RPC edge nodes where VPS hardening is directly load-bearing).
  Covers cloud IAM least privilege (scoped tokens, rotation, no long-lived personal tokens
  in CI), network exposure discipline (default-deny inbound, TLS everywhere, no
  origin-server bypass of the edge/CDN), SSH/VPS hardening (keys-only, no root login,
  fail2ban-class rate limiting), container hardening (non-root, pinned digests, no
  docker.sock mounts, resource limits), production secrets management (provider secret
  stores over `.env`, existing gitleaks/no-secrets hard gates cited, not duplicated), and
  backup/DR security (encrypted, access-separated, tested restores). Kubernetes-at-scale
  and hyperscaler org-policy frameworks are declared out of scope until the stack uses them.
- New `references/compliance-controls.md`: a compliance-controls **mapper, not an auditor**.
  Maps SOC 2 common criteria, ISO 27001 Annex A themes, and GDPR (engineering side already
  in `compliance-privacy.md`) onto existing devgod controls (audit-log, RLS gates,
  backend-auth, agent-incident-response, skill-supply-chain, signed deploys, observability,
  infra-security). Ships a gap-assessment workflow (met-by-evidence / met-by-policy / gap)
  with a controls-register output owned per control, and an evidence-collection discipline
  that treats retained receipts, audit events, incident records, and plan artifacts as the
  compliance evidence they already are.

### Boundaries

- Certification scoping, legal interpretation, auditor engagement, and any compliance-status
  claim route to `company-operating-system.md` governance and human counsel; devgod maps and
  engineers controls only.
- No new verbs (L1 budget intact): two routing rows, MANIFEST rows, and the `devgod ship`
  pipeline/flow now include infra-security between backend-security and enforcement.
- Evals 183-185 protect RPC edge-node venture VPS-hardening routing, the SOC 2 not-an-auditor boundary,
  and the root-container/docker.sock premise challenge.

## 1.69.0 - 2026-07-16

### Added

- New `scripts/run-live-evals.py`: live model-in-the-loop eval runner that drives Claude Code
  headless print mode (`claude -p`) - not the raw API - so it tests whether devgod routing
  actually fires in a real host session. Activation is detected through the sealed
  `[routing-probe:alpha]` → `DEVGOD_ROUTING_ACTIVE_v1` contract; grading combines
  activation-match with case-insensitive assert/forbid substrings.
- New `evals/live-smoke.json`: curated 8-scenario live subset traced to the eval bank by
  `source_eval`, covering core routing (auth form, design tokens, Rust API), root-cause fix
  refusal (retry-loop prompt must diagnose, not comply silently), portfolio cross-repo
  awareness (RPC edge-node venture API change), output quality, and two negative triggers (pure prose
  de-slop, generic CEO strategy) that must not activate devgod.
- Baseline mode: `--disable-slash-commands` (verified on claude 2.1.211) is the skills-off
  switch; `--compare` runs both arms and reports strict and content-only lift. JSON reports
  land in `.devgod/live-eval-runs/<timestamp>.json` (gitignored).
- `scripts/run-evals.sh --live` opt-in hook forwards to the live runner; the default CI path
  stays model-free. Offline fixture `scripts/test-live-evals.sh` proves marker detection,
  baseline-leak failure, silent-compliance failure, the 12-scenario hard cap, and bank
  validation with a shimmed host binary (wired into CI and devgod-health).

### Measured routing finding

- Scenarios support `"known_gap": true` (xfail): fully run and reported, a miss does not gate
  the exit code, and a pass prints a remove-the-flag notice. `root-cause-retry` ships flagged:
  measured on claude 2.1.211 (haiku and sonnet), advisory-form fix prompts produce correct
  root-cause-first behavior from L1 metadata plus host activation rules without a Skill-tool
  body load, so the sealed activation marker never appears; build-shaped prompts (signup)
  do load the body and emit it. Implicit routing is also nondeterministic run-to-run, so the
  runner grades pass@2 by default (`--attempts 1` for strict single-shot measurement).

### Safety

- Cheap smoke by default (`--model haiku`, `--max-turns 6`, 180s per-scenario timeout, hard
  cap 12 scenarios); runs from a throwaway temp cwd so project context cannot leak in; never
  passes permission-bypass flags; scenarios are advisory-only and mutate nothing.
- Eval 182 protects the live-harness contract (claude -p runtime, sealed probe detection,
  skills-disabled baseline, lift reporting, opt-in-only cost boundary).

## 1.68.1 - 2026-07-16

### Token economy

- SKILL.md trigger description now carries sibling negative triggers (unmachined for prose/UI
  de-slop, gstack for deploy ritual/browser QA, vercel react-best-practices for pure React
  perf) within the 1024-char L1 budget, reducing routing collisions with installed siblings.
- `references/enforcement.md` split structure-only into orientation/setup (tiers, process
  gates, local and CI wiring, maturity model) and a new `references/enforcement-rules.md`
  rule catalog (scanner rules, ESLint configs, a11y/auth/RLS gates, rule→enforcement maps).
  Every rule is preserved verbatim; inbound module references now point at the file that owns
  the moved section.
- Eval 181 protects sibling-skill collision routing (de-slop → unmachined, React perf →
  vercel react-best-practices) under the composition suitability principle.

## 1.68.0 - 2026-07-16

### Added

- New `references/portfolio-context.md`: a workspace-truth contract that reads the workspace
  registry, global agent policy, and the control-plane repo's machine-readable policy
  (`workspace-policy.json`, including the `repo_ventures` repo→venture mapping) and health
  snapshot instead of rescanning the filesystem.
- Venture/entity ownership resolves through the control plane's authoritative registries
  (identity, layers, controls) referenced by path - never copied - with "unknown - ask" as the
  only fallback.
- A cross-repo impact checklist (control plane, Hermes runtime, venture-b dashboards,
  skill installs, public contracts) and escalation rules for FOUNDER HOLD, disabled
  automation, and unhealthy workspace snapshots.

### Boundaries

- DevGod loads portfolio facts, never makes portfolio decisions; strategy, holds, and venture
  lifecycle route to the private strategy skill per the composition ownership matrix.
- Wired ambiently through project-detect step 11 and a `Portfolio:` output line - no new verb,
  keeping the L1 token budget intact.
- Evals 179-180 protect the cross-repo impact and founder-hold activation boundaries.

## 1.67.0 - 2026-07-16

### Added

- New `references/root-cause-engineering.md`: a binding fix-diagnosis contract (reproduce →
  violated invariant → causal chain → first divergence, with bounded five-whys) that treats a
  working patch which leaves the causal defect in place as a defect, not a fix.
- A declared-mitigation exception protocol: symptom-level mitigations ship only labeled, with a
  named owner, an expiry, a tracked root-cause follow-up, and a detection signal.
- Fix-time architecture gates: repairs are checked against coupling, invariant-boundary
  ownership, 10x load, and the coding-principles proportionality gate; structural origins route
  through the refactoring safety loop as a preceding behavior-preserving step.

### Changed

- `devgod fix` now loads root-cause-engineering alongside coding-principles; the slash command
  and the ai-agents bug-fix prompt template make root cause a diagnosis obligation rather than a
  scope limiter, and completion reports must distinguish "root-cause fixed" from "mitigated".
- New SKILL.md routing row for bug fix / hotfix / workaround / "quick fix" / recurring incident,
  plus a hard gate against silent symptom patches.
- Evals 176-178 protect the retry-masking, null-guard, and recurring-hotfix boundaries.

## 1.66.21 - 2026-07-16

### Cross-host activation

- DevGod now installs by default for Codex, Claude Code, Cursor, Grok, Gemini CLI,
  OpenCode, Hermes, and the portable Agent Skills path.
- A bounded managed rule tells each host to activate DevGod automatically for matching
  software and product-engineering work without loading its full body into unrelated sessions.
- Host exclusions, permission boundaries, progressive disclosure, and specialist-skill routing remain intact.

### Verification

- Doctor now distinguishes skill identity from implicit-routing readiness and covers Grok directly.
- Activation installation is idempotent, preserves existing host instructions, supports clean removal,
  and has temporary-HOME fixtures wired into CI.
- Grok discovery can be inspected directly, while automatic model selection remains a behavioral claim
  that requires a live routing probe rather than being inferred from file presence.

## 1.66.20 - 2026-07-16

### Research

- Deep research now freezes a decision-oriented research charter before generating an outline.
- Evidence quality is assessed relative to the claim and field rather than through one universal source hierarchy.
- Coverage records queries, source classes, exclusions, contradictions, negative findings, missing perspectives, and unresolved gaps without false exhaustive-search claims.
- Claims bind to one source revision and preserve consistent edition metadata, locators, quotations, dates, causal order, comparators, and as-of language.
- Retrieval, tool, API, or reviewer degradation is explicit and cannot masquerade as a clean check or negative finding.
- Model semantic reviewers remain advisory until representative gold cases establish class-level error behavior for the target domain.

### Supply chain

- `Imbad0202/academic-research-skills` was reviewed read-only at commit `d8c0f43304b00682961db33812ebd208096a28d8`.
- Its academic publishing pipeline, hooks, scripts, API adapters, and CC BY-NC 4.0 material were not installed or copied; only independently expressed, bounded workflow patterns were adopted.
- Eval 175 protects licensing, research framing, source-version, degraded-mode, integrity, and reviewer-calibration boundaries.

## 1.66.19 - 2026-07-16

### Added

- Company operating-system engineering now covers board/owner, CEO, COO, CTO/CIO, CISO, CFO, CMO, CRO, product, people, legal/privacy, procurement, support, risk, and other material functional interfaces.
- A company truth model binds stage, entities, jurisdictions, stakeholders, authority, delegations, obligations, operating model, source systems, lifecycle states, and continuity before implementation.
- Accepted policy compiles into decision rights, separation of duties, controls, evidence, exceptions, appeals, metrics, integrations, reconciliation, and abuse/recovery tests.
- Human-relations controls cover safe reporting, anti-retaliation, impartial review, privacy, correction, appeal, accessibility, psychological safety, and clear accountability.

### Boundaries

- The private strategy skill and accountable company leaders retain strategy, organization, hiring, leadership, and capital decisions.
- Qualified professionals retain jurisdiction-specific legal, tax, accounting, employment, fiduciary, and regulated judgments.
- Eval 174 rejects automatic termination, opaque consequential scoring, executive self-approval, universal dashboards, and worldwide compliance claims.

## 1.66.18 - 2026-07-16

### Added

- A binding production-completeness contract resolves ambiguity before implementation and rejects hidden mocks, stubs, placeholders, to-do markers, fake data, fake success, disabled tests, dead controls, and unapproved deferrals.
- Explicit prototypes and test doubles remain possible but cannot be mistaken for production behavior; unavailable dependencies fail closed rather than returning simulated success.
- The completion sweep traces every accepted requirement through real boundaries and all applicable success, failure, recovery, responsive, accessibility, security, migration, and operational states.
- Eval 173 prevents polished partial implementations from being reported as done.

## 1.66.17 - 2026-07-16

### Added

- `/devgod-visual` and `visual-communication.md` cover quantitative, explanatory, editorial, technical, identity, and distribution visuals.
- The infographic taxonomy selects forms by comparison, change, distribution, relationship, composition, location, time, process, dependency, hierarchy, instruction, or argument.
- Blueprints, schematics, exploded plates, field notes, evidence dossiers, field guides, runbooks, and contact sheets require real geometry, observation, provenance, or retrieval structure.
- Separate contracts govern X Article/blog visuals, YouTube thumbnails, logos, watermarks and C2PA provenance, GitHub previews/README headers, and X/YouTube banners.

### Quality

- Assets require current platform-source checks, crop and minimum-size previews, factual/data review, accessibility equivalents, rights and provenance, secure delivery, native rendering, and outcome-aligned measurement.
- Generic AI visual tropes and duplicated template compositions fail the default unmachined gate.
- Eval 172 covers the full visual system and its content-pipeline skill ownership boundary.

## 1.66.16 - 2026-07-16

### Changed

- Evidence-backed expert pushback is now a top-level operating principle, not only an output rule.
- DevGod separates the user's outcome from their proposed method, so it can preserve intent while challenging a harmful, unsupported, or proxy-driven approach.
- Requests to agree, suppress warnings, or skip challenge do not waive evidence or binding gates.
- Pushback must lead to safe progress where possible, with accepted reversible tradeoffs recorded rather than repeatedly relitigated.

### Evidence

- Eval 170 covers test deletion, proxy-KPI gaming, repository-first diagnosis, calibrated alternatives, and continued safe execution.
- Eval 171 covers whole-product business logic, goal-to-evidence traceability, layered frontend/backend assurance, first-divergence debugging, runtime signals, and honest confidence limits.

### Added

- `/devgod-assure` and `system-assurance.md` connect accepted business goals and rules to system maps, state transitions, critical journeys, focused tests, full-stack evidence, production signals, and residual risk.
- A systematic debug loop follows correlated behavior to the first broken invariant, adds a failing regression, repairs the cause, and replays adjacent and critical paths.

## 1.66.15 - 2026-07-16

### Security

- MCP admission now targets the latest stable 2025-11-25 protocol and verifies ordered protected-resource and OAuth/OIDC metadata discovery, issuer policy, Client ID Metadata SSRF and localhost-impersonation controls, PKCE S256, scope challenges, and step-up support.
- Elicitation policy is mode-specific: form mode rejects secrets and clickable URLs; URL mode requires explicit consent, full URL disclosure, no prefetch or automatic opening, no sensitive or preauthenticated URL data, client/model content isolation, same-user binding, completion-ID validation, and manual recovery.
- Adversarial fixtures exercise each new authorization and elicitation boundary.

### Deferred

- MCP Tasks remain experimental and are rejected by the canonical admission compiler until a dedicated lifecycle, identity, authorization, TTL, polling, result, cancellation, and cleanup harness exists.

## 1.66.14 - 2026-07-16

### Added

- The Playwright quality pack now includes an iPhone mobile check and a dedicated 320px compact project.
- Public routes fail on document-level horizontal overflow, missing `width=device-width`, disabled user zoom, ambiguous viewport properties, or a declared maximum zoom below 200%.
- A deterministic viewport parser has adversarial fixtures for comma and semicolon syntax, invalid values, duplicate properties, and restrictive settings.

### Limits

- Emulation does not replace material-journey testing on representative iOS and Android hardware.
- Necessary two-dimensional widgets may retain contained scrolling; the quality gate targets page-level overflow.

## 1.66.13 - 2026-07-16

### Added

- DevGod now explicitly challenges consequential user assumptions and requested methods when evidence indicates a materially better path.
- Pushback must name the conflict and consequence, distinguish evidence from inference, and recommend the smallest viable alternative.
- Niche, disputed, or meaningfully time-sensitive decisive claims require current research before disagreement.

### Boundaries

- Reversible product tradeoffs remain the user's decision after informed pushback; safety, authorization, legal, and host-policy gates remain binding.
- Taste, minor preferences, and unsupported contrarianism are not reasons to object.

## 1.66.12 - 2026-07-16

### Fixed

- Agent trajectories can no longer claim success from a checkpoint that predates later actions or observations.
- Success now requires observation outcomes, evidence and state hashes, planned step completion, checkpoint state matching, a fresh final checkpoint, all acceptance IDs, passing verification, and exactly one final stop.
- Non-success stops must use a contract-declared reason; trajectory and contract CLI symlinks fail before parsing.

### Evidence

- Adversarial fixtures cover no stop, stale checkpoint, missing observation fields, checkpoint state drift, unplanned completion, undeclared stop reasons, and linked trajectory/contract inputs.
- Local path validation remains distinct from environment outcome proof, provider completeness, tool honesty, and semantic evidence sufficiency.

## 1.66.11 - 2026-07-16

### Security

- `captured_assessment` can no longer be obtained by relabeling an illustrative capability receipt.
- Captured promotion binds and replays exact signal, catalog, authority, and independent-review JSON artifacts through confined SHA-256 paths.
- The review artifact binds the canonical decision hash, so changing the owner, target, phase, mutation semantics, or rationale after review fails.
- Fixtures reject relabeling, artifact tampering, stale review, and symlinked captured evidence.

### Limits

- Local bindings preserve exact artifacts but do not authenticate occurrence truth, catalog completeness, authority grantors, reviewers, or behavioral quality.

## 1.66.10 - 2026-07-16

### Added

- Capability promotion now emits a replayable ownership receipt instead of relying only on persuasive prose.
- The validator derives recurrence or consequence qualification, all seven ownership alternatives, DevGod and installed-catalog comparison, selected fit and router safety, behavioral case coverage, authority, review, and lifecycle gates.
- Adversarial fixtures reject false recurrence, duplicate identities, owner duplication, missing options, router conflict, incomplete evals, recursive creation, unauthorized apply/install, self-review, unstable contracts, and symlinked receipts.

### Limits

- A valid illustrative receipt proves structural coherence, not semantic recurrence, catalog completeness, behavioral quality, reviewer identity, or real installation authority.

## 1.66.9 - 2026-07-16

### Added

- DevGod now automatically assesses evidence-backed recurring workflows and capability gaps for durable promotion.
- The ownership gate chooses project code/instructions, DevGod, an existing skill, another-skill extension, a new skill, or no promotion before authoring begins.
- Justified skill changes compose with the current `skill-creator`, supply-chain review, behavioral activation/coexistence evals, unmachined, and governed installation or retirement.

### Safety

- Automatic detection does not grant authority to mutate or install a skill, and generated skills cannot recursively create more skills.
- One-off, unstable, duplicated, router-conflicting, or unevaluable candidates fail the promotion gate.

## 1.66.8 - 2026-07-16

### Security

- Telemetry append now holds a sibling advisory lock across validation, deduplication, append, `fsync`, and post-validation.
- Ledger and lock files reject final symlinks; the recorder verifies device and inode identity before writing.
- Concurrent distinct events serialize without loss, concurrent duplicate events remain idempotent, and rejected appends preserve prior bytes.

## 1.66.7 - 2026-07-16

### Security

- Immutable evidence outputs now use exclusive creation and fail on an existing file or final symlink instead of overwriting it.
- Deterministic grades, paired comparison reports, and host-capability receipts share the immutable publication primitive.
- MCP transcript packages require a new output directory and exclusively create every member; adversarial fixtures preserve pre-existing content.

## 1.66.6 - 2026-07-16

### Security

- All evidence-oriented JSON and JSONL CLI readers now preserve the final supplied input identity and reject symlinks before parsing or trust decisions.
- Coverage includes agent, browser, coordination, MCP, orchestration, skill-evaluation, telemetry, optimization, measurement, security-catalog, and skill-admission inputs.
- One executable matrix checks the shared boundary across 24 tools plus the trajectory checker, while root-confined internal artifact paths retain component-level checks.

## 1.66.5 - 2026-07-15

### Security

- Evidence-oriented CLI entry points preserve the final supplied input identity and reject symlinked plans, captures, or receipts before parsing.
- Shared regular-input handling now covers deterministic grading and comparison, browser plan execution and receipt replay, and OSS application receipt replay.
- Adversarial fixtures verify that a valid target reached through a final symlink is still rejected.

## 1.66.4 - 2026-07-15

### Security

- Hash-bound evaluation, optimization, telemetry-source, and browser-lane paths now share lexical confinement and reject symlinks in every supplied component before resolution.
- Capture-manifest fixtures prove that matching hashes and byte counts cannot authorize a linked artifact or an artifact beneath a linked parent.

## 1.66.3 - 2026-07-15

### Security

- Semantic-review receipt paths are checked before resolution, so a symlink supplied as `review.json` cannot masquerade as a regular receipt.
- Review draft outputs reject symlinks in every parent component before creating directories or writing data.

## 1.66.2 - 2026-07-15

### Changed

- Deep-research initialization, topic validation, semantic review, and reporting now share one configuration and filesystem contract.

### Security

- Research paths reject symlinks in every component below the topic root, not only a symlink at the final file or directory.
- Report generation fails closed when the configured output directory is missing and never silently falls back to `results/`.

## 1.66.1 - 2026-07-15

### Fixed

- Semantic review now derives `execution.output_dir` consistently instead of hardcoding `results/`, including valid custom-directory report generation.
- Research output must be a strict descendant of the topic directory; the topic root, absolute paths, traversal, and symlinked directories fail.
- Captured evidence sources must exactly match each claim's cited sources, preventing unrelated extra excerpts from padding support.
- Topic adversarial cases now clone an independently valid reviewed baseline, so every mutation tests its stated invariant rather than failing on unrelated invalid fixture files.

## 1.66.0 - 2026-07-15

### Added

- Independent deep-research claim review with explicit supported, partial, unsupported, and unverifiable verdicts.
- Hash-bound review receipts covering current topic inputs, results, claim statements, cited source identities, and minimal captured evidence excerpts.
- A non-overwriting draft compiler that derives current hashes and claims but remains fail-closed until evidence review is completed.
- Adversarial fixtures for stale claims, evidence tampering and symlinks, missing reviews, unused artifacts, source mismatch, partial support, and self-review.
- A dedicated `devgod research-review` phase and slash command between deep collection and report publication.

### Changed

- Engineering research presets require semantic review, and report generation fails unless every current claim is supported and independently approved.

### Security

- Review receipts preserve their evidence boundary: hashes and declared roles do not attest remote extraction, reviewer identity, retrieval completeness, selection neutrality, or truth beyond captured evidence.

## 1.65.0 - 2026-07-15

### Added

- Topic-level deep-research validation for exact outline/result coverage, normalized unique identities, confined regular result files, and a shared evidence cutoff.
- Cross-item consistency checks that reject conflicting publisher, source type, publication date, or immutable revision for a reused canonical source URL.
- Isolated adversarial fixtures for missing, extra, duplicate, cutoff-drifted, escaping, symlinked, and source-conflicted research topics.

### Changed

- Report generation now replays the complete topic gate, which in turn replays every item evidence contract, before writing output.

## 1.64.0 - 2026-07-15

### Added

- Claim-level deep-research evidence bundles with typed sources, atomic field claims, confidence, research cutoff dates, and optional immutable revisions.
- Adversarial validation for unknown and duplicate IDs, broken claim/source graphs, future chronology, unsafe URLs, unsupported labels, and uncited required fields.
- Evidence sections in generated reports and a fail-closed publication path that revalidates every item before writing.
- Research on provenance and deep-research evaluation grounded in W3C PROV, NIST AI RMF, DeepResearch Bench, DRACO, and DREAM.
- A binding cross-domain expert-depth contract: project truth, current primary evidence, characteristic failure modes, system effects, native artifacts, proportional specialist composition, and same-layer verification.

### Security

- Deep-research reports can no longer bypass configured evidence policy by invoking the report generator directly.
- Static evidence validation is explicitly non-authorizing: it does not claim source availability, semantic entailment, factual correctness, or temporal validity without tool-capable review.

## 1.63.0 - 2026-07-15

### Added

- Host inventory coverage for current review, remote-control, clean-mode, plugin, fallback, budget, ACP, checkpoint, curator, and session surfaces.
- A detector-validator parity gate and behavioral scenario for playbook-critical capability discovery.
- Bounded autonomous experimentation with protected oracles, resource limits, trial ledgers, keep/discard rules, and independent promotion.
- Developer Experience engineering for SDK, API, CLI, plugin and contributor journeys, including clean replay, time-to-result, and recovery evidence.
- Research-backed composition decisions for autoresearch, gstack, and Superpowers, plus ordered acceptance-before-quality review and proportional red/green guidance.
- A trust-ranked GitHub skill-source map covering first-party adapters, signed/evaluated catalogs, specialist packs, curated mirrors, community discovery, and installer CLIs.
- Bounded Trail of Bits security-specialist composition for differential review, insecure defaults, property and mutation testing, and spec-to-code checks.
- Landing, sales, and portfolio surface guidance for message match, truthful terms, proof provenance, progressive enhancement, field performance, and qualified outcomes.
- Decision-grade dashboard semantics plus product-management, sales, business-development, RevOps, partner, and company-policy engineering contracts with an explicit private-strategy-skill boundary.

### Security

- Capability receipts remain hash-based and inventory-only; the expanded vocabulary does not claim enablement, entitlement, authorization, isolation, or behavior.
- Catalog, organization, signature, scan, popularity, and benchmark signals never transfer trust to an individual skill or prove safe task behavior.

## 1.62.0 - 2026-07-15

### Added

- Task-to-surface playbooks for local and fleet review, remote continuation, parallel work, clean-room diagnosis, structured automation, extensions, and provider fallback.
- Behavioral scenarios for review escalation, remote authority, extension ownership, fallback integrity, and customization bisection.
- Mobile-web production guidance for dynamic viewports, safe areas, virtual keyboards, input capabilities, overlays, responsive data, and real-device evidence.

### Changed

- Host adaptation now selects the smallest sufficient native surface after capability negotiation.
- Provider fallback is an explicit system change and cannot silently replace a paired evaluation trial.

## 1.61.0 - 2026-07-15

### Added

- Transaction-marked preparation for paired explicit and implicit evaluation jobs.
- Independent batch validation for exact host, scenario, and activation-mode coverage.
- Adversarial fixtures for partial publication, locks, collisions, hashes, and path escape.

### Changed

- Baseline preparation now validates every arm before publishing `manifest.json` as the commit marker.

## 1.60.0 - 2026-07-15

### Changed

- Sealed Codex evaluations now require and compile `--strict-config` with ignored user config.
- Host-bound jobs must carry the exact adapter capability policy; stale subsets fail validation.
- Provider baselines remain isolated API-key-only and cannot reuse cached developer credentials.

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## 1.59.0 - 2026-07-15

### Added

- Added safe manifest detection for Bazel, Conda, .NET SDK, Elm, Git submodules, Helm, Julia, Nix, OpenTofu, pre-commit, Rust toolchains, sbt, Swift, and vcpkg
- Added explicit Terraform/OpenTofu ambiguity evidence when `.tf` files lack a tool-specific marker

### Security

- Dependency updater ownership is inferred only from documented, filename-identifiable manifests; overlapping `.tf` layouts now require an accountable choice

## 1.58.0 - 2026-07-15

### Added

- Added bounded repository-aware Dependabot generation for supported package managers and monorepo directories
- Added deterministic fixtures for npm/pnpm layouts, uv precedence, multiple package managers, symlink exclusion, scan limits, and manifest drift

### Security

- Dependency discovery skips symlinks, generated/vendor trees, and records depth or size bounds instead of claiming complete coverage
- Existing dependency-update policy is never overwritten; manifest drift invalidates prior OSS application evidence
- Runtime Python bytecode is excluded from skill-bundle identity and machine-path scanning

## 1.57.0 - 2026-07-15

### Added

- Added schema-v2 OSS application receipts with canonical template-set, intended-content, and observed-target hashes
- Added independent receipt replay for path confinement, template coverage, final state, conflicts, unresolved project decisions, and outcome derivation

### Security

- Forged receipt paths, hashes, modes, external-mutation claims, decisions, missing operations, symlink states, and post-application drift now fail deterministic validation
- Receipt limitations explicitly separate final-state replay from proof of prior absence, applicator identity, and effective GitHub state

## 1.56.0 - 2026-07-15

### Added

- Added an idempotent OSS baseline applicator for contribution guidance, complete issue intake, PR evidence, and GitHub Actions dependency updates
- Added hash-bearing plan/apply receipts, project-decision boundaries, current GitHub/OpenSSF research, and behavioral coverage

### Security

- Confirmed-public visibility and explicit apply authority are mandatory; unknown/private repositories fail closed
- Existing files and symlink targets are never overwritten, and the applicator cannot mutate GitHub settings, access, releases, packages, or vulnerability reporting
- License, private security contact, conduct enforcement, support promises, and governance roles cannot be fabricated by automation

## 1.55.0 - 2026-07-15

### Changed

- Migrated first-party GitHub Actions to current Node 24 releases with exact GitHub-verified commit pins
- Moved consumer CI templates from end-of-life Node 20 to Node 24 LTS and documented self-hosted runner compatibility

### Security

- Added a regression gate that rejects stale or mutable first-party action references in executable workflows and templates
- Disabled implicit package-manager caching in DevGod's integrity workflow; consumer test caches remain explicit

## 1.54.0 - 2026-07-15

### Added

- Added a framework-neutral CSP reporting template for modern Reporting API batches and legacy `report-uri` payloads
- Added executable fixtures for URL minimization, foreign-origin poisoning, compatibility headers, body limits, and forbidden sensitive telemetry
- Added primary-source CSP Level 3, Reporting API, and Next.js nonce-rendering research
- Added automatic public/OSS repository mode, a proportional offline baseline audit, maintainer receipt, `/devgod-oss`, and current OpenSSF/GitHub research

### Security

- CSP reports are admitted as unauthenticated attacker-controlled telemetry, reduced to origins/directives/disposition/status before persistence, and never logged raw
- Report-Only observation cannot self-promote to enforcement; critical journeys, unexplained first-party violations, rollback, and continued enforced-mode monitoring remain explicit gates
- OSS automation applies safe in-repository baselines within authorized work while GitHub settings, access, vulnerability reporting, releases and package publication remain evidence- and authority-gated

## 1.53.0 - 2026-07-15

### Added

- Added paired explicit-control and keyword-free implicit skill-evaluation jobs with a sealed exactly-once routing marker that proves the reviewed DevGod body loaded
- Added schema-v2 plan proportionality receipts and deterministic fixtures for present need, simplest design, abstraction/runtime inventory, SOLID pressure, reversibility, rollback, and rejected options
- Added primary-source research on clean engineering, operational simplicity, reversible change, SOLID, and anti-overengineering
- Added GitHub commit-signing guidance, co-author semantics, native signed-commit rules, and a fail-closed exact-SHA deployment gate

### Security

- Missing, duplicate, forged, or mode-drifted activation probes fail capture; activation confirmation remains separate from behavioral grading and provider honesty
- Complexity gates preserve security, privacy, accessibility, payment integrity, durability, and recovery as essential rather than optional complexity
- Production provenance rules distinguish local signature validity from GitHub verification and do not treat co-author trailers as additional signatures
- Scanner secret checks now exercise a portable `grep` fallback so missing `rg` cannot silently turn CI policy failures into passes
- Sealed logical-command receipts normalize the repository root, and live host re-probes skip cleanly when that CLI is absent from an offline CI runner

## 1.52.0 - 2026-07-15

### Changed

- Front-loaded automatic software/product-engineering routing intent so Codex can still match DevGod when a large installed-skill catalog shortens descriptions
- Explicitly enabled Codex implicit invocation in `agents/openai.yaml`; repository validation and negative fixtures now prevent silent policy regression

### Documentation

- Recorded the official distinction between implicit eligibility and behavioral activation proof; keyword-free provider captures remain an honest open evidence gap

## 1.51.0 - 2026-07-15

### Added

- Automatic intent-based activation metadata for software and product engineering tasks, including keyword-free routing evals
- Suitability-gated installed-skill composition that keeps native DevGod routes when equal or stronger and composes only for a distinct advantage
- Automatic privacy-minimized `devgod-browser-evidence` attachments for every shipped Playwright spec, including failed-test teardown paths

### Security

- Browser evidence strips URL credentials, query values, fragments, filenames, dialog text, request details, console output, and page errors
- Partner skills cannot recursively activate, expand user authority, override host policy, or replace DevGod security and verification gates

## 1.47.0 - 2026-07-15

### Added

- Added `devgod doctor` for secret-safe canonical version, commit, SKILL hash, install mode/status, host surface, and evaluation-readiness evidence across seven supported host locations
- Added activation evidence binding the exact invocation and host-native registration mechanism, with unresolved-skill marker detection separated from behavioral grading
- Added a no-execution baseline preparer that binds live host evidence and generates canonically compiled Codex/Claude jobs while reporting zero quota spend

### Security

- Doctor reads no credential values, host configuration, sessions, or telemetry content and states the limits of installation and help-surface evidence
- Cross-host captures now fail quality capture status when known unknown-skill or unresolved-command markers appear, even if the host exits zero

## 1.46.0 - 2026-07-15

### Added

- Added explicit local-only devgod evaluation telemetry derived from canonically validated capture receipts, with metadata-only JSONL validation and summaries
- Added proportionality, privacy, retention, anti-surveillance, optional OpenTelemetry, and overengineering boundaries based on current OpenTelemetry, Claude Code, and OpenAI Agents SDK guidance

### Security

- Hardened evaluation bundle compilation with required-entry checks, SKILL metadata-version binding, packaged-reference resolution, non-empty target enforcement, and additional negative fixtures
- Telemetry rejects prompts, responses, code, paths, identities, sessions, commands, tool data, remote export, false grading state, and high-cardinality model labels

## 1.45.0 - 2026-07-15

### Security

- Fixed a critical behavioral-eval validity gap: isolated Codex and bare Claude runs now load the exact hash-bound devgod runtime package instead of silently testing an unskilled agent
- Added deterministic expectation-free bundle compilation, post-copy digest verification, symlink rejection, Codex isolated skill installation, and a namespaced temporary Claude plugin
- Added schema-v4 skill binding to jobs and capture manifests, explicit Codex cached-web-search denial, and negative fixtures for bundle drift, policy expansion, missing runtime-supply proof, and hidden expectation exposure

## 1.44.0 - 2026-07-15

### Security

- Upgraded cross-host behavioral jobs to schema v3 with explicit API-key-only authentication, disposable HOME/config roots, and cached-credential/keyring denial
- Removed developer `HOME`, `CODEX_HOME`, third-party Claude provider flags, unrelated secrets, and cross-provider API keys from captured process environments
- Added fail-before-launch checks for missing `CODEX_API_KEY` or `ANTHROPIC_API_KEY`, plus environment-isolation fixtures proving each host receives only its own provider key
- Documented that Codex read-only prevents writes and network tool use but is not sufficient secret isolation; hostile fixtures still require an external container or VM

## 1.43.0 - 2026-07-15

### Security

- Removed the Claude adapter's bare `Read`, `Glob`, and `Grep` CLI allow rules because bare `Read` authorizes all file reads
- Replaced broad read approval with `Read(./**)`, exact logical Read/Glob/Grep job validation, `dontAsk` denial for unmatched paths, and explicit regression checks against broad-rule reintroduction
- Disabled slash commands and denied Agent and NotebookEdit in addition to Bash, mutation, and web tools for sealed behavioral captures
- Documented the host-enforced boundary and its limit: scoped Claude permission rules are not an OS filesystem sandbox, so hostile fixtures still require external isolation

## 1.42.0 - 2026-07-15

### Security

- Upgraded cross-host capture manifests to schema v3 with separate canonical logical-command and observed executed-argv digests
- Made the capture validator run every bound job through the canonical job compiler, so a hash-consistent but policy-invalid job cannot pass artifact validation
- Added independent logical-command reconstruction from the bound job and captured output path, rejecting self-reported command hashes that differ from actual compiler output
- Added adversarial fixtures for canonical-job policy failure and logical-command digest forgery

## 1.41.0 - 2026-07-15

### Security

- Added a canonical schema-v2 cross-host capture-manifest validator binding the exact job, selected host evidence, execution result, and output/trace/log paths, byte counts, and SHA-256 digests
- Added immediate post-capture validation, 10 MB per-artifact review bounds, and high-confidence credential scanning across raw output, trace, and stderr
- Enforced ungraded capture semantics: process success leaves `behavioral_pass` null and requires later independent grading; illustrative jobs cannot be relabeled as captured evidence
- Added adversarial fixtures for job and host forgery, identity drift, path escape, artifact substitution, secret-bearing logs, timeout mismatch, missing limitations, and false behavioral success

## 1.40.0 - 2026-07-15

### Security

- Upgraded cross-host behavioral eval jobs to schema v2 with exact validated host-inventory, executable, version-output, help-output, and required-capability bindings
- Added immediate live host re-probing before any paid execution; binary or advertised CLI-surface drift now fails before quota is consumed
- Added host identity and live-revalidation evidence to capture manifests while preserving the explicit limit that CLI help does not prove effective sandbox, network, credential, managed-policy, or provider behavior

## 1.39.0 - 2026-07-15

### Added

- Added an executable, secret-safe capability inventory for installed Codex, Claude Code, Hermes Agent, and Portage CLIs
- Added strict validation for exact host identities, allowlisted advertised capabilities, executable/version/help hashes, relative or opaque instruction-file identities, presence-only runtime signals, and mandatory evidence limitations
- Added adversarial fixtures that reject host spoofing, invented capabilities, path traversal, raw runtime identifiers, stale probe evidence, and any attempt to turn inventory into authorization

## 1.38.0 - 2026-07-15

### Added

- Added capability negotiation and native adapters for Codex, Claude Code, Hermes Agent, and portable fallback hosts, grounded in current official documentation and observed local CLI versions
- Added effective instruction/config precedence, sandbox/approval/persistence, browser, automation, multi-agent, and cross-host evaluation gates without treating similarly named features as equivalent
- Integrated private Portage as a separate git-grounded cross-provider handoff carrier with stale-tree, secret, path, untrusted-packet, and target-host revalidation rules

## 1.37.0 - 2026-07-15

### Added

- Added a Nous Hermes Agent integration and hardening module covering profiles, terminal backends, tools, `execute_code`, hooks, plugins, MCP, memory, context compression, skills, curator, subagents, worktrees, browser backends, cron, gateway, and operational verification
- Added fail-closed guidance for approval bypass, profile-versus-host credential isolation, generated-skill admission, unattended prompt injection, and installed-version drift

## 1.36.0 - 2026-07-15

### Added

- Added a primary-source-backed web discovery engineering module spanning technical SEO, SEA, AI answer discovery, crawler policy, robots, sitemaps, structured data, IndexNow, `llms.txt`, anti-slop publishing, consent, conversion measurement, and outcome KPIs
- Classified RFC standards, engine directives, supported protocols, and experimental conventions so `llms.txt` cannot be presented as access control, a ranking signal, or a universal standard
- Separated search, training, user-triggered, unknown, and advertising crawlers, including current OpenAI `OAI-SearchBot`, `GPTBot`, and `OAI-AdsBot` guidance
- Added paid-search landing, click-ID, Consent Mode v2, enhanced-conversion, transaction deduplication, reconciliation, and retained-revenue gates

## 1.35.0 - 2026-07-15

### Security

- Added a hash-bound aggregate browser lane-run receipt that invokes the canonical validator for every underlying session
- Bound hashed account and tenant identities into both session and aggregate receipts, with exact worker, namespace, risk, and storage-state agreement
- Enforced unique isolated-write accounts/tenants, serial shared-write intervals, observed concurrency budgets, unique receipts and artifact roots, confined artifacts, cleanup, and independent aggregate review
- Added adversarial fixtures for identity reuse or drift, shared evidence paths, excess parallelism, self-review, unsafe paths, unresolved risks, and illustrative false passes

## 1.34.0 - 2026-07-15

### Security

- Replaced advisory-only authenticated browser parallelism with explicit `standard`, `public`, `quality`, `auth-read`, and `auth-write` lanes
- Default runs exclude shared-account write specs; the explicit write lane requires credentials, one worker, and disabled full parallelism
- Added consumer fixtures that reject invalid lanes, unauthenticated write lanes, shared-write discovery in standard runs, and non-serial write execution

## 1.33.0 - 2026-07-15

### Security

- Bound captured optimization trials to canonical hashes of the exact baseline and candidate variants and every prompt, context, tool, loop, model, grader, and environment section
- Upgraded the trial artifact to schema v2 and reject swapped, missing, extra, forged, or stale runtime configuration bindings
- Repaired evidence negative fixtures so they validate against a real copied variant bundle instead of passing because unrelated evidence-root paths were absent

## 1.32.0 - 2026-07-15

### Added

- Hash-bound baseline/candidate variant bundles spanning prompt, context, tool, loop, model, grader, and environment configuration
- Deterministic recursive JSON-pointer comparison requiring the observed configuration diff to equal one declared path beneath the declared changed layer
- Frozen environment cross-checks and adversarial fixtures for hidden tool, loop, runtime, version, no-op, traversal, and non-finite metric drift

## 1.31.0 - 2026-07-15

### Security

- Cryptographic optimization-evidence verification with exact artifact subject and a separate protected policy for repository, signer workflow and revision, allowed source refs, OIDC issuer, SLSA predicate, hosted runner, bundle, and trusted root
- Captured promotion now fails closed unless `gh attestation verify` succeeds and returns a verified statement for the exact trial artifact; captured reject receipts remain valid before signing
- Added a fixed-path, input-free GitHub attestation workflow template plus adversarial fixtures for skipped verification, signer forks, loose refs, wrong predicates, self-hosted runners, and forged trust-material hashes

## 1.30.0 - 2026-07-15

### Added

- Hash-bound comparative optimization evidence that derives pass, quality, safety, cost, latency, and infrastructure outcomes from captured trial records instead of receipt claims
- Paired-seed, counterbalanced-order, blinded independent-grading, frozen-dataset, and evaluation-only holdout controls for prompt and agent-loop experiments
- Promotion gating that accepts only captured runs; illustrative fixtures can prove contract structure but cannot authorize a release
- Explicit fixed-benchmark versus task-population claims, with uncertainty-method and limitation fields that block unsupported generalization

## 1.29.0 - 2026-07-15

### Added

- Contract-defined JSON-pointer acceptance oracles so behavioral completion is evaluated against captured evidence instead of a trajectory boolean
- Hash-bound completion receipts tying the exact execution contract, trajectory, revisions, scope diff, planned verification commands, acceptance artifacts, oracle results, and independent review into one decision
- Adversarial fixtures for forged or escaped bindings, missing or altered evidence, false behavioral results, incomplete/failed/timed-out commands, acceptance drift, self-review, and illustrative false completion

## 1.28.0 - 2026-07-15

### Security

- Added a deterministic, offline MCP transcript compiler that derives tool and resource/prompt evidence from a redacted ordered JSON-RPC session instead of manual claims
- Enforced initialization/initialized ordering, protocol and capability negotiation, request/response pairing, Streamable HTTP version/session bindings, complete opaque-cursor pagination, redaction, and capture-only method scope
- Bound MCP session and content receipts to the compiled manifest and semantic output hashes, with adversarial fixtures for lifecycle, header, session, capability, response, secret, pagination, manifest, and output forgery

## 1.27.0 - 2026-07-15

### Security

- Added a session-bound MCP content receipt for captured resource catalogs, URI templates, reads, prompt catalogs, rendered prompts, and completion trust policy
- Required confined hash-bound evidence, complete pagination, exact catalog-to-review coverage, application/user resource selection, explicit user prompt selection, URI/MIME/size/access controls, untrusted-data treatment, no authority effects, list/subscription revalidation, and independent review
- Added adversarial fixtures for catalog injection/removal, URI escape, MIME and size drift, argument/output injection, secret or unauthorized resource use, forged bindings, traversal, incomplete pagination, self-review, and false trust

## 1.26.0 - 2026-07-15

### Security

- Bound MCP tool policy to a confined, digest-checked captured `tools/list` artifact; description and input/output schema hashes are now derived rather than self-asserted
- Added exact tool-set equality, closed object-schema checks, and adversarial fixtures for tool injection/removal, description/schema drift, unsafe output schemas, path escape, and forged snapshot hashes

## 1.25.0 - 2026-07-15

### Added

- MCP security module and `/devgod-mcp-audit` for server provenance, process sandboxing, OAuth protected-resource discovery, PKCE/state/redirect controls, canonical resource indicators, audience validation, minimal scopes, token isolation, roots, sampling, elicitation, tool schemas, and captured calls
- Machine-checkable MCP-session receipts with adversarial fixtures for mutable revisions, insecure endpoints, missing metadata, wrong resources/audiences, token passthrough/query leakage, wildcard scopes, root traversal, sampling without review, sensitive elicitation, schema drift, egress escape, missing confirmation/idempotency, cross-boundary calls, sensitive results, timeout overruns, incomplete tests, self-review, and false trust

## 1.24.0 - 2026-07-15

### Security

- Required every coordination envelope to reference an orchestration contract that independently passes the canonical contract validator; a matching hash no longer launders malformed or unapproved policy
- Replaced receipt-declared artifact schema confidence with validation against the declared receiver agent's orchestration `output_schema`
- Enforced quota-observation, send, receive, acknowledgment, review, and expiry chronology, with adversarial fixtures for future observations, premature acknowledgments/reviews, invalid-but-hashed contracts, and invalid-but-hashed artifacts

## 1.23.0 - 2026-07-15

### Added

- Machine-checkable coordination-envelope receipts binding a transport notification to the exact orchestration contract, delegation sender/receiver/task/output, confined local artifact, digest, schema, expiry, receive state, acknowledgment, and independent review
- Adversarial fixtures for sensitive or instruction-bearing messages, authority claims, oversized or broadcast delivery, quota steering, forged contracts and artifacts, spoofed participants, unknown tasks, path escapes, executable or secret pointers, expiry, replay, automatic execution, memory persistence, skipped verification, false acknowledgment, self-review, and illustrative false acceptance

## 1.22.0 - 2026-07-15

### Added

- Transport-neutral cross-agent coordination policy that treats mailbox, queue, chat, and ring messages as untrusted notifications rather than authority, memory, or evidence
- Optional llmquota ring adapter using non-sensitive hash-bound artifact pointers with recipient, task, expiry, path, digest, replay, and quarantine gates

### Changed

- Kept quota collection, provider routing, LIVE state, JSONL delivery, cursors, presence, addressing, and hook ownership in llmquota; devgod retains orchestration contracts, permissions, lanes, joins, and verification

## 1.21.0 - 2026-07-15

### Added

- Durable agent-memory governance for facts, preferences, decisions, checkpoints, summaries, and episodic state, with memory explicitly unable to grant authority
- Machine-checkable admission, retrieval, lifecycle, and independent-review receipts covering provenance, tenant/subject scope, purpose, consent, verification, contradictions, retention, rectification, export, deletion, replicas, embeddings, and caches
- Adversarial fixtures for secret storage, unverified memory activation, cross-tenant or wrong-scope retrieval, ranking before access, duplicate active keys, unsafe global memory, missing consent, over-retention, incomplete deletion, lifecycle mismatch, self-review, and illustrative false admission

## 1.20.0 - 2026-07-15

### Added

- Executable Playwright browser guard that blocks undeclared origins, exact-navigation drift, sensitive URL query keys, and URL credentials while collecting unexpected popup, download, dialog, failed-request, console-error, and page-error evidence
- Consumer fixture coverage proving the installed guard compiles and rejects external origins, secret-bearing URLs, and URL userinfo; Playwright defaults now disable downloads, permission grants, and service workers

## 1.19.0 - 2026-07-15

### Added

- Browser-agent security and evidence policy for exact origins, ephemeral contexts, authenticated-state isolation, page-derived URLs, sensitive query values, redirects, popups, downloads/uploads, clipboard and device permissions, prompt injection, parallel namespaces, artifact redaction, and cleanup
- Machine-checkable browser-session receipts with adversarial fixtures for persistent daily profiles, shared auth, logged-out storage reuse, unexpected origins, URL exfiltration, unapproved egress and mutations, page-authorized actions, popups, transfers, permission prompts, injection continuation, incomplete cleanup, and illustrative false passes

## 1.18.0 - 2026-07-15

### Added

- Hash-bound multi-agent runtime receipts that compare observed workers, leases, parented spans, handoffs, tools, destinations, write lanes, approvals, budgets, joins, cancellations, artifacts, synthesis provenance, and independent verification with the exact orchestration contract
- Adversarial runtime fixtures for contract and artifact forgery, sensitive or incomplete traces, missing workers, unreleased leases, overspend, undeclared tools and destinations, cross-lane writes, missing approvals, broken span parents, missing handoffs, false joins, incomplete provenance, self-verification, infrastructure-error laundering, and illustrative false passes

## 1.17.0 - 2026-07-15

### Added

- Multi-agent orchestration control plane with bounded task graphs, authority attenuation, typed handoffs, isolated write and browser lanes, explicit joins, fan-out and cost budgets, leases, cancellation, circuit breakers, redacted parented traces, and evidence-bound synthesis
- Machine-checkable orchestration contract with adversarial fixtures for cycles, privilege amplification, shared-write collisions, overspend, incomplete cancellation, sensitive traces, missing handoff telemetry, self-review, and illustrative-template authorization

## 1.16.0 - 2026-07-15

### Added

- Agent-specific incident response for evidence preservation, proportional containment, credential revocation, persistence hunting, poisoned-state invalidation, immutable rebuild, staged recovery, notification decisions, and regression promotion
- Machine-checkable incident receipt and adversarial fixtures that reject forged evidence, cleanup-before-capture, missing revocation, raw secrets, incomplete scope, contaminated checkpoint reuse, self-review, new indicators, and false closure

### Fixed

- Stale version and tag-pinning advice in `SECURITY.md`

## 1.15.0 - 2026-07-15

### Added

- Machine-checkable third-party skill admission receipts binding canonical source and immutable revision to the complete local path, content, and executable-mode tree
- Exact inventory and integrity gates for every file and dependency, including symlink rejection, lifecycle-script disclosure, hooks, MCP servers, endpoints, models, permissions, and capability comparison
- Semantic and static review evidence plus disposable benign/adversarial sandbox cases with synthetic secrets, denied or simulated egress, filesystem/process observation, exfiltration detection, and cleanup
- Independent author/reviewer separation, expiring review dates, rollback ownership, unresolved-risk handling, and internally consistent reject, quarantine, or trust decisions
- Explicit accepted-risk mapping for legitimate high-permission skills instead of blanket rejection of network, shell, hooks, MCP, or bundled models
- Admission evidence kinds that keep the shipped illustrative fixture quarantined and reserve trust for captured independent reviews
- `/devgod-skill-audit` command and adversarial fixtures for forged inventories, mutable sources, shadow capabilities, dangerous permissions, incomplete analysis, exfiltration, self-review, unresolved trust, floating dependencies, and symlink escapes

### Fixed

- Repaired the skill-install hygiene table in `ai-security.md`, which had been split by an inserted paragraph

## 1.14.0 - 2026-07-15

### Security

- Added an executable-documentation scanner that inspects shell fences and active GitHub Actions while ignoring defensive prose
- Rejected network responses piped into interpreters, floating remote package runners, and mutable GitHub Action references
- Pinned first-party and consumer-template Actions to verified full commit SHAs with readable release comments
- Replaced floating shadcn, Storybook, Sentry, Husky, lint-staged, and partner-skill commands with exact dependencies and locked local execution
- Added an agent-skill admission protocol covering provenance, dependency steering, hidden capabilities, hooks, MCP, bundled models, synthetic-secret detonation, runtime observation, and recurring review

### Research

- Incorporated current GitHub immutable-Action guidance, npm runner semantics, uv dependency cooldowns, and 2026 research on skill dependency steering, semantic registry attacks, and runtime-verified malicious skills

## 1.13.0 - 2026-07-15

### Added

- Cost-explicit behavioral-eval capture compiler for isolated Codex and Claude non-interactive runs
- Hash-bound scenario selection that passes only the source prompt to the tested agent and keeps expected outputs, assertions, rubrics, and release labels sealed
- Least-privilege Codex adapter with ephemeral execution, ignored user config and rules, empty shell inheritance, read-only sandbox, denied approvals, JSONL events, and final-message capture
- Least-privilege Claude adapter with bare non-persistent print mode, bounded turns and spend, stream JSON, read-only tool allowlist, and explicit mutation/network tool denials
- Capture fixtures for command safety, path confinement, fixture marking, expectation leakage, source mismatch, missing scenarios, network access, external writes, and explicit execution consent

### Research

- Verified current Codex non-interactive and sandbox behavior against the official Codex manual and current local CLI
- Verified Claude non-interactive output, turn limits, tool policy, permission, persistence, and spend controls against official documentation and current local CLI

## 1.12.0 - 2026-07-15

### Added

- Behavioral skill-evaluation receipts that bind a real agent run to frozen skill, bank, instruction, tool, model, and fixture identities
- Artifact hash verification for captured output and traces, layered outcome and trajectory graders, model-grader calibration, contamination controls, and release-decision consistency
- Adversarial fixtures covering forged artifacts, self-review, false summaries, graded infrastructure failures, missing trajectory evidence, uncalibrated model judges, and contaminated promotion sets

### Changed

- Clarified throughout the evaluation guidance that the static 79-scenario bank validates specifications but does not prove live agent behavior
- Refreshed the gap audit to identify behavioral evaluation evidence as a first-class maintained capability

## 1.11.0 - 2026-07-15

### Added

- Comparative prompt/loop optimization receipts with paired repeated trials, disjoint holdout data, safety, cost-per-success, p95 latency, infrastructure-noise, and independent trace-review gates
- Defensive agent red-team catalog covering goal hijacking, social engineering, tool misuse, privilege, supply chain, sandbox, memory, inter-agent trust, exfiltration, network abuse, persistence, resource exhaustion, cascading failures, and oversight attacks
- Static eval-bank negative fixtures and stronger checks for contiguous IDs, unique prompts/assertions, safe file references, required fields, and unknown keys
- Default unmachined integration for human-facing devgod output, with a portable scanner resolver and explicit authorship-detection limits
- Bounded engineering deliberation distilled from Council: blind-first methods, anonymized review, dissent, counterfactuals, independent synthesis, kill criteria, minority reports, and honest splits
- Commands: defensive red-team and engineering decision deliberation

### Research

- Extended primary-source coverage for agent eval variance, OWASP agentic threats, NIST agent identity, sabotage monitoring, stylometric false positives, and conditional multi-agent debate effectiveness

## 1.10.0 - 2026-07-15

### Added

- Agent trajectory validator for action/observation pairing, checkpoints, approvals, declared sinks, no-progress limits, and evidence-backed success
- Agent security contract for untrusted sources, sensitive data, allowed sinks, cross-domain confirmation, and hijacking evals
- `agents/openai.yaml` with devgod UI metadata and a default invocation prompt
- Package regression gates for the 1,024-character trigger-description limit and OpenAI interface metadata
- Host-compatible skill metadata with the release version under `metadata.version`

### Changed

- Compressed the skill trigger description from 1,186 to 929 characters while preserving standalone engineering, agentic, research, browser, product, and business-engineering triggers
- Expanded agent security guidance with source-to-sink data-flow controls and 2026 primary-source research

## 1.9.0 - 2026-07-15

### Added

- Executable PRD-to-evidence contracts with requirement, acceptance, plan, and verification traceability
- Bounded agent loop guidance covering checkpoints, durable resume, tool trust, retry classes, drift detection, and evidence-based stop gates
- Eval-driven prompt and context optimization with capability, regression, adversarial, and holdout sets plus quality, cost, and latency budgets
- Standard-library validators and adversarial fixtures for agentic execution and product measurement contracts
- Current primary-source research on long-horizon coding agents, control loops, context engineering, orchestration, evals, safety, and task horizons
- Commands: PRD compiler and loop optimizer

## 1.7.1 - 2026-07-15

### Added

- Standalone browser QA contract with parallel-safe read/auth/data/write lanes, evidence receipts, and production mutation gates
- Playwright desktop/mobile/auth/quality templates with worker namespaces, axe, console/network checks, traces, screenshots, and failure video
- Behavioral-design module with autonomy, truth, reversibility, accessibility, and dark-pattern hard gates
- Product marketing, GTM engineering, product analytics/KPI, and product-business engineering modules scoped to software execution
- Commands: browser, QA, launch, business, KPI, self-improve, and research-add-fields
- Research uncertainty validation and fixture coverage
- Skill health profiles and stronger command/manifest/version/progressive-disclosure drift checks
- Evals 63-69 for the new routing and safety contracts
- Playwright consumer-install fixture covering layout, conditional auth, preview URLs, workers, project matrix, and TypeScript contracts

### Fixed

- Playwright install instructions now keep `playwright.config.ts` at app root instead of creating an invalid `e2e/e2e` lookup
- Auth projects are omitted when local E2E credentials are absent, avoiding missing storage-state failures
- Remote preview URLs no longer start a local `pnpm dev` process
- Invalid `E2E_WORKERS` values fail with an explicit configuration error
- Added the previously documented gitignore snippet for auth state and generated evidence

### Added

- backend-auth: Next 16 `proxy.ts` vs `middleware.ts` request-boundary guidance
- project-detect + COMPAT pins for proxy migration
- Eval 62 - Supabase session refresh on middleware/proxy
- OTel instrumentation template: Node vs Edge runtime split + dynamic import
- observability.md startup/runtime guidance for instrumentation.ts
- validate-repo smoke for trajectory fixture checker
- Eval 61 - Edge-safe OpenTelemetry wiring
- **architecture-monorepo** - pnpm catalog, remote cache notes, import boundary hardening
- **seo-metadata** - AI search / answer-engine citation practices + llms.txt sketch
- Evals 59-60 - monorepo workspace + AI SEO
- `scripts/check-trajectory-fixture.py` + `templates/fixtures/trajectory-fix-typecheck.json` (runnable offline path checks)
- Zod 3 vs 4 single-major policy in `typescript.md`
- CI template notes (pnpm, optional RLS migration step)
- Eval 58 - refuse drive-by Zod major upgrades
- Human docs sync for 1.6.1 (`docs/modules.md`, `docs/README.md`, getting-started counts)
- Realtime private Broadcast/Presence authorization in `data-layer.md`
- Eval 57 - private Realtime org channels

## 1.6.1 - 2026-07-14

### Added

- Loop engineering pack: outer-loop contract, risk gates, `/devgod-loop-agent`, maker-checker, plan sample, eval CI
- AI modules: `ai-security`, `ai-boundary`, `ai-evals` (+ trajectory fixture stub)
- SaaS modules: `backend-pgvector`, `backend-fts`, `backend-admin`, `billing-metered`, `design-motion`
- Templates: `rate-limit.ts`, `eslint.config.mjs`, expanded cache-tags
- Privacy DSAR depth, onboarding empty-state orchestration, deploy canary smoke
- Server Action CSRF/origins hardening notes (proxies, patch cadence)
- Auth adapter note for Clerk/Auth.js (non-default)
- Eval bank 37-56; research footers on L3 modules

### Changed

- `feature-flags` kill switches; `email-notifications` behavioral drip/dunning
- `frontend-performance` INP; `frontend-testing` pyramid CI counts
- `COMPAT.md` / skill version **1.6.1**

### Added (detail backlog)


- **compliance-privacy** - retention classes, DSAR queue, large export jobs, delete cascade hardening
- **ai-evals** - concrete trajectory fixture JSON + offline path checker
- **Research footers** - L3 modules missing gap-audit pointer
- **Evals 54-55** - GDPR export/delete + trajectory fixture
- **product-onboarding** - empty states as primary surface, behavior-gated checklist, anti-noise orchestration
- **deploy-ops** - expanded post-deploy smoke + canary composition with gstack
- **Evals 52-53** - activation empty state + post-deploy verification
- **gap-audit** - executive snapshot refresh; legacy P0 rows marked done
- **`references/design-motion.md`** - density scales, motion tokens, reduced-motion, INP-aware motion
- **`templates/lib/rate-limit.ts`** - Upstash sliding-window helper for Server Actions
- **frontend-performance** - deeper INP checklist (transitions, hydration, thin handlers)
- **frontend-testing** - pyramid CI counts and a11y smoke row
- **Evals 50-51** - motion/density + rate-limit action
- **`references/billing-metered.md`** - usage records, quotas, idempotent Stripe report, hard/soft limits
- **feature-flags** - flag types, kill switch, rollout ladder, flags vs entitlements
- **Evals 48-49** - metered billing + gradual rollout/kill switch
- **email-notifications** - behavioral onboarding suppress-on-activation, dunning sequence, email_log index
- **data-layer** - Realtime auth/RLS/presence rules
- **`templates/eslint.config.mjs`** - Next flat ESLint for CI `--max-warnings=0`
- **Evals 46-47** - lifecycle email + ESLint enforce
- **`references/backend-fts.md`** - Postgres full-text search (stored tsvector, GIN, rank, tenant scope)
- **`references/backend-admin.md`** - staff support, impersonation TTL, audit, anti-patterns
- **Evals 44-45** - FTS routing and support impersonation
- **`references/backend-pgvector.md`** - tenant-scoped embeddings, HNSW, RAG RPC, RLS, ingest jobs
- **data-layer** cacheLife presets + Cache Components Suspense rules; cache-tags content/rag helpers
- **Eval 43** - semantic search / pgvector routing
- **`/devgod-loop-agent`** - outer-loop recipe (budgets, maker/checker, stop conditions)
- **Evals 37-42** - ai-boundary keys, evaluation runner choice, portage handoff, verify-before-done, MCP risk, loop-agent
- Smoke eval IDs include 37 and 40
- **Loop engineering P0 (from `devgod-loop-ai-engineering` research)** - outer-loop contract, stop/budget defaults, maker-checker, risk gate table, multi-file plan rule in `references/workflows.md`
- **Loop engineering P1** - maker≠checker checker preference table; `ai-boundary.md`; `ai-evals.md` harness matrix; loop-ci backoff; loop-ship Vercel/canary compose; project-detect AI/harness signals
- **`references/ai-security.md`** - LLM/tools/MCP/skill supply-chain checklist; linked from backend-security + MANIFEST + SKILL
- **`references/ai-boundary.md`** - product ↔ model service shape and scaffold checklist
- **`references/ai-evals.md`** - skill bank vs promptfoo vs Braintrust vs trajectory
- **`templates/plan.sample.json`** - copy-ready plan artifact example
- **composition.md** - portage handoff recipe, gstack↔devgod loop catalog, canary/careful/ai-harness rows
- **CI** - `evals` job: `run-evals.sh --smoke` + validate plan sample on every PR/main
- **Deep research (v1.6)** - `references/deep-research.md` (Weizhena/Deep-Research-skills adapted): outline → parallel deep agents → validated JSON → report; engineering presets in `templates/research/`; `scripts/research-validate-json.py`, `scripts/research-report.py`; slash `/devgod-research*`
- **`references/web-search-modules/*`** - source strategy packs for research agents
- **`references/background-jobs.md`** - queues/workers, webhook→job, idempotency, decision tree (Inngest / Trigger / pg-boss / Python)
- **`references/backend-multitenant.md`** - orgs, memberships, roles, invites, RLS helpers, transfer/offboarding
- **`references/audit-log.md`** - append-only audit events, RLS, retention
- **`references/billing-seats.md`** - org seat quantity, invite gates, Stripe quantity
- **`references/composition.md`** - partner skill ownership matrix (unmachined, gstack cso/qa/ship/investigate, portage, silo)
- **`templates/playwright/`** - dual-project E2E (public + auth.setup storageState)
- **`templates/lib/instrumentation.ts`** - Next.js `@vercel/otel` bootstrap + span conventions
- **`templates/lib/cache-tags.ts`** - central cache tag registry
- **`templates/plan-artifact.schema.json`** + **`scripts/validate-plan.sh`** - Plan → Validate → Execute
- **`scripts/test-scan.sh`** + **`scripts/fixtures/{pass,fail}`** - scanner fixture CI
- **`scripts/run-evals.sh`** - static eval harness (`--smoke` / `--full` / `--json`)
- **`scripts/devgod-health.sh`** - target-app health score (tsc/lint/test/scan)
- **`COMPAT.md`** - stack pin matrix
- **Rate-limit / abuse scan** in `scripts/devgod-scan.sh --backend` (WARN) and `--strict` (FAIL); exempt via `devgod:ratelimit-exempt`
- Scan UX: `--json`, `--quiet`, duration line; tighter secret globs (skip docs/research markdown)
- **Supply-chain checks** in `scripts/validate-repo.sh` (`set -euo pipefail`, no curl|bash install patterns in scripts/)
- Multi-host install: `install-all-agents.sh --hosts cursor,claude,codex,agents,hermes,opencode,gemini [--force-dirs]`
- SECURITY.md section **Installing this skill** (pin SHA/tag, ToxicSkills-class caution)
- enforcement.md table for rate-limit scanner rules
- observability.md OpenTelemetry section; CSP reporting pipeline; toast a11y appendix
- 4 new eval scenarios (audit-log, seats, plan artifact, enforce/scan)
- `CODE_OF_CONDUCT.md`

### Changed

- SKILL: Composition + PVE; routing for jobs/multitenant/audit/seats/Playwright/OTel
- MANIFEST templates + scripts catalog
- gap-audit: P0/P1 craft rows marked shipped
- Inspired by gstack: partner ownership, completeness bias, browser QA vs CI E2E, health wrapper

## 1.6.0 - 2026-07-13

### Added

- **Deep research pipeline** integrated into devgod verbs and commands
- Engineering field presets: library-eval, stack-selection, competitor-tech, security
- `research-validate-json.py` + `research-report.py`
- Composition: partner `research*` skills equivalent; prefer `devgod research*` for stack decisions

### Changed

- Skill version **1.6.0**
- SKILL routing, MANIFEST, verbs, slash-commands, composition matrix

## 1.5.0 - 2026-07-13

### Added

- **`references/python.md`** - peer language module (FastAPI services, workers, AI boundary, uv/ruff/basedpyright)
- **`research/python/`** - formal deep research: outline, fields, **44/44** validated results, report
- Python detection in `project-detect.md`; stack-rules peer section
- `devgod-scan.sh --python` (+ auto-detect): PY-LOCK, PY-JWT, PY-LIFESPAN, PY-SA14, requests/CORS warns
- SKILL routing, hard gates, and e2e flow for Python services

### Changed

- Skill version **1.5.0** - TS product boundary · Python services/workers/AI · Rust hot paths
- MANIFEST engineering + research catalog; docs/modules.md
- gap-audit: Python peer complete; background jobs partially covered via python.md tiers

### Research findings

Python greenfield default (as_of 2026-07-13): CPython 3.13, uv, ruff, basedpyright, FastAPI,
Pydantic v2, SQLAlchemy 2 async, Taskiq/Temporal job tiers, OpenAPI→TS contracts.

## 1.4.0 - 2026-07-13

### Added

- `references/refactoring.md` - when/what/how/why for app code + agent skills
- `research/refactoring-research.md` - Fowler + Anthropic progressive-disclosure corpus
- Verb + slash: `devgod refactor` / `/devgod-refactor` (`commands/devgod-refactor.md`)
- Evals for refactor discovery and skill-structure progressive disclosure

### Changed

- **Skill structure refactor** (behavior-preserving for agents using the skill):
 - SKILL.md thinned to progressive-disclosure router (~160 lines; was ~225 with full routing tables)
 - Full catalog ownership clarified: `references/MANIFEST.md` is canonical index
 - Description: third-person triggers + negative triggers (non-web stacks)
 - Operating principles: structure-before-sprawl (`refactoring.md`)
- Brand realigned to silo family: monochrome dark (`#0a0a0a`), mono type, SVG-first
- Replaced neon gradient raster banner with `header.svg` + monochrome blueprints
- README tightened to match silo structure (header → one-liner → install → tables)
- Tighter router mark (thicker strokes, three columns) matching silo icon weight
- Added `header.png`, `logo.png`, `og.svg`/`og.png` (1280×720 social)
- README + docs de-slopped with [unmachined](https://github.com/0xNyk/unmachined); CI runs its `scan_text.py` on shipped prose
- Composition section links the public unmachined install

## 1.3.1 - 2026-07-12

### Added

- Brand kit: logo mark/wordmark (SVG + PNG), README banner, architecture/verbs/enforcement blueprint SVGs (`assets/`)
- `assets/BRAND.md` - color, type, naming rules
- `LICENSE` (MIT), `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md`
- `scripts/validate-repo.sh` - integrity checks for modules, commands, evals, path hygiene
- `.github/workflows/validate.yml` - CI for skill package integrity
- `.github/pull_request_template.md` - contributor checklist
- OSS-ready install docs (clone-relative paths; no machine-specific absolute paths)

### Changed

- README restructured for open-source readiness: banners, blueprints, portable install
- Getting started + enforcement docs use `$DEVGOD` / clone-relative install
- Install scripts print portable verify steps
- Banner compressed (~1.7MB PNG → ~113KB JPG)

### Fixed

- Hardcoded personal absolute paths removed from published docs
- Eval count drift in docs (29 → 30)

## 1.3.0 - 2026-07-12

### Added

- 23 Cursor slash commands under `commands/`
- `references/workflows.md` - pipelines, audit-fix loop, `/loop` recipes
- `scripts/install-commands.sh`, `scripts/install-all-agents.sh`
- Docs hub: getting-started, verbs, slash-commands, architecture, modules, enforcement-setup
- Eval 30: `/devgod-loop-verify` behavior

## 1.2.0 - 2026-07

### Added

- `skill-authoring.md`, `agent-skills-research.md`, `MANIFEST.md`
- Human `docs/` separation from agent load path
- Evals 22-29 (plan, fix, flow, flags, monorepo, incident, routing)

### Changed

- `SKILL.md` deduped (~200 lines) with audit template and disambiguation

## 1.1.0 - 2026-07

### Added

- i18n, storage, backend-testing, feature-flags, compliance-privacy
- storybook-dx, architecture-monorepo

## 1.0.0 - 2026-07

### Added

- Full domain coverage: design, frontend, backend, billing, deploy, SEO, email, onboarding
- Enforcement scripts + GitHub templates + pgTAP sample

## 0.9.0 - earlier

- AI agents / prompting module

## 0.8.0 - earlier

- Research corpora + enforcement tooling baseline

## 0.1.0 - earlier

- Initial skill: TypeScript, Rust, Next.js, Supabase fullstack OS
