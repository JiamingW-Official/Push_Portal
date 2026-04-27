#!/usr/bin/env python3
"""
Unify nav + footer across all Push_Portal HTML pages.

What it does per page:
1. Inject <link rel="stylesheet" href="assets/nav.css"> into <head> (idempotent)
2. Replace existing <nav>...</nav> block (+ optional <div class="nav-mobile-panel">...</div>)
   with the unified .site-nav template. Marks current page .active.
3. For index.html: also insert .sub-nav with section anchors right after .site-nav.
4. For push-team-dashboard.html: insert .site-nav right after <body>.
5. Insert <footer class="site-footer"> before </body> (idempotent).
6. Inject <script src="assets/nav.js" defer></script> into <head> (idempotent).
7. Skip nda.html (no nav by design, but add footer).

Run: python3 scripts/unify_nav.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Pages that get nav (17 pages — nda excluded from nav)
PRIMARY_NAV_PAGES = [
    "index.html",
    "project-intro.html",
    "pitch-deck.html",
    "investor-qa.html",
    "push-strategy-core.html",
    "economics.html",
]
DROPDOWN_NAV_PAGES = [
    "attribution.html",
    "metrics-dashboard.html",
    "push-team-dashboard.html",
    "deep-dive.html",
]
NAV_PAGES = PRIMARY_NAV_PAGES + DROPDOWN_NAV_PAGES  # 17 total
# nda.html gets footer but NO nav

ALL_PAGES_FOR_FOOTER = NAV_PAGES + ["nda.html"]


# ---------- NAV TEMPLATE ----------
def build_nav(active_page: str) -> str:
    """Return <nav class='site-nav'> HTML with the correct link marked .active."""

    def active(link_file: str) -> str:
        return ' class="active"' if link_file == active_page else ""

    return f"""<nav class="site-nav">
  <a href="index.html" class="nav-logo">PUSH</a>
  <div class="nav-links">
    <a href="index.html"{active("index.html")} data-en="Overview" data-zh="首页">Overview</a>
    <a href="pitch-deck.html"{active("pitch-deck.html")} data-en="Pitch Deck" data-zh="路演">Pitch Deck</a>
    <a href="investor-qa.html"{active("investor-qa.html")} data-en="Investor Q&amp;A" data-zh="投资人问答">Investor Q&amp;A</a>
    <div class="nav-more">
      <button class="nav-more-btn" aria-haspopup="true" aria-expanded="false">
        <span data-en="More" data-zh="更多">More</span> <span class="nav-more-caret">▾</span>
      </button>
      <div class="nav-more-panel nav-more-panel-compact" role="menu">
        <div class="nav-more-group">
          <div class="nav-more-heading" data-en="Core" data-zh="核心">Core</div>
          <a href="project-intro.html"{active("project-intro.html")} data-en="Product" data-zh="产品">Product</a>
          <a href="push-strategy-core.html"{active("push-strategy-core.html")} data-en="Strategy" data-zh="战略">Strategy</a>
          <a href="economics.html"{active("economics.html")} data-en="Economics" data-zh="经济模型">Economics</a>
          <a href="attribution.html"{active("attribution.html")} data-en="Attribution" data-zh="归因机制">Attribution</a>
        </div>
        <div class="nav-more-group">
          <div class="nav-more-heading" data-en="Reference" data-zh="参考资料">Reference</div>
          <a href="deep-dive.html"{active("deep-dive.html")} data-en="Deep Dive" data-zh="深度解读">Deep Dive</a>
          <a href="metrics-dashboard.html"{active("metrics-dashboard.html")} data-en="Metrics" data-zh="指标">Metrics</a>
          <a href="push-team-dashboard.html"{active("push-team-dashboard.html")} data-en="Team" data-zh="团队">Team</a>
        </div>
      </div>
    </div>
  </div>
  <div class="nav-actions">
    <button class="nav-lang">中 / EN</button>
    <button class="nav-burger" aria-label="Menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>"""


INDEX_SUB_NAV = """<div class="sub-nav">
  <a href="#problem" data-en="Problem" data-zh="问题">Problem</a>
  <a href="#solution" data-en="Solution" data-zh="方案">Solution</a>
  <a href="#how" data-en="How It Works" data-zh="工作流">How It Works</a>
  <a href="#pricing" data-en="Pricing" data-zh="定价">Pricing</a>
  <a href="#beachhead" data-en="Beachhead" data-zh="根据地">Beachhead</a>
  <a href="#plan" data-en="90-Day Plan" data-zh="90天计划">90-Day Plan</a>
  <a href="#why-now" data-en="Why Now" data-zh="为何现在">Why Now</a>
</div>"""


