#!/usr/bin/env python3
"""Exercise native installation in isolated homes without launching LLMs."""

import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from skill_hosts import HOST_PATHS, skill_paths

ROOT = Path(__file__).resolve().parent.parent


class NativeSkillsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="devgod-native-")
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name) / "home with spaces"

    def install(self, *args, success=True):
        result = subprocess.run(
            ["bash", str(ROOT / "scripts/install-all-agents.sh"), "--home", str(self.home), *args],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)
        return result

    def test_all_hosts_and_repeat_without_global_side_effects(self):
        self.install("--hosts", "all")
        before = {str(p): p.lstat().st_mtime_ns for p in self.home.rglob("*")}
        self.install("--hosts", "all")
        self.assertEqual(before, {str(p): p.lstat().st_mtime_ns for p in self.home.rglob("*")})
        for rel in HOST_PATHS.values():
            path = self.home / rel
            self.assertEqual(path.resolve(), ROOT)
            for bundled in ("SKILL.md", "references/project-detect.md", "scripts/devgod-scan.sh"):
                self.assertEqual((path / bundled).read_bytes(), (ROOT / bundled).read_bytes())
        self.assertFalse((self.home / "AGENTS.md").exists())
        self.assertFalse((self.home / ".hermes/memories").exists())
        self.assertFalse((self.home / ".cursor/commands").exists())
        self.assertFalse((self.home / ".claude/CLAUDE.md").exists())

    def test_preview_and_bad_arguments_write_nothing(self):
        self.install("--hosts", "all", "--dry-run")
        self.assertFalse(self.home.exists())
        for args in (("--hosts", "claude,typo"), ("--hosts", ""), ("--hosts",), ("--hosts", "all", "--skills-dir", "unused")):
            self.install(*args, success=False)
            self.assertFalse(self.home.exists())

    def test_selected_host_creates_fresh_root(self):
        self.install("--hosts", "hermes")
        self.assertTrue((self.home / ".hermes/skills/devgod/SKILL.md").is_file())
        self.assertEqual([p.name for p in self.home.iterdir()], [".hermes"])

    def test_auto_only_detected_roots(self):
        (self.home / ".claude").mkdir(parents=True)
        self.install()
        self.assertTrue((self.home / ".claude/skills/devgod").is_symlink())
        self.assertEqual([p.name for p in self.home.iterdir()], [".claude"])

    def test_conflict_preflight_preserves_data_and_other_hosts(self):
        conflict = self.home / ".hermes/skills/devgod"
        conflict.mkdir(parents=True)
        (conflict / "local.txt").write_text("keep me")
        self.install("--hosts", "claude,hermes", success=False)
        self.assertEqual((conflict / "local.txt").read_text(), "keep me")
        self.assertFalse((self.home / ".claude").exists())

    def test_wrong_and_dangling_links_are_preserved(self):
        conflict = self.home / ".claude/skills/devgod"
        conflict.parent.mkdir(parents=True)
        for target in (self.home, self.home / "missing"):
            conflict.symlink_to(target)
            self.install("--hosts", "claude", success=False)
            self.assertEqual(conflict.readlink(), target)
            conflict.unlink()

    def test_uninstall_only_own_links_and_preflight_all_hosts(self):
        self.install("--hosts", "all")
        foreign = self.home / ".claude/skills/devgod"
        foreign.unlink()
        foreign.mkdir()
        (foreign / "custom.txt").write_text("keep")
        self.install("--hosts", "all", "--uninstall", success=False)
        self.assertTrue((self.home / ".cursor/skills/devgod").is_symlink())
        (foreign / "custom.txt").unlink()
        foreign.rmdir()
        self.install("--hosts", "all", "--uninstall", "--dry-run")
        self.assertTrue((self.home / ".cursor/skills/devgod").is_symlink())
        self.install("--hosts", "all", "--uninstall")
        self.install("--hosts", "all", "--uninstall")
        self.assertFalse(any((self.home / rel).is_symlink() for rel in HOST_PATHS.values()))
        self.install("--hosts", "all", "--uninstall", "--pull", success=False)

    def test_custom_native_directory(self):
        custom = Path(self.temp.name) / "another host/skills"
        self.install("--skills-dir", str(custom))
        self.assertEqual((custom / "devgod").resolve(), ROOT)
        self.assertFalse(self.home.exists())

    def test_profile_roots_and_explicit_home_isolation(self):
        env = {"HERMES_HOME": str(self.home / "hermes-profile"),
               "CLAUDE_CONFIG_DIR": str(self.home / "claude-profile"),
               "XDG_CONFIG_HOME": str(self.home / "xdg")}
        with patch.dict(os.environ, env):
            paths = skill_paths()
            self.assertEqual(paths["hermes"], Path(env["HERMES_HOME"]) / "skills/devgod")
            self.assertEqual(paths["claude"], Path(env["CLAUDE_CONFIG_DIR"]) / "skills/devgod")
            self.assertEqual(paths["opencode"], Path(env["XDG_CONFIG_HOME"]) / "opencode/skills/devgod")
            self.install("--hosts", "hermes")
            self.assertFalse((self.home / "hermes-profile").exists())

    def test_doctor_accepts_native_only_and_detects_missing_selected_host(self):
        spec = importlib.util.spec_from_file_location("doctor", ROOT / "scripts/devgod-doctor.py")
        doctor = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(doctor)
        self.install("--hosts", "codex,hermes")
        with patch.object(doctor, "host_inventory", return_value={"available": False, "hosts": []}):
            report = doctor.build_report(ROOT, self.home, "codex,hermes")
            self.assertEqual(report["decision"], "healthy")
            self.assertEqual(report["activation_adapters"], [])
            (self.home / ".hermes/skills/devgod").unlink()
            self.assertEqual(doctor.build_report(ROOT, self.home, "codex,hermes")["decision"], "repair_required")


if __name__ == "__main__":
    unittest.main()
