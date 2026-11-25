# Rudolfova (Karla Liebknechta): zpráva o 3D modelu ulice a jeho pramenech

Projekt MOST, GRAFIT FIT ČVUT, 25. 11. 2026. Geometrie a stránka: Claude (Anthropic); textury doplňuje Codex. Web: https://grafitctu.github.io/most/rudolfova/

## Co kde stálo

Poloha všech domů pochází z GIS vrstvy projektu, která je vektorizací historického plánu města Mostu z roku 1938. Rudolfova v ní vede jako ulice č. 63 s 23 budovami. Západní strana od Teplické: nárožní hostinec 692 „Zum grünen Baum“, Griesbachova řada 830, 812, 851, 865, Riessovy domy 1131 a nárožní 1166 u Goethovy, za Goethovou 1167 a 1216 (roh Grillparzerovy), dál na sever dva bloky 1503 a 1504 pro železniční zřízence, dvojdům 1833/1835, dům 1824 (v GIS označený 1784) a 1813. Východní strana: stará nádražní budova 513/514 a skladiště 729 s domkem 878 až u kolejiště, vily 1691 a 1692 a na severním konci u Pařidelské dům 1825. Budova bez čísla popisného 130 m východně od ulice do modelu nepatří. Kliknutím na zelený nebo oranžový dům v mapě otevřete jeho stránku.

### Co o ulici říkají archivní listy

- Situace na projektu čp. 1216 (J. Staněk, 1903, 1:720) řadí parcely 1167 | 1216 | 1182 u Goethovy; skica z roku 1942 u čp. 1131 kreslí blok Goethe-Str. – Rudolf-Straße – Reichsbahn s domy 1166, 1131, 965, 851, 812, 830.

- Situace Franze Griesbacha (1891) ukazuje jeho parcely 3022 podél „Aerarial-Strasse nach Teplitz“ a cesty k pražsko-duchcovské dráze; hostinec 692 stojí na nároží.

- Skici KSPPOP u rodinných domů na severu nesou čísla domů 17–20 a 4–6; karta k čp. 1824 uvádí, že vedlejší polovina dvojdomu (1813) byla při fotografování už v demolici.

### Databázová oblast „Liebknechtova“ je širší než ulice

Živý výpis z databáze Libuše (23. 10. 2026) obsahuje v oblasti 29 struktur. Dvacet jedna z nich jsou domy této ulice; čp. 1167 má strukturu bez jediné přílohy. Dalších struktury leží podle GIS v Pařidelské (426, 1425 – jiné vlákno), v Nádražní nebo nemají v GIS budovu; jejich přílohy jsme prohlédli, ale modelovány zde nejsou:

| Čp. | Ulice podle GIS | Přílohy |
|---|---|---|
| 426 | Pařidelská | 16 |
| 540 | Gassmanova, Nádražní | 15 |
| 552 | v GIS není | 1 |
| 740 | Nádražní, Okružní | 2 |
| 1425 | Pařidelská | 14 |
| 1784 | Pod Širokým vrchem, Rudolfova | 2 |
| 1930 | v GIS není | 3 |

## Odkud jsou prameny

### Databáze Libuše projektu MOST

U všech 29 struktur oblasti Liebknechtova jsme 23. 10. 2026 živě načetli seznam příloh, pouze pro čtení: 303 příloh (213 unikátních souborů): černobílé fotografie, archivní karty, pohlednice, stavební plány a jejich kolorované odvozeniny. Snapshot ze září 2026 měl jiný obsah (chyběly struktury 692 a 1167, u mnoha domů přibyly listy) – pracujeme jen se živým stavem a jeho kontrolními součty. Každou přílohu jsme otevřeli; náhledy jsou na stránkách domů a seznam s SHA-256 v [zprávě](ZPRAVA.md).

### Stavební plány

Ulice má neobvykle mnoho výkresů: projekty Franze Griesbacha pro domy 830 (18. 12. 1891), 812, 851 (1898) a 865 (1888) a pro hostinec 692 (1891), projekty Josefa Riesse pro 1131 a nárožní 1166 (říjen 1901), plán Kateřiny Staňkové pro 1216 (1903) se situací, krovem a řezem, úplnou sadu typového domu pro železniční zřízence B1 (Praha 1924) pro bloky 1503/1504, plán vil Theresia Tiefbau-Gewerkschaft (Wettstein 1929) pro 1691/1692 a plány stavitele Bartáka pro rodinné domy 1813, 1825, 1833, 1835. Projekt dokládá záměr, ne provedení: u šesti domů bez fotografie je proto celý model projektová hypotéza.

### Fotografie a karty

Fotografií je méně než plánů: průčelí 1216 s tabulkou 1216/13 a jeho dvůr, pohlednice z železniční lávky do Teplické s nárožím 692 (před 1918), blok 1503/1504 z ulice a ze dvora, staré nádraží 513/514 z obou stran, skladiště 729 s domkem 878, vily 1691/1692, dvojdům 1833/1835, 1825 a 1824; dům 1813 jen při demolici. Ručně psané karty KSPPOP a jejich skici určují, co snímek ukazuje a kde dům stál.

### Odvozeniny

Kolorované snímky v databázi jsou rekonstrukce, ne prameny. O tvaru, otvorech a poškození rozhoduje původní černobílá fotografie.

### GIS a terén

Polohy, natočení a šířky průčelí jsou z GIS vrstvy (vektorizace plánu 1938). Výšky budov v GIS jsou jen zástupný údaj; výšky domů jsou z kótovaných řezů nebo odhad z fotografií. Ulice je v modelu vodorovná (žádný výškopis) a profil ulice (vozovka 10 m, chodníky 2,5 m) je hypotéza.

## Jak vznikla geometrie

- **Rešerše plánů a identita.** Pro každý dům jsme otevřeli všechny přílohy jeho struktury i sousedů. Datace a měřítko se četly v plném rozlišení (u 1166 rozhodlo měřítko odvozené z kót řezu, kterou stěnu list zobrazuje). Pořadí domů potvrzují situace na listech 1216 (1903), 1131 (1942) a skici KSPPOP; rozpor GIS štítku 1784 s archivním čp. 1824 je zapsán v knize nesouladů.

- **Poloha v ulici.** Z GIS půdorysu je průčelní linie k ose ulice, natočení a obrys domu; registr `street_layout_gis.json` drží polohu všech domů. Dům s rizalitem má líc rizalitu na průčelní linii a ustoupené části za ní.

- **Plán domu.** `geometry_plan.json` popisuje průčelí, otvory, římsy, parapety, nadokenní římsy, frontony, pilastry, vikýře, střechu, další fasády (nároží, dvůr, rizalit) a seznam hypotéz. Osy doložených domů jsou z rektifikované fotografie (1216) nebo z fotografie s rámečkem; u projektových domů z výkresu pohledu.

- **Stavba v Blenderu 4.5.** Parametrický builder (verzovaná kopie builderu Kulové z 20. 10. 2026 s doplňky pro ustoupené plochy, zkosené boky střech a zkosená křídla) vyrobí BLEND a GLB s uzavřeným podkrovím a podbitím pod okapy.

- **Brána.** Každý dům prošel automatickou branou: 103 680 paprsků ze 120 pohledů do podkroví, pokrytí zdiva střechou, zkolabovaná UV, síť a počty otvorů proti záznamu `facade_evidence` po fasádách (u domů z projektu proti výkresu).

