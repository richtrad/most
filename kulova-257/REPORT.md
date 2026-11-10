# Kulová čp. 257 — rekonstrukce SOL 6.1

Nový pracovní model torza domu z obou archivních karet a situačního náčrtu. Předchozí modely a originály zůstaly zachované. Výstupy: editovatelný Blender, samostatný GLB s vloženými texturami, lokální web a úplná sada kontrolních kamer. Zpracovatel geometrie, registrace, skriptů a kontroly: SOL 6.1; rasterové doplnění prováděl samostatný vestavěný obrazový model.

## Prameny a první krok

Živá metadata Libuše ověřena 2. 10. 2026. Vyhledány přílohy 257, 256, 258, širší řady 259–261 a 265–267; posouzena metadata celé oblasti a společné přílohy. Pro 257 nalezen situační náčrt, dvě označené archivní karty a původní fotografie. Osmnáct sousedních plánových listů bylo otevřeno ve třech přehledech; chybějící společný plán 261/262/263 byl nově stažen. Rozsah, zdrojová ID, datum a omezení jsou v plan_search.json. Náčrt 257/1 nemá ověřené datum ani měřítko, nenahrazuje stavební zaměření. Půdorysy různých sousedních domů se nepoužily jako rozměry 257.

## Geometrie a registrace G

Pět samostatných fotoploch, 13 otvorů (9 oken, 2 dveře a 2 nízké klenuté otvory). Fotografie byla perspektivně registrována na roviny; pak se upravovala geometrie otvorů podle hran podkladu. Nešlo o variantu T: fasádní otvory se nepřegenerovávaly, aby zakryly chybu modelu. U zadních otvorů se zaznamenaly čtyři hrany, protože prostý obdélník nechával na zdi fotografický klín. Jejich zdánlivé zešikmení není doložené zaměření deformace stavby. Která část je perspektivní chyba a která poškození, z pramenů přesně nepoznáme.

Ostění je průchozí a má vlastní metrické UV; dochované rámové pásy jsou samostatné. Nepřidávalo se nové sklo ani obnovená křídla. První okno z uličního snímku ponechává doložené zakrytí. Parapety mají lokální C: 8 mm / 3 segmenty. Hlavní dveře mají mělký práh, bez kopírování schodů čp. 261. Okapy ani vikýře nejsou v tomto torzu přesvědčivě doložené, proto nevznikly. Architektura nebyla opravena do obydleného stavu.

Rozměry vycházejí z přibližného GIS obrysu a poměrů na snímcích. Jednotlivé výšky a spojení krovu nejsou měřené. Orientace lokálních souřadnic odpovídá rohové fotografii; model není georeferencovaný do městské sestavy. Záznam geometry_hypotheses.json odlišuje konkrétní odhady od dokladů.

## Materiálové doplnění a opravy

Vytvořeny dva skutečné obrazové edity s uloženými cíli, maskami, prompty, raw výstupy a chráněnými kompozity. První doplnil omítku, dřevo a cihly pro nové hloubkové plochy. Keramická řada byla vizuálně odmítnuta: vypadala jako cihly, proto se na střechu používá skutečný fotografický donor krytiny. Druhý edit doplnil zakrytý spodek přístavby a odstranil duplicitní fotografický pás krovu v horní části zadní zdi. Pozdější maska tohoto pásu byla rozšířena z 28 na 85 px podle renderu; všechny otvory zůstaly chráněné. Oba kompozity mají maximální změnu chráněného pixelu **0**. Toto ověřuje ochranu dat, nikoli historickou správnost nového obsahu.

Po prvních renderech se ztmavilo ostění i interiér a zavedla neutrální prezentační podstava. Exportér Blenderu nepřenesl konstantní násobení barvy MixRGB; proto build.py explicitně uloží stejný standardní glTF baseColorFactor. Textury střechy a trámů se nepromítají z průčelí. Nepřidáváme historický detail pouhým zvětšením bitmapy: skutečné barevné zdroje mají 1464×1074 a 1486×1059 px; rektifikované plochy mají 1536/1200/960×640 px.

