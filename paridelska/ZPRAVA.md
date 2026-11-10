# Pařidelská (Paredler Straße): zpráva o 3D modelu ulice a jeho pramenech

Projekt MOST, GRAFIT FIT ČVUT, 3. 11. 2026. Geometrie a stránka: Claude (Anthropic); textury doplňuje Codex. Web: https://grafitctu.github.io/most/paridelska/

Stav: ve 3D jsou 4 z 4 budov s půdorysem v GIS. Model ulice (GLB) je k dispozici.

## Co kde stálo

Poloha všech domů pochází z GIS vrstvy projektu, která je vektorizací historického plánu města Mostu z roku 1938. Ulice v ní vede jako Pařidelská (něm. Paredler Strasse) od jihozápadu (od U hřiště) k severovýchodu s 8 budovami: 4 s číslem popisným (421 a 1084 na severozápadní straně, 426 a 1425 na jihovýchodní) a 4 bez čísla na jihozápadním konci u hřiště. Liebknechtova ulice odbočuje k jihu hned za dvojvilou 426; za vilami vedla státní dráha, naproti přes silnici ležel Deutscher Sportplatz (situace 1922). Dál k severovýchodu ležel za silnicí důl Evžen (Ležáky II) s budovou 1084. Kliknutím na dům v mapě otevřete jeho stránku.