- **Vizuální kontrola.** Čtyři osy, čtyři rohy střechy, dva podhledy pod okap a pohled shora v materiálových barvách i clay, detaily otvorů, vstupu, nároží a říms z exportovaného GLB; nálezy v manifestu každého domu.

- **Sestava ulice.** Domy na GIS polohách, vozovka s obrubníky, chodníky a předzahrádky (hypotéza profilu), rendery a prohlížeč.

Pracovní složky: F:\MOST\outputudolfova_street_claude_2026-10-23 (geometrie, QA, zpráva), brief pro Codex F:\MOST\outputudolfova_texturing_brief_claude_2026-10-24.

## Rozpory a hypotézy

- **Čp. 692 – projekt × realizace.** Projekt F. Griesbacha z roku 1891 má sedlovou střechu; pohlednice z železniční lávky (před 1918) ukazuje mansardu s pěti vikýři a zkosené nároží s portálem a balkonem. Model sleduje pohlednici; mansarda je zjednodušena na valbu s vikýři (štítek částečné hypotézy).

- **Čp. 1166 – zrcadlový pohled.** Výkres pohledu (říjen 1901) má zkosené nároží vpravo, situace a GIS je kladou na severovýchodní roh. Podle měřítka jde o průčelí do Goethovy (19 m); osy jsou vyneseny od nároží, strana do Rudolfovy (13 m) je bez výkresu a má čtyři osy jako hypotézu.

- **GIS štítek 1784 × archivní 1824.** Budovu mezi 1835 a 1813 vede GIS jako čp. 1784, ale skici a karty KSPPOP tam kladou čp. 1824 (polovinu dvojdomu s 1813). Plán „1784“ patří domu Strejcových na parcele 442/1 v Lomu u Mostu. Model vede dům jako 1824 a rozpor uvádí.

- **Jen projekty.** Domy 830, 812, 851, 865, 1131 a 1166 nemají žádnou fotografii; jsou modelovány z výkresů pohledů a řezů jako projektové hypotézy. Čp. 1167 nemá v databázi nic – model je odhad podle GIS a sousedů.

- **Čp. 1813** je fotografován jen při demolici; průčelí je podle plánu Bartáka a zrcadlově podle sousední poloviny 1824.

- **Živý výpis × snapshot.** Oblast Liebknechtova měla ve snapshotu ze září 2026 37 struktur, živě 29: deset pohlednicových struktur Nádražní zmizelo, 692 a 1167 přibyly, u 18 struktur přibyly přílohy. Pracujeme jen s živým stavem.

- **Šířky.** GIS šířky souhlasí s kótovanými plány v mezích 0,3 m (1216: 12,81 × 12,50; 1131: 11,16 × 11,00); u 1503/1504 je půdorys 24,75 m z krovu typu B1.

- **Výšky a terén.** Ulice je v modelu vodorovná; výšky okapů jsou z řezů (Griesbach 2 × 4,00 m, Riess 3,20 + 3,70, Staněk 3,70/3,60/3,50, typ B1 4 × 3,35) nebo odhad z fotografií (692, nádraží, skladiště). Kóty od ±0 přízemí jsou přepočteny na úroveň ulice.

Všechny rozpory jsou zapsány s obrázky v knize nesouladů pramenů projektu (případy `2026-11-03_rudolfova_*`).

## Přehled domů

| Čp. | Strana | Typ | Štítek | Podlaží | Průčelí × okap (m) | Revize | Přílohy | Textury |
|---|---|---|---|---|---|---|---|---|
| 692 | západní | nárožní hostinec „Zum grünen Baum“ | částečně hypotéza | 2 + mansarda | 15,4 × 10,4 | r3 | 6 | bez textur (hypotéza – jen prosté materiály) |
| 830 | západní | jednopatrový dům (projekt Griesbach 1891) | projektová hypotéza | 2 | 9,4 × 9,2 | r3 | 1 | bez textur (hypotéza – jen prosté materiály) |
| 812 | západní | jednopatrový dům (projekt Griesbach) | projektová hypotéza | 2 | 9,5 × 9,0 | r3 | 2 | bez textur (hypotéza – jen prosté materiály) |
| 851 | západní | jednopatrový dům (projekt Griesbach 1898) | projektová hypotéza | 2 | 9,3 × 8,9 | r3 | 1 | bez textur (hypotéza – jen prosté materiály) |
| 865 | západní | jednopatrový dům (projekt Griesbach 1888) | projektová hypotéza | 2 | 9,5 × 9,1 | r3 | 1 | bez textur (hypotéza – jen prosté materiály) |
| 1131 | západní | jednopatrový dům Josefa Riesse (projekt 1901) | projektová hypotéza | 2 | 11,0 × 7,7 | r2 | 2 | bez textur (hypotéza – jen prosté materiály) |
| 1166 | západní | nárožní dům Josefa Riesse (projekt 1901) | projektová hypotéza | 2 | 19,2 × 7,8 | r3 | 2 | bez textur (hypotéza – jen prosté materiály) |
| 1167 | západní | dům bez pramene (hypotéza podle GIS) | hypotéza podle GIS | 2 (odhad) | 13,1 × 9,0 | r2 | 0 | bez textur (hypotéza – jen prosté materiály) |
| 1216 | západní | dvoupatrový secesní dům Kateřiny Staňkové (1903) | doloženo | 3 | 12,5 × 12,2 | r3 | 5 | zatím bez textur |
| 729 | východní | skladiště u kolejiště | částečně hypotéza | 1 | 61,3 × 6,5 | r1 | 9 | bez textur (hypotéza – jen prosté materiály) |
| 878 | východní | domek u skladiště | částečně hypotéza | 1 | 14,6 × 5,5 | r1 | 9 | bez textur (hypotéza – jen prosté materiály) |
| 513 | východní | stará nádražní budova, severní část | částečně hypotéza | 2 | 22,1 × 11,8 | r2 | 33 | bez textur (hypotéza – jen prosté materiály) |
| 514 | východní | stará nádražní budova, jižní část | částečně hypotéza | 2 | 21,2 × 11,8 | r2 | 30 | bez textur (hypotéza – jen prosté materiály) |
| 1503 | západní | obytný dům pro železniční zřízence, typ B1 (1924) | doloženo | 4 | 24,8 × 17,3 | r2 | 30 | zatím bez textur |
| 1504 | západní | obytný dům pro železniční zřízence, typ B1 (1924) | doloženo | 4 | 24,8 × 17,3 | r2 | 31 | zatím bez textur |
| 1691 | východní | vila Theresia Tiefbau-Gewerkschaft (1929) | doloženo | 2 | 11,2 × 7,9 | r2 | 16 | zatím bez textur |
| 1692 | východní | vila Theresia Tiefbau-Gewerkschaft (1929) | doloženo | 2 | 11,2 × 7,9 | r2 | 17 | zatím bez textur |
| 1833 | západní | rodinný dvojdům Kubíkových, jižní polovina | doloženo | 2 | 13,1 × 6,6 | r1 | 9 | zatím bez textur |
| 1835 | západní | rodinný dům Jaroslava Janáta, severní polovina dvojdomu | doloženo | 2 | 11,9 × 6,5 | r2 | 8 | zatím bez textur |
| 1824 | západní | polovina dvojdomu 1813/1824 (GIS štítek 1784) | identita 1824 / 1784 | 2 | 10,4 × 6,7 | r1 | 8 | bez textur (hypotéza – jen prosté materiály) |
| 1813 | západní | rodinný dům Hodlových, polovina dvojdomu | částečně hypotéza | 2 | 12,5 × 6,7 | r1 | 12 | bez textur (hypotéza – jen prosté materiály) |
| 1825 | východní | rodinný dům Jansových | doloženo | 2 + podkroví | 11,1 × 7,5 | r2 | 18 | zatím bez textur |

