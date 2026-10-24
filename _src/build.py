"""Build the guitar practice app from the three page sources.

Run: python3 guitar/_src/build.py

Sources (artifact form, no html/head skeleton): fretboard-drills.html,
pentatonic-box-map.html, practice-tools.html. Placeholders {{DRILLS}},
{{BOXMAP}}, {{TOOLS}} and <!--SUITE:page--> markers are filled per target.

Offline app: guitar/index.html is ONE self-contained file holding all three
pages and the fonts. Sandboxed browsers (Flatpak Firefox) are only given the
file you open, so the app must not depend on any second file. The index.html
files in fretboardDrills/, pentatonicBoxMap/ and practiceTools/ are the same
app, opening on that page.

Online app: _src/app/ (index.html + box-map.html + tools.html), a multi-page
version for hosting as a claude.ai artifact; with ARTIFACT_URL set, also
_src/standalone-box-map.html. Both are build output and not committed.
"""
import base64, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GUITAR = os.path.dirname(HERE)  # this script lives in guitar/_src
APP_URL = os.environ.get('ARTIFACT_URL', '')  # optional: where the old stand-alone Box Map page should point
PAGES = [('drills', 'Fretboard Drills', 'basics', 'fretboard-drills.html'),
         ('boxmap', 'Pentatonic Box Map', 'scales', 'pentatonic-box-map.html'),
         ('tools', 'Tuner &amp; Metronome', 'tools', 'practice-tools.html')]
