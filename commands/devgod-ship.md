---
description: Production pre-flight — deploy-ops, security headers, enforcement gates, observability.
---

# /devgod-ship

Load devgod `SKILL.md`. Pipeline: **deploy-ops → backend-security → enforcement → observability**.

## Checklist

- [ ] Env tiers documented (`.env.example` complete)
- [ ] Migrations applied **before** app deploy order
- [ ] CSP / security headers configured
- [ ] `devgod-scan --strict` passes
- [ ] RLS migration gate passes
- [ ] Sentry or error tracking configured
- [ ] Post-deploy smoke steps listed
- [ ] No secrets in client bundle

## Verify

```bash
npm run typecheck
npm run lint:ci 2>/dev/null || true
bash scripts/devgod-scan.sh --strict 2>/dev/null || true
```

## Compose

Run **gstack `/ship`** for final deploy checklist when user is ready to deploy.

## Loop

Until all gates pass: `/devgod-loop-ship`
