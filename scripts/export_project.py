#!/usr/bin/env python3
"""
4PRD Project Exporter
Extracts any of the 4 skins into an independent, standalone Git repository.

Usage:
    python scripts/export_project.py <skin_name> <destination_directory>
Example:
    python scripts/export_project.py menumind ~/projects/menumind
"""

import sys
import shutil
from pathlib import Path

SKIN_NAMES = {"menumind", "listguard", "clausewindow", "exhibit"}

def export(skin: str, dest_dir: Path):
    if skin not in SKIN_NAMES:
        print(f"Error: Unknown skin '{skin}'. Choose from: {', '.join(sorted(SKIN_NAMES))}", file=sys.stderr)
        sys.exit(1)

    repo_root = Path(__file__).resolve().parent.parent
    app_dir = repo_root / "app"
    spec_dir = repo_root / "specs" / skin

    if dest_dir.exists() and any(dest_dir.iterdir()):
        print(f"Error: Target directory '{dest_dir}' already exists and is not empty.", file=sys.stderr)
        sys.exit(1)

    dest_dir.mkdir(parents=True, exist_ok=True)
    print(f"Exporting standalone '{skin}' repository to: {dest_dir}...")

    # Copy core harness, web, and tests
    shutil.copytree(app_dir / "harness", dest_dir / "app" / "harness")
    shutil.copytree(app_dir / "web", dest_dir / "app" / "web")
    shutil.copytree(app_dir / "tests", dest_dir / "app" / "tests")

    # Copy the selected skin
    dest_skins = dest_dir / "app" / "skins"
    dest_skins.mkdir(parents=True, exist_ok=True)
    (dest_skins / "__init__.py").write_text('"""Standalone skins package."""\n', encoding="utf-8")
    shutil.copy(app_dir / "skins" / "stub.py", dest_skins / "stub.py")
    shutil.copytree(app_dir / "skins" / skin, dest_skins / skin)

    # Copy the selected evals
    dest_evals = dest_dir / "app" / "evals"
    dest_evals.mkdir(parents=True, exist_ok=True)
    if (app_dir / "evals" / skin).exists():
        shutil.copytree(app_dir / "evals" / skin, dest_evals / skin)
    if (app_dir / "evals" / "receipts.sqlite").exists():
        shutil.copy(app_dir / "evals" / "receipts.sqlite", dest_evals / "receipts.sqlite")

    # Copy pyproject.toml & config
    shutil.copy(app_dir / "pyproject.toml", dest_dir / "app" / "pyproject.toml")
    shutil.copy(app_dir / ".gitignore", dest_dir / "app" / ".gitignore")

    # Create pre-configured .env.example
    env_content = f"""# Pre-configured .env for {skin.upper()}
ENV=demo
SKIN={skin}
NAMED_HUMAN=Operator
NAMED_ROLE=Triage Lead
NAMED_ORG=Enterprise

DEMO_TOKEN=
TF_BASE_URL=https://api.tokenfactory.nebius.com/v1
TF_API_KEY=
TF_MODEL_OBSERVE=Qwen/Qwen3-VL-30B-A3B
TF_MODEL_JUDGE=Qwen/Qwen3-8B
TF_MODEL_GENERATE=Qwen/Qwen3-8B
DECISION_BACKEND=tf_json
AUTO_ALLOW=0
"""
    (dest_dir / "app" / ".env.example").write_text(env_content, encoding="utf-8")

    # Copy spec documentation
    if spec_dir.exists():
        shutil.copytree(spec_dir, dest_dir / "spec")

    # Copy design and threat model
    dest_docs = dest_dir / "docs"
    dest_docs.mkdir(parents=True, exist_ok=True)
    if (repo_root / "specs" / "design" / "MASTER.md").exists():
        shutil.copy(repo_root / "specs" / "design" / "MASTER.md", dest_docs / "MASTER_DESIGN.md")
    if (repo_root / "specs" / "security" / "owasp-threat-model.md").exists():
        shutil.copy(repo_root / "specs" / "security" / "owasp-threat-model.md", dest_docs / "THREAT_MODEL.md")

    # Create standalone README.md
    readme_content = f"""# {skin.upper()}: Standalone Enterprise Decision System

Extracted from 4PRD Decision Harness.

## Quickstart
```bash
cd app
uv sync --extra dev
uv run pytest
SKIN={skin} uv run uvicorn web.app:app --host 0.0.0.0 --port 8000 --reload
```
"""
    (dest_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"Export complete! You can now `cd {dest_dir}` and initialize git.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/export_project.py <skin_name> <destination_directory>")
        sys.exit(1)
    export(sys.argv[1].lower(), Path(sys.argv[2]).resolve())
