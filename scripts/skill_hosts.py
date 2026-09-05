"""Native user skill roots shared by installation and provenance checks."""

import os
import shutil
from pathlib import Path

HOST_PATHS = {
    "cursor": ".cursor/skills/devgod",
    "claude": ".claude/skills/devgod",
    "codex": ".agents/skills/devgod",
    "agents": ".agents/skills/devgod",
    "hermes": ".hermes/skills/devgod",
    "opencode": ".config/opencode/skills/devgod",
    "gemini": ".gemini/skills/devgod",
    "grok": ".grok/skills/devgod",
}


def skill_paths(home: Path | None = None) -> dict[str, Path]:
    """An explicit home is hermetic; otherwise honor supported profile roots."""
    paths = {host: (home or Path.home()) / rel for host, rel in HOST_PATHS.items()}
    if home is None:
        for host, variable in (("hermes", "HERMES_HOME"), ("claude", "CLAUDE_CONFIG_DIR")):
            if os.environ.get(variable):
                paths[host] = Path(os.environ[variable]).expanduser() / "skills/devgod"
        if os.environ.get("XDG_CONFIG_HOME"):
            paths["opencode"] = Path(os.environ["XDG_CONFIG_HOME"]).expanduser() / "opencode/skills/devgod"
    return paths


def select_hosts(value: str, paths: dict[str, Path], detect_binaries: bool = True) -> tuple[str, ...]:
    if value == "all":
        return tuple(paths)
    if value == "auto":
        binaries = {"cursor": ("cursor", "cursor-agent", "agent"), "agents": ()}
        return tuple(host for host, path in paths.items()
                     if path.parent.parent.is_dir()
                     or (host == "codex" and (path.parents[2] / ".codex").is_dir())
                     or (detect_binaries and any(shutil.which(binary)
                         for binary in binaries.get(host, (host,)))))
    hosts = tuple(dict.fromkeys(part.strip() for part in value.split(",")))
    unknown = set(hosts) - set(paths)
    if unknown:
        raise ValueError("unknown or empty hosts: " + ", ".join(sorted(unknown)))
    return hosts
