#!/usr/bin/env python3
"""Rebind the skill-eval sample hash chain to the current SKILL.md / runtime.

A devgod version bump — or any edit to the runtime package (SKILL.md,
references, scripts, templates, …) — invalidates every skill-eval sample
binding at once:

  - the skill version               (skill_bundle.version / skill_binding.version / skill_version)
  - the SKILL.md content hash        (run.environment.skill_sha256)
  - the canonical bundle hash        (skill_bundle.sha256 / skill_binding.sha256 / grade.skill_sha256)
  - the eval-bank hash               (run.environment.bank_sha256)
  - the job -> capture -> grade/oracle file-content chain ({path, sha256} nodes)

Left unbound, the samples fail their own validators and devgod-health drops.
This retargets them all to the current tree, idempotently, then self-verifies
with the real grader.

Design: the "value" bindings are rebound by VALUE substitution keyed off the
current (old) values found in canonical reference fields — no field paths are
hardcoded except those references, so an added binding that reuses an old value
is caught automatically. The file-content chain is rebound generically: any
{path, sha256} object whose path resolves to a sample file gets sha256 =
sha256(that file), iterated to a fixpoint so job -> capture -> grade converges.

Usage:
  python3 scripts/rebind-skill-eval.py            # rebind in place, then verify
  python3 scripts/rebind-skill-eval.py --check     # report drift only; exit 1 if a rebind is needed
  python3 scripts/rebind-skill-eval.py --root DIR  # operate on an alternate tree (tests)
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path


def fsha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def skillmd_version(root: Path) -> str:
    m = re.search(r'^\s*version:\s*"([^"]+)"', (root / "SKILL.md").read_text(encoding="utf-8"), re.M)
    if not m:
        sys.exit("rebind: SKILL.md metadata.version not found")
    return m.group(1)


def bundle_sha256(root: Path) -> str:
    """The canonical runtime-package digest, computed by the very function the
    validators use, so the tool can never disagree with the checker."""
    spec = importlib.util.spec_from_file_location("_cse", root / "scripts" / "capture-skill-eval.py")
    if spec is None or spec.loader is None:
        sys.exit("rebind: cannot load scripts/capture-skill-eval.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.bundle_sha256(root)


def canonical_values(root: Path) -> dict:
    run = load(root / "templates/agentic/skill-eval-run.sample.json")
    bank_path = run["environment"]["bank_path"]
    return {
        "VER": skillmd_version(root),
        "BUNDLE": bundle_sha256(root),
        "SKILLMD": fsha(root / "SKILL.md"),
        "BANK": fsha(root / bank_path),
    }


def current_values(root: Path) -> dict:
    """The old values, read from canonical reference fields (self-configuring)."""
    job = load(root / "templates/agentic/skill-eval-job.sample.json")
    run = load(root / "templates/agentic/skill-eval-run.sample.json")
    return {
        "VER": job["skill_bundle"]["version"],
        "BUNDLE": job["skill_bundle"]["sha256"],
        "SKILLMD": run["environment"]["skill_sha256"],
        "BANK": run["environment"]["bank_sha256"],
    }


def sample_paths(root: Path) -> list[Path]:
    return sorted(Path(p) for p in glob.glob(str(root / "templates/agentic/skill-eval-*.json")))


def chain_nodes(obj, names: set[str], out: list):
    """Collect (current_sha256, target_name) for every {path, sha256} object
    whose path points at a sample file."""
    if isinstance(obj, dict):
        p, s = obj.get("path"), obj.get("sha256")
        if isinstance(p, str) and isinstance(s, str) and Path(p).name in names:
            out.append((s, Path(p).name))
        for v in obj.values():
            chain_nodes(v, names, out)
    elif isinstance(obj, list):
        for v in obj:
            chain_nodes(v, names, out)


def detect_drift(root: Path) -> list[str]:
    """Return human-readable drift reasons; empty means already bound."""
    reasons = []
    cur, new = current_values(root), canonical_values(root)
    for k in ("VER", "BUNDLE", "SKILLMD", "BANK"):
        if cur[k] != new[k]:
            reasons.append(f"{k.lower()} {cur[k][:12]} -> {new[k][:12]}")
    names = {p.name for p in sample_paths(root)}
    for sp in sample_paths(root):
        nodes: list = []
        chain_nodes(load(sp), names, nodes)
        for have, target in nodes:
            want = fsha(root / "templates/agentic" / target)
            if have != want:
                reasons.append(f"{sp.name}: {target} digest {have[:12]} -> {want[:12]}")
    return reasons


def replace_in_samples(root: Path, old: str, new: str) -> int:
    if old == new:
        return 0
    n = 0
    for sp in sample_paths(root):
        t = sp.read_text(encoding="utf-8")
        if old in t:
            sp.write_text(t.replace(old, new), encoding="utf-8")
            n += 1
    return n


def rebind(root: Path) -> None:
    cur, new = current_values(root), canonical_values(root)
    # 1. Value bindings (versions are quoted so only skill-version fields match;
    #    hashes are full 64-char digests, unique by construction).
    replace_in_samples(root, f'"{cur["VER"]}"', f'"{new["VER"]}"')
    for k in ("BUNDLE", "SKILLMD", "BANK"):
        replace_in_samples(root, cur[k], new[k])
    # 2. File-content chain to a fixpoint (job -> capture -> grade/oracle).
    names = {p.name for p in sample_paths(root)}
    for _ in range(len(names) + 2):
        changed = False
        for sp in sample_paths(root):
            nodes: list = []
            chain_nodes(load(sp), names, nodes)
            for have, target in nodes:
                want = fsha(root / "templates/agentic" / target)
                if have != want:
                    sp.write_text(sp.read_text(encoding="utf-8").replace(have, want), encoding="utf-8")
                    changed = True
        if not changed:
            break
    else:
        sys.exit("rebind: file-content chain did not converge (cyclic {path,sha256}?)")


def verify(root: Path) -> bool:
    """Self-check: the real grader must accept the rebound capture sample."""
    cap = root / "templates/agentic/skill-eval-capture.sample.json"
    oracle = root / "templates/agentic/skill-eval-oracle.sample.json"
    r = subprocess.run(
        [sys.executable, str(root / "scripts/grade-skill-eval-capture.py"), str(cap),
         "--oracle", str(oracle), "--root", str(root), "--output", str(root / ".rebind-verify.json")],
        capture_output=True, text=True,
    )
    (root / ".rebind-verify.json").unlink(missing_ok=True)
    if r.returncode != 0:
        sys.stderr.write("rebind: grader rejected the rebound sample:\n" + (r.stdout or r.stderr)[:400] + "\n")
        return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Rebind the skill-eval sample hash chain.")
    ap.add_argument("--check", action="store_true", help="report drift only; exit 1 if rebind needed")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent), help="repo root")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    reasons = detect_drift(root)
    if args.check:
        if reasons:
            print("skill-eval chain drift — rebind needed:")
            for r in reasons:
                print(f"  - {r}")
            return 1
        print("skill-eval chain: bound (no drift)")
        return 0

    if not reasons:
        print("skill-eval chain already bound; nothing to do")
        return 0 if verify(root) else 3
    print("rebinding skill-eval chain:")
    for r in reasons:
        print(f"  - {r}")
    rebind(root)
    remaining = detect_drift(root)
    if remaining:
        sys.stderr.write("rebind: drift remains after rebind:\n  " + "\n  ".join(remaining) + "\n")
        return 3
    if not verify(root):
        return 3
    print("rebind complete and grader-verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
