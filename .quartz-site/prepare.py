#!/usr/bin/env python3
"""Copy the vault into Quartz's content/ folder and adapt it for the website.

Run by the GitHub Actions workflow:  python3 prepare.py <vault dir> <quartz content dir>
- skips Obsidian/Git/site folders,
- makes Home.md the homepage (index.md),
- rewrites figure embeds ![[file.svg|360]] into Markdown images with a vault-root path,
  because Quartz does not resolve the path of embedded SVG files.
"""
import os, re, shutil, sys
from urllib.parse import quote

vault, content = (os.path.abspath(p) for p in sys.argv[1:3])
SKIP_DIRS = {'.git', '.obsidian', '.github', '.quartz-site', '.trash', 'templates'}
IMG = re.compile(r'!\[\[([^\]|#]+?\.(?:svg|png|jpe?g|gif|webp))(?:\|[^\]]*)?\]\]', re.I)

shutil.rmtree(content, ignore_errors=True)
by_name = {}
for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for f in files:
        src = os.path.join(root, f)
        rel = os.path.relpath(src, vault)
        dst = os.path.join(content, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        by_name.setdefault(f, dst)

fixed = missing = 0
for root, _, files in os.walk(content):
    for f in files:
        if not f.endswith('.md'):
            continue
        p = os.path.join(root, f)
        s = open(p, encoding='utf-8').read()
        def repl(m):
            global fixed, missing
            target = m.group(1).strip()
            path = os.path.join(content, target) if os.path.exists(os.path.join(content, target)) else by_name.get(os.path.basename(target))
            if not path:
                missing += 1
                return m.group(0)
            fixed += 1
            return '![](' + quote(os.path.relpath(path, content).replace(os.sep, '/'), safe='/.-_~') + ')'
        t = IMG.sub(repl, s)
        if t != s:
            open(p, 'w', encoding='utf-8').write(t)

home = os.path.join(content, 'Home.md')
if os.path.exists(home):
    shutil.copy2(home, os.path.join(content, 'index.md'))
print(f'copied vault; rewrote {fixed} figure embeds ({missing} not found)')