FOOTER_HTML = """<footer class="site-footer">
  <div class="footer-grid footer-grid-3">
    <div class="footer-col">
      <div class="footer-heading" data-en="Main" data-zh="主导航">Main</div>
      <a href="index.html" data-en="Overview" data-zh="首页">Overview</a>
      <a href="pitch-deck.html" data-en="Pitch Deck" data-zh="路演">Pitch Deck</a>
      <a href="investor-qa.html" data-en="Investor Q&amp;A" data-zh="投资人问答">Investor Q&amp;A</a>
    </div>
    <div class="footer-col">
      <div class="footer-heading" data-en="Core" data-zh="核心">Core</div>
      <a href="project-intro.html" data-en="Product" data-zh="产品">Product</a>
      <a href="push-strategy-core.html" data-en="Strategy" data-zh="战略">Strategy</a>
      <a href="economics.html" data-en="Economics" data-zh="经济模型">Economics</a>
      <a href="attribution.html" data-en="Attribution" data-zh="归因机制">Attribution</a>
    </div>
    <div class="footer-col">
      <div class="footer-heading" data-en="Reference" data-zh="参考资料">Reference</div>
      <a href="deep-dive.html" data-en="Deep Dive" data-zh="深度解读">Deep Dive</a>
      <a href="metrics-dashboard.html" data-en="Metrics" data-zh="指标">Metrics</a>
      <a href="push-team-dashboard.html" data-en="Team" data-zh="团队">Team</a>
      <a href="nda.html" data-en="NDA" data-zh="保密协议">NDA</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span data-en="© 2026 Push. AI-powered customer acquisition agency for local businesses." data-zh="© 2026 Push. 面向本地商家的 AI 获客代理公司。">© 2026 Push.</span>
  </div>
</footer>"""


# ---------- HEAD INJECTION ----------
NAV_CSS_LINK = '<link rel="stylesheet" href="assets/nav.css">'
SHARED_CSS_LINK = '<link rel="stylesheet" href="assets/shared.css">'
NAV_JS_SCRIPT = '<script src="assets/nav.js" defer></script>'
FAVICON_LINK = '<link rel="icon" type="image/svg+xml" href="favicon.svg">'
FONT_PRELOAD_1 = '<link rel="preload" href="assets/fonts/jetbrains-mono-latin-1cd702cd.woff2" as="font" type="font/woff2" crossorigin>'
FONT_PRELOAD_2 = '<link rel="preload" href="assets/fonts/archivo-latin-2a392e77.woff2" as="font" type="font/woff2" crossorigin>'
ANALYTICS_SCRIPT = '<script defer src="/_vercel/insights/script.js"></script>'
SPEED_INSIGHTS = '<script defer src="/_vercel/speed-insights/script.js"></script>'


def inject_head(html: str) -> str:
    """Inject shared.css + nav.css + nav.js + favicon + font preload + analytics
    into <head> if not already present. Fallback: before <body> if no </head>.
    Also strips Google Fonts links (we self-host now)."""
    # Strip any Google Fonts preconnect/link (we self-host fonts now)
    html = re.sub(
        r"\s*<link[^>]+fonts\.(googleapis|gstatic)\.com[^>]*>",
        "",
        html,
    )
    # Strip any legacy preconnect comments left over
    html = re.sub(
        r'\s*<link\s+rel="preconnect"\s+href="https://fonts\.(googleapis|gstatic)\.com"[^>]*>',
        "",
        html,
    )

    want = [
        FAVICON_LINK,
        FONT_PRELOAD_1,
        FONT_PRELOAD_2,
        SHARED_CSS_LINK,
        NAV_CSS_LINK,
        NAV_JS_SCRIPT,
        ANALYTICS_SCRIPT,
        SPEED_INSIGHTS,
    ]
    missing = [w for w in want if w not in html]
    if not missing:
        return html
    injection = "".join(f"  {m}\n" for m in missing)
    if "</head>" in html:
        html = html.replace("</head>", injection + "</head>", 1)
    elif "<body" in html:
        html = re.sub(
            r"(<body[^>]*>)", injection.replace("\n", "") + r"\1", html, count=1
        )
    return html


