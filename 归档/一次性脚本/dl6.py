import urllib.request,ssl
ctx=ssl.create_default_context();ctx.check_hostname=False;ctx.verify_mode=ssl.CERT_NONE
t={'ss_gend':'https://www.vie-publique.fr/files/rapport/pdf/288964.pdf',
   'ss_pref':'https://www.vie-publique.fr/files/rapport/pdf/288944.pdf',
   'ddd_2026_158':'https://www.bassinesnonmerci.fr/wp-content/uploads/2026/07/Decision-2026-158-du-Defenseur-des-droits.pdf',
   'senat_r18_450':'https://www.senat.fr/rap/r18-450/r18-4501.pdf'}
log=[]
for k,u in t.items():
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0'})
        d=urllib.request.urlopen(req,timeout=60,context=ctx).read()
        open(rf'.\pdf\{k}.pdf','wb').write(d); log.append(f'{k} OK {len(d)}')
    except Exception as e: log.append(f'{k} ERR {type(e).__name__} {str(e)[:70]}')
open(r'.\pdf\dl6.txt','w',encoding='utf-8').write('\n'.join(log)); print('\n'.join(log))