## Domy jednotlivě

### Čp. 692: nárožní hostinec „Zum grünen Baum“

> **Stav rekonstrukce – částečně hypotéza:** Jen část domu je doložena fotografií; zbytek je odvozen z plánu nebo ze sousedního domu.

- Nárožní dům Teplická × Rudolfova se zkoseným nárožím (obloukový portál, balkon), pět os do Rudolfovy, mansardová střecha s vikýři. Realizace podle pohlednice z železniční lávky (před 1918) se liší od projektu F. Griesbacha z roku 1891 (sedlová střecha).
- Prameny: pohlednice „Blick vom Eisenbahnsteg in die Teplitzer Strasse“, projekt 1891 (fasáda, řez, krov, situace parcel Griesbach), skica dvorního objektu 1943, GIS půdorys
- Střecha: mansarda s pěti vikýři podle pohlednice; v modelu zjednodušena na valbu se štítovými vikýři (rozhodnutí k posouzení)
- GIS půdorys id 1215 (ulice Rudolfova); geometrie revize r3, 825 polygonů.
- Hypotézy: vysky podlazi (okap 10.4) odhad z pohlednice (projekt 1891: 4.25 + 4.25 + sklep 2.60 nad terenem ~1 m); polohy otvoru do Teplicke a na narozi = hypoteza z sikmeho zaberu pohlednice; mansarda zjednodusena na valbu (topologie strechy neodpovida prameni) - viz roof_check; dvorni objekt (Hofgebaeude 1943) nemodelovan

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_692,704,744,723_001.jpg | fotografie | 67a7dd5b9440 |
| cp_692_001.jpg | plán / výkres | 3e2628c05ccc |
| cp_692_002.jpg | plán / výkres | c72f7ef17873 |
| cp_692_003.jpg | plán / výkres | 0c7cae5ed8c8 |
| cp_692_004.jpg | plán / výkres | 8e0baf63f9e6 |
| cp_692_005.jpg | plán / výkres | 45337bc5e938 |

### Čp. 830: jednopatrový dům (projekt Griesbach 1891)

> **Stav rekonstrukce – projektová hypotéza:** Dům je doložen jen stavebním projektem (plán), ne fotografií; provedení ani dochovaný stav v 60. letech nejsou ověřeny.

- Řadový jednopatrový dům se čtyřmi osami (1 + 2 + 1) a vraty vpravo podle plánu F. Griesbacha z 18. 12. 1891 na parcele 3022 u cesty k pražsko-duchcovské dráze.
- Prameny: projekt (stavební plán), fotografie domu neexistuje: cp_830_001 (Ansicht, Situation, Profil, půdorysy)
- Střecha: sedlová, hřeben podél ulice (Profil), 2 komíny
- GIS půdorys id 1214 (ulice Rudolfova); geometrie revize r3, 311 polygonů.
- Hypotézy: dum dolozen jen projektem 1888-1898 - provedeni, pozdejsi upravy ani stav v 60. letech nejsou overeny; hloubka hlavniho traktu 12.0 m a dvorni pristavek (schody/zachody) 2.3 x 3.0 m zjednoduseny podle pudorysu; bosaz prizemi, vlys s konzolami pod rimsou a sambrany = textura

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_830_001.jpg | plán / výkres | 5626c04b14d3 |

### Čp. 812: jednopatrový dům (projekt Griesbach)

> **Stav rekonstrukce – projektová hypotéza:** Dům je doložen jen stavebním projektem (plán), ne fotografií; provedení ani dochovaný stav v 60. letech nejsou ověřeny.

- Řadový jednopatrový dům se třemi osami, vraty vpravo a frontony nad okny patra podle projektu F. Griesbacha (90. léta 19. století).
- Prameny: projekt (stavební plán), fotografie domu neexistuje: cp_812_001 a cp_812_002
- Střecha: sedlová, hřeben podél ulice, 2 komíny
- GIS půdorys id 1213 (ulice Rudolfova); geometrie revize r3, 327 polygonů.
- Hypotézy: dum dolozen jen projektem 1888-1898 - provedeni, pozdejsi upravy ani stav v 60. letech nejsou overeny; hloubka hlavniho traktu 12.0 m a dvorni pristavek (schody/zachody) 2.3 x 3.0 m zjednoduseny podle pudorysu; bosaz prizemi, vlys s konzolami pod rimsou a sambrany = textura

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_812_001.jpg | plán / výkres | 26aa796f8bb6 |
| cp_812_002.jpg | plán / výkres | 58fae7f2eaa2 |

### Čp. 851: jednopatrový dům (projekt Griesbach 1898)

> **Stav rekonstrukce – projektová hypotéza:** Dům je doložen jen stavebním projektem (plán), ne fotografií; provedení ani dochovaný stav v 60. letech nejsou ověřeny.

- Řadový jednopatrový dům se čtyřmi osami (1 + 2 + 1), vraty vpravo a dvěma volskými oky podle projektu F. Griesbacha (kolky 1898).
- Prameny: projekt (stavební plán), fotografie domu neexistuje: cp_851_001
- Střecha: sedlová, hřeben podél ulice, 2 volská oka, 2 komíny
- GIS půdorys id 1212 (ulice Rudolfova); geometrie revize r3, 383 polygonů.
- Hypotézy: dum dolozen jen projektem 1888-1898 - provedeni, pozdejsi upravy ani stav v 60. letech nejsou overeny; hloubka hlavniho traktu 12.0 m a dvorni pristavek (schody/zachody) 2.3 x 3.0 m zjednoduseny podle pudorysu; bosaz prizemi, vlys s konzolami pod rimsou a sambrany = textura

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_851_001.jpg | plán / výkres | 2a0f3e9c63ca |

### Čp. 865: jednopatrový dům (projekt Griesbach 1888)

> **Stav rekonstrukce – projektová hypotéza:** Dům je doložen jen stavebním projektem (plán), ne fotografií; provedení ani dochovaný stav v 60. letech nejsou ověřeny.

- Řadový jednopatrový dům se třemi osami, vraty vlevo, frontony v patře a třemi volskými oky podle projektu F. Griesbacha (kolky 1888).
- Prameny: projekt (stavební plán), fotografie domu neexistuje: cp_865_001
- Střecha: sedlová, hřeben podél ulice, 3 volská oka, 2 komíny
- GIS půdorys id 1211 (ulice Rudolfova); geometrie revize r3, 492 polygonů.
- Hypotézy: dum dolozen jen projektem 1888-1898 - provedeni, pozdejsi upravy ani stav v 60. letech nejsou overeny; hloubka hlavniho traktu 12.0 m a dvorni pristavek (schody/zachody) 2.3 x 3.0 m zjednoduseny podle pudorysu; bosaz prizemi, vlys s konzolami pod rimsou a sambrany = textura

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_865_001.jpg | plán / výkres | fc6236f9f6bb |

