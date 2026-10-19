import re, sys
s = open(r'C:\WorkSpace\调查研究\sources\actors-cross.md', encoding='utf-8').read()
urls = sorted(set(re.findall(r'https?://[^\s\)\]<>"|]+', s)))
print("UNIQUE_URLS", len(urls))
for u in urls:
    print(u)
