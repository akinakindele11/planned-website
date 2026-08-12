import re, pathlib

NAV = pathlib.Path('_tpl_nav.html').read_text(encoding='utf-8')
POST = pathlib.Path('_tpl_post.html').read_text(encoding='utf-8')

GTAG = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-D8H1FF8BS4"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-D8H1FF8BS4');
    </script>
"""


def head(title, desc, keywords, url, depth, extra_ld=""):
    css = ('../' * depth) + 'css/style.css'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Planned Limited">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://plannedltd.co.uk/{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="https://plannedltd.co.uk/{url}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://plannedltd.co.uk/images/og-image.png">
    <meta property="og:site_name" content="Planned Limited">

    <title>{title}</title>
    <link rel="stylesheet" href="{css}">
{extra_ld}</head>"""


def crumbs(items):
    out = ['    <!-- Breadcrumbs -->', '    <div class="breadcrumbs">', '        <div class="container">']
    for i, (label, href) in enumerate(items):
        if i == len(items) - 1:
            out.append(f'            <span>{label}</span>')
        else:
            out.append(f'            <a href="{href}">{label}</a> &gt;')
    out += ['        </div>', '    </div>', '']
    return '\n'.join(out)


def hero(h1, sub, cta_text, cta_href):
    return f"""    <!-- Hero Section -->
    <section class="hero-service">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>{h1}</h1>
            <p>{sub}</p>
            <a href="{cta_href}" class="btn btn-primary">{cta_text}</a>
        </div>
    </section>
"""


def sec(h2, paras, lst=None):
    s = f'                    <section>\n                        <h2>{h2}</h2>\n'
    for para in paras:
        s += f'                        <p>{para}</p>\n'
    if lst:
        s += '                        <ul>\n'
        for li in lst:
            s += f'                            <li>{li}</li>\n'
        s += '                        </ul>\n'
    s += '                    </section>\n\n'
    return s


def intro(paras):
    s = '                    <section class="intro-section">\n'
    for para in paras:
        s += f'                        <p>{para}</p>\n'
    s += '                    </section>\n\n'
    return s


def sidebar(cta_h3, cta_p, cta_btn, info_h4, items, cta_href="/contact"):
    s = f"""                <div class="sidebar-cta-card">
                    <h3>{cta_h3}</h3>
                    <p>{cta_p}</p>
                    <a href="{cta_href}" class="btn btn-secondary">{cta_btn}</a>
                </div>

                <div class="sidebar-info-card">
                    <h4>{info_h4}</h4>
                    <ul>
"""
    for i in items:
        s += f'                        <li>{i}</li>\n'
    s += '                    </ul>\n                </div>\n'
    return s


def page(path, title, desc, keywords, url, depth, crumb, h1, sub, body, side,
         cta_h2, cta_p, cta_btn, cta_href="/contact", cta_text="Request this review", extra_ld=""):
    post = re.sub(
        r'(?s)(<section class="cta-section">\s*<div class="container">\s*)<h2>.*?</h2>\s*<p>.*?</p>\s*<a href="[^"]*" class="btn btn-primary btn-large">.*?</a>',
        lambda m: m.group(1) + f'<h2>{cta_h2}</h2>\n            <p>{cta_p}</p>\n            <a href="{cta_href}" class="btn btn-primary btn-large">{cta_btn}</a>',
        POST, count=1)
    doc = (head(title, desc, keywords, url, depth, extra_ld) + NAV + crumbs(crumb)
           + hero(h1, sub, cta_text, cta_href)
           + '\n    <!-- Main Content -->\n    <main class="container content-wrapper">\n        <div class="content-layout">\n'
           + '            <div class="content-main">\n                <div class="content-inner">\n'
           + body
           + '                </div>\n            </div>\n\n            <aside class="content-sidebar">\n'
           + side
           + '            </aside>\n        </div>\n    </main>\n\n' + post)
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(doc, encoding='utf-8')
    return path