### Čp. 1131: jednopatrový dům Josefa Riesse (projekt 1901)

> **Stav rekonstrukce – projektová hypotéza:** Dům je doložen jen stavebním projektem (plán), ne fotografií; provedení ani dochovaný stav v 60. letech nejsou ověřeny.

- Jednopatrový dům 11 × 11 m se vstupem uprostřed a sdruženými okny podle projektu z října 1901; skica z roku 1942 (nouzový byt ve dvoře) potvrzuje polohu v řadě 865 | 1131 | 1166.
- Prameny: projekt (stavební plán), fotografie domu neexistuje: cp_1131_001 (Ansicht, Profil, půdorysy), cp_1131_002 (situace bloku 1942)
- Střecha: sedlová, hřeben podél ulice, 2 komíny
- GIS půdorys id 1210 (ulice Rudolfova); geometrie revize r2, 268 polygonů.
- Hypotézy: dum dolozen jen projektem 10/1901 - provedeni a stav v 60. letech neovereny; dvorni schodistovy pristavek 4.7 x 2.5 m zjednodusen (Grundbau); bosaz prizemi a sambrany = textura

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1131_001.jpg | plán / výkres | 2e08b6c5167d |
| cp_1131_002.jpg | plán / výkres | 7f2a0122107d |

### Čp. 1166: nárožní dům Josefa Riesse (projekt 1901)

> **Stav rekonstrukce – projektová hypotéza:** Dům je doložen jen stavebním projektem (plán), ne fotografií; provedení ani dochovaný stav v 60. letech nejsou ověřeny.

- Nárožní dům Goethova × Rudolfova se zkoseným nárožím a krámem; šest os do Goethovy podle projektu z října 1901, strana do Rudolfovy bez výkresu pohledu.
- Prameny: projekt (stavební plán), fotografie domu neexistuje: cp_1166_001 (Profil, Ansicht, Situation, půdorysy), cp_1166_002 (1. patro)
- Střecha: sedlová nad křídlem do Goethovy s valbou nad nárožím (hypotéza), nižší dvorní blok s pultem
- GIS půdorys id 1209 (ulice Rudolfova); geometrie revize r3, 480 polygonů.
- Hypotézy: dum dolozen jen projektem 10/1901; zrcadleni Ansichtu vuci situaci (narozi vpravo x SV roh) - osy vyneseny od narozi; pruceli do Rudolfovy (13 m, mistnosti 20/19/18) bez vykresu: 4 osy hypoteza; zkoseni narozi 1.3 m podle Ansichtu (GIS roh ostry); jizni prodlouzeni vychodniho kridla (GIS) jako nizsi blok s pultovou strechou; schodistovy vystupek GIS 0.45 m vynechan

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1166_001.jpg | plán / výkres | 7af7bcca5fc2 |
| cp_1166_002.jpg | plán / výkres | 5bde1a487c4b |

### Čp. 1167: dům bez pramene (hypotéza podle GIS)

> **Stav rekonstrukce – hypotéza podle GIS:** Bez pramene v archivu Libuše: půdorys z GIS, výšky a členění fasády jsou odhad podle sousedů.

- Dům mezi 1220 a 1216 známý jen z GIS půdorysu a ze situace 1903 na plánu čp. 1216; v databázi nemá žádnou přílohu.
- Prameny: žádné – GIS půdorys, situace 1903 na cp_1216_001
- Střecha: sedlová (odhad podle sousedů)
- GIS půdorys id 1148 (ulice Rudolfova); geometrie revize r2, 205 polygonů.
- Hypotézy: cely dum je hypoteza podle GIS pudorysu a sousedu: 2 podlazi (okap 9.0 m), 4 osy, vrata vpravo, sedlova strecha; na fotografii 1216 (ATO119_10_28_102) je vlevo videt sklon strechy souseda nad nizsim okapem - 1167 byl nizsi nez 1216

### Čp. 1216: dvoupatrový secesní dům Kateřiny Staňkové (1903)

- Dvoupatrový dům se čtyřmi osami, průjezdem a pilastry; na fotografii nese tabulku 1216/13. Osy jsou z rektifikované fotografie, výšky z plánu J. Staňka 1903.
- Prameny: fotografie průčelí a dvora (schodišťový rizalit), plán 1903 (řez, pohled, situace 1167 | 1216 | 1182, krov, půdorysy)
- Střecha: sedlová, hřeben podél ulice, 3 komíny (krov 1903); dvorní rizalit s pultem
- GIS půdorys id 1149 (ulice Rudolfova); geometrie revize r3, 562 polygonů.
- Hypotézy: polohy otvoru dvorniho pruceli a rizalitu odhad z nerektifikovane fotografie; hloubka rizalitu 1.7 m (plan: 1.60 + zed); sirka 12.50 podle planu; GIS hrana 12.81 m (rozdil 0.31 m ponechan jako spara k 1182); plochy pilastru 6 cm, florální reliéfy a bosáž přízemí = textura (Codex)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_28_102.jpg | fotografie | e18be1e5a77f |
| ATO119_10_28_102_col.png | odvozenina (kolorovaná / FRONT) | cb6a3e00ef80 |
| ATO119_10_28_103.jpg | fotografie | b8b8756f441b |
| ATO119_10_28_103_col.png | odvozenina (kolorovaná / FRONT) | 26dba1b60f9a |
| cp_1216_001.jpg | plán / výkres | 2d7f95049032 |

### Čp. 729: skladiště u kolejiště

> **Stav rekonstrukce – částečně hypotéza:** Jen část domu je doložena fotografií; zbytek je odvozen z plánu nebo ze sousedního domu.

- Dlouhý přízemní objekt (61 m) s rampou podél kolejí za nádražím; fotografie od kolejiště.
- Prameny: fotografie cp_729,878_001–003, GIS půdorys
- Střecha: sedlová
- GIS půdorys id 1558 (ulice Rudolfova); geometrie revize r1, 331 polygonů.
- Hypotézy: výška okapu 6,5 m a sklon střechy ~35° odhad (šikmé snímky); otvory uliční (západní) strany – žádná fotografie; vrata a okna k rampě v pravidelném rytmu 6,1 m – odhad; stříška nad rampou zjednodušena na vodorovnou desku (na snímku pokračuje sklon střechy); volná rampa jižně od skladu 8 m – odhad

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_729,878_001.jpg | archivní karta | e42f5fb6b16c |
| cp_729,878_001.jpg | fotografie | ec56fece4bf9 |
| cp_729,878_001_col.png | odvozenina (kolorovaná / FRONT) | a4ebd7aeee89 |
| cp_729,878_002.jpg | fotografie | db265235bcc8 |
| cp_729,878_002.jpg | archivní karta | 95f3b5636c80 |
| cp_729,878_002_col.png | odvozenina (kolorovaná / FRONT) | b662a84f4268 |
| cp_729,878_003.jpg | archivní karta | 7918e4cbab73 |
| cp_729,878_003.jpg | fotografie | 153cbc5b79ba |
| cp_729,878_003_col.png | odvozenina (kolorovaná / FRONT) | 797874a3c8d1 |

### Čp. 878: domek u skladiště

> **Stav rekonstrukce – částečně hypotéza:** Jen část domu je doložena fotografií; zbytek je odvozen z plánu nebo ze sousedního domu.

