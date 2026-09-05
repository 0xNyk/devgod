---
description: File upload pipeline — Supabase Storage, RLS, Server Actions, pgTAP tests.
---

# /devgod-upload

Load devgod `SKILL.md` + `references/workflows.md` (File upload).

Upload feature follows this invocation.

## Pipeline

```
backend-storage → backend-api → backend-database → backend-testing
```

## Hard gates

- Server generates storage path from `userId` — not client
- Storage RLS on `storage.objects` (folder prefix)
- Optional `public.files` metadata row
- Zod: size + MIME validation
- `getUser()` on upload Server Action
- Short TTL signed URLs for private reads

## Verify

```bash
supabase test db  # storage RLS tests when configured
bash scripts/devgod-scan.sh --backend --strict 2>/dev/null || true
```