ARTIFACT = {'drills': 'index.html', 'boxmap': 'box-map.html', 'tools': 'tools.html'}
VIEWS = {'drills': '#drills', 'boxmap': '#boxmap', 'tools': '#tools'}
LOCAL_DIR = {'drills': 'fretboardDrills', 'boxmap': 'pentatonicBoxMap', 'tools': 'practiceTools'}
FONT_LINKS = re.compile(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\n'
                        r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\n'
                        r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2[^"]*">\n')
# Latin subsets from Google Fonts, SIL Open Font License 1.1. The first two are variable fonts.
FONTS = [('Big Shoulders Display', '700 800', 'big-shoulders-display.woff2'),
         ('Figtree', '400 700', 'figtree.woff2'),
         ('IBM Plex Mono', '500', 'ibm-plex-mono-500.woff2'),
         ('IBM Plex Mono', '600', 'ibm-plex-mono-600.woff2')]

def nav(cur, links):
    items = ['<span class="suite-label">Guitar practice</span>']
    for key, label, small, _ in PAGES:
        if key == cur:
            items.append(f'<span aria-current="page">{label}<small>{small}</small></span>')
        else:
            items.append(f'<a href="{links[key]}">{label}<small>{small}</small></a>')
    return '<nav class="suite" aria-label="Guitar practice pages">\n    ' + '\n    '.join(items) + '\n  </nav>'

def fill(src, cur, links, nav_html=None):
    s = src.replace(f'<!--SUITE:{cur}-->', nav_html or nav(cur, links))
    for key, ph in (('drills', '{{DRILLS}}'), ('boxmap', '{{BOXMAP}}'), ('tools', '{{TOOLS}}')):
        s = s.replace(ph, links[key])
    assert '{{' not in s and '<!--SUITE' not in s, cur
    return s

def wrap(s, cover):
    """Give a page its own document skeleton (artifact sub-pages and the offline views)."""
    s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
    s = s.replace('body{background:var(--paper);', 'body{margin:0;background:var(--paper);', 1)
    cut = s.index('</style>') + len('</style>')
    head, body = s[:cut], s[cut:].strip()
    vp = 'width=device-width, initial-scale=1' + (', viewport-fit=cover' if cover else '')
    safe = ('<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n'
            if cover else '')
    return (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="{vp}">\n'
            + safe + head + '\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')

def font_css():
    rules = []
    for family, weight, name in FONTS:
        data = base64.b64encode(open(os.path.join(HERE, 'fonts', name), 'rb').read()).decode()
        rules.append(f'@font-face{{font-family:"{family}";font-style:normal;font-weight:{weight};font-display:swap;'
                     f'src:url("data:font/woff2;base64,{data}") format("woff2")}}')
    return ''.join(rules)

# The offline shell: each page runs in its own iframe (srcdoc), created the first time it is shown
# and kept afterwards, so switching pages is instant and keeps state (a running metronome keeps going).
# Links to #drills, #boxmap and #tools inside a page change the shell's hash instead of navigating.
SHELL_JS = r'''(() => {
  'use strict';
  const PAGES = __PAGES__;
  const FONT_CSS = __FONTS__;
  const TITLES = {drills: 'Fretboard Drills', boxmap: 'Pentatonic Box Map', tools: 'Tuner & Metronome'};
  const START = __START__;
  const BRIDGE = `<script>document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest("a[href^='#']");if(!a)return;var v=a.getAttribute("href").slice(1);if(v==="drills"||v==="boxmap"||v==="tools"){e.preventDefault();parent.location.hash=v;}},true);<\/script>`;
  const frames = {};
  const current = () => { const h = location.hash.slice(1); return PAGES[h] ? h : START; };
  function show() {
    const v = current();
    if (!frames[v]) {
      const f = document.createElement('iframe');
      f.id = `view-${v}`;
      f.title = TITLES[v];
      f.setAttribute('allow', 'microphone; autoplay');
      f.srcdoc = PAGES[v].replace('</head>', `<style>${FONT_CSS}</style>${BRIDGE}</head>`);
      document.body.appendChild(f);
      frames[v] = f;
    }
    Object.keys(frames).forEach(k => { frames[k].hidden = k !== v; });
    document.title = TITLES[v];
    frames[v].focus();
  }
  window.addEventListener('hashchange', show);
  show();
})();'''

def shell(start, pages_json, fonts_json):
    js = (SHELL_JS.replace('__PAGES__', pages_json).replace('__FONTS__', fonts_json)
          .replace('__START__', json.dumps(start)))
    title = dict((k, l) for k, l, _, _ in PAGES)[start].replace('&amp;', '&')
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{title}</title>\n'
            '<!-- Guitar practice app (Fretboard Drills, Pentatonic Box Map, Tuner & Metronome), built by _src/build.py.\n'
            '     Everything is in this one file so it works offline and in sandboxed browsers.\n'
            '     Embedded fonts: Big Shoulders Display, Figtree, IBM Plex Mono (SIL Open Font License 1.1). -->\n'
            '<style>\nhtml,body{margin:0;height:100%;background:#EBEEF3}\n'
            '@media (prefers-color-scheme: dark){html,body{background:#0F1219}}\n'
            'iframe{position:fixed;inset:0;width:100%;height:100%;border:0;display:block}\n'
            'iframe[hidden]{display:none}\n</style>\n</head>\n<body>\n'
            '<noscript><p style="font-family:sans-serif;padding:16px">This app needs JavaScript turned on.</p></noscript>\n'
            f'<script>\n{js}\n</script>\n</body>\n</html>\n')

src = {k: open(os.path.join(HERE, f), encoding='utf-8').read() for k, _, _, f in PAGES}

# 1. Online app: one artifact, the drills page is its index, the others are sub-pages.
app = os.path.join(HERE, 'app'); os.makedirs(app, exist_ok=True)
for key, *_ in PAGES:
    page = fill(src[key], key, ARTIFACT)
    out = page if key == 'drills' else wrap(page, cover=True)
    assert 'claude.ai/artifact' not in out
    open(os.path.join(app, ARTIFACT[key]), 'w', encoding='utf-8').write(out)

# 2. The old stand-alone Box Map artifact now points to the app (only when ARTIFACT_URL is set).
if APP_URL:
    solo_nav = ('<nav class="suite" aria-label="Guitar practice pages">\n    <span class="suite-label">Guitar practice</span>\n'
                f'    <a href="{APP_URL}" target="_blank" rel="noopener">Open the full app<small>drills, box map, tuner and metronome</small></a>\n  </nav>')
    open(os.path.join(HERE, 'standalone-box-map.html'), 'w', encoding='utf-8').write(fill(src['boxmap'], 'boxmap', ARTIFACT, solo_nav))

# 3. Offline app: one self-contained file, no web addresses anywhere.
views = {}
for key, *_ in PAGES:
    page = fill(src[key], key, VIEWS)
    page, n = FONT_LINKS.subn('', page)
    assert n == 1, key
    views[key] = wrap(page.replace(' target="_blank" rel="noopener"', ''), cover=False)
# Escape "<" so nothing inside the JSON can close or confuse the shell's <script> element.
pages_json = json.dumps(views).replace('<', '\\u003c')
fonts_json = json.dumps(font_css())
outputs = {'index.html': 'drills'}
outputs.update({f'{d}/index.html': k for k, d in LOCAL_DIR.items()})
for rel, start in outputs.items():
    out = shell(start, pages_json, fonts_json)
    bad = re.findall(r'https?://[^\s"\'<)\\]+', out)
    assert not bad, (rel, bad[:5])
    assert out.count('</script>') == 1, rel
    path = os.path.join(GUITAR, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(out)
print(f'built: offline app ({len(out) // 1024} KB, one file) in {", ".join(outputs)}; online app in _src/app/')
