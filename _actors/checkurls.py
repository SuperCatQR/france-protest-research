import urllib.request, ssl, sys
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

urls = [
 "https://www.leparisien.fr/politique/gilets-jaunes-comment-se-positionnent-les-partis-politiques-29-11-2018-7957161.php",
 "https://www.lepoint.fr/politique/les-gilets-jaunes-divisent-les-partis-politiques-14-11-2018-2271513_20.php",
 "https://www.tf1info.fr/societe/exclusif-sondage-lci-pres-d-un-francais-sur-deux-soutient-le-mouvement-de-contestation-des-lyceens-2468625.html",
 "https://www.ladepeche.fr/2019/03/19/pourquoi-fo-ne-participe-pas-a-la-manifestation-intersyndicale-daujourdhui,8077060.php",
 "https://www.aefinfo.fr/depeche/617591-69-des-francais-soutiennent-le-mouvement-du-5-decembre-contre-la-reforme-des-retraites-sondage-harris-interactive-rtl-aef-info",
 "https://www.caradisiac.com/hausse-des-prix-des-carburants-la-carte-des-blocages-prevus-le-17-novembre-172150.htm",
 "https://altermidi.org/2018/11/17/la-gauche-face-aux-gilets-jaunes-du-malaise-au-soutien/",
 "https://www.senat.fr/dossier-legislatif/ppl17-575.html",
 "https://www.vie-publique.fr/dossierlegislatif/JORFDOLE000047022789",
 "https://www.conseil-constitutionnel.fr/decision/2023/2023849DC.htm",
 "https://www.ouest-france.fr/politique/bloquons-tout-le-10-septembre-quels-partis-politiques-soutiennent-le-mouvement-8704bbcc-7e5d-11f0-a01f-a0b34f4aa520",
 "https://www.publicsenat.fr/actualites/societe/bloquons-tout-le-10-septembre-qui-la-soutient-qui-sen-tient-a-distance",
 "https://www.humanite.fr/social-et-economie/mobilisations-retraites/retraites-65-des-francais-pour-la-greve-reconductible-des-ce-7-mars-785214",
 "https://www.franceinfo.fr/economie/retraite/reforme-des-retraites/reforme-des-retraites-l-intersyndicale-veut-amplifier-le-mouvement-mais-rejette-par-avance-la-responsabilite-d-eventuels-debordements_5716793.html",
 "https://www.ici.fr/infos/economie-social/reforme-des-retraites-la-gauche-denonce-une-regression-sociale-le-rn-veut-faire-barrage-5251153",
 "https://www.europe1.fr/societe/sondage-blocus-des-lycees-73-des-francais-favorables-a-la-suspension-de-lexcuse-de-minorite-pour-les-jeunes-qui-participent-a-des-violences-1148459",
 "https://www.franceinfo.fr/societe/education/parcoursup/parcoursup/direct-lycees-nouvelle-journee-de-blocages-apres-les-700-interpellations-de-jeudi_3088959.html",
 "https://www.snetap-fsu.fr/Communique-de-presse-de-l-intersyndicale-du-seconde-degre-et-des-organisations.html",
 "https://upr-info.org/sites/default/files/country-document/2023-04/HRW_UPR43_FRA_E_Main.pdf",
 "https://www.defenseurdesdroits.fr/sites/default/files/2023-03/DDD_Rapport-maintien-ordre_201712.pdf",
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def check(u):
    try:
        req = urllib.request.Request(u, headers={"User-Agent": UA, "Accept-Language": "fr-FR,fr;q=0.9"})
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            return (r.status, u)
    except Exception as e:
        code = getattr(e, "code", None)
        return (code if code else type(e).__name__, u)

with ThreadPoolExecutor(max_workers=8) as ex:
    for st, u in ex.map(check, urls):
        print(f"{str(st):>18}  {u}")
