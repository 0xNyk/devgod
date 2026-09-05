#!/usr/bin/env bash
# Native devgod skill installation. See --help for host selection and preview.
set -euo pipefail
DEVGOD_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$DEVGOD_ROOT/scripts/install-native-skills.py" "$@"