# ---------- NAV REPLACEMENT ----------
# Match <nav>...</nav> (NOT nav class="slide-dots" etc). Greedy inside block but bounded by </nav>.
# Must be followed optionally by <div class="nav-mobile-panel">...</div>
NAV_BLOCK_RE = re.compile(
    r'<nav>\s*.*?</nav>\s*(?:<div\s+class="nav-mobile-panel"[^>]*>.*?</div>\s*)?',
    re.DOTALL,
)


SITE_NAV_BLOCK_RE = re.compile(r'<nav class="site-nav">.*?</nav>\s*', re.DOTALL)


def replace_nav(html: str, active_page: str, *, insert_if_missing: bool = False) -> str:
    """Replace first <nav>...</nav>(+mobile-panel) or existing <nav class="site-nav">
    with unified nav. If neither is present and insert_if_missing, place after <body>.
    """
    new_nav = build_nav(active_page)
    if '<nav class="site-nav"' in html:
        # Replace the existing site-nav block with the new version (rebrand pass).
        html = SITE_NAV_BLOCK_RE.sub(new_nav + "\n\n", html, count=1)
    elif NAV_BLOCK_RE.search(html):
        html = NAV_BLOCK_RE.sub(new_nav + "\n\n", html, count=1)
    elif insert_if_missing:
        html = re.sub(r"(<body[^>]*>\s*)", f"\\1\n{new_nav}\n\n", html, count=1)
    return html


# ---------- INDEX SUB-NAV ----------
def inject_sub_nav(html: str) -> str:
    """For index.html: insert .sub-nav right after .site-nav."""
    if 'class="sub-nav"' in html:
        return html
    return re.sub(r"(</nav>\s*)", f"\\1\n{INDEX_SUB_NAV}\n\n", html, count=1)


# ---------- FOOTER INJECTION ----------
FOOTER_BLOCK_RE = re.compile(r'<footer class="site-footer">.*?</footer>\s*', re.DOTALL)


def inject_footer(html: str) -> str:
    """Insert/replace footer before </body> if possible, else before </html>, else append."""
    if FOOTER_BLOCK_RE.search(html):
        return FOOTER_BLOCK_RE.sub(FOOTER_HTML + "\n\n", html, count=1)
    if "</body>" in html:
        return html.replace("</body>", f"\n{FOOTER_HTML}\n\n</body>", 1)
    if "</html>" in html:
        return html.replace("</html>", f"\n{FOOTER_HTML}\n\n</html>", 1)
    return html + f"\n{FOOTER_HTML}\n"


# ---------- MAIN ----------
def process(path: Path) -> dict:
    name = path.name
    html = path.read_text(encoding="utf-8")
    original = html
    actions = []

    # 1. Head injection (all pages incl. nda)
    before = html
    html = inject_head(html)
    if html != before:
        actions.append("head(css+js)")

    # 2. Nav replacement
    if name in NAV_PAGES:
        before = html
        insert_if_missing = True  # all NAV_PAGES get nav, inserted if not present
        html = replace_nav(html, name, insert_if_missing=insert_if_missing)
        if html != before:
            actions.append("nav")

    # 3. Index sub-nav
    if name == "index.html":
        before = html
        html = inject_sub_nav(html)
        if html != before:
            actions.append("sub-nav")

    # 4. Footer (all pages incl. nda)
    before = html
    html = inject_footer(html)
    if html != before:
        actions.append("footer")

    if html != original:
        path.write_text(html, encoding="utf-8")
        return {"name": name, "changed": True, "actions": actions}
    return {"name": name, "changed": False, "actions": []}


def main():
    results = []
    for name in ALL_PAGES_FOR_FOOTER:
        path = ROOT / name
        if not path.exists():
            print(f"SKIP (missing): {name}")
            continue
        r = process(path)
        results.append(r)
        tag = "✓" if r["changed"] else "-"
        print(
            f"{tag} {r['name']:35s} {', '.join(r['actions']) if r['actions'] else '(no changes)'}"
        )

    changed = sum(1 for r in results if r["changed"])
    print(f"\n{changed} / {len(results)} files updated.")


if __name__ == "__main__":
    main()