- Domek s valbovou střechou vedle skladiště 729.
- Prameny: fotografie cp_729,878_002, GIS půdorys
- Střecha: valba
- GIS půdorys id 1557 (ulice Rudolfova); geometrie revize r1, 193 polygonů.
- Hypotézy: výška okapu 5,5 m odhad; uliční (západní) okna a východní otvory – odhad; rampa u kanceláří navazuje na rampu skladu – odhad

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_729,878_001.jpg | fotografie | ec56fece4bf9 |
| cp_729,878_001.jpg | archivní karta | e42f5fb6b16c |
| cp_729,878_001_col.png | odvozenina (kolorovaná / FRONT) | a4ebd7aeee89 |
| cp_729,878_002.jpg | archivní karta | 95f3b5636c80 |
| cp_729,878_002.jpg | fotografie | db265235bcc8 |
| cp_729,878_002_col.png | odvozenina (kolorovaná / FRONT) | b662a84f4268 |
| cp_729,878_003.jpg | archivní karta | 7918e4cbab73 |
| cp_729,878_003.jpg | fotografie | 153cbc5b79ba |
| cp_729,878_003_col.png | odvozenina (kolorovaná / FRONT) | 797874a3c8d1 |

### Čp. 513: stará nádražní budova, severní část

> **Stav rekonstrukce – částečně hypotéza:** Jen část domu je doložena fotografií; zbytek je odvozen z plánu nebo ze sousedního domu.

- Severní polovina (číslo 513 podtržené na kartě 007, snímek od 1691) staré budovy pražsko-duchcovského nádraží mezi Rudolfovou a kolejištěm (skica KSPPOP 513/1 + 514/2).
- Prameny: fotografie cp_513,514_001–008, FOTO-000783, karty, skica
- Střecha: valby se štítovými rizality
- GIS půdorys id 1560 (ulice Rudolfova); geometrie revize r2, 654 polygonů.
- Hypotézy: výšky podlaží ~4,0 m (řady oken na snímku 003), okap 11,8 – odhad; osy střední části 2 × 4 podle snímku z kolejiště (8 os) – polohy odhad; okulus ve štítu, šambrány, římsy pod štíty = textura; střední štít jako dvě poloviny (513 vpravo, 514 vlevo) na společné zdi

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| FOTO-000783.jpg | fotografie | 80c0f734383c |
| FOTO-000783_col.png | odvozenina (kolorovaná / FRONT) | 89c70903625a |
| cp_513,514,1503,1504_001.jpg | fotografie | 0ffbc27d40c8 |
| cp_513,514,1503,1504_001.jpg | archivní karta | ec473294bb64 |
| cp_513,514,1503,1504_001_col.png | odvozenina (kolorovaná / FRONT) | ba64e3c5925d |
| cp_513,514_001.jpg | fotografie | d1af0fdc0e8b |
| cp_513,514_001.jpg | fotografie | 0af6fffcb033 |
| cp_513,514_001.jpg | archivní karta | 4ec0ef28dd7a |
| cp_513,514_001.jpg | archivní karta | b5210d6317a6 |
| cp_513,514_001.jpg | odvozenina (kolorovaná / FRONT) | 0fdf6bd73654 |
| cp_513,514_002.jpg | archivní karta | 2e669ab3e573 |
| cp_513,514_002.jpg | fotografie | 6cecd0ba95ce |
| cp_513,514_002_col.png | odvozenina (kolorovaná / FRONT) | 311175be7dc7 |
| cp_513,514_003.jpg | fotografie | 9070c9400845 |
| cp_513,514_003.jpg | archivní karta | a23b23a542e6 |
| cp_513,514_003_col.png | odvozenina (kolorovaná / FRONT) | 73016d121976 |
| cp_513,514_004.jpg | fotografie | 5fdb589a1026 |
| cp_513,514_004.jpg | archivní karta | 94e17dbcd143 |
| cp_513,514_004_col.png | odvozenina (kolorovaná / FRONT) | 160774d95e6c |
| cp_513,514_005.jpg | fotografie | 6e9494325bed |
| cp_513,514_005.jpg | archivní karta | 685465514c19 |
| cp_513,514_005_col.png | odvozenina (kolorovaná / FRONT) | 83b6fd592626 |
| cp_513,514_006.jpg | fotografie | 6b7678bbd81b |
| cp_513,514_006.jpg | archivní karta | 41bed257ef1d |
| cp_513,514_006_col.png | odvozenina (kolorovaná / FRONT) | c7e6aeed13a9 |
| cp_513,514_007.jpg | plán / výkres | 417613b6c773 |
| cp_513,514_007.jpg | archivní karta | af09e1e7bd0c |
| cp_513,514_007.jpg | odvozenina (kolorovaná / FRONT) | c92f006ac0d0 |
| cp_513,514_007.jpg | fotografie | b6ce2c749e10 |
| cp_513,514_007_col.png | odvozenina (kolorovaná / FRONT) | 449019007c87 |
| cp_513,514_008.jpg | fotografie | 6b065168fa0b |
| cp_513,514_008.jpg | archivní karta | eaaa5af9f0c2 |
| cp_513,514_008_col.png | odvozenina (kolorovaná / FRONT) | 82f88cad9f9e |

### Čp. 514: stará nádražní budova, jižní část

> **Stav rekonstrukce – částečně hypotéza:** Jen část domu je doložena fotografií; zbytek je odvozen z plánu nebo ze sousedního domu.

- Jižní polovina staré nádražní budovy (číslování polovin viz kniha nesouladů, případ 513/514).
- Prameny: táž série jako 513
- Střecha: valby se štítovými rizality
- GIS půdorys id 1561 (ulice Rudolfova); geometrie revize r2, 654 polygonů.
- Hypotézy: výšky podlaží ~4,0 m (řady oken na snímku 003), okap 11,8 – odhad; osy střední části 2 × 4 podle snímku z kolejiště (8 os) – polohy odhad; okulus ve štítu, šambrány, římsy pod štíty = textura; střední štít jako dvě poloviny (513 vpravo, 514 vlevo) na společné zdi

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| FOTO-000783.jpg | fotografie | 80c0f734383c |
| FOTO-000783_col.png | odvozenina (kolorovaná / FRONT) | 89c70903625a |
| cp_513,514,1503,1504_001.jpg | fotografie | 0ffbc27d40c8 |
| cp_513,514,1503,1504_001.jpg | archivní karta | ec473294bb64 |
| cp_513,514,1503,1504_001_col.png | odvozenina (kolorovaná / FRONT) | ba64e3c5925d |
| cp_513,514_001.jpg | fotografie | 0af6fffcb033 |
| cp_513,514_001.jpg | archivní karta | 4ec0ef28dd7a |
| cp_513,514_002.jpg | archivní karta | 2e669ab3e573 |
| cp_513,514_002.jpg | fotografie | 6cecd0ba95ce |
| cp_513,514_002_col.png | odvozenina (kolorovaná / FRONT) | 311175be7dc7 |
| cp_513,514_003.jpg | fotografie | 9070c9400845 |
| cp_513,514_003.jpg | archivní karta | a23b23a542e6 |
| cp_513,514_003_col.png | odvozenina (kolorovaná / FRONT) | 73016d121976 |
| cp_513,514_004.jpg | fotografie | 5fdb589a1026 |
| cp_513,514_004.jpg | archivní karta | 94e17dbcd143 |
| cp_513,514_004_col.png | odvozenina (kolorovaná / FRONT) | 160774d95e6c |
| cp_513,514_005.jpg | fotografie | 6e9494325bed |
| cp_513,514_005.jpg | archivní karta | 685465514c19 |
| cp_513,514_005_col.png | odvozenina (kolorovaná / FRONT) | 83b6fd592626 |
| cp_513,514_006.jpg | archivní karta | 41bed257ef1d |
| cp_513,514_006.jpg | fotografie | 6b7678bbd81b |
| cp_513,514_006_col.png | odvozenina (kolorovaná / FRONT) | c7e6aeed13a9 |
| cp_513,514_007.jpg | plán / výkres | 417613b6c773 |
| cp_513,514_007.jpg | fotografie | b6ce2c749e10 |
| cp_513,514_007.jpg | odvozenina (kolorovaná / FRONT) | c92f006ac0d0 |
| cp_513,514_007.jpg | archivní karta | af09e1e7bd0c |
| cp_513,514_007_col.png | odvozenina (kolorovaná / FRONT) | 449019007c87 |
| cp_513,514_008.jpg | archivní karta | eaaa5af9f0c2 |
| cp_513,514_008.jpg | fotografie | 6b065168fa0b |
| cp_513,514_008_col.png | odvozenina (kolorovaná / FRONT) | 82f88cad9f9e |

