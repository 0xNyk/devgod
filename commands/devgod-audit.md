---
description: Audit code or UI against devgod rubrics — report with severity, no edits.
---

# /devgod-audit

Load devgod `SKILL.md`. Mode: **audit only — no file edits**.

Target: user's path, feature, or "full stack" follows this invocation.

## Output format (mandatory)

Use SKILL.md audit template:

```markdown
## devgod audit: [target]
**Modules**: ...
**Score**: ...

### Critical
- [file:line] issue → fix

### Warning
- ...

### Enforcement gaps
- ...

### Passed
- ...
```

## Route by target

| Target | Modules |
|---|---|
| UI / dashboard | design-system, design-accessibility, design-patterns |
| Performance | frontend-performance, frontend-streaming |
| Backend / API | backend-api, backend-auth, backend-database |
| Security | backend-security, backend-auth |
| Enforcement | enforcement.md + maturity L0–L4 |
| Full stack | Score each touched domain |

## Rules

- Quote specific issues with fixes — **no praise padding**
- Recommend scripts/CI for checklist-only gaps
- If Critical > 0, suggest `/devgod-fix` after report
