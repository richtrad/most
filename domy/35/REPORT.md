# Čp. 35 – celá pracovní varianta domu, r8b / balík r9

Výsledky jsou pouze lokální. Původní fotografie, modely i všechny rozpracované varianty zůstaly zachované. Tento balík obsahuje celý pracovní dům; **nejde dosud o plně metricky a historicky validovanou rekonstrukci**. Celý plán všech rohových domů stále běží.

## Provedené opravy

- Obě uliční fasády z místních zdrojů: A má čtyři horní okna, B šest. Dřívější čtyřosý FRONT z Úzké byl zamítnut jako podklad pro celou dlouhou stěnu.
- Celkem 18 otvorů (A 8, B 10), 730 dílčích ploch stěn a zapuštěných výplní; 84 návratových ploch ostění a říms. Skutečné fotografické rámy, výplně, izolátory a poškození zůstávají převážně ve fotografické textuře. Hloubky otvorů 0,08–0,24 m a vystoupení říms jsou modelové hypotézy.
- Odstraněna předstupující lampa a potrubí ve zdrojovém B. Doplněny pouze maskované chybějící okraje a návratové materiály; čtyři skutečné builtin editace pro tento dům, celkem 24 ve v5. Geometrická obrazová reference B zachovává luminanci původní fotografie mimo rekonstrukční masky. Známé pixely při skládání generovaných doplňků jsou chráněné.
- Opravená orientace hřebene podle původní nárožní fotografie: rovnoběžně s krátkou čtyřosou fasádou A. Převzatý model měl orientaci opačnou. Nový povrch krytiny navazuje na zděděné zalomení půdorysu, uzavřené jsou i skryté stěny. Výška okapu 8 m, hřebene 11,75 m a jeho délka 6,4 m zůstávají pracovní parametry, nikoli fotograficky změřené hodnoty.
- Opravené mezery zadních stěn z prvního pokusu výměny střechy: stěny jsou nyní řezané přesně v okapové rovině, nikoli odstraňované celé trojúhelníky přes tuto rovinu. Dva opakované rohové vrcholy smyček nové střechy způsobovaly nulové exportní trojúhelníky; odstraněny pouze tyto nulové části.
- Závěrečné sladění modrošedých omítek podle A: B RGB násobky 1,015849 / 1,009904 / 0,976489 v masce omítky. Okna, zdivo a ostatní chráněné části mimo masku beze změny. Skrytá omítka sladěna samostatně. Historický odstín není doložený; všude model_hypothesis / provisional / locked:false. Tato barevná úprava nepoužila novou generaci.
- Opravená místní klasifikace tří konkrétních souborů z PLANE na PHOTO_BW po vizuální kontrole jejich obsahu. Původní soubory ani vzdálená metadata nebyly upravené. Z originálu B 2160 × 2930 px byla do výsledného FRONTu 3352 × 1280 px vrácena zdrojová luminance. Registrace: 3800 geometricky souhlasných bodů, medián chyby 0,093 px v rozlišení původního menšího výřezu; nejde o přesnost 3D/GIS. Rekonstruované oblasti zachovány přesně, přechod do zdrojové luminance má 16px vnitřní náběh. Bez generativního doostření.

## Výsledky kontrol

Fresh GLB import: **5 vložených obrazů, 2387 texturovaných trojúhelníků, 0 kolapsů UV, odchylka vrcholů 0.0 m**. Změna vysokého rozlišení zachovává geometrii i UV. Kontrola exportu sama nepotvrzuje historickou přesnost. V balíku jsou čtyři rendery, nový import, zdroje, fronty, geometrické a barevné QA a lokální 3D prohlížeč s původním modelem ze zálohy.

Původní fotografie B je velmi šikmá a na vzdáleném konci rozostřená. Větší zdroj zlepšuje dostupné detaily, ale z nejvzdálenější části nevytváří stejně ostrou referenci jako z bližší. Přesná ortorektifikace a nestejnoměrné poměry oken zůstávají k další kalibraci. Čtyři horní okna A a šest B jsou zachovány; jemné prostorové členění rámů není samostatně dokončené.

## GIS a hranice platnosti

Lokální GIS čp. 35 / objekt 92 leží na rohu Horovy a Úzké mezi čp. 34 a 36. Kandidátní párování uličních hran je uvedené v registration.json a v překryvu mapy. Krátká stěna modelu má 14,1 m proti 12,3347 m v GIS, dlouhá 19,14 m proti 19,5925 m. Tříbodový afinní návrh má hlavní měřítka 1,032764 a 0,864007. Zadní konec převzatého zalomení nesouhlasí s protějším GIS rohem o 1,7224 m; nejde o nezávisle změřenou chybu GIS.

**Tři fitované body nejsou nezávislá validace. Transformace nebyla aplikována do GLB a model není vydáván za georeferencovaný.** EPSG:5514 a lokální počátek byly ověřené zpětným převodem; náhodná výšková náhrada GIS 10,3 m nebyla použita. Původní dvorní fotografie ukazuje vnitřní průchod/úzký dvůr; příslušnost jednotlivých dvorních stěn k vnějšímu půdorysu zatím nebyla určena. Vnější skryté stěny modelu proto zůstávají jednoduchou hypotézou, vnitřní dvůr není rekonstruovaný.

K plnému uzavření zbývá zdrojově navázat šířku A a zadní půdorys, výšku a délku hřebene, případný komín/menší střešní prvky a příslušnost dvorní fotografie. Neuzavřené části nejsou důvodem znovu dělat hotová ostění či inventuru. Čp. 174 má obdobně otevřenou nezávislou metrickou/roof validaci; jeho dosavadní balík zůstává zachovaný. **Počet plně validovaných domů v celém plánu je stále 0.**

## Použití

Spusťte `python serve.py` a otevřete `http://127.0.0.1:8773/`. Server zpřístupňuje jen tento lokální balík; knihovny Three.js jsou přibalené. GLB a Blender lze otevřít samostatně. Přiložený manifest a kontrola ZIP dokládají byteovou integritu. Zápisy do živé Libuše a uploady: 0.
