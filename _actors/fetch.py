import sys, re, io, os, gzip, zlib
import urllib.request, urllib.error

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
        if "gzip" in enc:
            data = gzip.decompress(data)
        elif "deflate" in enc:
            data = zlib.decompress(data)
        ct = r.headers.get("Content-Type", "")
        return data, ct

def to_text(raw, ct):
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            s = raw.decode(enc)
            break
        except Exception:
            continue
    else:
        s = raw.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style|noscript|svg|head)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h[1-6]>|</li>|</tr>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    import html as _h
    s = _h.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()

if __name__ == "__main__":
    url = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    raw, ct = get(url)
    if "pdf" in ct.lower() or url.lower().endswith(".pdf"):
        if out:
            open(out, "wb").write(raw)
            print("SAVED_PDF", out, len(raw))
        else:
            print("PDF", len(raw))
        sys.exit(0)
    txt = to_text(raw, ct)
    if out:
        open(out, "w", encoding="utf-8").write(txt)
        print("SAVED", out, len(txt))
    else:
        print(txt)
