# Žatecká (Čs. armády): zpráva o 3D modelu ulice a jeho pramenech

Dávka `zatecka_street_claude_2026-10-17`, zpracování Claude (Anthropic) pro projekt MOST, GRAFIT FIT ČVUT, 17.–18. 10. 2026, revize r4 23.–26. 10. 2026. Web: https://grafitctu.github.io/most/zatecka/

Zpráva shrnuje výběr ulice, prameny, postup, soubory, hypotézy a kontrolu. Druhá část uvádí u každého domu identitu a všechny přílohy.

## Proč právě Žatecká

Zadání znělo: okrajová ulice daleko od centra, která v databázi Libuše nemá žádný 3D model, ale má dost domů a fotografií. Ze živého seznamu 150 oblastí (stav 17. 10. 2026) jsme oblasti seřadili podle vzdálenosti jejich domů od 1. náměstí v GIS a podle počtu domů, fotografií a modelů.

Žatecká vyhověla nejlépe: 25 čísel popisných, žádný model, fotografie u všech domů a situační náčrt u 24 z nich. Domy s GIS půdorysem leží 480 až 850 m od 1. náměstí. Vzdálenější oblasti mají jen několik domů nebo žádné fotografie. Dalšími kandidáty bez modelů jsou U hřiště, U náhonu, Mánesova a Komenského.

V databázi je ulice zdvojená. Oblast „Žatecká“ a oblast „Cs_Armady“ mají stejná čísla popisná i stejné přílohy; v druhé chybí štítky typu přílohy. Pracovali jsme s oblastí Žatecká a duplicitu zapsali u každého domu.

## Odkud jsou prameny

### Databáze Libuše projektu MOST

U každé z 25 staveb jsme načetli seznam příloh a stáhli jejich soubory, pouze pro čtení. Celkem 210 příloh: 90 fotografií, 85 rubů archivních karet, 25 situačních náčrtů a 10 pohlednic. Obsahově unikátních souborů je 172, protože sdílené snímky, například `cp_1006,1019_001`, visí u obou domů. Každý soubor má v záznamu domu zapsaný kontrolní součet SHA-256.

### Archivní karty a fotografie

Fotografie a karty pocházejí z dokumentace domů před demolicí starého Mostu; karty používají poválečný název ulice Čs. armády a řada z nich popisuje už zbořené sousedy. Přesně datované nejsou: snímek s vozem Škoda 1000 MB vznikl nejdříve v roce 1964 a jedna karta pivovaru nese poznámku „≈1971“. Pohlednice jsou starší, z doby před první světovou válkou až meziválečné. Karty nesou razítka „Památkové odd. KSPPOP Ústí n. L.“ a „Okresní archiv v Mostě“ a signaturu XI/D; část karet podepsal F. Čermák. Ručně psaný předmět karty říká, co snímek ukazuje, odkud byl pořízen a kdo jsou sousedé. To je hlavní doklad identity domů.

### Situační náčrty

Přílohy se štítkem PLANE jsou ručně kreslené, nekótované plánky parcel: obrys domu, hřebeny a valby střechy, komíny, orientační čísla, sousední pozemky, zahrady a průchody. Nejsou to stavební výkresy. Pořadí domů a tvary střech z nich čteme, rozměry ne.

### GIS model města

Vrstva `scene-data.json` obsahuje 1 400 historických půdorysů v místních souřadnicích EPSG:5514. Pro Žateckou z ní pochází osa ulice a 14 půdorysů. Jedenáct vil s čísly 1867 až 1918 ve vrstvě chybí.

### Co chybí

Stavební výkresy s kótami, řezy a kolorované FRONTy pro tuto ulici neexistují. Výšky podlaží, rozměry otvorů a sklony střech proto odhadujeme z fotografií a model zůstává bez textur.

Každou přílohu jsme skutečně otevřeli: kontaktní listy, montáže fotografií v plné velikosti, výřezy textů karet a náčrty v plné velikosti. U každého domu je seznam příloh s náhledy na jeho stránce a v souboru `plan_search.json`.

## Jak vznikal model a kde jsou soubory