Půdorysy vil jsou v modelu podle kótovaných stavebních plánů (426: 27,00 × 12,35 m s rizalitem 0,8 m, 1922; 1425: 14,00 × 9,20 m, 1925) a jsou ukotvené na polygony GIS; u dvojvily 426 kreslí GIS čelo vystupující 2,1 m, které plán nezná. Domy 421 a 1084 mají půdorys přímo z GIS (viz [Rozpory](#rozpory)).

### Úseky ulice
- JV · jihovýchodní strana (vily u Liebknechtovy a dráhy): 426, 1425
- SZ · severozápadní strana (u hřiště): 421, 1084

### Databázová oblast „Pařidelská“ a co modelováno není

Oblast Pařidelská v databázi Libuše obsahuje při živém načtení 3. 11. 2026 6 struktur (421, 509, 990, 1084, 1124, 1426); záznamy vil 426 a 1425 byly v databázi sloučeny do sousední oblasti Liebknechtova, kde jsou uloženy stavební plány, karty a fotografie. Při prvním zpracování 29. 10. 2026 archiv neodpovídal (zapsáno v knize nesouladů); 3. 11. 2026 jsme načetli a otevřeli všechny přílohy. Domy bez půdorysu v GIS, dům jiné ulice a průmyslový areál jen s projekty jsou předány jako blocked:

| Čp. | Proč není modelován | Přílohy v databázi |
|---|---|---|
| 990 | dům u smaltovny Elisa (dříve Austria) vlevo u silnice, stál do likvidace Mostu; fotografie fasády při demolici existuje, ale GIS pro něj nemá půdorys | 6 |
| 1124 | hospoda Austria u smaltovny, stála do likvidace Mostu; fotografie fasády existuje, bez půdorysu v GIS | 6 |
| 1426 | štíhlý dům u cesty v areálu dolu Evžen, zbořen před rokem 1965; jen vzdálený snímek ~1960, bez půdorysu v GIS | 5 |
| 522 | dům Tyršovy ulice (karty KSPPOP „Tyršova čp. 522“, v GIS pod Jahnovou 730 m odtud); na kartě ke snímku smaltovny jen zmíněn | 34 |
| 509 | cihelna Berty Hinke – devět stavebních plánů (komíny, sušárny, pec), bez fotografie a bez čísla v GIS; průmyslový areál není modelován | 9 |

## Odkud jsou prameny

### Stavební plány Ernsta Wettsteina 1922 a 1925

Obě vily mají kótované projekty mosteckého stavitele Ernsta Wettsteina pro Theresia Tiefbau-Gewerkschaft: dvojvila 426 z 24. 7. 1922 (Vorderansicht, podkroví, řezy a–b a c–d, půdorysy sklepa, přízemí a patra, situace se silnicí Brüx–Paredl, sportovištěm a dráhou) a vila 1425 ze září 1925 (pohled, řez, půdorysy, krov, situace 1:1440) s plánem oplocení z roku 1926. Projekt není realizace: půdorysy a výšky jsou z plánů, skladbu fasád ověřují fotografie.

### Fotodokumentace KSPPOP 1974 a Komplet Starý Most

Fotografie z roku 1974 s kartami Krajského střediska státní památkové péče a ochrany přírody v Ústí nad Labem popisují stanoviště a sousedy: u dvojvily 426 uliční průčelí ve dvou záběrech („průčelí domu do ulice, pohled směrem od dráhy k rozcestí Liebknechtovy“), nádvorní stranu ve dvou polovinách a řadu dvojvil z Liebknechtovy; u vily 1425 průčelí z protější strany Pařidelské, nároží s Liebknechtovou a nádvorní stranu se vstupem. K oběma vilám patří náčrty střech KSPPOP a snímky z demolice. Soubor Komplet Starý Most přidává k domu 421 jediný snímek Prachového mlýna (~1925) a k domům 1084 a 1426 dva vzdálené pohledy na důl Evžen (~1960, ~1965). Cílová epocha modelu jsou 70. léta.

### Starší plány a cizí domy

Ve struktuře 426 jsou i plány z let 1874–1897 sdílené se strukturou 540 (Husovo náměstí); patří dřívějšímu domu téhož čísla a nebyly použity. Struktura 421 obsahuje kromě snímku mlýna i kartu, fotografii a náčrt domu v ulici J. Švermy, na který bylo číslo 421 později přeneseno; ani ty nebyly použity.

### Databáze Libuše projektu MOST

Databáze byla použita pouze pro čtení (0 zápisů). Při prvním zpracování 29. 10. 2026 archiv neodpovídal a oba modely vil vznikly z kopií, které 23. 10. 2026 načetlo jiné vlákno; 3. 11. 2026 jsme načetli živě seznam oblastí a 590 příloh 36 struktur (oblasti Pařidelská, Liebknechtova, Tyršova a Husovo náměstí, vybrané podle oblasti, čísla popisného nebo zmínky čísla v názvu souboru) a všechny otevřeli na kontaktních listech; karty jsme četli v plné velikosti. Oblast Pařidelská má 6 struktur a 42 příloh, záznamy vil jsou v oblasti Liebknechtova.

### Odvozeniny

Kolorované snímky a výřezy v databázi jsou rekonstrukce, ne prameny. O tvaru, otvorech a nápisech rozhoduje původní černobílá fotografie nebo plán.

### GIS a terén

Polohy a natočení domů jsou z GIS vrstvy (vektorizace plánu 1938, místní souřadnice). Půdorysy vil jsou z kótovaných plánů a kotvené na GIS polygony; u 426 GIS kreslí vystupující čelo 20,3 × 2,1 m, které plán nezná. Domy 421 a 1084 mají půdorys přímo z GIS. Výšky budov v GIS jsou jen náhodný zástupný údaj: výšky vil jsou z elevací a řezů 1922 a 1925 (projekt, ±0,6 m), u domu 421 z poměrů na snímku, u 1084 odhad. Terén je zatím plochý (z = 0 u všech domů); historický výškopis nebyl k dispozici.

## Jak vznikla geometrie

- **Rešerše plánů.** Nejdříve jsme prohledali databázi: všech 590 příloh 36 struktur jsme otevřeli na kontaktních listech, karty jsme četli v plné velikosti a listy použité pro geometrii v plném rozlišení (titulek, datum, měřítko, stavebník, sousedé). Plány z let 1874–1897 u domu 426 a podklady ze Švermovy ulice u domu 421 patří jiným domům a byly vyřazeny.

- **Identita a orientace domů.** Situační plánky z let 1922 a 1925 (silnice Brüx–Paredl, Liebknechtova, dráha, sportoviště), popisy stanovišť na kartách a GIS určují, že obě vily stojí na jihovýchodní straně silnice u odbočky Liebknechtovy: 426 blíž k městu, 1425 za ní. Štítové průčelí vily 1425 hledí do Pařidelské, vstup s vnějším schodištěm je na nádvorní straně; dvojvila 426 má průčelí do silnice a balkony dozadu k dráze. Dům 421 je podle karty Prachový mlýn „po pravé straně silnice naproti dolu Evžen“, dům 1084 budova dolu „bližší komína“.

- **Fasáda jen z fotografie nebo plánu s domem v rámečku.** Na každém použitém snímku a elevaci je dům v červeném rámečku a každý otvor má ID (G okna přízemí, U okna patra, A podkrovní okna, D dveře, H vytahovací vikýř, B_ zadní fasáda, L_ a R_ křídla, N_ a S_ boční stěny). Počty otvorů z rámečků kontroluje brána proti plánu modelu; otvory, které pramen neukazuje, jsou přiznané hypotézy.

- **Měřítko.** Výšky a šířky jsou z kótovaných plánů (426: elevace 1922 34,3 px/m a řez c–d; 1425: pohled a řez 1925), u fotografií poměry (zadní strana 426: 83 px/m; mlýn 421: ~135 px/m na líci). Kde se projekt liší od fotografie, model sleduje fotografii.

- **Střecha.** Členění střech je z plánů krovu a podkroví a z náčrtů KSPPOP, sklony z řezů; střecha hotového modelu se změří ze sítě (426: hřeben 17,0 m, sklon 43,6°; 1425: hřeben 11,4 m; 421: hřeben 8,9 m).

- **Stavba v Blenderu.** Parametrický builder bez okna (`build_house_20261028.py`, týž jako u ulice U Pražské brány) vyrobí z `geometry_plan.json` BLEND a GLB. Otvory jsou skutečné niky, štít rizalitu a zadní štít 426 jsou vikýř a křídlo s vlastní zdí, balkony a schodiště jsou boxy, materiály jsou jen ID pro pozdější textury. Dům 1084 je jen objem s valbovou střechou.

- **Kontrola.** Brána geometrie (prosvítání podkroví paprsky, nekryté zdivo, střecha nad prázdnem, UV, síť, počty otvorů) a vizuální kontrola: pohledy s materiály a bez barev (čtyři strany, čtyři rohy shora, dva podhledy u okapu, shora), detaily otvorů a záznam kontroly. Dům se do ulice umístí až po prošlé bráně a prohlédnuté sadě.

- **Sestava ulice.** Registr `street_layout_gis.json` drží polohu, natočení a revizi každého domu (rámec X = východ, Y = sever); okolní budovy z GIS zastupují v sestavě šedé bloky.

Pracovní složka: F:\MOST\output\paridelska_street_claude_2026-10-29\ (domy, kontroly, registr poloh; prameny jen ke čtení; doplněno 3. 11. 2026).

## Rozpory a hypotézy

- **421: Prachový mlýn a přenesené číslo.** Struktura 421 obsahuje dva domy: snímek Prachového mlýna na Pařidelské (~1925) a kartu KSPPOP s fasádou a náčrtem domu v ulici J. Švermy, na který bylo číslo po roce 1930 přeneseno, když mlýn zanikl při rozšiřování lomu dolu Evžen. Plán města 1938 (GIS) mlýn ještě vede, proto je v sestavě; stav v 60. letech není doložen a datum zániku neznáme. Model vychází z jediného snímku: pravá polovina průčelí (2 osy) a východní štít; levá polovina za stromem, vstup za sloupkem branky, boční a zadní stěny a výšky jsou hypotéza (štítek).

- **1084: budova dolu z dálky.** Karty Komplet Starý Most přiřazují číslo 1084 stavbě „bližší komína“ v areálu dolu Evžen (Ležáky II); snímky z odvalu (~1960) a z náspu trati (~1965) ukazují důl z dálky a fasády nelze číst. Model je objemová hypotéza: půdorys GIS 2071, dvě podlaží, valbová střecha, bez otvorů (štítek). Které z budov na snímcích je 1084, zůstává otevřené.

- **990 a 1124 u smaltovny, 1426 u dolu, 522 v Tyršově.** Podle karty k velmi starému pohledu na smaltovnu Elisa (dříve Austria) stály domy 1124 (hospoda Austria) a 990 vlevo u silnice „do celkové likvidace Mostu“ a mají fotografie fasád z demolice, ale GIS pro ně u ulice 56 nemá půdorys (náčrt je klade k dráze mimo osu ulice). Dům 1426 byl zbořen před rokem 1965 a půdorys nemá. Číslo 522 patří domu v Tyršově ulici (karty KSPPOP, GIS pod Jahnovou). Všechny jsou předány jako blocked.

- **1425: kam hledí štít a kde je vstup.** Plán z roku 1925 kreslí průčelí s tympanonem a vstup s vnějším schodištěm na protilehlých stranách. Karty KSPPOP popisují snímek průčelí „z protější strany Pařidelské“ a snímek vstupu jako „nádvorní stranu“: model proto staví štít do ulice (severozápad) a vstup dozadu (jihovýchod).

- **426: projekt potvrzený fotografiemi.** Při prvním zpracování byla uliční fasáda doložena jen projektem 1922 a nesla štítek; 3. 11. 2026 přibyly fotografie KSPPOP 1974 uličního průčelí („pohled směrem od dráhy k rozcestí Liebknechtovy“), které potvrzují 10 + 10 oken, 4 podkrovní okna rizalitu a vikýř severovýchodního křídla. Štítek byl zrušen. Vikýř jihozápadního křídla na snímcích vidět není (podle plánu), štít má volutová ramena a oválné okénko (textura). Starší plány 1874–1897 ve stejné struktuře jsou sdílené se strukturou 540 (Husovo náměstí) a patří dřívějšímu domu.

- **426: půdorys GIS proti plánu.** GIS kreslí uliční čelo 20,3 m vystupující o 2,1 m, plán z roku 1922 kótuje 27,00 × 12,35 m s rizalitem 10,45 m vystupujícím 0,8 m. Model drží plán a je ukotven na zadní hranu GIS polygonu; kanonický GIS zůstává beze změny.

- **Výšky z plánů a snímků.** Římsa 426 je 10,0 m a hřeben 17,0 m podle elevace a řezu c–d (±0,6 m); u 1425 římsa 7,1 m, vrchol štítu 9,5 m a hřeben 11,4 m podle pohledu a řezu 1925 (±0,3 m); u 421 okap 5,6 m a hřeben 8,9 m z poměrů na snímku (±0,4 m); u 1084 odhad.

- **Boční stěny** vil mají okna podle půdorysů; žádná fotografie je neukazuje celé. Zadní přístavky 1425 v GIS polygonu a podkrovní okna zadní strany 426 nejsou modelovány; lizény, šambrány, okenice, oválné okénko a kartuše zadního štítu jsou textura. Polovalby mlýna 421 builder nemá – štíty jsou plné.

- **Terén** je plochý (z = 0 u všech domů), ačkoli silnice k Pařidlům stoupá podél dráhy; historický výškopis nebyl k dispozici.

- **Dvorní a nedoložené strany** jsou bez otvorů, pokud je žádný pramen neukazuje.

Údaje jsou v datech označené jako `model_hypothesis`, `status: provisional`, `locked: false`.

## Kniha nesouladů pramenů

Případy, kdy si prameny odporují (plán proti fotografii, GIS proti plánu, chybně zařazený list, nedostupný archiv), zapisujeme do interní knihy nesouladů pramenů projektu MOST. Ta se zatím nepublikuje, proto zde uvádíme jen identifikátory případů této ulice (7):
- `2026-10-29_paridelska_1425-orientace-stit-k-ulici-vstup-vzadu` – Pařidelská 1425: průčelí s tympanonem hledí do Pařidelské, vstup se schodištěm je vzadu – orientaci rozhodly karty, ne plán oplocení
- `2026-10-29_paridelska_426-stare-plany-1874-1897-jiny-dum` – Pařidelská 426: plány z let 1874–1897 (Wenzels-Vorstadt, Panzner, Wustel, Spitz) patří dřívějšímu domu č. 426, fotografovaná dvojvila je projekt z roku 1922
- `2026-10-29_paridelska_api-vypadek-zdroje-nedostupne` – Pařidelská: 29. 10. 2026 archiv Libuše neodpovídal (TCP timeout), dávka začala z kopií jiných vláken – 421, 1084, 990, 1124, 1426 a 522 zůstaly bez pramenů
- `2026-11-03_paridelska_1084-1426-budovy-dolu-evzen` – Pařidelská 1084 a 1426: budovy dolu Evžen (Ležáky II) doložené jen vzdálenými snímky ~1960/1965; 1084 má půdorys v GIS, 1426 ne
- `2026-11-03_paridelska_421-prachovy-mlyn-cp-preneseno-do-svermovy` – Pařidelská 421: budova GIS 1573 = bývalý „Prachový mlýn“ doložený jediným snímkem ~1925; číslo 421 bylo po roce 1930 přeneseno na dům v ulici J. Švermy
- `2026-11-03_paridelska_426-fotografie-pruceli-potvrzuji-projekt` – Pařidelská 426: po obnovení archivu přibyly fotografie KSPPOP 1974 uličního průčelí – projekt 1922 byl realizován, štítek zrušen; plány 1874–1897 jsou sdílené se strukturou 540 (Husovo náměstí)
- `2026-11-03_paridelska_990-1124-u-smaltovny-522-tyrsova` – Pařidelská 990 a 1124 stály u smaltovny Elisa (hospoda Austria) a vydržely do likvidace Mostu, ale GIS pro ně nemá půdorys; 522 je dům v Tyršově ulici

## Přehled domů

| Čp. | Úsek | Typ | Štítek | Podlaží | Průčelí × okap (m) | Revize | Přílohy | Stav / textury |
|---|---|---|---|---|---|---|---|---|
| 426 | JV | dvojvila Theresia Tiefbau-Gewerkschaft s rizalitem a štítem (1922) | – | 2 + podkroví | 27,0 × 10,0 | r1 | 45 | bez textur (částečně hypotéza – jen prosté materiály) |
| 1425 | JV | vila Theresia Tiefbau-Gewerkschaft s tympanonem (1925) | – | 2 | 14,0 × 7,1 | r1 | 24 | zatím bez textur |
| 421 | SZ | bývalý „Prachový mlýn“, dům doložený jediným snímkem (~1925) | částečně hypotéza | 2 | 12,5 × 5,5 | r1 | 8 | bez textur (částečně hypotéza – jen prosté materiály) |
| 1084 | SZ | budova dolu Evžen (Ležáky II), objemová hypotéza | hypotéza | 2 (odhad) | 15,1 × 7,0 | r1 | 8 | bez textur (hypotéza – jen prosté materiály) |

## Domy jednotlivě

### Čp. 426: dvojvila Theresia Tiefbau-Gewerkschaft s rizalitem a štítem (1922)

- Dvojvila na parcele 3049 vedle vily 1425, projekt Ernsta Wettsteina z 24. 7. 1922 pro Theresia Tiefbau-Gewerkschaft (situace: silnice Brüx–Paredl, naproti Deutscher Sportplatz, za domem státní dráha). Karty KSPPOP: „zadní strana domu souběžného s Pařidelskou, se strany ul. Liebknechtovy“ a „nárožní dům 426 do Pařidelské, poslední vlevo v řadě dvouvilek“. GIS budova 1570 (27,3 m). Starší plány z let 1874–1897 ve stejné struktuře patří dřívějšímu domu téhož čísla.
- Prameny: plán E. Wettstein 1922 (Vorderansicht, podkroví, řezy a–b, c–d, půdorysy přízemí, patra a sklepa, situace), fotografie KSPPOP 1974 (uliční průčelí z Pařidelské ve dvou záběrech, nádvorní strana ve dvou polovinách, řada dvojvil z Liebknechtovy) s kartami, náčrt střech KSPPOP, snímky z demolice (ATO), GIS půdorys 1570
- Střecha: valbová střecha s hřebenem podél domu, příčná sedlová střecha rizalitu se štítem vpředu i vzadu, vikýře křídel, tři komíny; sklon ~44°
- GIS budova 1570 (popisek 426); geometrie revize r1, 877 polygonů.
- Hypotézy: uliční průčelí potvrzují fotografie KSPPOP z roku 1974 doplněné 3. 11. 2026 (10 + 10 oken, 4 podkrovní okna, vikýř severovýchodního křídla); vikýř jihozápadního křídla na snímcích vidět není (podle plánu), štít má ve skutečnosti volutová ramena a oválné okénko (textura); výšky z elevace a řezu 1922: přízemí +1,25 m, okna 1,8–3,75 / 5,45–7,4 m, římsa křídel 10,0 m, podkrovní okna rizalitu 10,6–12,2 m, hřeben 17,0 m (±0,6 m); zadní fasáda z fotografie 1974 a půdorysů: balkony v nárožích, schodišťové okno, vstup se stupněm; podkrovní okna vzadu nemodelována; boční okna podle půdorysů bez fotografie; rozpor GIS (čelo 20,3 m vystupující 2,1 m) × plán (rizalit 10,45 m, 0,8 m): model podle plánu, kotveno na GIS

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_18_049.jpg | fotografie | 8b63d58c7f10 |
| ATO119_10_18_050.jpg | fotografie | be567630bfe7 |
| ATO119_10_18_051.jpg | fotografie | dc21fdcb52ab |
| ATO119_10_18_052.jpg | fotografie | 5b01009a1e2a |
| ATO119_10_18_053.jpg | fotografie | 1b05ba6d7b56 |
| ATO119_10_5_037.jpg | fotografie | 87a041d86d95 |
| cp_426,540_001.jpg | plán / výkres | 16a0dafa31a1 |
| cp_426,540_002.jpg | plán / výkres | 72e0d77e7ebb |
| cp_426,540_003.jpg | plán / výkres | 3e4a46a9a4e0 |
| cp_426,540_004.jpg | plán / výkres | 60c626ac7ad7 |
| cp_426,540_005.jpg | plán / výkres | 48a9e7337d98 |
| cp_426,540_006.jpg | plán / výkres | a0e18c94370b |
| cp_426,540_007.jpg | plán / výkres | 0ccebaf29676 |
| cp_426,540_008.jpg | plán / výkres | 6a1bb24d673b |
| cp_426,540_009.jpg | plán / výkres | b7f4df410911 |
| cp_426,540_010.jpg | plán / výkres | 290afd92b1cf |
| cp_426,540_011.jpg | plán / výkres | 0ab9c591a83e |
| cp_426_001.jpg | archivní karta | 8a1f85bf9a1b |
| cp_426_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 364ced98c3a2 |
| cp_426_001.jpg | fotografie | c66dda9dd381 |
| cp_426_001.jpg | fotografie | fc7a10d2566c |
| cp_426_001.jpg | archivní karta | 2f0ade6cf435 |
| cp_426_001__2.jpg | archivní karta | 8a1f85bf9a1b |
| cp_426_001__2.jpg | fotografie | fc7a10d2566c |
| cp_426_002.jpg | archivní karta | f7352d48f632 |
| cp_426_002.jpg | archivní karta | 0ac8965fd223 |
| cp_426_002.jpg | fotografie | c055672f6b44 |
| cp_426_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | ede46c84af34 |
| cp_426_002.jpg | fotografie | 036aac9df7cf |
| cp_426_002__2.jpg | archivní karta | f7352d48f632 |
| cp_426_002__2.jpg | fotografie | c055672f6b44 |
| cp_426_002_col.png | kolorovaná odvozenina | 30606cd1a985 |
| cp_426_003.jpg | archivní karta | b7bd98e7e32d |
| cp_426_003.jpg | fotografie | 7e49be586e07 |
| cp_426_003.jpg | fotografie | 7e49be586e07 |
| cp_426_003.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | abbd5e698fd7 |
| cp_426_003.jpg | archivní karta | b7bd98e7e32d |
| cp_426_004.jpg | fotografie | e72aea5eb4bc |
| cp_426_004.jpg | archivní karta | 8f32424a6dca |
| cp_426_004.jpg | fotografie | e72aea5eb4bc |
| cp_426_004.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | c592127a6329 |
| cp_426_004.jpg | plán / výkres | bb8a7584d51d |
| cp_426_004.jpg | plán / výkres | bb8a7584d51d |
| cp_426_004.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 546fe9440fa0 |
| cp_426_004.jpg | archivní karta | 8f32424a6dca |

### Čp. 1425: vila Theresia Tiefbau-Gewerkschaft s tympanonem (1925)

- Vila na parcele 3050 v rohu Pařidelské a Liebknechtovy, postavená v letech 1925–26 pro Theresia Tiefbau-Gewerkschaft (plán stavitele Ernsta Wettsteina ze září 1925, plán oplocení 1926 „Umzäunung des neuen Wohnhauses Nr 1425“). Karty KSPPOP popisují stanoviště: z protější strany Pařidelské (vpravo dům 1825, vlevo hradlo starého nádraží), z nároží Pařidelské a Liebknechtovy a nádvorní stranu. GIS budova 2072.
- Prameny: plán E. Wettstein 9/1925 (Ansicht, řez, půdorysy, krov, situace 1:1440), plán oplocení 1926 (1:500), fotografie 1974 (průčelí z ulice, nároží, nádvorní strana) s kartami KSPPOP, snímky z demolice (ATO, doplněno 3. 11. 2026; boční stěna na nich bez oken), náčrt KSPPOP 1425/1, GIS půdorys 2072
- Střecha: valbová střecha s hřebenem rovnoběžným s ulicí, štít rizalitu vbíhá do valby, dva komíny; sklon podle řezu ~40°
- GIS budova 2072 (popisek 1425); geometrie revize r1, 514 polygonů.
- Hypotézy: výšky z plánu 1925 (projekt): okna přízemí 1,45–3,15 m, patra 4,70–6,45 m, římsa 7,1 m, vrchol štítu 9,5 m, hřeben 11,4 m – fotografie potvrzují skladbu, ne rozměry (±0,3 m); boční stěny mají 2 okna na podlaží podle půdorysu; z nároží (1974) je čitelné jen 1 okno patra a snímek z demolice (ATO) ukazuje boční stěnu bez oken – boční okna zůstávají otevřenou hypotézou; vnější schodiště k zadnímu vstupu zjednodušeno na 4 stupně a podestu; zadní přístavky (prádelna, kůlna) v GIS polygonu nejsou modelovány; lizény, šambrány a okenice jsou textura

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_18_034.jpg | fotografie | 19d4f4575dff |
| ATO119_10_18_037.jpg | fotografie | 1d91bc0582da |
| ATO119_10_18_038.jpg | fotografie | 34cd38151536 |
| ATO119_10_18_039.jpg | fotografie | e3d16e737cc8 |
| ATO119_10_5_041.jpg | fotografie | 46d2f4132729 |
| cp_1425_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | a1eab7a9520f |
| cp_1425_001.jpg | fotografie | 833990fb1881 |
| cp_1425_001.jpg | archivní karta | 5f2a2643bec8 |
| cp_1425_001.jpg | plán / výkres | d3d68c78360d |
| cp_1425_001.jpg | archivní karta | 29ae9888fbcb |
| cp_1425_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 108de79608c5 |
| cp_1425_001.jpg | fotografie | fefe776cf923 |
| cp_1425_001__2.jpg | archivní karta | 29ae9888fbcb |
| cp_1425_001__2.jpg | plán / výkres | f1de0fe27f8b |
| cp_1425_001__2.jpg | fotografie | fefe776cf923 |
| cp_1425_001_col.png | kolorovaná odvozenina | d0bc2249050e |
| cp_1425_002.jpg | plán / výkres | ad132c3ec85d |
| cp_1425_002.jpg | fotografie | c9f41a51ac9d |
| cp_1425_002.jpg | archivní karta | 9969d6807b25 |
| cp_1425_003.jpg | archivní karta | 17638360d8fd |
| cp_1425_003.jpg | fotografie | e8f3edde6e02 |
| cp_1425_003.jpg | plán / výkres | 78bbfa815962 |
| cp_1425_004.jpg | plán / výkres | a3237c10c82b |
| cp_1425_005.jpg | plán / výkres | c01423ab4f23 |

### Čp. 421: bývalý „Prachový mlýn“, dům doložený jediným snímkem (~1925)

> **Upozornění – částečně hypotéza:** Dům je doložen jediným snímkem z doby kolem roku 1925 (pravá polovina průčelí a východní štít); levá polovina, ostatní strany a výšky jsou hypotéza. Stav v 60. letech není doložen – podle karty mlýn zanikl při rozšiřování lomu.

- Budova GIS 1573 na severozápadní straně silnice naproti dolu Evžen, před drážním podjezdem: tzv. Prachový mlýn (Pulvermühle), v době snímku kolem roku 1925 už přestavěný na byty. Podle karty Komplet Starý Most zanikl při rozšiřování povrchového lomu dolu (později Ležáky II) a jeho číslo bylo po roce 1930 přeneseno na přestavbu vedle hostince Bílý Beránek v ulici J. Švermy; karta KSPPOP s fasádou a náčrt 421/5 u Švermovy patří tomu pozdějšímu domu. Plán města 1938 (GIS) dům na Pařidelské ještě vede.
- Prameny: fotografie Okresního muzea ~1925 (jediný snímek domu) s kartou Komplet Starý Most, GIS půdorys 1573 (12,5 × 9,5 m); karta KSPPOP 10.243, fotografie fasády a náčrt u Švermovy = pozdější dům téhož čísla (nepoužito)
- Střecha: sedlová s polovalbami podle snímku (východní štít s malou valbou), hřeben podél průčelí, sklon ~35°, vytahovací vikýř, komín na hřebeni
- GIS budova 1573 (popisek 421); geometrie revize r1, 176 polygonů.
- Hypotézy: jediný snímek je z doby kolem roku 1925; stav v 60. letech není doložen (mlýn zanikl při rozšiřování lomu, datum neznámé); na snímku je jen pravá polovina průčelí (2 osy) a východní štít; levá polovina za stromem a kůlnou: okno a vstupní dveře za sloupkem branky jsou hypotéza; výšky z poměrů na snímku (okap 5,6 m, hřeben 8,9 m) ±0,4 m; boční a zadní stěny bez otvorů; polovalby builder nemá – štíty jsou plné; kůlna před domem a budova vlevo nejsou modelovány

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_421_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | f6b366085459 |
| cp_421_001.jpg | fotografie | 45355e765bcc |
| cp_421_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | d08129257474 |
| cp_421_001.jpg | archivní karta | af92604a2bd0 |
| cp_421_001.jpg | archivní karta | 52d6bb1ad703 |
| cp_421_001.jpg | fotografie | 441e66a3fa80 |
| cp_421_001.jpg | plán / výkres | 4fa474a828aa |
| cp_421_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 3cc5009d99d6 |

### Čp. 1084: budova dolu Evžen (Ležáky II), objemová hypotéza

> **Upozornění – hypotéza:** Objemová hypotéza: půdorys z GIS, podlaží a střecha odhadnuté podle vzdálených snímků dolu Evžen (~1960, ~1965); fasády nejsou doloženy, proto jsou bez otvorů.

- Budova GIS 2071 (15,1 × 14,3 m) na severozápadní straně silnice v areálu bývalého dolu Evžen, později Ležáky II. Karty Komplet Starý Most ke snímkům z odvalu (~1960) a z náspu trati k Mariánským Radčicím (~1965) uvádějí: „štíhlý dům vlevo u cesty míval čp. 1426, bližší komína 1084“ a „dům 1426 je již zbořen“. Snímky ukazují areál dolu z dálky, fasády nejsou čitelné.
- Prameny: dvě fotografie dolu (~1960, ~1965) s kartami Komplet Starý Most, náčrt situace areálu, GIS půdorys 2071
- Střecha: valbová podle siluety na snímku (odhad)
- GIS budova 2071 (popisek 1084); geometrie revize r1, 69 polygonů.
- Hypotézy: celý dům je objemová hypotéza: půdorys z GIS, dvě podlaží a valbová střecha odhadnuté podle vzdálených snímků; bez oken a dveří; ztotožnění čísla 1084 s budovou GIS 2071 předpokládá, že plán 1938 označuje tutéž stavbu jako karta

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1084,1426_001.jpg | archivní karta | 815f4eb80e28 |
| cp_1084,1426_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 35d1fe06cc3e |
| cp_1084,1426_001.jpg | fotografie | 36fedead7320 |
| cp_1084,1426_001.jpg | plán / výkres | dd39ff6ea2d2 |
| cp_1084,1426_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | b30ce1c46890 |
| cp_1084_001.jpg | archivní karta | 14b2b9c30da8 |
| cp_1084_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | eb92820f9a45 |
| cp_1084_001.jpg | fotografie | 9610e0bb68a1 |
