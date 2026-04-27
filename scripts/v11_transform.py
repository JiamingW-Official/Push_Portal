#!/usr/bin/env python3
"""
Mechanical v11 transform across Push_Portal HTML pages.
- Remove dead Archivo/JetBrains font preloads.
- Insert Magvix/Darky/CSGenioMono preloads if missing.
- Wrap .eyebrow in `(LIKE THIS)` format + add `with-line`.
- Wrap .footer-heading in parens.
- Convert <h1>...</h1> to <h1 class="hero-darky">...</h1>
- Wrap data-en / data-zh pairs to match the parenthetical eyebrow format.
"""
import re
from pathlib import Path

ROOT = Path("/Users/jiamingw/Documents/GitHub/Push_Portal")

PAGES = [
    "pitch-deck.html",
    "investor-qa.html",
    "project-intro.html",
    "push-strategy-core.html",
    "economics.html",
    "attribution.html",
    "deep-dive.html",
    "metrics-dashboard.html",
    "push-team-dashboard.html",
    "nda.html",
]

PRELOAD_BLOCK = """  <link rel="preload" href="assets/fonts/Magvix-Regular.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="assets/fonts/Darky-ExtraBold.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="assets/fonts/CSGenioMono-Regular.ttf" as="font" type="font/ttf" crossorigin>"""

DEAD_FONT_LINE_RE = re.compile(
    r'^\s*<link rel="preload" href="assets/fonts/(?:archivo-latin|jetbrains-mono-latin)[^>]*>\s*$',
    re.M,
)


def wrap_parens(s: str) -> str:
    s = s.strip()
    if not s:
        return s
    if s.startswith("(") and s.endswith(")"):
        return s
    return f"({s})"


def transform_eyebrow_attr(match: re.Match) -> str:
    full = match.group(0)
    # full = e.g. <span class="eyebrow" data-en="01 · The Pitch" data-zh="01 · 一句话">01 · The Pitch</span>
    # Rewrite class -> "eyebrow with-line"
    # Wrap data-en / data-zh / inner text in parens.
    out = full
    # Class
    out = re.sub(r'class="eyebrow"', 'class="eyebrow with-line"', out, count=1)

    # data-en + data-zh values
    def wrap_attr(m: re.Match) -> str:
        attr = m.group(1)
        val = m.group(2)
        return f'{attr}="{wrap_parens(val)}"'

    out = re.sub(r'(data-en)="([^"]*)"', wrap_attr, out)
    out = re.sub(r'(data-zh)="([^"]*)"', wrap_attr, out)

    # Inner text between > and </span>
    def wrap_inner(m: re.Match) -> str:
        prefix = m.group(1)
        text = m.group(2)
        suffix = m.group(3)
        return f"{prefix}{wrap_parens(text)}{suffix}"

    out = re.sub(
        r'(<span class="eyebrow with-line"[^>]*>)([^<]*)(</span>)',
        wrap_inner,
        out,
    )
    return out


EYEBROW_RE = re.compile(r'<span class="eyebrow"[^>]*>[^<]*</span>')


def transform_footer_heading_attr(match: re.Match) -> str:
    full = match.group(0)
    out = full

    def wrap_attr(m: re.Match) -> str:
        attr = m.group(1)
        val = m.group(2)
        return f'{attr}="{wrap_parens(val)}"'

    out = re.sub(r'(data-en)="([^"]*)"', wrap_attr, out)
    out = re.sub(r'(data-zh)="([^"]*)"', wrap_attr, out)

    def wrap_inner(m: re.Match) -> str:
        prefix = m.group(1)
        text = m.group(2)
        suffix = m.group(3)
        return f"{prefix}{wrap_parens(text)}{suffix}"

    out = re.sub(
        r'(<div class="footer-heading"[^>]*>)([^<]*)(</div>)',
        wrap_inner,
        out,
    )
    return out


FOOTER_HEADING_RE = re.compile(r'<div class="footer-heading"[^>]*>[^<]*</div>')


def upgrade_h1(html: str) -> str:
    # Convert <h1>...</h1> in page-hero to <h1 class="hero-darky">.
    # Use Darky for content pages (not Magvix — that's reserved for landing index).
    return re.sub(
        r'<h1(\s+data-en="[^"]*")?(\s+data-zh="[^"]*")?\s*>',
        lambda m: f'<h1 class="hero-darky"{m.group(1) or ""}{m.group(2) or ""}>',
        html,
        count=1,
    )


def fix_preloads(html: str) -> str:
    # Remove dead lines.
    html = DEAD_FONT_LINE_RE.sub("", html)
    # Insert v11 preloads after favicon link if not already there.
    if "Magvix-Regular.ttf" in html and "Darky-ExtraBold.ttf" in html:
        return html
    insertion_point = re.search(r'(<link rel="icon"[^>]*>)', html)
    if not insertion_point:
        return html
    return (
        html[: insertion_point.end()]
        + "\n"
        + PRELOAD_BLOCK
        + html[insertion_point.end() :]
    )


def transform(html: str) -> str:
    html = fix_preloads(html)
    html = EYEBROW_RE.sub(transform_eyebrow_attr, html)
    html = FOOTER_HEADING_RE.sub(transform_footer_heading_attr, html)
    html = upgrade_h1(html)
    # Tidy: collapse 3+ blank lines to 1 (from the dead-line removal)
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html


def main():
    for name in PAGES:
        path = ROOT / name
        before = path.read_text(encoding="utf-8")
        after = transform(before)
        if before == after:
            print(f"[skip] {name}")
            continue
        path.write_text(after, encoding="utf-8")
        # Count what changed for the report.
        delta_eyebrow = before.count('class="eyebrow"') - after.count('class="eyebrow"')
        delta_with_line = after.count("eyebrow with-line") - before.count(
            "eyebrow with-line"
        )
        print(f"[done] {name}  -eyebrow={delta_eyebrow}  +with-line={delta_with_line}")


if __name__ == "__main__":
    main()
