import urllib.request, sys, os

url = "https://www.vie-publique.fr/files/rapport/pdf/303867.pdf"
out = r"pdf\cdc_finances_2026.pdf"

proxies = [
    None,
    {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"},
    {"http": "socks5://127.0.0.1:10808", "https": "socks5://127.0.0.1:10808"},
]

for p in proxies:
    try:
        if p:
            op = urllib.request.build_opener(urllib.request.ProxyHandler(p))
        else:
            op = urllib.request.build_opener()
        op.addheaders = [("User-Agent", "Mozilla/5.0")]
        data = op.open(url, timeout=90).read()
        with open(out, "wb") as f:
            f.write(data)
        print("OK", len(data), "via", p)
        sys.exit(0)
    except Exception as e:
        print("FAIL", p, type(e).__name__, str(e)[:120])

sys.exit(1)
