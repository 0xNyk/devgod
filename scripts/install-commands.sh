#!/usr/bin/env bash
# Install native DevGod command aliases. Use --help for hosts and scope.
set -euo pipefail
DEVGOD_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$DEVGOD_ROOT/scripts/install-command-aliases.py" "$@"
