---
description: Build markdown report from deep-research JSON results.
---

# /devgod-research-report

Load devgod `SKILL.md` + **`references/deep-research.md`**.

Mode: **Phase 3 REPORT**.

```bash
: "${DEVGOD:?Set DEVGOD to the resolved skill directory}"
python3 "$DEVGOD/scripts/research-report.py" \
  --topic-dir ./{topic_slug} \
  --toc-fields github_stars,license,recommendation_tier
```

Optional HITL: which fields appear in TOC.

## Output

`{topic_slug}/report.md` — then hand off to `devgod plan` if implementing a pick.
