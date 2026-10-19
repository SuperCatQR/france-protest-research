import re
s = open(r'C:\WorkSpace\调查研究\sources\actors-cross.md', encoding='utf-8').read()
required = ["RN","LFI","PS","EELV","PCF","Renaissance","LR","Horizons","MoDem",
            "CGT","CFDT","FO","UNL","FIDL","SNES-FSU","FCPE","MEDEF",
            "OHCHR","HRW","Amnesty","Mijatović","ECHR","Défenseur des droits","CNCDH"]
for r in required:
    print(f"{r:>22}: {s.count(r)}")
# CJK char count (body text, excluding URLs)
body = re.sub(r'https?://\S+', '', s)
cjk = len(re.findall(r'[\u4e00-\u9fff]', body))
print("\nCJK chars:", cjk)
print("Total chars:", len(s))
print("Non-space chars:", len(re.sub(r'\s', '', s)))
