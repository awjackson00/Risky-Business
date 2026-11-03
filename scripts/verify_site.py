"""Verify copied static capstone pages and their local asset references."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path("docs")
REQUIRED = [
    "index.html",
    "results.html",
    "writeup.html",
    "reproducibility.html",
    "assets/css/style.css",
    "assets/figures/figure1.png",
    "assets/figures/figure2.png",
    "assets/figures/figure3.png",
    "assets/poster.pdf",
    "LICENSE",
]

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag in {"link", "script", "a", "img"}:
            target = data.get("href") if tag in {"link", "a"} else data.get("src")
            if target:
                self.targets.append(target)

errors = []
for path in REQUIRED:
    entry = ROOT / path
    if not entry.is_file() or entry.stat().st_size == 0:
        errors.append(f"Missing or empty: {path}")

for name in ["index.html", "results.html", "writeup.html", "reproducibility.html"]:
    file = ROOT / name
    if not file.is_file():
        continue
    html = file.read_text(encoding="utf-8")
    refs = References()
    refs.feed(html)
    for link in refs.targets:
        parsed = urlparse(link)
        if parsed.scheme or parsed.netloc or link.startswith(("#", "//", "mailto:", "tel:")):
            continue
        resolved = file.parent / unquote(parsed.path)
        if not resolved.exists():
            errors.append(f"Broken local reference in {name}: {link}")
    print(f"{name}: {len(refs.targets)} links/assets checked")

if errors:
    raise SystemExit("\n".join(errors))
print("Full Risky Business website and original asset references verified.")
