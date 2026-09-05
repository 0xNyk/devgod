# Module map

All reference modules grouped by domain. Agents load via [MANIFEST.md](../references/MANIFEST.md).

**Skill version:** 1.90.0

**Routers** (start here for a domain):

| Module | Domain |
|---|---|
| [project-detect.md](../references/project-detect.md) | Session start - detect stack |
| [frontend.md](../references/frontend.md) | UI, RSC, components, forms |
| [backend-supabase.md](../references/backend-supabase.md) | Auth, DB, API, webhooks |
| [ai-agents.md](../references/ai-agents.md) | Prompting, agent workflows |
| [workflows.md](../references/workflows.md) | Pipelines, outer-loop, risk gates |
| [skill-authoring.md](../references/skill-authoring.md) | Build agent skills |
| [capability-promotion.md](../references/capability-promotion.md) | Turn recurring capability gaps into the correct reusable owner |
| [deep-research.md](../references/deep-research.md) | Outline → deep → claim review → report |
| [skill-behavior-evals.md](../references/skill-behavior-evals.md) | Captured behavioral skill runs and promotion evidence |
| [skill-supply-chain.md](../references/skill-supply-chain.md) | Third-party skill admission and executable-guidance provenance |

---

## Design

| Module | Covers |
|---|---|
| [design-system.md](../references/design-system.md) | Tokens, color, typography, spacing |
| [design-motion.md](../references/design-motion.md) | Density, motion tokens, reduced-motion |
| [design-accessibility.md](../references/design-accessibility.md) | WCAG 2.2 AA, focus, contrast, targets |
| [design-patterns.md](../references/design-patterns.md) | Forms, dashboards, responsive, hierarchy |
| [design-taste.md](../references/design-taste.md) | Distinctive aesthetic, anti-AI-slop UI, named tone + signature |
| [conversion-ui.md](../references/conversion-ui.md) | Landing anatomy, CTAs, hero |
| [behavioral-design.md](../references/behavioral-design.md) | Ethical behavior design and dark-pattern gates |
| [visual-communication.md](../references/visual-communication.md) | Infographics, blueprints, field notes, thumbnails, logos, watermarks, and banners |
| [company-operating-system.md](../references/company-operating-system.md) | Company leadership, functions, people, governance, finance/legal operations, controls, and evidence |

## Frontend

| Module | Covers |
|---|---|
| [frontend-performance.md](../references/frontend-performance.md) | Core Web Vitals, INP, images, fonts |
| [frontend-state.md](../references/frontend-state.md) | URL, TanStack Query, Zustand decision tree |
| [frontend-streaming.md](../references/frontend-streaming.md) | Suspense, loading.tsx, error.tsx |
| [frontend-testing.md](../references/frontend-testing.md) | Vitest, RTL, Playwright pyramid |
| [browser-qa.md](../references/browser-qa.md) | Parallel browser lanes, evidence, mutation safety |
| [secure-package-html-preview.md](../references/secure-package-html-preview.md) | Sandboxed on-disk package HTML previews |
| [frontend-i18n.md](../references/frontend-i18n.md) | next-intl, locale routing, hreflang |
| [storybook-dx.md](../references/storybook-dx.md) | Optional Storybook for shadcn |
| [stack-rules.md](../references/stack-rules.md) | Tailwind v4, Next 16, shadcn syntax |

## Backend

