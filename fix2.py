import re, os, glob

base = r'c:\Users\Ashley\OneDrive\Documents\VCS\vcs_new'
os.chdir(base)

pattern = re.compile(r'(<a\s[^>]*class="footer-social-media-icon"[^>]*>)\s*</a>', re.DOTALL)
icons = ['&#xf39e;', '&#xf16d;', '&#xf08c;']  # FB, IG, LI

for fpath in glob.glob('**/*.html', recursive=True):
    with open(fpath, 'r', encoding='utf-8') as f:
        txt = f.read()
    matches = list(pattern.finditer(txt))
    if not matches:
        continue
    count = [0]
    def replacer(m):
        icon = icons[count[0] % 3]
        count[0] += 1
        return m.group(1) + icon + '</a>'
    txt2 = pattern.sub(replacer, txt)
    if txt2 != txt:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(txt2)
        print('Fixed icons:', fpath)

# Also verify graphics-design link in index.html
idx = 'index.html'
with open(idx, 'r', encoding='utf-8') as f:
    txt = f.read()

if 'href="/services-subpages/web-design.html" class="services-single last' in txt:
    txt = txt.replace(
        'href="/services-subpages/web-design.html" class="services-single last',
        'href="/services-subpages/graphics-design.html" class="services-single last'
    )
    with open(idx, 'w', encoding='utf-8') as f:
        f.write(txt)
    print('Fixed graphics link in index.html')
else:
    print('Graphics link check: already OK or pattern different')
    import re as re2
    m = re2.search(r'gd01-graphic-design.*?href="([^"]+)"', txt, re2.DOTALL)
    if m:
        print('  Current graphics href:', m.group(1))

print('All done!')
