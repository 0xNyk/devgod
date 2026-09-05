---
description: Stripe billing pipeline — Checkout, Portal, webhooks, entitlements, security review.
---

# /devgod-billing

Load devgod `SKILL.md` + `references/workflows.md` (Stripe billing).

Billing requirements follow this invocation.

## Pipeline

```
billing-stripe → backend-webhooks → backend-database → gstack /cso
```

## Hard gates

- Checkout Session created **server-side**
- DB entitlements = source of truth — **never unlock on success_url alone**
- Webhook: raw body signature + idempotency on `event.id`
- RLS on subscription/customer tables
- Customer Portal for self-serve billing

## Before merge

Run or recommend **gstack `/cso`**.

## Implement

After plan approved → `/devgod-api` for handlers + `/devgod-schema` for tables.
