#!/usr/bin/env python3
"""Exercise an exported installer package from outside its checkout, without LLMs."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent


class CleanInstallTests(unittest.TestCase):
    def test_export_relocation_and_complete_lifecycle(self):
        with tempfile.TemporaryDirectory(prefix="devgod-clean-install-") as temporary:
            base = Path(temporary)
            source = base / "export with spaces"
            source.mkdir()
            shutil.copy2(ROOT / "SKILL.md", source / "SKILL.md")
            shutil.copytree(ROOT / "commands", source / "commands")
            scripts = source / "scripts"
            scripts.mkdir()
            for name in ("install-all-agents.sh", "install-native-skills.py", "skill_hosts.py",
                         "install-commands.sh", "install-command-aliases.py", "command_aliases.py"):
                shutil.copy2(ROOT / "scripts" / name, scripts / name)
            home = base / "isolated home"
            project = base / "consumer project"
            project.mkdir()

            def run(installer, *args, success=True):
                result = subprocess.run(
                    [sys.executable, str(source / "scripts" / installer), "--home", str(home),
                     "--hosts", "all", *args], cwd=project, capture_output=True, text=True,
                )
                self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)

            run("install-native-skills.py")
            run("install-command-aliases.py")
            run("install-command-aliases.py", "--check")
            old = source
            source = base / "relocated export"
            old.rename(source)
            # Managed wrappers refresh to the new path. Native links require an
            # explicit repair; the installer must not overwrite dangling links.
            run("install-native-skills.py", success=False)
            (home / ".hermes/skills/devgod").unlink()
            run("install-command-aliases.py")
            run("install-command-aliases.py", "--check")
            alias = home / ".codex/prompts/devgod-audit.md"
            self.assertIn(str(source.resolve()), alias.read_text())
            self.assertNotIn(str(old), alias.read_text())
            # Remove only the known fixture links to the old export.
            for link in list(home.rglob("devgod")):
                if link.is_symlink() and link.readlink() == old.resolve():
                    link.unlink()
            run("install-native-skills.py")
            run("install-command-aliases.py", "--uninstall")
            run("install-native-skills.py", "--uninstall")
            run("install-command-aliases.py", "--uninstall", "--check")
            self.assertEqual(list(project.iterdir()), [])
            self.assertFalse(list(home.rglob("devgod*.md")))
            self.assertFalse(list(home.rglob("devgod*.toml")))
            self.assertFalse(any(path.is_symlink() for path in home.rglob("*")))


if __name__ == "__main__":
    unittest.main()
