#!/usr/bin/env python3
"""Join README, docs/ and templates/ into one PLAYBOOK.md for single-file upload."""
from pathlib import Path
from datetime import date

root = Path(__file__).resolve().parent.parent
parts = [
    "# App Builder Community: Micro App Playbook (single file)\n",
    f"Built {date.today().isoformat()} from the app-builder-community repository. "
    "Upload this one file to a Claude or ChatGPT project. Each section below is one file of the repository.\n",
]
files = [root / "README.md"] + sorted((root / "docs").glob("*.md")) + sorted((root / "templates").glob("*.md"))
for f in files:
    rel = f.relative_to(root)
    parts.append(f"\n\n---\n\n<!-- file: {rel} -->\n")
    parts.append(f.read_text(encoding="utf-8").strip() + "\n")
out = root / "PLAYBOOK.md"
out.write_text("".join(parts), encoding="utf-8")
print(f"wrote {out} ({out.stat().st_size // 1024} KB, {len(files)} files)")