| Module | Covers |
|---|---|
| [backend-auth.md](../references/backend-auth.md) | SSR auth, proxy.ts / middleware.ts, sessions, adapters |
| [backend-database.md](../references/backend-database.md) | Migrations, schema, RLS, indexes |
| [backend-storage.md](../references/backend-storage.md) | Uploads, buckets, signed URLs |
| [backend-testing.md](../references/backend-testing.md) | pgTAP, RLS/action integration tests |
| [backend-api.md](../references/backend-api.md) | Server Actions, CSRF/origins, Route Handlers |
| [backend-webhooks.md](../references/backend-webhooks.md) | Stripe webhook handlers |
| [backend-multitenant.md](../references/backend-multitenant.md) | Orgs, memberships, roles, invites |
| [backend-fts.md](../references/backend-fts.md) | Postgres full-text search |
| [backend-pgvector.md](../references/backend-pgvector.md) | Embeddings, RAG RPC, tenant RLS |
| [backend-admin.md](../references/backend-admin.md) | Staff support, impersonation |
| [background-jobs.md](../references/background-jobs.md) | Queues, workers, webhook→job |
| [audit-log.md](../references/audit-log.md) | Append-only audit events |
| [billing-stripe.md](../references/billing-stripe.md) | Checkout, Portal, entitlements |
| [billing-seats.md](../references/billing-seats.md) | Org seat quantity + invite gates |
| [billing-metered.md](../references/billing-metered.md) | Usage meters, quotas, overage |
| [backend-security.md](../references/backend-security.md) | CSP, headers, reporting, hardening |
| [data-layer.md](../references/data-layer.md) | Queries, cache, Realtime (+ private channels) |

## AI product

| Module | Covers |
|---|---|
| [ai-boundary.md](../references/ai-boundary.md) | Product ↔ model service shape |
| [ai-security.md](../references/ai-security.md) | Tools, MCP, skill supply chain |
| [mcp-security.md](../references/mcp-security.md) | MCP OAuth, capabilities, tool schemas, roots, sampling, elicitation, and calls |
| [malware-detection.md](../references/malware-detection.md) | Obfuscated-dropper taxonomy, regex/AST/sandbox tiering, FP doctrine, where droppers hide |
| [ai-evals.md](../references/ai-evals.md) | Harness matrix, trajectory fixtures |

## Engineering

| Module | Covers |
|---|---|
| [typescript.md](../references/typescript.md) | Types, Zod, API boundaries |
| [python.md](../references/python.md) | FastAPI services, workers, AI, uv/ruff |
| [coding-principles.md](../references/coding-principles.md) | SOLID, craft, review standards |
| [system-architecture.md](../references/system-architecture.md) | Monolith, services, reliability |
| [system-assurance.md](../references/system-assurance.md) | Goals and business rules through full-stack and runtime evidence |
| [implementation-completeness.md](../references/implementation-completeness.md) | Anti-placeholder production completeness and false-done prevention |
| [root-cause-engineering.md](../references/root-cause-engineering.md) | Fix diagnosis contract, symptom-patch prohibition, declared mitigations |
| [portfolio-context.md](../references/portfolio-context.md) | Workspace/venture truth, repo→venture resolution, cross-repo impact |
| [rust.md](../references/rust.md) | Axum/Tokio services |
| [api-data-flows.md](../references/api-data-flows.md) | Cross-service data flows |
| [architecture.md](../references/architecture.md) | Single-app repo layout |
| [architecture-monorepo.md](../references/architecture-monorepo.md) | Turbo workspaces |
| [refactoring.md](../references/refactoring.md) | Behavior-preserving structure |

## Ops, growth, compliance

