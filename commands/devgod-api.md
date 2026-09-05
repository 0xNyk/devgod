---
description: Server Actions, Route Handlers, and API mutations with auth, Zod, and RLS.
---

# /devgod-api

Load devgod `SKILL.md`. Pipeline: **backend-api → backend-auth → backend-database → data-layer**.

API task follows this invocation.

## Mutation pipeline (always)

```
Rate limit (if sensitive)
  → Zod validate
  → getUser()
  → Authorize (RLS + explicit)
  → Mutate
  → updateTag / revalidateTag
```

## Hard gates

- `getUser()` not `getSession()` alone on mutations
- Zod on every external input
- No service role in client bundles
- Webhooks: `backend-webhooks.md` + gstack `/cso`

## Verify

```bash
npm run typecheck
bash scripts/devgod-scan.sh --backend --strict 2>/dev/null || true
```

## Related

- Data flow diagram first: `/devgod-flow`
- Stripe: `/devgod-billing`
