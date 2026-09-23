#!/usr/bin/env bash
# Quick launcher to run any 4PRD skin on localhost:8000
set -euo pipefail

SKIN="${1:-menumind}"
PORT="${2:-8000}"

VALID_SKINS="menumind listguard clausewindow exhibit stub"
if [[ ! " $VALID_SKINS " =~ " $SKIN " ]]; then
    echo "Error: Unknown skin '$SKIN'."
    echo "Available skins: $VALID_SKINS"
    exit 1
fi

echo "=========================================================="
echo " Starting 4PRD with SKIN: $SKIN on http://localhost:$PORT"
echo "=========================================================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT/app"
SKIN="$SKIN" uv run uvicorn web.app:app --host 0.0.0.0 --port "$PORT" --reload