Všechny cesty jsou relativní ke složce dávky `F:\MOST\output\zatecka_street_claude_2026-10-17\` v pracovním prostoru projektu.

- **Výběr ulice.** Živý seznam oblastí porovnaný s GIS. Výsledek: `evidence/area_live_zatecka_20261017.json`, `MODELING_PLAN.md`.

- **Stažení pramenů.** `scripts/live_get.py` uloží seznam příloh a hashe do `houses/cpN/evidence/live_get.json`, soubory do `sources/photos/`.

- **Prohlédnutí příloh.** `scripts/contact_sheets.py` a `review_sheets.py` vytvoří `evidence/contact_sheet.jpg`, `review_plan_photos.jpg` a `review_cards_text.jpg`. Identita a prameny domu: `scripts/house_notes.py` a `houses/cpN/plan_search.json`.

- **Poloha v ulici.** `scripts/gis_extract.py` a `gis_layout.py` zapíší půdorysy, průčelní hranu a natočení do `street_layout_gis.json`. Kontrolní obrázek: `evidence/layout_check.png`.

- **Geometrický plán domu.** `scripts/plans_*.py` vytvoří `houses/cpN/geometry_plan.json`: průčelí, otvory, římsy, vikýře, střecha a seznam hypotéz.

- **Stavba v Blenderu 4.5.** `scripts/build_house_z.py` (r4: `build_house_z4.py` s uzávěry podkroví v `z4_post.py`) běží bez okna a uloží `houses/cpN/rN/cp_N_G_rN.blend`, `.glb` a `build_stats.json`.

- **Kontrola.** Brána `tools/most_qa/geometry_gate.py` měří pohled do podkroví, krytí střechou, UV, síť a počty otvorů proti fotografii s rámečkem (`frames/`). `scripts/render_qa4.py` vykreslí 19 pohledů do `houses/cpN/r4/qa/`. Nálezy a výsledek: `qa_review.json` a `qa/visual_qa_r4.json`.

- **Sestava ulice.** `scripts/build_street_surfaces.py`, `assemble_street.py` a `render_street.py` vytvoří `street_r4/zatecka_street.blend`, `.glb` a rendery (povrchy ulice `street_surfaces_r3`).

- **Dokumentace.** `scripts/make_docs.py` píše README domů, `texture_handoff_spec.json` a `manifest.json` se SHA-256 všech výstupů. Tato stránka a `ZPRAVA.md` vznikají ze stejných dat.

## Jak jsme umístili 11 vil bez GIS půdorysu

Vily 1918, 1906/1907, 1914/1915, 1903/1904, 1899/1901, 1867 a 1872 v GIS vrstvě nejsou. Z pramenů jsme převzali jejich pořadí a stranu ulice. Konkrétní polohu a rozměry parcel jsme museli odhadnout.

### Doloženo prameny

- **Pořadí.** Každý náčrt nese orientační číslo (1918/10, 1906/11 až 1872/20) a popis sousedů, například „vlevo pozemek domu 2073, vpravo zahrada čp. 1906“ nebo „vpravo průchod do Vančurovy ulice“ u 1915. Karta k 1872 uvádí, že jde o poslední zbořenou vilu ulice.

- **Začátek řady.** Karta k průhledu ulicí popisuje odbočku Na střelišti s novostavbou 2073 a dodává, že „dále jdou vilky ulice ČSA 1918, 1906/1907, 1914/1915“.

- **Strana ulice.** Na náčrtech je ulice Čs. armády dole a předzahrádka pod úrovní ulice před domem. Zadní strana vily 1918 byla fotografována z domu 2072 na rohu Vančurovy, za ní je vidět muzeum 1360 na protější straně. Vily tedy stály na jihovýchodní straně mezi Žateckou a Vančurovou.

- **Kotva.** Osa Žatecké v GIS a půdorys domu 2073, jediného domu této části ulice, který v GIS je.

### Odhadnuto

- Řada začíná 32 m za křižovatkou Na střelišti, rozteč parcel je 10 až 12 m na dům, mezery mezi dvojdomy asi 5 m a průchod do Vančurovy asi 9 m.

- Stavební čára leží 14,5 m od osy ulice, plot 8,5 m od osy.

- Půdorysy 10 až 12 × 11 až 12 m podle proporcí průčelí na fotografiích.

Řada tak vychází asi na 200 m; skutečnost mohla být kratší i delší. Parametry jsou v `street_layout_gis.json` v části `villa_row`. Upřesnit je půjde podle historického katastru nebo leteckého snímku.

## Rozpory a hypotézy

- **Čp. 1006 a 1019.** GIS má popisky prohozené: půdorys označený „1006“ leží na severovýchodě, „1019“ na jihozápadním nároží. Fotografie `cp_1006,1019_001` má nad domy rukou psaná čísla 1019 vlevo a 1006 vpravo a náčrt uvádí 1019/6 a 1006/7. Model sleduje archiv; GIS půdorysy jsou použity podle polohy.

- **Pivovar 1041** je blokovaný hmotový model. GIS zná areál jako jediný sloučený půdorys, ruční náčrt areálu je bez měřítka a pohlednice ukazuje jiné rozložení fasád. Snímek `cp_1041_001` podle karty nezobrazuje areál, ale zbořené budovy na rohu proti Fučíkově škole. Pro skutečný model je potřeba plán s měřítkem nebo letecký snímek.
- **Gymnázium 1360** má jednu valbovou střechu nad celým půdorysem tvaru U; rastr oken je hypotéza, doložený je vstup v ose.

- **Výšky a otvory.** Výšky podlaží, rozměry oken a dveří a sklony střech jsou odhady z fotografií. Žádný údaj není historicky zaměřený.

- **Zjednodušení.** Obchodní výklady (699 POTRAVINY, 1006 PROBST) jsou niky, kruhový nárožní prvek 453 z náčrtu není modelován, zadní trakty a dvorní přístavky chybějí.

- **Dvojdomy.** Každá polovina nese svou polovinu společné střechy rozdělené na dělicí zdi. Tvar střechy, mansardová patra a vstupy ze zahrady jsou podle ručních náčrtů (bez měřítka), rozměry jsou poměry z náčrtu.
- **Čp. 2073** má hlavní průčelí a vstup do ulice Na Střelišti; do Žatecké směřuje boční stěna. Karta ho označuje jako „novostavbu“, ale dům je na plánu 1938.

- **Povrchy ulice.** Šířka vozovky, chodníků a poloha tramvajových kolejí jsou odhad podle fotografií. Na severovýchodním konci je osa vozovky posunuta o 1,3 m k severozápadu, protože GIS osa tam neleží uprostřed.

Všechny tyto údaje jsou v datech označené jako `model_hypothesis`, `status: provisional`, `locked: false`.

## Kontrola kvality

Každý dům prošel sadou 10 renderů: čtyři hlavní osy, čtyři šikmé pohledy na střechu a dva detaily průčelí. Geometrický audit hledal neuzavřené hrany, převrácené plochy, překrývající se plochy a průniky mezi domy.

- **Revize r1** odhalila překrývající se stupně schodů, konkávní plochy po ořezu otvorů, otevřené konce střešních křídel u 1360 a 770 a kameru uvnitř hmoty pivovaru.

- **Revize r2** vše opravila a přinesla kompletní kontrolní sadu pro všech 25 domů. Nové nálezy: okap vily 930 vyčníval 2 m před křídla, zadní křídlo 770 mělo plochý vršek a balkonové desky 1918 a 1867 protínaly arkýř.

- **Revize r3** opravila tyto čtyři domy.
- **Revize r4 (23.–25. 10. 2026)** přestavěla všech 25 domů podle nových kontrol: brána geometrie (pohled do podkroví, krytí střechou, počty otvorů proti fotografii s rámečkem) a 19 pohledů na dům. Fotografie s rámečky změnily počet os u osmi domů, náčrty změnily střechy vil. Vizuální kontrola našla černé pásy na společných zdech a podél obrubníků, komíny pod hřebenem a štíty místo valeb u společných zdí; vše je opravené. Aktuální sestava: všech 25 domů v r4, povrchy ulice v r3.

Výsledek r4: 24 z 25 domů prošlo, pivovar 1041 je blokovaný. Dřívější výsledek r3 byl 25 z 25 bez nových kontrol. Kontrola se týká geometrie; textury a historická správnost tím potvrzeny nejsou. Zbývají drobnosti v ohybu osy ulice: několik hran chodníku s nekonzistentní orientací a jeden zkroucený čtyřúhelník vozovky.

## Soubory ke stažení

- [Celá ulice, GLB (3,2 MB)](models/zatecka_street.glb) a [Blender (20 MB)](models/zatecka_street.blend), revize r4

- GLB jednotlivých domů jsou na jejich stránkách v sekci Soubory.

- [Zpráva v Markdownu](ZPRAVA.md) se seznamem pramenů všech domů

- [Přehled domů, JSON](data/houses.json) · [Původ každého souboru tohoto webu](sources.json)

### Mapa pracovní složky
| Cesta | Obsah |
|---|---|

| `README.md`, `MODELING_PLAN.md` | Souhrn dávky, plán modelování a rozhodnutí |

| `street_layout_gis.json` | Poloha a natočení všech domů, revize modelů, parametry vilové řady |

| `houses/cpN/plan_search.json` | Všechny přílohy domu se štítky, hashi a stavem rešerše, identita, hypotézy |

| `houses/cpN/geometry_plan.json` | Vstup builderu: rozměry, otvory, střecha, zdroje rozměrů |

| `houses/cpN/rN/` | Model revize: BLEND, GLB, statistiky, `qa/` s rendery a `qa_review.json` |

| `houses/cpN/evidence/` | Záznam stažení, kontaktní listy, montáže pramenů a texty karet |

| `street_r4/`, `street_surfaces_r3/` | Sestava ulice a povrchy, rendery (starší `street_r1`–`r3` zachovány) |
| `frames/`, `gate/`, `REPORT_R4.md` | Rámečky domů na fotografiích, výstupy brány geometrie, zpráva revize r4 |

| `qa/`, `audit/` | Vizuální kontrola všech domů, geometrické audity, logy stavby |

| `evidence/` | Snímek oblasti z databáze, GIS výřez, kontrola polohy, souhrn rešerše |

| `scripts/` | Všechny skripty postupu |

| `sources/photos/` | 210 stažených příloh; na webu jsou zmenšené náhledy |

| `manifest.json` | SHA-256 všech výstupů dávky |

## Revize r4 (23.–25. 10. 2026)

Všech 25 domů bylo znovu postaveno podle kontrol pracovního postupu platných od 19. 10. 2026: uzavřené podkroví a krytí střechou,
okna a dveře spočítané na fotografii s červeným rámečkem po dělicích zdech a tvar střechy porovnaný s ručním náčrtem. Každý dům
prošel automatickou bránou a 19 pohledy. Výsledek: 24 domů prošlo, pivovar 1041 je blokovaný. Podrobnosti: `REPORT_R4.md` v dávce.

### Opravy pramenů a popisů
- Čp. 1041: snímek `cp_1041_001` podle textu karty nezobrazuje areál pivovaru, ale starý snímek zbořených pivovarských budov na rohu proti Fučíkově škole (později jednotná fronta restaurace 110). Polohy věže a varny z něj nevycházejí; model je blokovaný.
- Čp. 1918: dvě zděná podlaží a šindelové mansardové patro, ne tři podlaží; arkýř je uprostřed průčelí, vstup ze zahrady.
- Čp. 2073: hlavní průčelí a vstup do ulice Na Střelišti, do Žatecké boční stěna se 2 osami. Označení „novostavba 1960s“ nebylo podložené (karta říká jen „novostavba“, dům je na plánu 1938).
- Počty os podle fotografií s rámečkem: 995 pět os, 774 pět os s arkýřem, 770 čtyři osy a vyšší římsa, 699 zaměněné uliční a nárožní fasády, 437 viditelná kratší strana je levá, 110 hala s osmi osami, 453/879 společný rytmus deseti os, 1006 bok se čtyřmi osami sdružených oken.
- Vily: valbová střecha přes celý dvojdům, mansardová patra uprostřed, vstupy se schody ze zahrady (ruční náčrty u každé poloviny).
- Název ulice: Československé armády je doložen ve vrstvě názvů k roku 1964; rok přejmenování prameny neudávají.

## Přehled domů

| Čp. | Strana | Or. č. | Typ | Podlaží | Průčelí × okap (m) | Poloha | Foto / náčrt / karty | Revize | QA |
|---|---|---|---|---|---|---|---|---|---|
| 110 | SZ | 1 | restaurace pivovaru (čp. 110) | 2 | 62,2 × 4,4 | GIS id 1515 | 3 / 1 / 2 | r4 | pass |
| 437 | SZ | 2 | třípodlažní dům v areálu pivovaru | 3 | 21,0 × 11,4 | GIS id 1506 | 2 / 1 / 1 | r4 | pass |
| 1041 | SZ | – | pivovar (areál, věž) | 3 | 88,0 × 11,0 | GIS id 1504 | 5 / 1 / 3 | r4 | blocked |
| 995 | SZ | 4 | vila (neobarokní) | 2 | 12,9 × 8,4 | GIS id 2938 | 5 / 1 / 5 | r4 | pass |
| 930 | SZ | 5 | vila | 2 | 6,5 × 7,6 | GIS id 2939 | 5 / 1 / 5 | r4 | pass |
| 1360 | SZ | – | reálné gymnázium / muzeum | 3 | 47,7 × 13,5 | GIS id 2937 | 8 / 1 / 1 | r4 | pass |
| 774 | JV | 1 | třípodlažní činžovní dům | 3 | 22,4 × 12,2 | GIS id 1512 | 2 / 1 / 2 | r4 | pass |
| 770 | JV | 2 | dvoupodlažní dům | 2 | 11,5 × 9,0 | GIS id 1513 | 4 / 1 / 4 | r4 | pass |
| 699 | JV | 3 | nárožní dům s obchodem POTRAVINY | 2 | 12,5 × 7,5 | GIS id 1514 | 5 / 1 / 5 | r4 | pass |
| 453 | JV | 4 | dvoupodlažní dům s mansardou (dvojice s 879) | 2 | 16,4 × 7,2 | GIS id 1519 | 2 / 1 / 1 | r4 | pass |
| 879 | JV | 5 | dvoupodlažní dům (dvojice s 453) | 2 | 12,1 × 7,2 | GIS id 1520 | 4 / 1 / 3 | r4 | pass |
| 1019 | JV | 6 | třípodlažní část dvojdomu (s 1006) | 3 | 13,1 × 11,6 | GIS id 1521 | 2 / 1 / 2 | r4 | pass |
| 1006 | JV | 7 | nárožní třípodlažní dům PROBST (s 1019) | 3 | 12,9 × 11,6 | GIS id 1522 | 6 / 2 / 4 | r4 | pass |
| 2073 | JV | – (Na střelišti) | bytový dům (průčelí a vstup do ulice Na Střelišti) | 3 | 23,4 × 9,6 | GIS id 2074 | 1 / 0 / 1 | r4 | pass |
| 1918 | JV | 10 | vila (2 zděná podlaží + šindelové mansardové patro) | 2 + mansarda | 11,5 × 7,0 | odhad | 5 / 1 / 5 | r4 | pass |
| 1906 | JV | 11 | polovina dvojdomu 1906/1907 | 2 | 10,5 × 6,6 | odhad | 3 / 1 / 3 | r4 | pass |
| 1907 | JV | 12 | polovina dvojdomu 1906/1907 | 2 | 10,5 × 6,6 | odhad | 3 / 1 / 3 | r4 | pass |
| 1914 | JV | 13 | polovina dvojdomu 1914/1915 | 2 | 10,5 × 6,6 | odhad | 4 / 1 / 4 | r4 | pass |
| 1915 | JV | 14 | polovina dvojdomu 1914/1915 | 2 | 10,5 × 6,6 | odhad | 4 / 1 / 4 | r4 | pass |
| 1903 | JV | 15 | polovina dvojdomu 1903/1904 | 2 | 10,5 × 6,6 | odhad | 4 / 1 / 4 | r4 | pass |
| 1904 | JV | 16 | polovina dvojdomu 1903/1904 | 2 | 10,5 × 6,6 | odhad | 5 / 1 / 5 | r4 | pass |
| 1899 | JV | 17 | polovina dvojdomu 1899/1901 | 2 | 10,0 × 6,6 | odhad | 2 / 1 / 2 | r4 | pass |
| 1901 | JV | 18 | polovina dvojdomu 1899/1901 | 2 | 10,0 × 6,6 | odhad | 2 / 1 / 2 | r4 | pass |
| 1867 | JV | 19 | vila (2 podlaží + mansardové podkroví) | 2 | 12,0 × 6,8 | odhad | 6 / 1 / 6 | r4 | pass |
| 1872 | JV | 20 | vila (poslední zbořená) | 2 | 12,0 × 6,8 | odhad | 8 / 1 / 8 | r4 | pass |

## Domy jednotlivě

### Čp. 110: restaurace pivovaru (čp. 110)

- Strana SZ, orientační číslo 1, poloha: GIS půdorys id 1515; model `houses/cp110/r4/cp_110_G_r4.glb` (530 polygonů).
- Identita: Plochostřechý dvoupodlažní objekt restaurace pivovaru s terasou na přízemní části (nápis RESTAURACE), navazující na dlouhou halu stáčírny 1041. Plán cp_110_001: „Plochostřeché patro restaurace“, „terasa na přízemku“, „nízký přístavek“, „ploché přízemí“; nároží k Žižkově (parčík Schneebergl).
- Použité prameny: cp_110_001 PLANE (situace 110 + 1041 + zbořené 774 naproti); cp_110_001 PHOTO (restaurace od Fučíkových sadů, pivovar s věží v pozadí); cp_110_002 PHOTO (ulice: dlouhá plochostřechá stáčírna s vysokými okny, RESTAU… vpravo); FOTO-000150 (kolorovaná pohlednice pivovaru, sdílená s 437/1041).
- GIS: GIS id 1515 (536 m², 62 vrcholů, zaoblené rohy) – dlouhý pás podél ulice
- Rozměry: GIS id 1515 strip 62 x 7-12.6 m (front jogs <1.6 m dropped)
- Průčelí: photos cp_110_001/002: flat-roofed 2-storey restaurant block with tall ground-floor windows, 1-storey ends; sketch cp_110_001 (A = restaurant floor, terrace at the NE end)
- Střecha: flat (sketch/photo)
- Kontrola: prošla (r4); průčelí: černý pás oplechování podél celé fasády nad přízemím (oplechování patra na ploché střeše leželo i na hraně v líci fasády) – opraveno v z4_post.py, nutná přestavba; po přestavbě 25. 10.: černý pás trvá – příčinou je atika ploché střechy v rovině fasády haly a přístavku; atika se nově vyřezává pod stojícími hmotami (krok o), nutná další přestavba; po druhé přestavbě 25. 10.: černý pás zmizel (atika vyříznuta pod halou a přístavkem); průčelí odpovídá rámečku cp_110_002
- Doklad fasád (r4): main: 15
- Hypotézy: výšky podlaží odhad (přízemí 4,2 m, patro 3,8 m); rozsah patra restaurace nad půdorysem odhad podle plánu A (SV část); okna odvozena z foto, počet os odhad; terrace railing at the NE end; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); axis positions from a 1D projective fit of the 8 regular hall bays on cp_110_002 (bay 2.41 m), heights scaled to an assumed 8.5 m hall (model_hypothesis, provisional, locked=false); restaurant 3rd window R3 and the entrance D1 are not visible on the street photo (hypothesis)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_110_001.jpg | situační náčrt | eebecf08c3d4 |
| FOTO-000150.jpg | fotografie | 6e26ed1120db |
| cp_110_001.jpg | fotografie | 59cac59b09a1 |
| cp_110_002.jpg | fotografie | fca731f84413 |
| cp_110_001.jpg | archivní karta (rub) | e4051b1837cb |
| cp_110_002.jpg | archivní karta (rub) | 3e08e24b51b1 |

### Čp. 437: třípodlažní dům v areálu pivovaru

- Strana SZ, orientační číslo 2, poloha: GIS půdorys id 1506; model `houses/cp437/r4/cp_437_G_r4.glb` (570 polygonů).
- Identita: Samostatný třípodlažní dům s valbovou střechou v nádvoří pivovaru mezi vrátnicí a přízemní částí 110 (plán cp_437_001: „bývalý průchod“ k 110). Foto cp_437_001: nárožní pohled, bosované přízemí, 5 os na delší straně, 3 osy na kratší, komín.
- Použité prameny: cp_437_001 PLANE; cp_437_001 PHOTO; FOTO-000150 (pohlednice).
- GIS: GIS id 1506 (266 m², obdélník 20,9 × 12,8 m)
- Rozměry: GIS id 1506 rectangle 20.98 x 12.78 m
- Průčelí: photo cp_437_001: 3 storeys, rusticated ground floor, 5 axes long side, 3 axes short side, hipped roof, chimney
- Střecha: hip (photo); pitch estimate
- Kontrola: prošla (r4); osy a kordony sedí s rámečkem cp_437_001; zadní a pravá strana bez otvorů/zrcadlo = hypotéza; pod okapem uzavřeno
- Doklad fasád (r4): main: 5 / 5 / 5; left: 2 / 2 / 2; right: hypotéza
- Hypotézy: delší (5osá) strana přiřazena k ulici podle GIS hrany; výšky podlaží odhad; entrance not visible on the street side; no door modelled; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_437_001.jpg | situační náčrt | 59e70a1e9460 |
| FOTO-000150.jpg | fotografie | 6e26ed1120db |
| cp_437_001.jpg | fotografie | a3ead86430f3 |
| cp_437_001.jpg | archivní karta (rub) | aca07ad7e3a8 |

### Čp. 1041: pivovar (areál, věž)

- Strana SZ, orientační číslo –, poloha: GIS půdorys id 1504; model `houses/cp1041/r4/cp_1041_G_r4.glb` (1645 polygonů).
- Identita: Areál pivovaru (Severočeské pivovary): cihlové stáčírny/varna, věž s cimbuřím a jehlancovou střechou, komín, vstupní brána s vrátnicí od ČSA. Foto cp_1041_001 (podle karty starý snímek zbořených pivovarských budov na rohu proti Fučíkově škole, ne pohled na areál), FOTO-000149 (kolorovaná pohlednice průčelí do ČSA), cp_1041_002/003 (ulice 1960s: kamenná ohradní zeď, brána, věž). Plán cp_1041_002 ověřuje polohu věže a halu stáčírny.
- Použité prameny: cp_1041_002 PLANE; cp_1041_001/002/003 PHOTO; FOTO-000149/150.
- GIS: GIS id 1504 (3942 m², 19 vrcholů) „Brauerei“
- Rozměry: GIS id 1504 polygon 88 m street front
- Průčelí: postcard FOTO-000149 + photos cp_1041_002/003: unified brick bottling facade with tall arched windows, tower with pyramid roof and crenellation, chimney; sketch cp_1041_002
- Střecha: massing hypothesis
- Kontrola: blokováno (r4); hmotový model: uliční průčelí 88 m s 2×21 okny odporuje pohlednici FOTO-000149 (nádvoří, hala se 4 osami u věže, štítové křídlo vlevo); geometrie uzavřená, bez škvír; oprava pramene: cp_1041_001 není letecký pohled na areál, ale starý snímek zbořených budov na rohu proti Fučíkově škole (karta); polohy věže a varny v r2 z něj proto nevycházejí
- Doklad fasád (r4): main: hypotéza + dveře 1
- Hypotézy: hmotový model: hlavní hala + varna + věž jako hypotéza rozložení výšek; věž umístěna u uličního průčelí podle pohlednice; detaily fasád (cihlové pilastry, štíty) jen schematicky; tower/brewhouse/chimney positions inside the GIS footprint estimated from the aerial photo cp_1041_001; skeleton roof over the whole footprint is a stand-in for several hall roofs; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1041_002.jpg | situační náčrt | 5f59aeda5576 |
| FOTO-000149.jpg | fotografie | 0fea7d5763b4 |
| FOTO-000150.jpg | fotografie | 6e26ed1120db |
| cp_1041_001.jpg | fotografie | 41a8524bd3cc |
| cp_1041_002.jpg | fotografie | e04a2414a2c2 |
| cp_1041_003.jpg | fotografie | 05e463a98282 |
| cp_1041_001.jpg | archivní karta (rub) | 29df7bbd5642 |
| cp_1041_002.jpg | archivní karta (rub) | 7eb03e4de781 |
| cp_1041_003.jpg | archivní karta (rub) | 05accf9d8408 |

### Čp. 995: vila (neobarokní)

- Strana SZ, orientační číslo 4, poloha: GIS půdorys id 2938; model `houses/cp995/r4/cp_995_G_r4.glb` (441 polygonů).
- Identita: Dvoupodlažní neobarokní vila mezi pivovarem a parkem (plán cp_995_001: vpravo „ČS. ARMÁDY TŘ.“, vlevo „areál pivovaru, už stáčírna“). Foto cp_995_001: uliční průčelí 3 osy, v patře balkon s obloukovými dveřmi, segmentový štít s oválným oknem; cp_995_003/005 boční a zadní strana s lodžií; cp_995_002 plot.
- Použité prameny: cp_995_001 PLANE; cp_995_001..005 PHOTO.
- GIS: GIS id 2938 (153,5 m², obdélník 12,9 × 12,0 m)
- Rozměry: GIS id 2938 rectangle 12.86 x 11.72 m
- Průčelí: photo cp_995_001: 3 axes, 1st floor balcony with arched door, pediments, segmental gable with oval window; cp_995_003/005 sides
- Střecha: low hip + gable dormer (photo)
- Kontrola: prošla (r4); 5 os průčelí a rizalit s balkonem a štítem sedí s cp_995_001; boky a zadní strana hypotéza; pohled pod okap uzavřený
- Doklad fasád (r4): main: 5 / 5; dormers: 1; left: hypotéza; right: hypotéza
- Hypotézy: výšky odhad (přízemí 4,0, patro 3,8); zadní lodžie zjednodušena; tvar střechy (nízká valba) z foto, sklon odhad; rear loggia (photo cp_995_003) not modelled; entrance on the garden side; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_995_001.jpg | situační náčrt | ff90c711eb3d |
| cp_995_001.jpg | fotografie | 63fab1c2e28c |
| cp_995_002.jpg | fotografie | 5c8cdda61e7b |
| cp_995_003.jpg | fotografie | db25f4e94b1a |
| cp_995_004.jpg | fotografie | eab17d1901a1 |
| cp_995_005.jpg | fotografie | 48ade9aafa7d |
| cp_995_001.jpg | archivní karta (rub) | 3d61bdb9fde7 |
| cp_995_002.jpg | archivní karta (rub) | 845b41424025 |
| cp_995_003.jpg | archivní karta (rub) | e7001580a4c7 |
| cp_995_004.jpg | archivní karta (rub) | 2ab92ef90874 |
| cp_995_005.jpg | archivní karta (rub) | eb9cacb89e10 |

### Čp. 930: vila

- Strana SZ, orientační číslo 5, poloha: GIS půdorys id 2939; model `houses/cp930/r4/cp_930_G_r4.glb` (295 polygonů).
- Identita: Dvoupodlažní vila s balkonem v patře a štítovým vikýřem nad vstupní osou, plot s kamennými sloupky (foto cp_930_001, cp_930_002 ulice). Plán cp_930_001: „Sady Rudé armády“ za domem, „ČS. ARMÁDY TŘ.“ vlevo, „příjezd do pivovarského pozemku“.
- Použité prameny: cp_930_001 PLANE; cp_930_001..005 PHOTO.
- GIS: GIS id 2939 (211 m², 8 vrcholů)
- Rozměry: GIS id 2939 polygon: central risalit 6.5 m at y=0, wings at y=1.9, 16.2 m total
- Průčelí: photo cp_930_001: 2 storeys, arched entrance with steps in the risalit, 1st floor balcony with door, gable above; one window per wing and floor
- Střecha: hip + front gable (photo)
- Kontrola: prošla (r4); rizalit s obloukovými dveřmi, schody, balkon s dveřmi a 2 okny, štít se sdruženým oknem; křídla po 1 okně; boční schody k zadním vstupům; pod okapem uzavřeno
- Doklad fasád (r4): main: 2 / 3 + dveře 1; dormers: 1; left: 1 / 1; right: 1 / 1
- Hypotézy: osy oken z šikmého foto; výšky odhad; vikýř/štít zjednodušen; window axes from oblique photo; ridge along the street; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); r3: main roof eave at the wing face; risalit covered by the gable volume

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_930_001.jpg | situační náčrt | 56f23d239cf0 |
| cp_930_001.jpg | fotografie | 1c05ebcd46bd |
| cp_930_002.jpg | fotografie | 2b04123d46b0 |
| cp_930_003.jpg | fotografie | 5cfd42a4d435 |
| cp_930_004.jpg | fotografie | e505a42c3388 |
| cp_930_005.jpg | fotografie | 8077a4b30376 |
| cp_930_001.jpg | archivní karta (rub) | 419a18f9b78f |
| cp_930_002.jpg | archivní karta (rub) | 1b469192c30f |
| cp_930_003.jpg | archivní karta (rub) | 48d3de3beb8b |
| cp_930_004.jpg | archivní karta (rub) | 936024295380 |
| cp_930_005.jpg | archivní karta (rub) | f87ecfa573c6 |

### Čp. 1360: reálné gymnázium / muzeum

- Strana SZ, orientační číslo –, poloha: GIS půdorys id 2937; model `houses/cp1360/r4/cp_1360_G_r4.glb` (2176 polygonů).
- Identita: Budova c.k. státního reálného gymnázia (pohlednice P-000045, P-000593 „K.K. STAATS-OBERREALGYMNASIUM“), později průmyslová škola a muzeum („budova nynějšího muzea čp. 1360“ na kartách 1918). Třípodlažní, vysoká valbová střecha s velkým štítem a řadou vikýřů, věžička. Foto cp_1360_001 (1960s).
- Použité prameny: cp_1360_001 PLANE+PHOTO; pohlednice P-000045(_2), P-000327(_2), P-000593, P-001040, P-001453.
- GIS: GIS id 2937 (2440 m², 22 vrcholů)
- Rozměry: GIS id 2937 polygon (front 47.7 m, wings)
- Průčelí: postcards P-000045/P-000593 (K.K. Staats-Oberrealgymnasium): 3 storeys, regular window grid, high hipped roofs with gable and dormers; photo cp_1360_001
- Střecha: massing hypothesis: constant-pitch straight skeleton 40 deg
- Kontrola: prošla (r4); jedna valbová střecha (straight skeleton) nad celým půdorysem U, bez střechy nad dvorem a bez nekrytého zdiva; pravidelný rastr os = hypotéza, vstup v ose doložen; pohled pod okap uzavřený
- Doklad fasád (r4): main: hypotéza + dveře 1; left_wing_a: hypotéza; left_wing_b: hypotéza; right_side: hypotéza
- Hypotézy: hmotový model: výšky odhad (římsa 13,5 m), štít a vikýře zjednodušeny; členění oken pravidelné, odhad; window grid regular 2.6 m from postcard impression; gable, dormers and roof lantern of the postcards not modelled; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); roof composed of four rectangular hips; junction valleys approximate; wing roof ends at junctions closed as hips (valley junction approximated)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1360_001.jpg | situační náčrt | 403c4f43b3a5 |
| cp_1360_001.jpg | fotografie | a3e7e9b1d3a4 |
| P-000045.jpg | pohlednice | fbc32bedbe41 |
| P-000045__2.jpg | pohlednice | e31e43780bb6 |
| P-000327.jpg | pohlednice | 48323f60078f |
| P-000327__2.jpg | pohlednice | a96b76474887 |
| P-000593.jpg | pohlednice | 162d8f1d9bf2 |
| P-001040.jpg | pohlednice | a8e066efc462 |
| P-001453.jpg | pohlednice | 681dba49b9b4 |
| cp_1360_001.jpg | archivní karta (rub) | ad3835048fc0 |

### Čp. 774: třípodlažní činžovní dům

- Strana JV, orientační číslo 1, poloha: GIS půdorys id 1512; model `houses/cp774/r4/cp_774_G_r4.glb` (450 polygonů).
- Identita: Třípodlažní dům na nároží ČSA/Fučíkovy sady (plán cp_774_001: „774/1“, Fučíkovy sady vlevo, dvůr čp. 774). Foto cp_774_001: neobarokní průčelí ~7 os, střední rizalit s balkonem a portálem; cp_770,774_001: dvorní strana po demolici sousedů.
- Použité prameny: cp_774_001 PLANE; cp_774_001, cp_770,774_001 PHOTO.
- GIS: GIS id 1512 (251 m², 7 vrcholů)
- Rozměry: GIS id 1512 polygon (front 22.43 m, depth 12-15.6 m)
- Průčelí: photo cp_774_001: 3 storeys, ~7 axes, central risalit with portal and 1st-floor balcony, pediments; rear cp_770,774_001
- Střecha: low hip (skeleton over GIS polygon)
- Kontrola: prošla (r4); 5 os, portál v ose 13,4 m, arkýř se 3 obloukovými okny a balkon nad ním sedí s cp_774_001; zadní strana se zalomením podle GIS; pod okapem uzavřeno
- Doklad fasád (r4): main: 4 / 4 / 5 + dveře 1
- Hypotézy: výšky podlaží odhad (4,2/3,6/3,6); rizalit a balkon zjednodušeny; zadní křídlo bez pramene; rear wing and courtyard annexes not modelled; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_774_001.jpg | situační náčrt | fcbd40842e2b |
| cp_770,774_001.jpg | fotografie | 102a82b33cb7 |
| cp_774_001.jpg | fotografie | 0aaeed2eba96 |
| cp_770,774_001.jpg | archivní karta (rub) | 0dae6bc26b02 |
| cp_774_001.jpg | archivní karta (rub) | f3047677761f |

### Čp. 770: dvoupodlažní dům

- Strana JV, orientační číslo 2, poloha: GIS půdorys id 1513; model `houses/cp770/r4/cp_770_G_r4.glb` (262 polygonů).
- Identita: Dvoupodlažní dům mezi 774 a 699 (plán cp_770_001: „770/2“, 774 vlevo, 699 vpravo). Foto cp_770_001: čelní průčelí 6 os v patře, v přízemí 5 oken + dveře vpravo, kordonová římsa; cp_699,770_001/002 (po demolici / nároží).
- Použité prameny: cp_770_001 PLANE; cp_770_001, cp_699,770_001, cp_699,770_002 PHOTO.
- GIS: GIS id 1513 (149 m², 7 vrcholů)
- Rozměry: GIS id 1513 polygon: main block 11.47 x 13.4 m + rear wing
- Průčelí: photo cp_770_001: 6 axes upper floor, 5 windows + door (right) ground floor, string course; sketch cp_770_001: 2 eyebrow dormers
- Střecha: saddle between party walls (sketch), ridge along the street
- Kontrola: prošla (r4); 4 osy, dveře ve 4. ose, kordon, 2 komíny a 2 volská oka podle cp_770_001; štíty u obou společných zdí po linii GIS bez přesahu; zadní křídlo s valbou
- Doklad fasád (r4): main: 3 / 4 + dveře 1
- Hypotézy: výšky odhad; volská oka podle plánu (2 ks); roof ridge along the street, gable party walls; rear wing height estimate; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); wing roof ends at junctions closed as hips (valley junction approximated); r3: rear wing eave = main eave (single masonry extrusion); eave 9.0 m from the frontal photo cp_770_001 scaled by the GIS width 11.47 m (r2: 7.3 m); photo cp_770,774_001 suggests about 8.3 m (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_770_001.jpg | situační náčrt | 60c3756aef18 |
| cp_699,770_001.jpg | fotografie | 42a5011c2ab6 |
| cp_699,770_002.jpg | fotografie | b1124e071010 |
| cp_770,774_001.jpg | fotografie | 102a82b33cb7 |
| cp_770_001.jpg | fotografie | 80e2db33c014 |
| cp_699,770_001.jpg | archivní karta (rub) | 1f254bfcd3de |
| cp_699,770_002.jpg | archivní karta (rub) | d9cf37ed2d25 |
| cp_770,774_001.jpg | archivní karta (rub) | 0dae6bc26b02 |
| cp_770_001.jpg | archivní karta (rub) | f9531de65ca1 |

### Čp. 699: nárožní dům s obchodem POTRAVINY

- Strana JV, orientační číslo 3, poloha: GIS půdorys id 1514; model `houses/cp699/r4/cp_699_G_r4.glb` (312 polygonů).
- Identita: Nárožní dvoupodlažní dům ČSA × R. Luxemburkové (plán cp_699_001: „699/3“, 770 vlevo, R. Luxemburkové vpravo). Foto cp_699_001 (nároží, obchod POTRAVINY, 3 osy do ČSA), cp_699_002 (z Luxemburkové, 5 os), cp_699_003, cp_699,770_002.
- Použité prameny: cp_699_001 PLANE; cp_699_001..003, cp_699,770_001/002 PHOTO.
- GIS: GIS id 1514 (165 m², obdélník)
- Rozměry: GIS id 1514 rectangle 12.49 x 13.21 m
- Průčelí: photos cp_699_001 (corner, shop), cp_699_002 (Luxemburkove side 5 axes), cp_699,770_002
- Střecha: hip to the corner, gable to 770 (sketch: ridge along CSA, eyebrow dormers)
- Kontrola: prošla (r4); průčelí 5 os s domovními dveřmi a obchodem, nárožní strana 4 osy; štít u společné zdi s 770, valba na nároží; komín končil pod hřebenem a nebyl vidět – zvýšen na hřeben + 0,8 m, nutná přestavba; po přestavbě 25. 10.: komín nad hřebenem viditelný; ostatní pohledy beze změny
- Doklad fasád (r4): main: 3 / 5 + dveře 2; right: 4 / 4
- Hypotézy: výšky odhad (4,0/3,6); obchodní výklady zjednodušeny na niky; shop windows simplified to niches; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_699_001.jpg | situační náčrt | 381998ef8ced |
| cp_699,770_001.jpg | fotografie | 42a5011c2ab6 |
| cp_699,770_002.jpg | fotografie | b1124e071010 |
| cp_699_001.jpg | fotografie | aa34ebfc72db |
| cp_699_002.jpg | fotografie | cd0837250c9f |
| cp_699_003.jpg | fotografie | 2c9d181e11a0 |
| cp_699,770_001.jpg | archivní karta (rub) | 1f254bfcd3de |
| cp_699,770_002.jpg | archivní karta (rub) | d9cf37ed2d25 |
| cp_699_001.jpg | archivní karta (rub) | d4418d45da12 |
| cp_699_002.jpg | archivní karta (rub) | bdf7a285bc20 |
| cp_699_003.jpg | archivní karta (rub) | daaa9c16017c |

### Čp. 453: dvoupodlažní dům s mansardou (dvojice s 879)

- Strana JV, orientační číslo 4, poloha: GIS půdorys id 1519; model `houses/cp453/r4/cp_453_G_r4.glb` (367 polygonů).
- Identita: Dům na nároží R. Luxemburkové (plán cp_453,879_001: „453/4“, kruhový nárožní prvek k Luxemburkové, „mansarda“, štítový vikýř uprostřed). Foto cp_453,879_001: dlouhé dvoupodlažní průčelí s trojúhelným štítem/vikýřem uprostřed; pohlednice P-000936 (dvůr pivovaru v pozadí).
- Použité prameny: cp_453,879_001 PLANE+PHOTO; P-000936.
- GIS: GIS id 1519 (133 m², 5 vrcholů)
- Rozměry: GIS id 1519 pentagon (front 16.36 m, right depth 9.41 m, diagonal rear-left)
- Průčelí: photo cp_453,879_001: 2 storeys, central triangular gable dormer; sketch cp_453,879_001: mansard room, round corner element (not modelled)
- Střecha: skeleton hip 35 deg + gable dormer
- Kontrola: prošla (r4); valba u společné zdi s 879 – fotografie cp_453,879_001 ukazuje střechu plynule navazující na 879; opraveno party_edges (štít na společné zdi), nutná přestavba; fasáda 6 os a štítový vikýř se 3 okny sedí; po přestavbě 25. 10.: štít na společné zdi s 879 v pořádku; pravý komín skončil pod zvýšeným hřebenem – komíny se nově zvedají 0,8 m nad krytinu (krok p), nutná další přestavba; po druhé přestavbě 25. 10.: oba komíny nad střechou, štít na společné zdi s 879
- Doklad fasád (r4): main: 4 / 5 + dveře 1; dormers: 3; diag: hypotéza
- Hypotézy: kruhový nárožní prvek z plánu nemodelován (nejasný tvar); osy a výšky odhad; round corner element of the sketch omitted; diagonal rear wall windows; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_453,879_001.jpg | situační náčrt | 7f7e49ee619f |
| cp_453,879_001.jpg | fotografie | b2e1a4ff0ae3 |
| P-000936.jpg | pohlednice | 6b5bb9495a95 |
| cp_453,879_001.jpg | archivní karta (rub) | cf14a6e37ff3 |

### Čp. 879: dvoupodlažní dům (dvojice s 453)

- Strana JV, orientační číslo 5, poloha: GIS půdorys id 1520; model `houses/cp879/r4/cp_879_G_r4.glb` (229 polygonů).
- Identita: Pokračování řady za 453 (plán „879/5“). Foto cp_453,879_001 (pravá část řady), cp_879_002 (bosovaná fasáda, valbová střecha, ze zahrady), cp_879_001 (dvůr).
- Použité prameny: cp_453,879_001 PLANE+PHOTO; cp_879_001/002 PHOTO; P-000936.
- GIS: GIS id 1520 (146 m², 9 vrcholů)
- Rozměry: GIS id 1520 polygon (rect 12.13 x 11.54 + rear bump)
- Průčelí: photos cp_453,879_001 (right part of the row), cp_879_002 (rusticated plaster, hip roof)
- Střecha: hip (photo)
- Kontrola: prošla (r4); osy 7–10 sjednoceného průčelí: dveře, velké dveře, okno, (okno za stromem = hypotéza); štít u 453 bez přesahu, zadní výstupek s valbou; komín končil pod hřebenem a nebyl vidět – zvýšen na hřeben + 0,8 m, nutná přestavba; po přestavbě 25. 10.: komín nad hřebenem viditelný; ostatní pohledy beze změny
- Doklad fasád (r4): main: 1 / 3 + dveře 2
- Hypotézy: osy a výšky odhad; dvorní přístavky nemodelovány; rear annex (bump) under the main roof overhang; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); rear jog of the GIS footprint (x 4.59-7.62, 1.2 m deep) covered by its own small hip roof; not visible on any photo (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_453,879_001.jpg | situační náčrt | 7f7e49ee619f |
| cp_453,879_001.jpg | fotografie | b2e1a4ff0ae3 |
| cp_879_001.jpg | fotografie | 18201780d3c7 |
| cp_879_002.jpg | fotografie | 96231bb22be9 |
| P-000936.jpg | pohlednice | 6b5bb9495a95 |
| cp_453,879_001.jpg | archivní karta (rub) | cf14a6e37ff3 |
| cp_879_001.jpg | archivní karta (rub) | 9815973e1ed6 |
| cp_879_002.jpg | archivní karta (rub) | 4bfd88f932e3 |

### Čp. 1019: třípodlažní část dvojdomu (s 1006)

- Strana JV, orientační číslo 6, poloha: GIS půdorys id 1521; model `houses/cp1019/r4/cp_1019_G_r4.glb` (428 polygonů).
- Identita: Severovýchodní (nižší orientační číslo) část třípodlažního dvojdomu „PROBST“: foto cp_1006,1019_001 má popisky „1019“ vlevo a „1006“ vpravo nad nárožím; plán cp_1006,1019_001: 879 | 1019/6 | 1006/7. POZOR: GIS má popisky obráceně (id 1521 „1006“ je SV, id 1522 „1019“ je JZ nároží) – model sleduje archivní popisky a pořadí orientačních čísel; GIS id použit podle polohy.
- Použité prameny: cp_1006,1019_001 PLANE+PHOTO; cp_1006,1019_002 PHOTO; cp_1006_001 PHOTO (ulice s tramvají).
- GIS: GIS id 1521 (175 m², 8 vrcholů) – poloha SV; popisek v GIS „1006“ (rozpor)
- Rozměry: GIS id 1521 polygon (rect 13.08 x 13.0 + rear bump); archive label 1019 (GIS label 1006 - conflict recorded)
- Průčelí: photo cp_1006,1019_001 (left part): 3 storeys, rusticated ground floor with arched windows, pediments on the 1st floor, entrance
- Střecha: low hip, continuous with 1006 (gable at the party wall)
- Kontrola: prošla (r4); 3 podlaží, bosované přízemí s obloukovými okny a vstupem uprostřed, frontony v 1. patře; štít u společné zdi s 1006; zadní výstupek se stříškou; osy = hypotéza (snímek silně zkrácený); komín končil pod hřebenem a nebyl vidět – zvýšen na hřeben + 0,8 m, nutná přestavba; po přestavbě 25. 10.: komín nad hřebenem viditelný; ostatní pohledy beze změny
- Doklad fasád (r4): main: hypotéza + dveře 1
- Hypotézy: rozpor popisků GIS × archiv – provisional; výšky odhad (4,0/3,6/3,6); GIS/archive label conflict (see plan_search.json); all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); rear jog of the GIS footprint (x 4.05-9.37, 1.2 m deep, probably a staircase) covered by its own small hip roof; not visible on any photo (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1006,1019_001.jpg | situační náčrt | d2d338dcec4e |
| cp_1006,1019_001.jpg | fotografie | 37c5ee4cd478 |
| cp_1006,1019_002.jpg | fotografie | 30127c15e2c5 |
| cp_1006,1019_001.jpg | archivní karta (rub) | cd299f8c851f |
| cp_1006,1019_002.jpg | archivní karta (rub) | c021b4eb85a0 |

### Čp. 1006: nárožní třípodlažní dům PROBST (s 1019)

- Strana JV, orientační číslo 7, poloha: GIS půdorys id 1522; model `houses/cp1006/r4/cp_1006_G_r4.glb` (839 polygonů).
- Identita: Nárožní část dvojdomu se zkoseným nárožím a balkonem na nároží, obchod PROBST v suterénu/přízemí nároží; boční průčelí do vedlejší ulice 4 osy. Foto cp_1006,1019_001, cp_1006_001 (ulice), cp_1006_001__2, cp_1006_002 (boční/zadní s komínem), plán cp_1006_001 (L půdorys s křídlem).
- Použité prameny: cp_1006_001 PLANE; cp_1006,1019_001 PLANE; cp_1006_001, cp_1006_001__2, cp_1006_002, cp_1006,1019_001/002 PHOTO; P-000936.
- GIS: GIS id 1522 (278 m², 7 vrcholů) – poloha JZ nároží; popisek v GIS „1019“ (rozpor)
- Rozměry: GIS id 1522 polygon with chamfer 3.85 m and rear wing; archive label 1006 (GIS 1019 - conflict recorded)
- Průčelí: photos cp_1006,1019_001 (corner with balcony, PROBST), cp_1006_002 (side/rear), cp_1006_001 street
- Střecha: low hip, skeleton over the L-shaped polygon
- Kontrola: prošla (r4); valba u společné zdi s 1019 (fotografie: plynulá nízká střecha) – opraveno party_edges; překrývající se frontony sdruženého okna U3/U4 (černý artefakt) – frontony odstraněny; nutná přestavba; nároží s balkonem a 4 osy sdružených oken na boku sedí s cp_1006,1019_001; po přestavbě 25. 10.: štít na společné zdi s 1019, střecha plynule navazuje; artefakt u sdruženého okna zmizel
- Doklad fasád (r4): main: 3 / 4 / 4 + dveře 1; chamfer: 1 / 1 + dveře 1; side: 8 / 8 / 8
- Hypotézy: rozpor popisků GIS × archiv – provisional; zkosené nároží v GIS není, modelováno podle foto; výšky odhad; GIS/archive label conflict; shop PROBST in the chamfer simplified to an arched door; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1006,1019_001.jpg | situační náčrt | d2d338dcec4e |
| cp_1006_001.jpg | situační náčrt | c406bd7b64c4 |
| cp_1006,1019_001.jpg | fotografie | 37c5ee4cd478 |
| cp_1006,1019_002.jpg | fotografie | 30127c15e2c5 |
| cp_1006_001.jpg | fotografie | 45b2bc4a4823 |
| cp_1006_001__2.jpg | fotografie | 2a3fb41f582d |
| cp_1006_002.jpg | fotografie | 92cac3fe9e3f |
| P-000936.jpg | pohlednice | 6b5bb9495a95 |
| cp_1006,1019_001.jpg | archivní karta (rub) | cd299f8c851f |
| cp_1006,1019_002.jpg | archivní karta (rub) | c021b4eb85a0 |
| cp_1006_001.jpg | archivní karta (rub) | e303fbaaa319 |
| cp_1006_002.jpg | archivní karta (rub) | ffa560075f5c |

### Čp. 2073: bytový dům (průčelí a vstup do ulice Na Střelišti)

- Strana JV, orientační číslo – (Na střelišti), poloha: GIS půdorys id 2074; model `houses/cp2073/r4/cp_2073_G_r4.glb` (735 polygonů).
- Identita: Třípodlažní bytový dům s valbovou střechou a balkony na nároží Na střelišti/Vančurova („novostavba čp. 2073“ dle karty 1906,1914,1918). Foto cp_2073_001 (ze zahrady). Bez plánu.
- Použité prameny: cp_2073_001 PHOTO (+karta).
- GIS: GIS id 2074 (235 m², obdélník 10,3 × 23,4 m, delší strana podél Na střelišti)
- Rozměry: GIS id 2074 rectangle 23.43 x 10.34 m
- Průčelí: photo cp_2073_001: 3 storeys, hipped roof, 2 chimneys, balconies on the garden side
- Střecha: hip
- Kontrola: prošla (r4); komíny (2) končily pod hřebenem a nebyly vidět – zvýšeno na hřeben + 0,8 m, nutná přestavba; strana do Žatecké 2 osy, zadní strana s balkony ve 2 řadách; vstup ze Střeliště nemodelován (poloha neznámá); po přestavbě 25. 10.: oba komíny nad hřebenem viditelné
- Doklad fasád (r4): main: hypotéza; back: hypotéza; right: 2 / 2
- Hypotézy: počet os odhad; výšky odhad (3,0 m podlaží); axes count 7 estimated; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); the long main facade faces Na Strelisti (entrance there per the KSPPOP card), the right short side faces Zatecka; the main facade itself is not photographed (model_hypothesis)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_2073_001.jpg | fotografie | 5742fc9428b7 |
| cp_2073_001.jpg | archivní karta (rub) | 8d239c6f3d91 |

### Čp. 1918: vila (2 zděná podlaží + šindelové mansardové patro)

- Strana JV, orientační číslo 10, poloha: odhad (sekvence); model `houses/cp1918/r4/cp_1918_G_r4.glb` (383 polygonů).
- Identita: První vila za pozemkem 2073 (plán cp_1918_001: vlevo „pozemek domu 2073“, vpravo „zahrada čp. 1906“). Foto cp_1918_001/002 (z ulice: 3 podlaží, dřevem obložené podkroví, arkýř s balkonem), cp_1918_003 (ze zahrady), cp_1918_004 (zadní strany vil z 2072, vzadu muzeum 1360).
- Použité prameny: cp_1918_001 PLANE; cp_1918_001..004 PHOTO; cp_1906,1914,1918_001 PHOTO.
- GIS: bez GIS půdorysu – poloha v řadě odvozena
- Rozměry: HYPOTHESIS 11.5 x 11 m (no GIS)
- Průčelí: photos cp_1918_001/002/003: 3 storeys, wood-clad attic storey under a low hip, bay with balcony on the street side
- Střecha: low hip over the attic storey
- Kontrola: prošla (r4); mansardové patro mělo vzadu a po stranách omítku místo šindelového pláště – opraveno mat_all, nutná přestavba; dvě zděná podlaží, arkýř uprostřed s balkonem, zahradní rizalit se vstupem a 4 stupni sedí s kartami; po přestavbě 25. 10.: šindelový plášť mansardy na všech stranách
- Doklad fasád (r4): main: 2 / 2; back: 3 / 4 + dveře 1
- Hypotézy: půdorys 11,5 × 11 m odhad; poloha: sekvence za 2073 (hypotéza); výšky odhad; entrance centred on the street side (photo shows a side entrance with stairs: uncertain); all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); r3: balcony slab lifted 2 cm above the bay top; masonry eave 7.0 m and mansard storey 7.0-9.4 m scaled from the photos (2 storeys + mansard); the garden basement level and the polygonal shape of the bay are not modelled (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1918_001.jpg | situační náčrt | 4eef196f7709 |
| cp_1906,1914,1918_001.jpg | fotografie | 74600388a0d3 |
| cp_1918_001.jpg | fotografie | c551c46c26e4 |
| cp_1918_002.jpg | fotografie | 4d01312d33c4 |
| cp_1918_003.jpg | fotografie | feaca789c3d4 |
| cp_1918_004.jpg | fotografie | b18e1fb78eff |
| cp_1906,1914,1918_001.jpg | archivní karta (rub) | 918eb097ee1f |
| cp_1918_001.jpg | archivní karta (rub) | d95a4d0c6c0d |
| cp_1918_002.jpg | archivní karta (rub) | 2465d6942e13 |
| cp_1918_003.jpg | archivní karta (rub) | c571e372e98a |
| cp_1918_004.jpg | archivní karta (rub) | 28d774311d9f |

### Čp. 1906: polovina dvojdomu 1906/1907

- Strana JV, orientační číslo 11, poloha: odhad (sekvence); model `houses/cp1906/r4/cp_1906_G_r4.glb` (352 polygonů).
- Identita: Levá (SV) polovina dvojdomu; plán cp_1906_001 (vlevo zahrada 1918, vpravo 1907, „mansardy“, schodiště vzadu). Foto cp_1906_001 (z ulice), cp_1906_002 (zezadu se schodišťovou věží).
- Použité prameny: cp_1906_001 PLANE; cp_1906_001/002 PHOTO; cp_1906,1914,1918_001.
- GIS: bez GIS
- Rozměry: HYPOTHESIS: 10.5 x 12.0 m half of a semi-detached villa (no GIS footprint); position = archive sequence
- Průčelí: photos cp_1906_001/002, cp_1907_001/002: 2 storeys + mansard attic, hipped top, rear stair tower
- Střecha: cp_1906_001.jpg PLANE (3c9f7823) – ruční náčrt střechy a parcely: valby na koncích, hřeben souběžný s ulicí, uprostřed vpředu i vzadu mansardové patro (Mansarda/Mansardy), vstupy ze zahrady
- Kontrola: prošla (r4); černý pás na společné zdi: zadní křídlo leží v rovině zdi hlavního domu (koplanární plochy stejného směru) – opraveno v z4_post (krok m), nutná přestavba; valba přes dvojdům, mansardová patra vpředu a vzadu, vstup ze zahrady sedí s náčrtem; po přestavbě 25. 10.: černý pás zmizel, společná zeď souvislá; ostatní pohledy beze změny
- Doklad fasád (r4): main: 2 / 2; dormers: 1; back: hypotéza
- Hypotézy: půdorys 10,5 × 12 m odhad; poloha sekvence; mansarda zjednodušena; entrance at the outer end of each half (uncertain); body depth, mansard storeys, rear block and dormer positions read on the unscaled hand sketch (ratios to the half width, averaged over both halves of the pair) – model_hypothesis, provisional, locked=false; eave 6.6 m, mansard storey 2.7 m, ridge rise 3.6 m estimated from photographs; small triangular dormers on the hipped ends and on the rear slope (sketch) are not modelled

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1906_001.jpg | situační náčrt | 436ad37e26cf |
| cp_1906,1914,1918_001.jpg | fotografie | 74600388a0d3 |
| cp_1906_001.jpg | fotografie | 6b3a7f6b96ea |
| cp_1906_002.jpg | fotografie | 21dcd0cf498f |
| cp_1906,1914,1918_001.jpg | archivní karta (rub) | 918eb097ee1f |
| cp_1906_001.jpg | archivní karta (rub) | adcd251490a6 |
| cp_1906_002.jpg | archivní karta (rub) | 33c55ab1975c |

### Čp. 1907: polovina dvojdomu 1906/1907

- Strana JV, orientační číslo 12, poloha: odhad (sekvence); model `houses/cp1907/r4/cp_1907_G_r4.glb` (346 polygonů).
- Identita: Pravá (JZ) polovina dvojdomu (plán cp_1907_001: vlevo 1906). Foto cp_1907_001 (z ulice), cp_1907_002 (zezadu).
- Použité prameny: cp_1907_001 PLANE; cp_1907_001/002 PHOTO.
- GIS: bez GIS
- Rozměry: HYPOTHESIS: 10.5 x 12.0 m half of a semi-detached villa (no GIS footprint); position = archive sequence
- Průčelí: photos cp_1906_001/002, cp_1907_001/002: 2 storeys + mansard attic, hipped top, rear stair tower
- Střecha: cp_1907_001.jpg PLANE (801ea125) – ruční náčrt střechy a parcely: valby na koncích, hřeben souběžný s ulicí, uprostřed vpředu i vzadu mansardové patro (Mansarda/Mansardy), vstupy ze zahrady
- Kontrola: prošla (r4); černý pás na společné zdi (stejná příčina jako 1906) – opraveno, nutná přestavba; zrcadlo 1906 podle náčrtu cp_1907_001; po přestavbě 25. 10.: černý pás zmizel; ostatní pohledy beze změny
- Doklad fasád (r4): main: 2 / 2; dormers: 1; back: hypotéza
- Hypotézy: zrcadlo 1906; poloha sekvence; entrance at the outer end of each half (uncertain); body depth, mansard storeys, rear block and dormer positions read on the unscaled hand sketch (ratios to the half width, averaged over both halves of the pair) – model_hypothesis, provisional, locked=false; eave 6.6 m, mansard storey 2.7 m, ridge rise 3.6 m estimated from photographs; small triangular dormers on the hipped ends and on the rear slope (sketch) are not modelled

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1907_001.jpg | situační náčrt | d3ceae21eada |
| cp_1903,1904,1907,1914,1915_001.jpg | fotografie | 7c795be5fbcf |
| cp_1907_001.jpg | fotografie | f9a8e755386c |
| cp_1907_002.jpg | fotografie | c1e818c7ce0f |
| cp_1903,1904,1907,1914,1915_001.jpg | archivní karta (rub) | 7b5ae2f6fcf0 |
| cp_1907_001.jpg | archivní karta (rub) | f7ebf3885972 |
| cp_1907_002.jpg | archivní karta (rub) | 5d2741e75d25 |

### Čp. 1914: polovina dvojdomu 1914/1915

- Strana JV, orientační číslo 13, poloha: odhad (sekvence); model `houses/cp1914/r4/cp_1914_G_r4.glb` (382 polygonů).
- Identita: Levá (SV) polovina dvojdomu (plán cp_1914_001: vlevo zahrada 1907, vpravo 1915). Foto cp_1914_001 (z ulice s autem), cp_1914,1915_001 (zezadu).
- Použité prameny: cp_1914_001 PLANE; cp_1914_001, cp_1914,1915_001 PHOTO; cp_1906,1914,1918_001; cp_1903,1904,1907,1914,1915_001.
- GIS: bez GIS
- Rozměry: HYPOTHESIS: 10.5 x 12.0 m half of a semi-detached villa (no GIS footprint); position = archive sequence
- Průčelí: photos cp_1914_001, cp_1915_001/002, cp_1914,1915_001: 2 storeys + mansard attic
- Střecha: cp_1914_001.jpg PLANE (bea8d1c0) – ruční náčrt střechy a parcely: valby na koncích, hřeben souběžný s ulicí, uprostřed vpředu i vzadu mansardové patro (Mansarda/Mansardy), vstupy ze zahrady
- Kontrola: prošla (r4); černý pás na společné zdi (koplanární zadní křídlo) – opraveno, nutná přestavba; průčelí s širokým oknem u nároží a mansardovým patrem sedí s cp_1914_001; po přestavbě 25. 10.: černý pás zmizel; ostatní pohledy beze změny
- Doklad fasád (r4): main: 2 / 2; dormers: 1; back: hypotéza
- Hypotézy: půdorys 10,5 × 12 m; poloha sekvence; entrance at the outer end of each half (uncertain); body depth, mansard storeys, rear block and dormer positions read on the unscaled hand sketch (ratios to the half width, averaged over both halves of the pair) – model_hypothesis, provisional, locked=false; eave 6.6 m, mansard storey 2.7 m, ridge rise 3.6 m estimated from photographs; small triangular dormers on the hipped ends and on the rear slope (sketch) are not modelled

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1914_001.jpg | situační náčrt | 689dfa72d009 |
| cp_1903,1904,1907,1914,1915_001.jpg | fotografie | 7c795be5fbcf |
| cp_1906,1914,1918_001.jpg | fotografie | 74600388a0d3 |
| cp_1914,1915_001.jpg | fotografie | cb4624a6a334 |
| cp_1914_001.jpg | fotografie | 610de9f27cc2 |
| cp_1903,1904,1907,1914,1915_001.jpg | archivní karta (rub) | 7b5ae2f6fcf0 |
| cp_1906,1914,1918_001.jpg | archivní karta (rub) | 918eb097ee1f |
| cp_1914,1915_001.jpg | archivní karta (rub) | d748688f42bc |
| cp_1914_001.jpg | archivní karta (rub) | b41c9b559b19 |

### Čp. 1915: polovina dvojdomu 1914/1915

- Strana JV, orientační číslo 14, poloha: odhad (sekvence); model `houses/cp1915/r4/cp_1915_G_r4.glb` (406 polygonů).
- Identita: Pravá (JZ) polovina dvojdomu; vpravo „průchod do Vančurovy ulice“ (plán cp_1915_001). Foto cp_1915_001 (z ulice), cp_1915_002 (plot).
- Použité prameny: cp_1915_001 PLANE; cp_1915_001/002 PHOTO.
- GIS: bez GIS
- Rozměry: HYPOTHESIS: 10.5 x 12.0 m half of a semi-detached villa (no GIS footprint); position = archive sequence
- Průčelí: photos cp_1914_001, cp_1915_001/002, cp_1914,1915_001: 2 storeys + mansard attic
- Střecha: cp_1915_001.jpg PLANE (e4d9c383) – ruční náčrt střechy a parcely: valby na koncích, hřeben souběžný s ulicí, uprostřed vpředu i vzadu mansardové patro (Mansarda/Mansardy), vstupy ze zahrady
- Kontrola: prošla (r4); černý pás na společné zdi (koplanární zadní křídlo) – opraveno, nutná přestavba; po přestavbě 25. 10.: černý pás zmizel; ostatní pohledy beze změny
- Doklad fasád (r4): main: 2 / 2; dormers: 1; back: hypotéza; side: 1 / 1
- Hypotézy: zrcadlo 1914; poloha sekvence; entrance at the outer end of each half (uncertain); body depth, mansard storeys, rear block and dormer positions read on the unscaled hand sketch (ratios to the half width, averaged over both halves of the pair) – model_hypothesis, provisional, locked=false; eave 6.6 m, mansard storey 2.7 m, ridge rise 3.6 m estimated from photographs; small triangular dormers on the hipped ends and on the rear slope (sketch) are not modelled

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1915_001.jpg | situační náčrt | 8dfb083ef711 |
| cp_1903,1904,1907,1914,1915_001.jpg | fotografie | 7c795be5fbcf |
| cp_1914,1915_001.jpg | fotografie | cb4624a6a334 |
| cp_1915_001.jpg | fotografie | de1dfcfe7ff4 |
| cp_1915_002.jpg | fotografie | 3eb7a94ed42d |
| cp_1903,1904,1907,1914,1915_001.jpg | archivní karta (rub) | 7b5ae2f6fcf0 |
| cp_1914,1915_001.jpg | archivní karta (rub) | d748688f42bc |
| cp_1915_001.jpg | archivní karta (rub) | c2c65fc85a3b |
| cp_1915_002.jpg | archivní karta (rub) | 7c405f4ec2a2 |

### Čp. 1903: polovina dvojdomu 1903/1904

- Strana JV, orientační číslo 15, poloha: odhad (sekvence); model `houses/cp1903/r4/cp_1903_G_r4.glb` (343 polygonů).
- Identita: „Dvouvilka“ 1903/1904 – levá polovina za průchodem do Vančurovy ul. (plán cp_1903_001: vlevo průchod, vpravo 1904, schodiště vzadu). Foto cp_1903_001 (z ulice), cp_1903_002 (plot), cp_1903_003 (zezadu).
- Použité prameny: cp_1903_001 PLANE; cp_1903_001..003 PHOTO; cp_1903,1904,1907,1914,1915_001 (zadní fronty z 2072).
- GIS: bez GIS
- Rozměry: HYPOTHESIS: 10.5 x 12.0 m half of a semi-detached villa (no GIS footprint); position = archive sequence
- Průčelí: photos cp_1903_001..003, cp_1904_001..004: 2 storeys + mansard attic, side entrance 1904
- Střecha: cp_1903_001.jpg PLANE (4952657a) – ruční náčrt střechy a parcely: valby na koncích, hřeben souběžný s ulicí, uprostřed vpředu i vzadu mansardové patro (Mansarda/Mansardy), vstupy ze zahrady
- Kontrola: prošla (r4); společný komín na dělicí zdi visel 0,4 m přes sousední polovinu – rozdělen na dvě poloviny, nutná přestavba; štít mansardy vpředu, schodišťová věž vzadu se vstupem a schody podle náčrtu; po přestavbě 25. 10.: polovina společného komínu stojí od koruny zdi, bez černé plochy na dělicí zdi; ostatní pohledy beze změny
- Doklad fasád (r4): main: 2 / 2; dormers: 2; back: hypotéza
- Hypotézy: půdorys 10,5 × 12 m; poloha sekvence; entrance at the outer end of each half (uncertain); body depth, mansard storeys, rear block and dormer positions read on the unscaled hand sketch (ratios to the half width, averaged over both halves of the pair) – model_hypothesis, provisional, locked=false; eave 6.6 m, mansard storey 2.7 m, ridge rise 3.6 m estimated from photographs; small triangular dormers on the hipped ends and on the rear slope (sketch) are not modelled

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1903_001.jpg | situační náčrt | b84cd0a757f8 |
| cp_1903,1904,1907,1914,1915_001.jpg | fotografie | 7c795be5fbcf |
| cp_1903_001.jpg | fotografie | 8acf59c4d9c1 |
| cp_1903_002.jpg | fotografie | e2643a0569ed |
| cp_1903_003.jpg | fotografie | fa6d98d8836a |
| cp_1903,1904,1907,1914,1915_001.jpg | archivní karta (rub) | 7b5ae2f6fcf0 |
| cp_1903_001.jpg | archivní karta (rub) | 516d27c64868 |
| cp_1903_002.jpg | archivní karta (rub) | c82cf70bf41f |
| cp_1903_003.jpg | archivní karta (rub) | 35e82834348b |

### Čp. 1904: polovina dvojdomu 1903/1904

- Strana JV, orientační číslo 16, poloha: odhad (sekvence); model `houses/cp1904/r4/cp_1904_G_r4.glb` (323 polygonů).
- Identita: Pravá polovina dvojdomu (plán cp_1904_001: vlevo 1903, vpravo zahrada 1899, garáž vzadu). Foto cp_1904_001 (z ulice), cp_1904_002/003 (zezadu, vstup z boku), cp_1904_004 (garáž).
- Použité prameny: cp_1904_001 PLANE; cp_1904_001..004 PHOTO.
- GIS: bez GIS
- Rozměry: HYPOTHESIS: 10.5 x 12.0 m half of a semi-detached villa (no GIS footprint); position = archive sequence
- Průčelí: photos cp_1903_001..003, cp_1904_001..004: 2 storeys + mansard attic, side entrance 1904
- Střecha: cp_1904_001.jpg PLANE (f5c9dc80) – ruční náčrt střechy a parcely: valby na koncích, hřeben souběžný s ulicí, uprostřed vpředu i vzadu mansardové patro (Mansarda/Mansardy), vstupy ze zahrady
- Kontrola: prošla (r4); pohledy bez vady; doplněna polovina společného komínu na dělicí zdi – nutná přestavba a nová kontrola; štít mansardy vpředu u dělicí zdi, zadní vstup se schody podle náčrtu; po přestavbě 25. 10.: polovina společného komínu stojí od koruny zdi, bez černé plochy na dělicí zdi; ostatní pohledy beze změny
- Doklad fasád (r4): main: hypotéza; dormers: hypotéza; back: hypotéza; side: 1 / 1
- Hypotézy: zrcadlo 1903; garáž nemodelována; entrance at the outer end of each half (uncertain); body depth, mansard storeys, rear block and dormer positions read on the unscaled hand sketch (ratios to the half width, averaged over both halves of the pair) – model_hypothesis, provisional, locked=false; eave 6.6 m, mansard storey 2.7 m, ridge rise 3.6 m estimated from photographs; small triangular dormers on the hipped ends and on the rear slope (sketch) are not modelled

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1904_001.jpg | situační náčrt | e590f9d7b48a |
| cp_1903,1904,1907,1914,1915_001.jpg | fotografie | 7c795be5fbcf |
| cp_1904_001.jpg | fotografie | 7d1e61de552c |
| cp_1904_002.jpg | fotografie | cacb126acfb2 |
| cp_1904_003.jpg | fotografie | a8638598ad16 |
| cp_1904_004.jpg | fotografie | 7e5da3079798 |
| cp_1903,1904,1907,1914,1915_001.jpg | archivní karta (rub) | 7b5ae2f6fcf0 |
| cp_1904_001.jpg | archivní karta (rub) | 6c36afa35e93 |
| cp_1904_002.jpg | archivní karta (rub) | bffb8d507b40 |
| cp_1904_003.jpg | archivní karta (rub) | 4e03f1f0c6f7 |
| cp_1904_004.jpg | archivní karta (rub) | fa9bd4110c48 |

### Čp. 1899: polovina dvojdomu 1899/1901

- Strana JV, orientační číslo 17, poloha: odhad (sekvence); model `houses/cp1899/r4/cp_1899_G_r4.glb` (336 polygonů).
- Identita: Levá polovina dvojdomu (plán cp_1899_001: vlevo zahrada 1904, vpravo 1901). Foto cp_1899_001 (z ulice), cp_1899_002 (ze zahrady).
- Použité prameny: cp_1899_001 PLANE; cp_1899_001/002 PHOTO.
- GIS: bez GIS
- Rozměry: HYPOTHESIS: 10.0 x 11.0 m half of a semi-detached villa (no GIS footprint); position = archive sequence
- Průčelí: photos cp_1899_001/002, cp_1901_001/002: 2 storeys + mansard attic
- Střecha: cp_1899_001.jpg PLANE (aa7bdc05) – ruční náčrt střechy a parcely: valby na koncích, hřeben souběžný s ulicí, uprostřed vpředu i vzadu mansardové patro (Mansarda/Mansardy), vstupy ze zahrady
- Kontrola: prošla (r4); společný komín na dělicí zdi visel přes sousední polovinu – rozdělen, nutná přestavba; mansardové patro vpředu a vzadu, vstup ze zahrady podle náčrtu; po přestavbě 25. 10.: polovina komínu v pořádku nad střechou, ale u paty černý čtverec (plocha komínu v rovině dělicí zdi pod korunou) – komín nově začíná na koruně zdi, nutná další přestavba; po přestavbě 25. 10.: polovina společného komínu stojí od koruny zdi, bez černé plochy na dělicí zdi; ostatní pohledy beze změny
- Doklad fasád (r4): main: hypotéza; dormers: hypotéza; back: hypotéza; side: 1 / 1
- Hypotézy: půdorys 10 × 11 m; poloha sekvence; entrance at the outer end of each half (uncertain); body depth, mansard storeys, rear block and dormer positions read on the unscaled hand sketch (ratios to the half width, averaged over both halves of the pair) – model_hypothesis, provisional, locked=false; eave 6.6 m, mansard storey 2.7 m, ridge rise 3.6 m estimated from photographs; small triangular dormers on the hipped ends and on the rear slope (sketch) are not modelled

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1899_001.jpg | situační náčrt | b44090d76bd4 |
| cp_1899_001.jpg | fotografie | f3bf3cc9f0a3 |
| cp_1899_002.jpg | fotografie | edacf6b7a793 |
| cp_1899_001.jpg | archivní karta (rub) | 67d09f274383 |
| cp_1899_002.jpg | archivní karta (rub) | 4bb1e4c7554b |

### Čp. 1901: polovina dvojdomu 1899/1901

- Strana JV, orientační číslo 18, poloha: odhad (sekvence); model `houses/cp1901/r4/cp_1901_G_r4.glb` (312 polygonů).
- Identita: Pravá polovina dvojdomu (plán cp_1901_001: vlevo dvorek 1899, vpravo dvůr domu 1867). Foto cp_1901_001 (z ulice), cp_1901_002 (ze zahrady).
- Použité prameny: cp_1901_001 PLANE; cp_1901_001/002 PHOTO.
- GIS: bez GIS
- Rozměry: HYPOTHESIS: 10.0 x 11.0 m half of a semi-detached villa (no GIS footprint); position = archive sequence
- Průčelí: photos cp_1899_001/002, cp_1901_001/002: 2 storeys + mansard attic
- Střecha: cp_1901_001.jpg PLANE (14b2e223) – ruční náčrt střechy a parcely: valby na koncích, hřeben souběžný s ulicí, uprostřed vpředu i vzadu mansardové patro (Mansarda/Mansardy), vstupy ze zahrady
- Kontrola: prošla (r4); doplněna polovina společného komínu – nutná přestavba a nová kontrola; po přestavbě 25. 10.: polovina společného komínu stojí od koruny zdi, bez černé plochy na dělicí zdi; ostatní pohledy beze změny
- Doklad fasád (r4): main: hypotéza; dormers: hypotéza; back: hypotéza
- Hypotézy: zrcadlo 1899; poloha sekvence; entrance at the outer end of each half (uncertain); body depth, mansard storeys, rear block and dormer positions read on the unscaled hand sketch (ratios to the half width, averaged over both halves of the pair) – model_hypothesis, provisional, locked=false; eave 6.6 m, mansard storey 2.7 m, ridge rise 3.6 m estimated from photographs; small triangular dormers on the hipped ends and on the rear slope (sketch) are not modelled

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1901_001.jpg | situační náčrt | 80ac86d1dca5 |
| cp_1901_001.jpg | fotografie | 56c215a9112b |
| cp_1901_002.jpg | fotografie | 83cad9ec791d |
| cp_1901_001.jpg | archivní karta (rub) | 7528dac6c534 |
| cp_1901_002.jpg | archivní karta (rub) | 6e81d7db3133 |

### Čp. 1867: vila (2 podlaží + mansardové podkroví)

- Strana JV, orientační číslo 19, poloha: odhad (sekvence); model `houses/cp1867/r4/cp_1867_G_r4.glb` (418 polygonů).
- Identita: Samostatná vila (plán cp_1867_001: vlevo zahrada domu 1899/1901, vpravo dvůr domu 1872; „balkon na arkýři“ k ulici, „podezd. balkon“ + schody vlevo). Foto cp_1867_001/002 (z ulice), cp_1867_003 (ze zahrady), cp_1872,1867_001..003 (zadky, pohled ulicí vzhůru).
- Použité prameny: cp_1867_001 PLANE; cp_1867_001..003, cp_1872,1867_001..003 PHOTO.
- GIS: bez GIS
- Rozměry: HYPOTHESIS 12 x 10.5 m (no GIS)
- Průčelí: photos cp_1867_001/002/003, sketch cp_1867_001: balcony on a street bay, pedestal balcony + stairs on the left side
- Střecha: mansard-type attic (photo cp_1867_002)
- Kontrola: prošla (r4); mansarda s vikýři, štít s balkonovými dveřmi a balkon na arkýři, podezděný balkon se schody podél levé zdi a zadní vstup podle náčrtu cp_1867_001
- Doklad fasád (r4): main: 1 / 2; dormers: hypotéza + dveře 1; left: hypotéza; back: hypotéza
- Hypotézy: půdorys 12 × 10,5 m; poloha sekvence; mansardové podkroví zjednodušeno; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); depth 9.16 m, bay, podium balcony with stairs along the left wall and rear entrance from the unscaled sketch cp_1867_001 PLANE (70c6061c) (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1867_001.jpg | situační náčrt | b75533a3421f |
| cp_1867_001.jpg | fotografie | 888eeb8183ff |
| cp_1867_002.jpg | fotografie | fe1e50f382a3 |
| cp_1867_003.jpg | fotografie | 7ebd3662c349 |
| cp_1872,1867_001.jpg | fotografie | 2151e7c52a83 |
| cp_1872,1867_002.jpg | fotografie | 23c1ce23b2c5 |
| cp_1872,1867_003.jpg | fotografie | 8cc9efff42f5 |
| cp_1867_001.jpg | archivní karta (rub) | f3255a950b76 |
| cp_1867_002.jpg | archivní karta (rub) | 98625ec5aff8 |
| cp_1867_003.jpg | archivní karta (rub) | 8296007ba27d |
| cp_1872,1867_001.jpg | archivní karta (rub) | b9e4a4f544db |
| cp_1872,1867_002.jpg | archivní karta (rub) | 0fe1363dc298 |
| cp_1872,1867_003.jpg | archivní karta (rub) | 3e2fd2d16d4c |

### Čp. 1872: vila (poslední zbořená)

- Strana JV, orientační číslo 20, poloha: odhad (sekvence); model `houses/cp1872/r4/cp_1872_G_r4.glb` (358 polygonů).
- Identita: Poslední zbořená vila ulice (karty: „2 poslední zbořené vilky“, za ní trojdům 2104–2106 Larcovy ul. zachován). Plán cp_1872_001: arkýř k ulici, zádveří vlevo, garáž vzadu. Foto cp_1872_001..005 (z ulice shora/zdola, bok, zadek).
- Použité prameny: cp_1872_001 PLANE; cp_1872_001..005, cp_1872,1867_001..003 PHOTO.
- GIS: bez GIS
- Rozměry: HYPOTHESIS 12 x 10.5 m (no GIS)
- Průčelí: photos cp_1872_001..005, sketch cp_1872_001: oriel to the street, porch (zadveri) on the left, hip roof with small dormers
- Střecha: hip (photo cp_1872_002/004)
- Kontrola: prošla (r4); arkýř se štítovým patrem a 2 okny, levé křídlo s valbou zaústěnou do hlavní střechy, zádveří se vstupem a 3 schody podle náčrtu cp_1872_001; okna vlevo a vpravo od arkýře v obou podlažích
- Doklad fasád (r4): main: 2 / 2; dormers: 2
- Hypotézy: půdorys 12 × 10,5 m; poloha sekvence; arkýř zjednodušen na hranol; porch size; all storey heights, opening sizes and roof pitches are estimates from photographs (model_hypothesis, provisional, locked=false); footprint depth 9.4 m, bay, gable storey, left wing and porch from the unscaled sketch cp_1872_001.jpg PLANE (f7dfe386) – ruční náčrt (ratios to the 12 m front); triangular dormers on the rear slope and right hip (sketch) not modelled (model_hypothesis, provisional, locked=false)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1872_001.jpg | situační náčrt | b8d07193f56a |
| cp_1872,1867_001.jpg | fotografie | 2151e7c52a83 |
| cp_1872,1867_002.jpg | fotografie | 23c1ce23b2c5 |
| cp_1872,1867_003.jpg | fotografie | 8cc9efff42f5 |
| cp_1872_001.jpg | fotografie | 43513147c4e6 |
| cp_1872_002.jpg | fotografie | 7201118916ed |
| cp_1872_003.jpg | fotografie | cea1dd5e1035 |
| cp_1872_004.jpg | fotografie | 9a60533d6625 |
| cp_1872_005.jpg | fotografie | 890ba79e0387 |
| cp_1872,1867_001.jpg | archivní karta (rub) | b9e4a4f544db |
| cp_1872,1867_002.jpg | archivní karta (rub) | 0fe1363dc298 |
| cp_1872,1867_003.jpg | archivní karta (rub) | 3e2fd2d16d4c |
| cp_1872_001.jpg | archivní karta (rub) | 43bb59a5c9e4 |
| cp_1872_002.jpg | archivní karta (rub) | 2cbc05a74ec6 |
| cp_1872_003.jpg | archivní karta (rub) | 739e959c64eb |
| cp_1872_004.jpg | archivní karta (rub) | 74fb4b566001 |
| cp_1872_005.jpg | archivní karta (rub) | 12d6d530ccb5 |
