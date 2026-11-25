#!/usr/bin/env python3
"""Fail if the playbook contains secrets, account ids, em dashes, or names that belong in a private platform add-on.

Add your own internal words to BANNED_EXTRA (or a private .playbook-banned file, one regex per line, never committed).
"""
import re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
files = [root / "README.md", root / "CONTRIBUTING.md", root / "CHANGELOG.md"] \
    + sorted((root / "docs").glob("*.md")) + sorted((root / "templates").glob("*.md"))

RULES = {
    "em dash": chr(0x2014),
    "secret-looking token": r"\b(EAA[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|xox[abp]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16})\b",
    "Meta ad account id": r"\bact_\d{6,}\b",
    "UUID (account or app id)": r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    "long numeric id": r"(?<![\d.,])\d{12,}(?![\d.,])",
    "email address": r"\b[\w.+-]+@[\w-]+\.[\w.]+\b",
    "phone number": r"\+\d{1,3}[\s-]?\d{5}[\s-]?\d{5}\b",
}
BANNED_EXTRA = []
extra = root / ".playbook-banned"
if extra.exists():
    BANNED_EXTRA += [l.strip() for l in extra.read_text().splitlines() if l.strip() and not l.startswith("#")]

problems = 0
for f in files:
    if not f.exists():
        continue
    for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        for name, rx in list(RULES.items()) + [("banned word", b) for b in BANNED_EXTRA]:
            if re.search(rx, line, flags=re.I if name == "banned word" else 0):
                print(f"{f.relative_to(root)}:{n}: {name}: {line.strip()[:120]}")
                problems += 1
if problems:
    print(f"\n{problems} problem(s). Fix them or move the detail to your private platform add-on.")
    sys.exit(1)
print("playbook check passed")
