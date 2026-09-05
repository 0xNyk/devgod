#!/usr/bin/env python3
"""Report secret-safe devgod installation provenance across supported hosts."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from skill_hosts import HOST_PATHS, select_hosts, skill_paths

VERSION = re.compile(r'^  version: "([^"]+)"$', re.MULTILINE)

ACTIVATION_MARKER = "<!-- devgod-auto:begin -->"
ACTIVATION_PATHS = {
    "cursor": (".cursor/rules/devgod-auto.mdc",),
    "claude": (".claude/CLAUDE.md", ".claude/Claude.md"),
    "codex": ("AGENTS.md",),
    "agents": ("AGENTS.md",),
    "hermes": (".hermes/memories/MEMORY.md",),
    "opencode": (".config/opencode/AGENTS.md",),
    "gemini": (".gemini/GEMINI.md",),
    "grok": (".grok/AGENTS.md", ".grok/Agents.md"),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def skill_identity(root: Path) -> tuple[str, str]:
    skill = root / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    match = VERSION.search(text)
    if match is None:
        raise ValueError(f"SKILL.md version missing at {root}")
    return match.group(1), digest(skill)


def git_identity(root: Path) -> dict[str, Any]:
    def run(*args: str) -> str | None:
        result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else None

    return {"commit": run("rev-parse", "HEAD"), "branch": run("branch", "--show-current"), "dirty": bool(run("status", "--porcelain"))}


def host_inventory(root: Path) -> dict[str, Any]:
    capture = root / "scripts" / "capture-host-capabilities.py"
    validator = root / "scripts" / "validate-host-capabilities.py"
    if not capture.is_file() or not validator.is_file():
        return {"available": False, "hosts": []}
    with tempfile.TemporaryDirectory(prefix="devgod-doctor-") as directory:
        output = Path(directory) / "inventory.json"
        made = subprocess.run([sys.executable, str(capture), "--cwd", str(root), "--output", str(output)], capture_output=True, text=True)
        checked = subprocess.run([sys.executable, str(validator), str(output)], capture_output=True, text=True) if made.returncode == 0 else made
        if checked.returncode != 0:
            return {"available": False, "hosts": []}
        data = json.loads(output.read_text(encoding="utf-8"))
    return {
        "available": True,
        "hosts": [
            {"id": item["id"], "installed": item["installed"], "capabilities": item["capabilities"]}
            for item in data["hosts"]
        ],
    }


def inspect_install(name: str, path: Path, canonical_root: Path, version: str, skill_sha: str) -> dict[str, Any]:
    item: dict[str, Any] = {"host": name, "location": HOST_PATHS[name], "present": path.exists(), "mode": "missing", "status": "missing"}
    if not path.exists():
        return item
    item["mode"] = "symlink" if path.is_symlink() else "copy"
    try:
        resolved = path.resolve(strict=True)
        installed_version, installed_sha = skill_identity(resolved)
    except (OSError, ValueError):
        item["status"] = "invalid"
        return item
    item.update({
        "version": installed_version,
        "skill_sha256": installed_sha,
        "canonical_target": resolved == canonical_root,
        "status": "current" if installed_version == version and installed_sha == skill_sha else "stale",
    })
    return item


def inspect_activation(name: str, home: Path) -> dict[str, Any]:
    relative_paths = ACTIVATION_PATHS[name]
    paths = [home / relative for relative in relative_paths]
    current = []
    for path in paths:
        try:
            current.append(path.is_file() and ACTIVATION_MARKER in path.read_text(encoding="utf-8"))
        except OSError:
            current.append(False)
    return {
        "host": name,
        "locations": list(relative_paths),
        "status": "current" if all(current) else "missing",
    }


def build_report(root: Path, home: Path | None, hosts: str = "all", require_activation: bool = False) -> dict[str, Any]:
    root = root.resolve()
    version, skill_sha = skill_identity(root)
    paths = skill_paths(home)
    selected = select_hosts(hosts, paths, detect_binaries=home is None)
    installs = [inspect_install(name, paths[name], root, version, skill_sha) for name in selected]
    for item in installs:
        item["profile_override"] = paths[item["host"]] != (home or Path.home()) / HOST_PATHS[item["host"]]
        if item["profile_override"]:
            item["location"] = {"hermes": "$HERMES_HOME/skills/devgod",
                                "claude": "$CLAUDE_CONFIG_DIR/skills/devgod",
                                "opencode": "$XDG_CONFIG_HOME/opencode/skills/devgod"}[item["host"]]
    # Legacy routing adapters are an independent opt-in check, not native discovery.
    activations = [inspect_activation(name, home or Path.home()) for name in selected] if require_activation else []
    healthy = bool(installs) and all(item["status"] == "current" for item in installs + activations)
    telemetry = root / ".devgod" / "telemetry" / "events.jsonl"
    return {
        "schema_version": 1,
        "decision": "healthy" if healthy else "repair_required",
        "canonical": {"version": version, "skill_sha256": skill_sha, **git_identity(root)},
        "installations": installs,
        "activation_adapters": activations,
        "host_inventory": host_inventory(root),
        "evaluation": {
            "telemetry_ledger_present": telemetry.is_file(),
            "codex_api_key_present": bool(os.environ.get("CODEX_API_KEY")),
            "anthropic_api_key_present": bool(os.environ.get("ANTHROPIC_API_KEY")),
        },
        "privacy": {
            "secret_values_read": False,
            "host_config_read": False,
            "session_content_read": False,
            "telemetry_content_read": False,
        },
        "limitations": [
            "Matching skill files prove installation identity, not host discovery or model selection behavior.",
            "CLI help capabilities do not prove effective authorization, sandbox, network, or behavior.",
            "API-key presence booleans do not prove validity, scope, budget, or permission to spend quota.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--home", type=Path, help="explicit home; ignores profile environment overrides")
    parser.add_argument("--hosts", default="all", help="all, auto, or comma-separated hosts")
    parser.add_argument("--require-activation", action="store_true", help="also require legacy routing adapters")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true", help="exit nonzero when any supported installation is missing, invalid, or stale")
    args = parser.parse_args()
    try:
        report = build_report(args.root, args.home, args.hosts, args.require_activation)
    except (OSError, ValueError) as exc:
        print(f"devgod doctor failed: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        canonical = report["canonical"]
        print(f"devgod doctor — v{canonical['version']} {str(canonical['commit'] or 'no-git')[:7]}")
        for item in report["installations"]:
            print(f"  {item['status']:<7} {item['host']:<8} {item['mode']:<7} {item['location']}")
        for item in report["activation_adapters"]:
            print(f"  {item['status']:<7} {item['host']:<8} routing {','.join(item['locations'])}")
        print(f"decision: {report['decision']}")
    return 1 if args.strict and report["decision"] != "healthy" else 0


if __name__ == "__main__":
    raise SystemExit(main())
