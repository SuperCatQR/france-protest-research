import sys, re, html, urllib.request, gzip, zlib

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def get(url, timeout=40):
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

for url in sys.argv[1:]:
    try:
        raw, ct = get(url)
        s = raw.decode("utf-8", "replace")
        out = []
        for m in re.finditer(r'(?is)<meta[^>]+(?:name|property)\s*=\s*["\'](og:description|description|og:title|twitter:description)["\'][^>]*>', s):
            tag = m.group(0)
            c = re.search(r'(?is)content\s*=\s*["\'](.*?)["\']', tag)
            if c:
                out.append((m.group(1), html.unescape(c.group(1))))
        # JSON-LD description
        for m in re.finditer(r'(?is)"description"\s*:\s*"(.*?)"', s):
            d = m.group(1)
            if len(d) > 80:
                out.append(("jsonld", html.unescape(d.replace('\\"','"'))))
        print("=== ", url)
        seen=set()
        for k,v in out:
            if v in seen: continue
            seen.add(v)
            print(f"[{k}] {v[:900]}")
        print()
    except Exception as e:
        print("=== ", url, "ERR", e)
