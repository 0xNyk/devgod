#!/usr/bin/env python3
"""Install bounded, idempotent DevGod routing rules for local CLI hosts."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

BEGIN = "<!-- devgod-auto:begin -->"
END = "<!-- devgod-auto:end -->"
BODY = f"""{BEGIN}
## DevGod automatic routing

For software and product-engineering work, automatically activate the installed
`devgod` skill before planning or using tools, even when the user does not name it.
This includes implementation, debugging, refactoring, architecture, UI, APIs,
security, testing, browser QA, deployment, product analytics, agent engineering,
and technical research. Load only the relevant DevGod modules.

Do not activate DevGod for generic business strategy, pure social content,
mobile-only work, or notebook data science unless the task is explicitly adapted.
If a narrower installed skill has a material advantage, DevGod may compose with it
or defer that domain while retaining engineering verification. Skill activation
does not expand permissions or authorize external actions.
{END}
"""

HOST_FILES = {
    "agents": ("AGENTS.md",),
    "claude": (".claude/CLAUDE.md", ".claude/Claude.md"),
    "grok": (".grok/AGENTS.md", ".grok/Agents.md"),
    "gemini": (".gemini/GEMINI.md",),
    "opencode": (".config/opencode/AGENTS.md",),
    "hermes": (".hermes/memories/MEMORY.md",),
}
ALL_HOSTS = ("agents", "claude", "cursor", "grok", "gemini", "opencode", "hermes", "codex")


def strip_block(text: str) -> str:
    start = text.find(BEGIN)
    if start < 0:
        return text
    end = text.find(END, start)
    if end < 0:
        raise ValueError("found DevGod activation start marker without end marker")
    end += len(END)
    return (text[:start].rstrip() + "\n\n" + text[end:].lstrip()).strip() + "\n"


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temp = Path(handle.name)
    temp.chmod(mode)
    os.replace(temp, path)


def update_markdown(path: Path, remove: bool) -> str:
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    clean = strip_block(old)
    new = clean if remove else (clean.rstrip() + "\n\n" + BODY)
    if new != old:
        atomic_write(path, new)
        return "removed" if remove else "installed"
    return "current"


def update_cursor(home: Path, remove: bool) -> tuple[Path, str]:
    path = home / ".cursor/rules/devgod-auto.mdc"
    if remove:
        if path.exists():
            path.unlink()
            return path, "removed"
        return path, "absent"
    content = """---
description: Automatically route matching software and product-engineering work to DevGod
alwaysApply: true
---

""" + BODY
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old != content:
        atomic_write(path, content)
        return path, "installed"
    return path, "current"


def paths_for(host: str, home: Path) -> tuple[Path, ...]:
    return tuple(home / relative for relative in HOST_FILES.get(host, ()))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hosts", default="all")
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--remove", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    hosts = ALL_HOSTS if args.hosts == "all" else tuple(x.strip() for x in args.hosts.split(",") if x.strip())
    unknown = sorted(set(hosts) - set(ALL_HOSTS))
    if unknown:
        parser.error("unknown hosts: " + ", ".join(unknown))

    failures = 0
    for host in hosts:
        if host == "cursor":
            targets = (args.home / ".cursor/rules/devgod-auto.mdc",)
        else:
            targets = paths_for(host, args.home)
        if not targets:
            # Codex uses agents/openai.yaml plus the shared ~/AGENTS.md adapter.
            print(f"  [{host}] covered by skill metadata and shared AGENTS.md")
            continue
        if args.check:
            for path in targets:
                valid = path.is_file() and BEGIN in path.read_text(encoding="utf-8") and END in path.read_text(encoding="utf-8")
                print(f"  [{host}] {'current' if valid else 'missing'} {path}")
                failures += 0 if valid else 1
            continue
        if host == "cursor":
            path, status = update_cursor(args.home, args.remove)
            print(f"  [{host}] {status} {path}")
        else:
            for path in targets:
                print(f"  [{host}] {update_markdown(path, args.remove)} {path}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