### Čp. 1503: obytný dům pro železniční zřízence, typ B1 (1924)

- Jižní blok dvojice stejných domů s šesti osami, štítovým středním rizalitem a obloukovými okny 3. patra; fotografie bloku z ulice, plány typu B1 (Praha, prosinec 1924).
- Prameny: plány (průčelí, řez, krov, půdorysy, situace parc. 3041/1), fotografie bloku a dvora
- Střecha: sedlová se štítovými čely, střední Zwerchhaus, dvorní rizalit a schodišťová věž
- GIS půdorys id 1562 (ulice Rudolfova); geometrie revize r2, 935 polygonů.
- Hypotézy: vysky odvozeny z pruceli 1:100 (46.3 px/m) - rez ma teren o ~2 m vys (dvur); ulicni uroven = spodni hrana kresby; okna dvorniho rizalitu a schodistove veze nemodelovana (boxy); typ B1 pouzit pro 1503; rozdil B1/B2 (zrcadleni) neoveren; vikyre DL/DR bez oken, stit Z1 jedno okno (foto: trojdilne)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1503,1504_001.jpg | plán / výkres | a59843626ae4 |
| cp_1503,1504_001.jpg | archivní karta | 101930bbf765 |
| cp_1503,1504_001.jpg | fotografie | 72dd3a39f69d |
| cp_1503,1504_001.jpg | odvozenina (kolorovaná / FRONT) | b78360591315 |
| cp_1503,1504_001__2.jpg | plán / výkres | 2039852488a5 |
| cp_1503,1504_001_col.png | odvozenina (kolorovaná / FRONT) | 43936e64703d |
| cp_1503,1504_002.jpg | plán / výkres | a343070044cd |
| cp_1503,1504_002.jpg | archivní karta | bc9ea820be17 |
| cp_1503,1504_002.jpg | fotografie | 40279f71d49c |
| cp_1503,1504_002_col.png | odvozenina (kolorovaná / FRONT) | f0ce7ec000f5 |
| cp_1503,1504_003.jpg | fotografie | 42ac15100070 |
| cp_1503,1504_003.jpg | odvozenina (kolorovaná / FRONT) | 64c9e442c213 |
| cp_1503,1504_003.jpg | plán / výkres | 343f568a86db |
| cp_1503,1504_003.jpg | archivní karta | f7970ea572fc |
| cp_1503,1504_003__2.jpg | plán / výkres | 1275fe7510bc |
| cp_1503,1504_003_col.png | odvozenina (kolorovaná / FRONT) | b6c930158419 |
| cp_1503,1504_004.jpg | plán / výkres | 0a458af12516 |
| cp_1503,1504_005.jpg | plán / výkres | 379508efac2c |
| cp_1503,1504_006.jpg | plán / výkres | 299847c3643a |
| cp_1503,1504_007.jpg | plán / výkres | 1e284614ad73 |
| cp_1503,1504_008.jpg | plán / výkres | 5c69f0a64f82 |
| cp_1503,1504_009.jpg | plán / výkres | 9c73f8823550 |
| cp_1503,1504_010.jpg | plán / výkres | d97b8a81989e |
| cp_1503,1504_011.jpg | plán / výkres | c3d1f8836005 |
| cp_1503,1504_012.jpg | plán / výkres | a62e0482d6c3 |
| cp_1503_001.jpg | fotografie | f4ffc4febeef |
| cp_1503_001.jpg | archivní karta | 1ffdd82db593 |
| cp_513,514,1503,1504_001.jpg | fotografie | 0ffbc27d40c8 |
| cp_513,514,1503,1504_001.jpg | archivní karta | ec473294bb64 |
| cp_513,514,1503,1504_001_col.png | odvozenina (kolorovaná / FRONT) | ba64e3c5925d |

### Čp. 1504: obytný dům pro železniční zřízence, typ B1 (1924)

- Severní blok téhož typu; na fotografii šikmo za 1503.
- Prameny: tytéž plány, fotografie dvora cp_1504_001
- Střecha: jako 1503
- GIS půdorys id 1563 (ulice Rudolfova); geometrie revize r2, 935 polygonů.
- Hypotézy: vysky odvozeny z pruceli 1:100 (46.3 px/m) - rez ma teren o ~2 m vys (dvur); ulicni uroven = spodni hrana kresby; okna dvorniho rizalitu a schodistove veze nemodelovana (boxy); typ B1 pouzit pro 1504; rozdil B1/B2 (zrcadleni) neoveren; vikyre DL/DR bez oken, stit Z1 jedno okno (foto: trojdilne)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1503,1504_001.jpg | fotografie | 72dd3a39f69d |
| cp_1503,1504_001.jpg | archivní karta | 101930bbf765 |
| cp_1503,1504_001.jpg | plán / výkres | a59843626ae4 |
| cp_1503,1504_001.jpg | odvozenina (kolorovaná / FRONT) | 22fcb35fa29a |
| cp_1503,1504_001__2.jpg | plán / výkres | 2039852488a5 |
| cp_1503,1504_001_col.png | odvozenina (kolorovaná / FRONT) | 43936e64703d |
| cp_1503,1504_002.jpg | plán / výkres | a343070044cd |
| cp_1503,1504_002.jpg | archivní karta | bc9ea820be17 |
| cp_1503,1504_002.jpg | fotografie | 40279f71d49c |
| cp_1503,1504_002_col.png | odvozenina (kolorovaná / FRONT) | f0ce7ec000f5 |
| cp_1503,1504_003.jpg | odvozenina (kolorovaná / FRONT) | 64c9e442c213 |
| cp_1503,1504_003.jpg | archivní karta | f7970ea572fc |
| cp_1503,1504_003.jpg | plán / výkres | 343f568a86db |
| cp_1503,1504_003.jpg | fotografie | 42ac15100070 |
| cp_1503,1504_003__2.jpg | plán / výkres | 1275fe7510bc |
| cp_1503,1504_003_col.png | odvozenina (kolorovaná / FRONT) | b6c930158419 |
| cp_1503,1504_004.jpg | plán / výkres | 0a458af12516 |
| cp_1503,1504_005.jpg | plán / výkres | 379508efac2c |
| cp_1503,1504_006.jpg | plán / výkres | 299847c3643a |
| cp_1503,1504_007.jpg | plán / výkres | 1e284614ad73 |
| cp_1503,1504_008.jpg | plán / výkres | 5c69f0a64f82 |
| cp_1503,1504_009.jpg | plán / výkres | 9c73f8823550 |
| cp_1503,1504_010.jpg | plán / výkres | d97b8a81989e |
| cp_1503,1504_011.jpg | plán / výkres | c3d1f8836005 |
| cp_1503,1504_012.jpg | plán / výkres | a62e0482d6c3 |
| cp_1504_001.jpg | archivní karta | 921cee4f8daf |
| cp_1504_001.jpg | fotografie | 8214234ad98b |
| cp_1504_001_col.png | odvozenina (kolorovaná / FRONT) | 94335c939ff2 |
| cp_513,514,1503,1504_001.jpg | fotografie | 0ffbc27d40c8 |
| cp_513,514,1503,1504_001.jpg | archivní karta | ec473294bb64 |
| cp_513,514,1503,1504_001_col.png | odvozenina (kolorovaná / FRONT) | ba64e3c5925d |

