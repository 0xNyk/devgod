---
description: Verify devgod installation identity, host surfaces, and evaluation readiness without reading secrets
---

# /devgod-doctor

Load `references/coding-agent-hosts.md` and run:

```bash
python3 scripts/devgod-doctor.py --json --strict
```

Report canonical version/commit/hash, each host installation mode and status, secret-safe host
capabilities, and evaluation readiness. Never print credential values or treat installation identity
as proof of skill activation, authorization, sandbox enforcement, or behavioral quality.
