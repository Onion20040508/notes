#!/usr/bin/env python3
"""Finish the site Quartz built: add the page-style switcher and slim the search index.

Run by the GitHub Actions workflow after the build:  python3 postbuild.py <site dir> <looks.js>
- copies looks.js to <site>/static/looks.js,
- adds to each page's <head>: an inline script that applies the saved look before the page is drawn,
  the extra Google Fonts the looks use, and looks.js itself.
  The tags carry data-persist, so Quartz keeps them when it swaps pages without a reload.
- slims the search index (static/contentIndex.json): Quartz's search downloads it on every page load
  and indexes every word in the browser, which made each load lag (27 MB, 3.3 million words for this
  vault). Each page keeps its opening text and its box titles ("Definition §23.2: Fundamental Group"),
  which is what search needs to find a definition or a theorem.
"""
import json, os, re, shutil, sys

site, js = (os.path.abspath(p) for p in sys.argv[1:3])
os.makedirs(os.path.join(site, 'static'), exist_ok=True)
shutil.copy2(js, os.path.join(site, 'static', 'looks.js'))

FONTS = ('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500'
         '&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400'
         '&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap')
HEAD = re.compile(r'<head[^>]*>')

pages = 0
for root, _, files in os.walk(site):
    for f in files:
        if not f.endswith('.html'):
            continue
        p = os.path.join(root, f)
        s = open(p, encoding='utf-8').read()
        m = HEAD.search(s)
        if not m or 'static/looks.js' in s:
            continue
        # absolute path, so it also works on 404.html, which GitHub serves at any address
        base = re.search(r'data-basepath="([^"]*)"', s)
        src = (base.group(1) if base else '') + '/static/looks.js'
        tags = ('<script data-persist>try{var l=localStorage.getItem("site-look");'
                'if(l)document.documentElement.setAttribute("data-look",l)}catch(e){}</script>'
                f'<link data-persist rel="stylesheet" href="{FONTS}">'
                f'<script data-persist defer src="{src}"></script>')
        open(p, 'w', encoding='utf-8').write(s[:m.end()] + tags + s[m.end():])
        pages += 1
print(f"added the page-style switcher to {pages} pages")

KIND = re.compile(r'^[ \t]*((?:Definition|Theorem|Lemma|Proposition|Corollary|Example|Remark|Principle|Law|Model'
                  r'|Notation|Caution|Derivation|Axiom|Exercise|Problem|Procedure)\b[^\n]{0,160})', re.M)
index = os.path.join(site, 'static', 'contentIndex.json')
if os.path.exists(index):
    before = os.path.getsize(index)
    data = json.load(open(index, encoding='utf-8'))
    for entry in data.values():
        text = entry.get('content') or ''
        titles = [m.group(1).strip() for m in KIND.finditer(text)]
        entry['content'] = re.sub(r'\s+', ' ', text[:1200])[:600] + '\n' + '\n'.join(dict.fromkeys(titles))
    with open(index, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    print(f'search index: {before / 2**20:.1f} MB -> {os.path.getsize(index) / 2**20:.1f} MB')