## Střecha, historická nejistota a stav dávky

Fotografie rozhodují o stavu po rozebrání střechy: otevřený trámový krov, omezené pásy krytiny a tři viditelné komíny. Situační náčrt ukazuje složitější střechu s další větví a čtvrtým značkovým komínem. Nelze bez dalšího tvrdit, že náčrt a fotografie zachycují stejnou etapu bourání. Současný model používá pravidelný pracovní krov a nízké odkryté křídlo. **Přesné prostorové přiřazení zadní větve a historická podoba styku střech zůstávají neuzavřené.** To není opraveno inpaintingem ani ukryto pod texturu. Obrys a tesařská konstrukce jsou výslovně hypotézy; model se automaticky nepropaguje do městské ulice. Batch může být technicky integritní a současně blokovaný pro tento historický geometrický důkaz.

## Kontroly a reprodukce

Každý otvor má front/left/right kameru s texturami i clay. Dále čtyři hlavní osy, čtyři střešní rohy, nároží, práh i pohled pod něj, omítkové poškození, krov, komíny, přístavba a klik na originály a plán. Kamery, expozice 0,8, hash konkrétního GLB a nálezy jsou v qa/cameras.json a qa/visual_qa.json. Technická kontrola reopen_audit.json potvrdila znovuotevření BLEND a vložené obrazové zdroje; nenahrazuje vizuální kontrolu.

Spuštění: `start_viewer.ps1`, web na http://127.0.0.1:8806/web/. `build.py` spustit přes Blender 4.5 na hotových texturách a openings.json; `render.cjs` přes Node s Playwright/Edge vytvoří celou sadu znovu. Přípravné a iterační skripty jsou historický záznam jednorázových kroků, některé nejsou idempotentní; nespouštět je všechny znovu nad finálními texturami. Původní model je v models/initial, první snímky v qa/initial.

## Porovnání SOL a Astra a využití

Renderer odpovídá předchozímu projektu: stejné světlo, ACES, expozice 0,8. Jde však o jiný dům, jiné zdroje a odlišnou geometrii. Nelze připsat rozdíl kvality pouze modelu ani vyhlásit kontrolovaný A/B výsledek. SOL vytvořil tento samostatný pracovní výsledek; Astra se v této úloze nespouštěla. Zdrojová kolorování vznikla dříve a AI inpainting používá samostatný obrazový model.

Využití účtu začalo na 63 %, po rešerši bylo 64 % a při pozdějších korekcích 65 %. Aktuální poslední odečet je v evidence/usage.json. Zaokrouhlená procenta účtu nejsou přesné tokeny domu ani jednotlivých fází; přesné pořadí tokenové náročnosti z nich nelze určit.

## Závěrečný záznam

110 kontrolních renderů, 13 otvorů se 3 texturovanými a 3 clay pohledy. Web: 7 posuvníků, žádné chybějící odkazy ani mobilní přetečení. BLEND znovu otevřen, 10 použitých souborových obrázků zabaleno; GLB má 9 vložených obrazových zdrojů po exportní deduplikaci. 4600 trojúhelníků, žádné degenerované UV. Integrita dávky ověřena; tři zadní fasády zůstávají model_side_review_required. Celkové QA passed=false kvůli historické geometrii, nikoli proto, že by selhalo načtení.

Práh byl při poslední kontrole výškově připojen ke spodku registrovaného dveřního otvoru; zdivo jej podpírá, pozice vzhledem k původnímu terénu zůstává odhad. Zbytek krytiny přesunut na zadní svah podle dvojice fotografií. Metrické UV opraveno na přibližné opakování 0,5 m pro fotografický donor tašek a 1,2 × 0,5 m pro cihlový donor, nikoli přehnaně velké jednotky.

Poslední měření využití: 65 %, změna proti začátku +2 procentní body. To není přesný počet tokenů.