### Čp. 1691: vila Theresia Tiefbau-Gewerkschaft (1929)

- Vila podle plánu E. Wettsteina 1929 (11,25 × 10 m), fotografie průčelí a boků.
- Prameny: plán 1929 (Ansicht, Schnitt, Situation, půdorysy), fotografie, skica KSPPOP
- Střecha: valba se štítem (plán)
- GIS půdorys id 1564 (ulice Rudolfova); geometrie revize r2, 290 polygonů.
- Hypotézy: GIS pudorys (12.94 x ~13.3 m, rizalit 1.2-1.7 m) je vetsi nez kotovany plan 11.25 x 10.0 (rizalit 0.44) - pouzit plan, dum vycentrovan na GIS; zadni a bocni otvory podle pudorysu 1929 a fotografii ze dvora - polohy hypoteza; schodiste a zadveri: venkovni schody 0.78 m a strisky jako bloky (Ansicht: stricka nad vstupem); lizeny rizalitu, hornicky znak ve stitu, sambrany = textura; male vetraci vikyre (foto 1691_003, 1692_002) nemodelovany

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1691,1692_001.jpg | plán / výkres | fbf126068d20 |
| cp_1691,1692_002.jpg | plán / výkres | 9a73837442ce |
| cp_1691,1692_003.jpg | plán / výkres | 7d7a119b5a71 |
| cp_1691_001.jpg | archivní karta | c425a50d846b |
| cp_1691_001.jpg | plán / výkres | 98a140f7d256 |
| cp_1691_001.jpg | fotografie | d95b2b01b07f |
| cp_1691_001.jpg | odvozenina (kolorovaná / FRONT) | 99b5e05b4526 |
| cp_1691_001_col.png | odvozenina (kolorovaná / FRONT) | 9b937b5d611b |
| cp_1691_002.jpg | fotografie | 70c1fff5e416 |
| cp_1691_002.jpg | archivní karta | 0447d4a1f2bf |
| cp_1691_002_col.png | odvozenina (kolorovaná / FRONT) | 3fe3bd07ab50 |
| cp_1691_003.jpg | archivní karta | 9f3b4145f849 |
| cp_1691_003.jpg | fotografie | 45c5e3c56343 |
| cp_1691_003_col.png | odvozenina (kolorovaná / FRONT) | 28d85b2400d4 |
| cp_1691_004.jpg | fotografie | f8549060ce96 |
| cp_1691_004.jpg | archivní karta | bb84baba0662 |

### Čp. 1692: vila Theresia Tiefbau-Gewerkschaft (1929)

- Druhá vila stejného typu severně od 1691.
- Prameny: týž plán, fotografie cp_1692_001–004
- Střecha: jako 1691
- GIS půdorys id 1565 (ulice Rudolfova); geometrie revize r2, 314 polygonů.
- Hypotézy: GIS pudorys (11.9 x ~13.3 m, rizalit 1.2-1.7 m) je vetsi nez kotovany plan 11.25 x 10.0 (rizalit 0.44) - pouzit plan, dum vycentrovan na GIS; zadni a bocni otvory podle pudorysu 1929 a fotografii ze dvora - polohy hypoteza; schodiste a zadveri: venkovni schody 0.78 m a strisky jako bloky (Ansicht: stricka nad vstupem); lizeny rizalitu, hornicky znak ve stitu, sambrany = textura; male vetraci vikyre (foto 1691_003, 1692_002) nemodelovany; dvojice zrcadlova vuci planu (vstup a schodiste na jihu) podle fotografie cp_1692_002 a karty

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1691,1692_001.jpg | plán / výkres | fbf126068d20 |
| cp_1691,1692_002.jpg | plán / výkres | 9a73837442ce |
| cp_1691,1692_003.jpg | plán / výkres | 7d7a119b5a71 |
| cp_1692_001.jpg | fotografie | 9db34b130f94 |
| cp_1692_001.jpg | odvozenina (kolorovaná / FRONT) | 89e97e994e4e |
| cp_1692_001.jpg | archivní karta | b0161f650ac2 |
| cp_1692_001.jpg | plán / výkres | a96f2338b515 |
| cp_1692_001_col.png | odvozenina (kolorovaná / FRONT) | ab6ceb7cc967 |
| cp_1692_002.jpg | archivní karta | 5cf116879788 |
| cp_1692_002.jpg | fotografie | b5275c1dbdee |
| cp_1692_002_col.png | odvozenina (kolorovaná / FRONT) | a073a5281e2d |
| cp_1692_003.jpg | fotografie | e1307cb240d9 |
| cp_1692_003.jpg | archivní karta | b8ad7bf47719 |
| cp_1692_003_col.png | odvozenina (kolorovaná / FRONT) | c32a43bffe62 |
| cp_1692_004.jpg | fotografie | 56f5d8bedd4d |
| cp_1692_004.jpg | archivní karta | 43ebe24e598f |
| cp_1692_004_col.png | odvozenina (kolorovaná / FRONT) | 9a791ea0b327 |

### Čp. 1833: rodinný dvojdům Kubíkových, jižní polovina

- Jižní polovina dvojdomu 1833/1835 podle plánu stavitele Bartáka a fotografie z ulice.
- Prameny: plán, fotografie cp_1833,1835_001, skica KSPPOP (17, 18)
- Střecha: podle plánu
- GIS půdorys id 1566 (ulice Rudolfova); geometrie revize r1, 205 polygonů.
- Hypotézy: sirka 13.11 (GIS) x projekt 11.90 - osy prepocteny pomerem; vysky z pohledu projektu (25.3 px/m) a rezu; dvorni schodistovy pristavek podle GIS jako blok s pultem; projekt Kubikovych byl dvojdum 21.35 m; pravou polovinu (9.45 m) nahradil dum Janatuv 1835 - k overeni

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1833,1835_001.jpg | plán / výkres | 83bc2565734b |
| cp_1833,1835_001.jpg | archivní karta | 99f3098bfdf5 |
| cp_1833,1835_001.jpg | fotografie | ec81ccbc4a8a |
| cp_1833,1835_001.jpg | odvozenina (kolorovaná / FRONT) | ec4ed38c26a2 |
| cp_1833,1835_001_col.png | odvozenina (kolorovaná / FRONT) | b3a306502299 |
| cp_1833_001.jpg | plán / výkres | 3f24af655989 |
| cp_1833_001.jpg | archivní karta | f833a4e2a7a2 |
| cp_1833_001.jpg | fotografie | 5a80c51309bd |
| cp_1833_001_col.png | odvozenina (kolorovaná / FRONT) | a317f7f9ab68 |

