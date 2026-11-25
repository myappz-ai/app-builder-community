#!/usr/bin/env python3
"""Build App-Builder-Playbook.pdf from README, docs/ and templates/ (one downloadable file)."""
from datetime import date
from pathlib import Path
import re

import markdown
from weasyprint import HTML

root = Path(__file__).resolve().parent.parent
files = [root / "README.md"] + sorted((root / "docs").glob("*.md")) + sorted((root / "templates").glob("*.md"))

REPO = "https://github.com/myappz-ai/micro-app-builder"


def fix_links(html: str) -> str:
    # Relative links to repo files point to GitHub so they work inside the PDF.
    def repl(m):
        href = m.group(1)
        if href.startswith(("http", "#", "mailto:")):
            return m.group(0)
        return f'href="{REPO}/blob/main/{href.lstrip("./")}"'
    return re.sub(r'href="([^"]+)"', repl, html)


sections = []
for f in files:
    text = f.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    sections.append(f'<section class="doc">{fix_links(body)}</section>')

css = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm;
  @bottom-center { content: "Micro App Builder playbook  |  page " counter(page); font-size: 8pt; color: #8a8494; } }
@page :first { @bottom-center { content: none; } }
body { font-family: "DejaVu Sans", sans-serif; font-size: 9.6pt; line-height: 1.45; color: #1A1620; }
h1 { font-size: 18pt; color: #7A2E5C; margin: 0 0 8pt; }
h2 { font-size: 13pt; color: #7A2E5C; margin: 14pt 0 6pt; }
h3 { font-size: 11pt; margin: 10pt 0 4pt; }
a { color: #7A2E5C; text-decoration: none; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 8.4pt; page-break-inside: auto; }
th, td { border: 0.5pt solid #d9d4de; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #f4eff6; }
tr { page-break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.2pt; background: #f4eff6; padding: 0 2pt; }
pre { background: #f7f4f9; border: 0.5pt solid #e4dee9; padding: 6pt; white-space: pre-wrap; word-wrap: break-word; }
pre code { background: none; padding: 0; font-size: 7.8pt; }
blockquote { border-left: 2pt solid #F2A93B; margin: 6pt 0; padding: 2pt 8pt; color: #4a4352; }
hr { border: none; border-top: 0.5pt solid #e4dee9; margin: 10pt 0; }
section.doc { page-break-before: always; }
.cover { page-break-after: always; padding-top: 70mm; }
.cover h1 { font-size: 30pt; margin-bottom: 6pt; }
.cover .sub { font-size: 13pt; color: #4a4352; margin-bottom: 30pt; }
.cover .bar { width: 40mm; height: 3pt; background: #F2A93B; margin: 14pt 0; }
.cover .meta { font-size: 9.5pt; color: #6b6474; line-height: 1.7; }
"""

cover = f"""
<div class="cover">
  <h1>Micro App Builder</h1>
  <div class="sub">The Micro App Playbook: build production apps in your sub-account with any AI assistant, from one prompt.</div>
  <div class="bar"></div>
  <div class="meta">
    How to use: upload this PDF to a Claude or ChatGPT project, then describe the app you want.<br>
    You need a sub-account on [Your Platform] (an AI-friendly app builder) and its two connector links.<br>
    Latest version: {REPO}/releases/latest<br>
    Edition: {date.today().strftime('%d %b %Y')}
  </div>
</div>
"""

html = f"<html><head><meta charset='utf-8'><title>Micro App Builder: Micro App Playbook</title><style>{css}</style></head><body>{cover}{''.join(sections)}</body></html>"
out = root / "App-Builder-Playbook.pdf"
HTML(string=html, base_url=str(root)).write_pdf(out)
print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
