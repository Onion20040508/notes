#!/usr/bin/env python3
"""Copy the vault into Quartz's content/ folder and adapt it for the website.

Run by the GitHub Actions workflow:  python3 prepare.py <vault dir> <quartz content dir>
- skips Obsidian/Git/site folders,
- makes Home.md the homepage (index.md),
- rewrites figure embeds ![[file.svg|360]] into Markdown images with a vault-root path,
  because Quartz does not resolve the path of embedded SVG files,
- rewrites links to folder notes ([[Topology]] for Math/Topology/Topology.md) into folder links
  ([[Math/Topology/|Topology]]): Quartz turns a folder note into the folder's page but then
  resolves [[Topology]] to a page that does not exist,
- rewrites two math spellings that Obsidian (MathJax) accepts but Quartz's math parser does not:
  a multi-line $$ block with formula text on its $$ lines gets each $$ on a line of its own,
  and \\$ inside math becomes {\\char36}.
Only the copy in content/ is changed; the vault itself is never touched.
"""
import os, re, shutil, sys
from urllib.parse import quote

vault, content = (os.path.abspath(p) for p in sys.argv[1:3])
SKIP_DIRS = {'.git', '.obsidian', '.github', '.quartz-site', '.trash', 'templates'}
IMG = re.compile(r'!\[\[([^\]|#]+?\.(?:svg|png|jpe?g|gif|webp))(?:\|[^\]]*)?\]\]', re.I)
LINK = re.compile(r'(?<!!)\[\[([^\]#|\\]+?)(\\?\|[^\]]*)?\]\]')
FENCE = re.compile(r'^[ \t>]*(```|~~~)')
DISPLAY = re.compile(r'^([ \t>]*)\$\$(.+?)\$\$', re.M | re.S)
DOLLAR = '{\\char36}'

shutil.rmtree(content, ignore_errors=True)
by_name = {}
folder_notes = {}  # lower-case note name -> folder path, for notes named like their folder
for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for f in files:
        src = os.path.join(root, f)
        rel = os.path.relpath(src, vault)
        dst = os.path.join(content, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        by_name.setdefault(f, dst)
        if f.endswith('.md') and f[:-3] == os.path.basename(root):
            folder_notes[f[:-3].lower()] = os.path.dirname(rel).replace(os.sep, '/')

counts = dict(figures=0, missing=0, folder_links=0, fences=0, dollars=0)


def fix_figure(m):
    target = m.group(1).strip()
    path = os.path.join(content, target) if os.path.exists(os.path.join(content, target)) else by_name.get(os.path.basename(target))
    if not path:
        counts['missing'] += 1
        return m.group(0)
    counts['figures'] += 1
    return '![](' + quote(os.path.relpath(path, content).replace(os.sep, '/'), safe='/.-_~') + ')'


def fix_links(line):
    in_table = line.lstrip(' \t>').startswith('|')
    def repl(m):
        name = m.group(1).strip()
        folder = folder_notes.get(name.lower())
        if not folder:
            return m.group(0)
        counts['folder_links'] += 1
        alias = m.group(2) or ('\\|' if in_table else '|') + name
        return f'[[{folder}/{alias}]]'
    return LINK.sub(repl, line)


def fix_display(prefix, body):
    if '\\$' in body:
        counts['dollars'] += body.count('\\$')
        body = body.replace('\\$', DOLLAR)
    lines = body.split('\n')
    if len(lines) > 1:
        # Quartz reads a $$ line like a code fence: text after the opening $$ is dropped and the
        # block only ends at a $$ on a line of its own.
        if lines[0].strip():
            body = '\n' + prefix + body
            counts['fences'] += 1
        if lines[-1].lstrip(' \t>').strip():
            body = body + '\n' + prefix
    return f'{prefix}$${body}$$'


def fix_inline(line):
    """Replace \\$ inside $...$ spans of one line; \\$ in plain text stays as it is."""
    if '\\$' not in line:
        return line
    out, i = [], 0
    while i < len(line):
        c = line[i]
        if c == '\\':
            out.append(line[i:i + 2]); i += 2; continue
        if c == '$' and not line.startswith('$$', i):
            j = i + 1
            while j < len(line) and line[j] != '$':
                j += 2 if line[j] == '\\' else 1
            if j < len(line):
                span = line[i + 1:j]
                counts['dollars'] += span.count('\\$')
                out.append('$' + span.replace('\\$', DOLLAR) + '$'); i = j + 1; continue
        out.append(c); i += 1
    return ''.join(out)


def fix_text(text):
    """Apply the link and math fixes to markdown outside code blocks."""
    parts = DISPLAY.split(text)  # [text, prefix, body, text, prefix, body, ...]
    res = []
    for k in range(0, len(parts), 3):
        res.append('\n'.join(fix_inline(fix_links(l)) for l in parts[k].split('\n')))
        if k + 2 < len(parts):
            res.append(fix_display(parts[k + 1], parts[k + 2]))
    return ''.join(res)


for root, _, files in os.walk(content):
    for f in files:
        if not f.endswith('.md'):
            continue
        p = os.path.join(root, f)
        s = open(p, encoding='utf-8').read()
        t = IMG.sub(fix_figure, s)
        # split off fenced code blocks; only the text between them is rewritten
        chunks, buf, in_code = [], [], False
        for line in t.split('\n'):
            if FENCE.match(line):
                if not in_code:
                    chunks.append((False, buf)); buf = []
                buf.append(line)
                if in_code:
                    chunks.append((True, buf)); buf = []
                in_code = not in_code
                continue
            buf.append(line)
        chunks.append((in_code, buf))
        t = '\n'.join(('\n'.join(b) if code else fix_text('\n'.join(b))) for code, b in chunks if b)
        if t != s:
            open(p, 'w', encoding='utf-8').write(t)

home = os.path.join(content, 'Home.md')
if os.path.exists(home):
    # Without a title Quartz names the page after its file ("index"); the page shows the title
    # above the text, so the note's own "# Home" heading is dropped to avoid showing it twice.
    s = open(home, encoding='utf-8').read()
    if not s.startswith('---\n'):
        s = '---\ntitle: Home\n---\n' + re.sub(r'\A# Home\n+', '', s)
    open(os.path.join(content, 'index.md'), 'w', encoding='utf-8').write(s)
print('copied vault; rewrote {figures} figure embeds ({missing} not found), {folder_links} folder-note links, '
      '{fences} $$ blocks with formula text on the $$ lines, {dollars} \\$ inside math'.format(**counts))
