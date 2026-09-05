# Compatibility / stack pins

**As-of:** 2026-08-23 · Skill **1.90.0**
**Rule:** Prefer these defaults in greenfield. Support one major back when easy; document breaks in CHANGELOG.

| Layer | Default (tested intent) | Notes |
|---|---|---|
| TypeScript | 5.x strict | App + skill examples |
| Next.js | **16.x App Router (LTS)** | Greenfield: Cache Components (`cacheComponents: true`), Turbopack, request boundary `proxy.ts`. Detect and keep Next 15 `middleware.ts` until a deliberate migration. |
| React | 19.2.x | RSC default |
| Tailwind | v4 | CSS-first `@theme`. With Turbopack, set explicit `@source` globs if HMR misses classes. |
| Supabase JS | v2 + `@supabase/ssr` | Cookie SSR; `getUser()` on mutations. Official Next 16 template uses `lib/supabase/proxy.ts`. |
| Zod | v3 or v4 | API boundaries either; don't mix major in one package tree without reason |
| Stripe | Checkout Sessions | Pin one API version per app (SDK default). PaymentIntents only for a custom Payment Element. Webhook raw body verify first. |
| Python | 3.12-3.13 | `uv` + lockfile; see python.md |
| Playwright | @playwright/test latest stable | templates/playwright |
| OTel | @vercel/otel | templates/lib/instrumentation.ts |
| MCP | Spec **2026-07-28** | Stateless HTTP default; Tasks are an optional extension, not core. See `mcp-security.md`. |
| Agent Skills | [agentskills.io](https://agentskills.io/specification) | `name` + `description` required; optional `license` / `compatibility` / `metadata`. SKILL.md body under 500 lines. |

## Scanner

| Flag | Default severity notes |
|---|---|
| secrets | always FAIL |
| rate-limit missing | WARN (`--backend`); FAIL (`--strict`) |
| getUser on mutate | FAIL under `--strict` |
| design palette | WARN/FAIL per design flags |

## Host installs

`scripts/install-all-agents.sh` supports Codex/shared Agent Skills, Claude Code,
Cursor, Grok, Hermes, Gemini CLI, and OpenCode. The installers require Python 3.10+
and Bash; no Python packages or model credentials are needed.

Command adapters use each host's native format. Codex uses `/prompts:devgod-*`;
other adapters use `/devgod-*`. See [native installation](docs/native-skills.md),
[command aliases](docs/slash-commands.md), and [release verification](docs/releasing.md)
for paths and the distinction between format tests and host execution.

## Not supported

- Pages Router as greenfield default (legacy only)
- Client-only Supabase with service role
- Python `on_event` lifespan style
- Greenfield `middleware.ts` on Next 16+ (migrate with `npx middleware-to-proxy .`)

## Security pins (2026)

| Item | Policy |
|---|---|
| Next.js | Stay on patched 16.x (or detected 15.x) - Server Action CSRF / origin handling has had CVEs; upgrade promptly |
| Request boundary | Next 16+: `proxy.ts` exporting `proxy`; Next 15: `middleware.ts`. Keep a shared `updateSession` helper either way. Confirm cookies persist in production (`npm run build && npm run start`), not only `next dev`. |
| Session cookies | SameSite=Lax or Strict; no long-lived service role in browser; do not strip Supabase `Cache-Control: private, no-store` |
| Server Actions | `getUser` + Zod + rate limit; set `serverActions.allowedOrigins` behind proxies |
| Stripe | Checkout Sessions + webhook unlock; never `success_url` query params |