| Module | Covers |
|---|---|
| [deploy-ops.md](../references/deploy-ops.md) | Vercel, envs, releases, canary smoke |
| [observability.md](../references/observability.md) | Logs, Sentry, OTel tracing |
| [seo-metadata.md](../references/seo-metadata.md) | Technical SEO, sitemap |
| [web-discovery-engineering.md](../references/web-discovery-engineering.md) | SEO, SEA, AI answers, crawler policy, robots, IndexNow, llms.txt, and measurement |
| [coding-agent-hosts.md](../references/coding-agent-hosts.md) | Codex, Claude Code, Hermes and portable host capability adaptation |
| [coding-agent-capability-playbooks.md](../references/coding-agent-capability-playbooks.md) | Task-to-surface selection for review, remote work, automation, extensions and fallback |
| [autonomous-experimentation.md](../references/autonomous-experimentation.md) | Protected-oracle autonomous experiment loops with budgets, ledgers and promotion gates |
| [developer-experience.md](../references/developer-experience.md) | SDK/API/CLI/plugin and contributor journeys, time-to-result and live audits |
| [hermes-agent-integration.md](../references/hermes-agent-integration.md) | Hermes profiles, tools, memory, curator, browser, cron, gateway and hardening |
| [email-notifications.md](../references/email-notifications.md) | Resend, lifecycle + dunning |
| [product-onboarding.md](../references/product-onboarding.md) | Activation UI, empty states |
| [compliance-privacy.md](../references/compliance-privacy.md) | GDPR export/delete, DSAR, consent |
| [infra-security.md](../references/infra-security.md) | Cloud IAM, network exposure, SSH/VPS and container hardening, secrets, backup/DR |
| [compliance-controls.md](../references/compliance-controls.md) | SOC 2 / ISO 27001 / GDPR control mapping, gap register, evidence discipline |
| [feature-flags.md](../references/feature-flags.md) | Rollouts, kill switches |
| [growth-funnels.md](../references/growth-funnels.md) | PLG, activation, retention, PQL |
| [product-marketing.md](../references/product-marketing.md) | Factual launch and sales-enablement surfaces |
| [gtm-engineering.md](../references/gtm-engineering.md) | Attribution, PQL, CRM and lifecycle data flows |
| [product-analytics.md](../references/product-analytics.md) | KPI trees, event contracts, experiments |
| [prd-to-evidence.md](../references/prd-to-evidence.md) | Traceable PRDs, acceptance, plans, and evidence |
| [agentic-engineering.md](../references/agentic-engineering.md) | Agent loops, orchestration, checkpoints, stop gates |
| [long-horizon-agents.md](../references/long-horizon-agents.md) | Session degradation, context budgets, externalized state, ongoing/cron agents |
| [prompt-optimization.md](../references/prompt-optimization.md) | Prompt, context, harness, and eval optimization |
| [agent-red-teaming.md](../references/agent-red-teaming.md) | Authorized defensive agent security evaluation |
| [agent-incident-response.md](../references/agent-incident-response.md) | Evidence-bound containment and clean agent recovery |
| [multi-agent-orchestration.md](../references/multi-agent-orchestration.md) | Delegation, authority, lanes, joins, budgets, and failure containment |
| [coordination-transports.md](../references/coordination-transports.md) | Untrusted mailbox/ring notifications and hash-bound handoff pointers |
| [browser-agent-security.md](../references/browser-agent-security.md) | Auth state, origins, URLs, injection, permissions, transfers, and browser evidence |
| [output-quality.md](../references/output-quality.md) | Scoped anti-slop and unmachined quality gates |
| [decision-engineering.md](../references/decision-engineering.md) | Bounded evidence-based deliberation and Council composition |
| [epistemic-honesty.md](../references/epistemic-honesty.md) | Confidence-tracks-evidence mechanism + correction-flip guard, calibrated abstention, verification independence |
| [product-business-engineering.md](../references/product-business-engineering.md) | Business goal to product/revenue architecture |

## Quality & composition

| Module | Covers |
|---|---|
| [code-quality.md](../references/code-quality.md) | Pre-ship review gates |
| [enforcement.md](../references/enforcement.md) | Enforcement tiers, setup, CI wiring, maturity model |
| [enforcement-rules.md](../references/enforcement-rules.md) | Rule catalog: scanner rules, lint configs, a11y/auth/RLS gates |
| [composition.md](../references/composition.md) | Partner skills (gstack, portage, unmachined) |

---

## Research corpora

Load via module footers - not at session start.

| Corpus | Feeds |
|---|---|
| [gap-audit.md](../research/gap-audit.md) | Coverage matrix + roadmap |
| [report.md](../research/report.md) | Provenance |
| [deep-2026-07.md](../research/deep-2026-07.md) | Multi-domain deepen |
| Domain `*-research.md` files | Design, frontend, backend, security, growth, AI agents |