### Čp. 1835: rodinný dům Jaroslava Janáta, severní polovina dvojdomu

- Severní polovina dvojdomu.
- Prameny: plán, fotografie, skica
- Střecha: podle plánu
- GIS půdorys id 1567 (ulice Rudolfova); geometrie revize r2, 213 polygonů.
- Hypotézy: sklepni okenka za plotem - podle pohledu projektu; vstup ze dvora (projekt: schodiste vzadu); sirka GIS 11.86 x projekt 11.15

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1833,1835_001.jpg | plán / výkres | 83bc2565734b |
| cp_1833,1835_001.jpg | fotografie | ec81ccbc4a8a |
| cp_1833,1835_001.jpg | archivní karta | 99f3098bfdf5 |
| cp_1833,1835_001.jpg | odvozenina (kolorovaná / FRONT) | ec4ed38c26a2 |
| cp_1833,1835_001_col.png | odvozenina (kolorovaná / FRONT) | b3a306502299 |
| cp_1835_001.jpg | fotografie | 7eac58d5acd0 |
| cp_1835_001.jpg | plán / výkres | a3855557f3d4 |
| cp_1835_001.jpg | archivní karta | 26ebfb920d74 |

### Čp. 1824: polovina dvojdomu 1813/1824 (GIS štítek 1784)

> **Stav rekonstrukce – identita 1824 / 1784:** Plán města 1938 zde tiskne čp. 1784, archivní karty a tabulka na domě čp. 1824 (viz kniha nesouladů). Fasáda je doložena fotografií, výšky jsou odhad.

- GIS budovu 1568 vede pod čp. 1784; podle skic a karet KSPPOP jde o archivní čp. 1824, dochovanou polovinu dvojdomu s 1813.
- Prameny: fotografie cp_1824_001/002, karty, skica; plán „1784“ (Strejcovi, parc. 442/1, 1932) k parcele nepatří
- Střecha: podle fotografie
- GIS půdorys id 1568 (ulice Rudolfova); geometrie revize r1, 230 polygonů.
- Hypotézy: vysky podle typu Bartakovych domu (rez 1813: prizemi 2.80, patro 2.70) - fotografie z blizka nelze rektifikovat; GIS bocni pristavek (2.0 x 6.2) na zadni fotografii neni - vynechan; zadni otvory a balkon odhadem z nerektifikovane fotografie

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1824_001.jpg | fotografie | df69302b02b6 |
| cp_1824_001.jpg | archivní karta | cc66a7561387 |
| cp_1824_001.jpg | plán / výkres | f6142a3b3856 |
| cp_1824_001.jpg | odvozenina (kolorovaná / FRONT) | 87159be3e914 |
| cp_1824_001_col.png | odvozenina (kolorovaná / FRONT) | 8067eb4efa55 |
| cp_1824_002.jpg | fotografie | 53515430959a |
| cp_1824_002.jpg | archivní karta | a77725ae8e04 |
| cp_1824_002_col.png | odvozenina (kolorovaná / FRONT) | 0570aa62fdfd |

### Čp. 1813: rodinný dům Hodlových, polovina dvojdomu

> **Stav rekonstrukce – částečně hypotéza:** Jen část domu je doložena fotografií; zbytek je odvozen z plánu nebo ze sousedního domu.

- Severní polovina dvojdomu 1813/1824; fotografie jen z demolice, průčelí podle plánu a zrcadlově podle 1824.
- Prameny: plán Bartáka, fotografie z demolice, skica (20)
- Střecha: podle plánu
- GIS půdorys id 1569 (ulice Rudolfova); geometrie revize r1, 171 polygonů.
- Hypotézy: ulicni fasada jen podle projektu 1932 - realizace nedolozena (dum fotografovan az pri demolici); vysky podle rezu projektu

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1813_001.jpg | fotografie | a711637b5f92 |
| cp_1813_001.jpg | plán / výkres | 67699ae3efc7 |
| cp_1813_001.jpg | archivní karta | 4245469a2225 |
| cp_1813_001.jpg | odvozenina (kolorovaná / FRONT) | 6c7dc3f01609 |
| cp_1813_001__2.jpg | plán / výkres | bf239eca2366 |
| cp_1813_001_col.png | odvozenina (kolorovaná / FRONT) | 77c37cd0d0c4 |
| cp_1813_002.jpg | archivní karta | 69ef8a46545e |
| cp_1813_002.jpg | fotografie | 8e001d860ac3 |
| cp_1813_002_col.png | odvozenina (kolorovaná / FRONT) | 2d232985df86 |
| cp_1813_003.jpg | fotografie | 0ec6f6d88d18 |
| cp_1813_003.jpg | archivní karta | 51cc40897b4a |
| cp_1813_003_col.png | odvozenina (kolorovaná / FRONT) | 7491a62fa6fd |

### Čp. 1825: rodinný dům Jansových

- Vila na východní straně u Pařidelské podle plánu Bartáka a fotografií průčelí a zahrady.
- Prameny: plán, fotografie cp_1825_001–005, skica (6)
- Střecha: valba (plán, fotografie)
- GIS půdorys id 1571 (ulice Rudolfova); geometrie revize r2, 209 polygonů.
- Hypotézy: vysky z pohledu projektu (33 px/m): okap 7.5, hreben 12.1; polohy vikyru odhad z fotografie; vstup ze strany/dvora podle rezu (schodiste vzadu)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1825_001.jpg | fotografie | 26783f66e10c |
| cp_1825_001.jpg | odvozenina (kolorovaná / FRONT) | 9e1141fcb329 |
| cp_1825_001.jpg | plán / výkres | 866501f18e80 |
| cp_1825_001.jpg | archivní karta | a0ab26a38d42 |
| cp_1825_001__2.jpg | plán / výkres | 42e009562638 |
| cp_1825_001_col.png | odvozenina (kolorovaná / FRONT) | 389e3a1e381d |
| cp_1825_002.jpg | archivní karta | 99ab154a678d |
| cp_1825_002.jpg | fotografie | 577df3e81107 |
| cp_1825_002_col.png | odvozenina (kolorovaná / FRONT) | 3b10a8124c2c |
| cp_1825_003.jpg | archivní karta | 6fbe38186775 |
| cp_1825_003.jpg | fotografie | b51fe56145c4 |
| cp_1825_003_col.png | odvozenina (kolorovaná / FRONT) | 53bceef3baf6 |
| cp_1825_004.jpg | archivní karta | a6d54ae4222e |
| cp_1825_004.jpg | fotografie | 850b136c773b |
| cp_1825_004_col.png | odvozenina (kolorovaná / FRONT) | 77e1ca9291ee |
| cp_1825_005.jpg | archivní karta | b68c00cb17c5 |
| cp_1825_005.jpg | fotografie | 7667ed0f4616 |
| cp_1825_005_col.png | odvozenina (kolorovaná / FRONT) | 2038f5fb1403 |
