"""Apply the shared header (_tpl_nav.html) and footer (_tpl_post.html) to every page.

Run from the site root:  python3 _sync_layout.py
Idempotent: re-running after editing a template updates every page the same way.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
SKIP = {'_tpl_nav.html', '_tpl_post.html', 'google6813e7b730d20195.html'}

NAV = re.search(r'<nav class="navbar".*?</nav>', (ROOT / '_tpl_nav.html').read_text(encoding='utf-8'), re.S).group(0)
FOOTER = re.search(r'<footer class="footer".*?</footer>', (ROOT / '_tpl_post.html').read_text(encoding='utf-8'), re.S).group(0)
MAIN_JS = '<script src="/js/main.js"></script>'

NAV_RE = re.compile(r'(?:<header(?: class="header")?[^>]*>\s*)?<nav class="navbar"[^>]*>.*?</nav>(?:\s*</header>)?', re.S)
FOOT_RE = re.compile(r'<footer class="footer"[^>]*>.*?</footer>', re.S)
JS_RE = re.compile(r'[ \t]*<script src="[^"]*js/main\.js"[^>]*></script>\n?')


def sync(path):
    s = path.read_text(encoding='utf-8')
    orig = s
    s, n_nav = NAV_RE.subn(lambda m: NAV, s, count=1)
    s, n_foot = FOOT_RE.subn(lambda m: FOOTER, s, count=1)
    if not n_nav or not n_foot:
        print(f'WARN {path}: nav={n_nav} footer={n_foot}')
    s = JS_RE.sub('', s)
    s = re.sub(re.escape(FOOTER) + r'\s*', lambda m: FOOTER + '\n\n    ' + MAIN_JS + '\n', s, count=1)
    if s != orig:
        path.write_text(s, encoding='utf-8')
        return True
    return False


if __name__ == '__main__':
    changed = 0
    for p in sorted(ROOT.rglob('*.html')):
        if p.name in SKIP or '.git' in p.parts:
            continue
        changed += sync(p)
    print(f'{changed} pages updated')
