import sys, re, os
import fitz  # PyMuPDF

def pdf2txt(path, out=None):
    doc = fitz.open(path)
    parts = []
    for i, page in enumerate(doc):
        parts.append(f"\n===== p.{i+1} =====\n" + page.get_text("text"))
    txt = "".join(parts)
    txt = re.sub(r"[ \t\xa0]+", " ", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    if out:
        open(out, "w", encoding="utf-8").write(txt)
        return out, len(txt), len(doc)
    return None, len(txt), len(doc)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        out = os.path.splitext(p)[0] + ".txt"
        o, n, pages = pdf2txt(p, out)
        print(f"{p} -> {o}  chars={n} pages={pages}")
