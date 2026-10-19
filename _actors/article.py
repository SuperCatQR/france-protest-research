import sys, re, html, urllib.request, gzip, zlib

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def get(url, timeout=45):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        enc = r.headers.get("Content-Encoding", "")
        if "gzip" in enc: data = gzip.decompress(data)
        elif "deflate" in enc: data = zlib.decompress(data)
        return data, r.headers.get("Content-Type","")

def clean(s):
    s = re.sub(r"(?is)<(script|style|noscript|svg|head|footer|nav)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h[1-6]>|</li>|</tr>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s

def paras(s):
    # keep lines that look like prose
    out=[]
    for ln in s.split("\n"):
        ln=ln.strip()
        if len(ln) < 60: continue
        out.append(ln)
    return out

for url in sys.argv[1:]:
    try:
        raw, ct = get(url)
        s = clean(raw.decode("utf-8","replace"))
        ps = paras(s)
        print("#### ", url, f"({len(ps)} paras)")
        for p in ps[:45]:
            print(p)
        print()
    except Exception as e:
        print("#### ", url, "ERR", repr(e)[:200])
