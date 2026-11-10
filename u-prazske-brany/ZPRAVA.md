# U Pražské brány (Am Prager Tor): zpráva o 3D modelu ulice a jeho pramenech

Projekt MOST, GRAFIT FIT ČVUT, 29. 10. 2026. Geometrie a stránka: Claude (Anthropic); textury doplňuje Codex. Web: https://grafitctu.github.io/most/u-prazske-brany/

Stav: ve 3D je 6 z 6 modelovaných budov. Model ulice (GLB) je k dispozici.

## Co kde stálo

Poloha všech domů pochází z GIS vrstvy projektu, která je vektorizací historického plánu města Mostu z roku 1938. Ulice v ní vede jako U Pražské brány (něm. Am Prager Tor) s 6 budovami, všechny s číslem popisným. Dům 251 je v GIS veden pod touž ulicí, ale průčelím hledí do Šmeralova náměstí. Kliknutím na dům v mapě otevřete jeho stránku.

Šířky parcel v GIS u domů 449 a 495 neodpovídají stavebním plánům (1891, 1930) ani zaměření z roku 1972: model používá plánové šířky 15,0 m a 5,83 m a zbytek řady (25,8 m) připadá domu 250; kanonický GIS se nemění (viz [Rozpory](#rozpory)).

### Úseky ulice
- N · jižní strana Šmeralova náměstí (u ústí ulice): 251
- Z · západní strana ulice (od náměstí k Fučíkovým sadům): 250, 495, 449
- V · východní strana ulice (od náměstí k Rybalkově): 247, 249

### Databázová oblast „U Pražské brány“ a co modelováno není

Oblast U Pražské brány v databázi Libuše obsahuje 7 struktur (při živém načtení 23. 10. 2026 byly sloučeny dřívější dvě oblasti a nově přibyla struktura 251). Jedna struktura obsahuje jen pohlednice a leží podle GIS v jiné ulici; její přílohy jsme načetli a prohlédli, modelována není:

| Čp. | Poznámka | Ulice podle GIS | Přílohy |
|---|---|---|---|
| 245 | jen čtyři pohlednice (letecké snímky ~1920), dům stojí v GIS pod Rozmarýnovou – nemodelován v této dávce | v GIS není | 4 |

## Odkud jsou prameny

### Fotodokumentace KSPPOP 1965–1975

Ulici zachycuje fotodokumentace Krajského střediska státní památkové péče a ochrany přírody v Ústí nad Labem z let 1965–1975 (karty s popisem stanoviště a sousedů, fotograf Záša 1974, Čermák 1973, Poláček 1974, Villert ~1970, Šejner ~1965) a soubor „Komplet: Starý Most“. Domy na snímcích stojí, nároží 449 a 249 jsou zachycena z křižovatky, celá západní řada z plochy náměstí a pohled z věže piaristického kostela ukazuje střechy a zadní stěny 250, 495 a 449. Cílová epocha modelu jsou 60.–70. léta.

### Zaměření 1972–1974 a stavební plány 1891–1930

Pro domy 249, 449 a 495 existují zaměření z let 1972–1974 (O. Horáková: půdorysy přízemí 1:50; V. Novák: průčelí 1:50) pořízená před demolicí. Starší stavební plány jsou plán F. Griesbacha z roku 1891 pro nárožní dům 449 (kótovaný půdorys 15,00 × 17,50 m), plán krámského portálu O. Zienerta z roku 1930 pro 495 (průčelí 5,83 m) a projekty C. Hinkeho z let 1898–1928 pro dvorní křídlo domu 249. Projekt není realizace: model sleduje fotografii, kde se liší (495 má na plánu 1930 tři okna v patře, na fotografii dvě). Ke každému domu patří i ruční náčrt střech KSPPOP s čísly sousedů, který dává členění střech.

### Databáze Libuše projektu MOST

Seznamy příloh jsme načetli živě 23. 10. 2026, pouze pro čtení (0 zápisů). Oblast U Pražské brány má 7 struktur a 203 příloh (161 různých souborů podle SHA-256): 50 plánů a výkresů, 45 fotografií, 32 archivních karet, 12 pohlednic, 14 kolorovaných odvozenin a 50 dalších odvozenin bez tagu. Kromě toho jsme otevřeli 550 příloh 25 struktur sousedních oblastí (Rozmarýnová, Šmeralovo náměstí, Leninova, U jeptišek, Elišova), na kterých jsou domy ulice v pozadí nebo z náměstí.

### Odvozeniny

Kolorované snímky a výřezy v databázi jsou rekonstrukce, ne prameny. O tvaru, otvorech a nápisech rozhoduje původní černobílá fotografie nebo plán.

### GIS a terén

Polohy a natočení domů jsou z GIS vrstvy (vektorizace plánu 1938, místní souřadnice). Šířky parcel u 449 a 495 GIS udává chybně (12,0 a 7,6 m proti 15,0 a 5,83 m z plánů), proto model používá plánové šířky a dům 250 dostává zbytek řady. Výšky budov v GIS jsou jen náhodný zástupný údaj: výšky domů jsou ze zaměření 1974 (249, 449) a z fotografií. Terén je zatím plochý (výška ulice z = 0 u všech domů), ačkoli ulice klesá od náměstí k sadům; je to provizorní hypotéza.

## Jak vznikla geometrie

- **Rešerše plánů.** Nejdříve jsme prohledali databázi stavebních plánů: všech 203 příloh oblasti a 550 příloh sousedních oblastí jsme otevřeli na kontaktních listech, karty jsme četli v plné velikosti a listy použité pro geometrii v plném rozlišení (titulek, datum, měřítko, uliční nebo dvorní objekt, sousedé). Dva listy ve struktuře 495 patří jiným domům a byly vyřazeny.

- **Identita a pořadí domů.** Popisy stanovišť na kartách KSPPOP, náčrty střech s čísly sousedů a situační plánky z let 1891, 1899 a 1930 určují pořadí od náměstí: západ 251 (jen do náměstí) – 250 – 495 – 449, východ 247 – 249. Šířky z GIS jsme ověřili proti plánům a poměrům na fotografiích.

- **Fasáda jen z fotografie nebo zaměření s domem v rámečku.** Na každém použitém snímku je dům v červeném rámečku a každý otvor má ID (G okna přízemí, U okna patra, M okna 1. patra, D dveře, S výkladce, A nebo O štítová okénka a volská oka, E_ a Q_ a S_ pro druhé fasády). Počty otvorů z rámečků kontroluje brána proti plánu modelu; otvory, které snímek neukazuje, jsou přiznané hypotézy.

- **Měřítko.** Výšky dávají zaměření V. Nováka z roku 1974 (145 px/m, ověřeno kótou plánu 1891 u domu 449), u ostatních domů poměry na fotografiích; vodorovné polohy u šikmých snímků perspektivní přepočet. Kde se projekt liší od realizace, model sleduje fotografii.

- **Střecha.** Členění střech je z ručních náčrtů KSPPOP (ulice vždy dole), sklony a hřebeny ze siluet zaměření a fotografií; střecha hotového modelu se změří ze sítě.

- **Stavba v Blenderu.** Parametrický builder bez okna (`build_house_20261028.py`, odvozený z builderu U hřiště, Rudolfovy a Kulové; nově štítová zeď do ulice s volským okem a opravené uzavření podkroví nad přístavky) vyrobí z `geometry_plan.json` BLEND a GLB. Otvory jsou skutečné niky, volská oka otevírají krytinu, materiály jsou jen ID pro pozdější textury.

- **Kontrola.** Brána geometrie (prosvítání podkroví paprsky, nekryté zdivo, střecha nad prázdnem, UV, síť, počty otvorů) a vizuální kontrola: pohledy s materiály a bez barev (čtyři strany, čtyři rohy shora, dva podhledy u okapu, shora), detaily otvorů a záznam kontroly. Dům se do ulice umístí až po prošlé bráně a prohlédnuté sadě.

- **Sestava ulice.** Registr `street_layout_gis.json` drží polohu, natočení a revizi každého domu (rámec X = východ, Y = sever); okolní budovy z GIS zastupují v sestavě šedé bloky.

Pracovní složka: F:\MOST\output\u_prazske_brany_street_claude_2026-10-23\ (domy, kontroly, registr poloh; prameny jen ke čtení).

## Rozpory a hypotézy

- **449 a 495: šířky parcel v GIS proti plánům.** GIS dává domu 449 jen 12,0 m do ulice a 10,9 m do Fučíkových sadů, plán F. Griesbacha z roku 1891 kótuje 15,00 × 17,50 m; dům 495 má v GIS 7,6 m, plán portálu z roku 1930 i zaměření z roku 1972 dávají 5,83 m. Součet západní řady (46,6 m) v GIS souhlasí, posunuté jsou jen dělicí zdi, a tak dům 250 dostává zbytek 25,8 m. Kanonický GIS zůstává beze změny.

- **249: zaměřené průčelí je 7,65 m široké, GIS bok 12,46 m.** List „PRŮČELÍ 1:50, V. Novák 1974“ má stejné měřítko skenu jako list domu 449 (145 px/m), takže zaměřená dvouosá fasáda s volutovým štítem je 7,65 m široká; GIS i náčrt střech dávají jižnímu boku 12,5–13 m. Fotografie z roku 1974 navíc ukazují tři štíty (malý severní, střední nad dvouosou částí uliční fasády a velký na jižní fasádě). Model klade zaměřenou jednotku od nároží na jižní fasádu a její skladbu používá i pro štítovou část uliční fasády; zbytek a osy uliční fasády jsou hypotéza.

- **250: zadní část podle GIS, nebo podle náčrtu.** GIS polygon je hlubší v jižní polovině u domu 495, náčrt střech KSPPOP kreslí zadní křídlo s dvorkem naopak u náměstí. Model drží GIS: hlavní blok 8,5 m hluboký a nízký jižní přístavek s pultovou střechou; tři volská oka do náměstí z náčrtu nejsou modelována.

- **495: cizí listy ve struktuře.** Dva plány uložené u domu 495 patří jiným stavbám (čp. 268 v Minoritské ulici, 1885; hospodářská budova téhož stavebníka ve Friedhofsstraße, 1929) a nebyly použity. Plán z roku 1930 kreslí v patře tři okna, fotografie z roku 1974 ukazuje dvě: model sleduje fotografii.

- **251: nová struktura v živé databázi.** Snapshot z 11. 9. 2026 strukturu 251 neznal; při živém načtení 23. 10. 2026 má fotografii, kartu a náčrt střech. Přízemí je na jediném snímku zakryté autobusy, proto je hypotéza a styk s domem 250 je odečten ze změny střešní plochy.

- **247: spojený dům bez plánů.** Dvě historické části pod jedním číslem jsou doloženy jen šikmými snímky z let 1970–1974 a náčrtem střech; výšky, osy, krámy přízemí a zadní budovy jsou hypotéza, poloha portálu s balkonem (10,3 m od nároží) je z náčrtu.

- **449: uliční fasáda jen šikmo.** Jižní průčelí do sadů je zaměřeno (4 osy, štít se dvěma okénky), uliční východní fasáda je na šikmých snímcích: tři osy patra s balkonem a štítem jsou spočtené, výkladce a vstup v přízemí jsou podle projektu z roku 1891.

- **Výšky a terén.** Výšky podlaží, říms a střech jsou ze zaměření 1974 (249, 449) a z poměrů na fotografiích; sklony střech jsou odhady. Terén je plochý (z = 0), ačkoli ulice klesá od náměstí k sadům; historický výškopis nebyl k dispozici.

- **Dvorní a nedoložené strany** jsou bez otvorů, pokud je žádný pramen neukazuje.

Údaje jsou v datech označené jako `model_hypothesis`, `status: provisional`, `locked: false`.

## Kniha nesouladů pramenů

Případy, kdy si prameny odporují (plán proti fotografii, GIS proti plánu, chybně zařazený list), zapisujeme do interní knihy nesouladů pramenů projektu MOST. Ta se zatím nepublikuje, proto zde uvádíme jen identifikátory případů této ulice (4):
- `2026-10-28_u-prazske-brany_249-novak-7m-vs-gis-12m-tri-stity` – U Pražské brány 249: zaměřené průčelí Nováka 1974 je 7,65 m široké, GIS bok do Rybalkovy má 12,46 m; dům má tři štíty
- `2026-10-28_u-prazske-brany_250-hlubsi-cast-gis-vs-nacrt` – U Pražské brány 250: GIS má hlubší část půdorysu u 495, náčrt střech kreslí zadní křídlo u náměstí
- `2026-10-28_u-prazske-brany_449-495-sirky-gis-vs-plany` – U Pražské brány 449 a 495: GIS šířky parcel neodpovídají stavebním plánům, rozdíl pohlcuje sousední 250
- `2026-10-28_u-prazske-brany_zivy-get-vs-snapshot-251` – U Pražské brány: živá databáze sloučila dvě oblasti a přidala strukturu 251 – snapshot z 11. 9. 2026 ji neznal

## Přehled domů

| Čp. | Úsek | Typ | Štítek | Podlaží | Průčelí × okap (m) | Revize | Přílohy | Stav / textury |
|---|---|---|---|---|---|---|---|---|
| 251 | N | přízemní dům s patrem do náměstí, zadní sklad | částečně hypotéza | 2 | 12,4 × 7,8 | r1 | 11 | bez textur (částečně hypotéza – jen prosté materiály) |
| 250 | Z | dlouhý nárožní dům s pohřební službou a trafikou | – | 2 | 25,8 × 7,5 | r1 | 27 | zatím bez textur |
| 495 | Z | úzký dům s řeznictvím a štítem do ulice | – | 2 + štít | 5,8 × 8,6 | r1 | 26 | zatím bez textur |
| 449 | Z | nárožní dům u Fučíkových sadů s krámy a balkonem | částečně hypotéza | 2 + štít | 17,5 × 8,2 | r1 | 45 | bez textur (částečně hypotéza – jen prosté materiály) |
| 247 | V | spojený nárožní dům u náměstí s portálem a balkonem | částečně hypotéza | 2 | 27,3 × 8,3 | r1 | 34 | bez textur (částečně hypotéza – jen prosté materiály) |
| 249 | V | třípodlažní nárožní dům u Rybalkovy se třemi štíty | částečně hypotéza | 3 + štíty | 20,0 × 10,8 | r1 | 56 | bez textur (částečně hypotéza – jen prosté materiály) |

## Domy jednotlivě

### Čp. 251: přízemní dům s patrem do náměstí, zadní sklad

> **Upozornění – částečně hypotéza:** Patro a střecha podle fotografie 1974; přízemí je na snímku zakryto autobusy a je hypotéza, hranice s 250 odečtena ze střechy.

- Dům na jižní straně Šmeralova náměstí vpravo od nárožního domu 250; karta KSPPOP neg. 10.946 popisuje jeho fasádu z plochy náměstí, vlevo rohák 250, vpravo proluku po pekárně 253. Živá databáze má strukturu 251 nově (snapshot z 11. 9. 2026 ji neznal).
- Prameny: fotografie cp_251_001 (karta KSPPOP neg. 10.946, 1974), náčrt střech KSPPOP 251/12, GIS půdorys 329, sdílené snímky náměstí
- Střecha: sedlová střecha s hřebenem rovnoběžným s náměstím, valba k domu 250, požární štít k proluce 253, dvě volská oka (obočí); zadní patrový sklad podle GIS
- GIS budova 329 (popisek 251); geometrie revize r1, 365 polygonů.
- Hypotézy: přízemí je na jediném snímku zakryté autobusy – dveře a okna přízemí jsou hypotéza; styk s 250 je odečten ze změny střešní plochy, ne ze spáry; výšky z poměrů snímku (89,5 px/m) ±0,3 m; sklon střechy a hřeben jsou odhad; zadní sklad má výšku okapu domu; přístavek WC a kůlna z náčrtu jsou nemodelované

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp251_a_crop_V.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | b3bbb2ee2b14 |
| cp251_b_crop_V.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | a59962841d9f |
| cp_244,245,246,247,250,251_001.tif.jpg | fotografie | d79e22187f04 |
| cp_246,247,250,251_001.jpg | fotografie | d822c17be8ad |
| cp_250,251,253,254,255_001.jpg | fotografie | 1c5b387ad44c |
| cp_251.jpg | plán / výkres | 1d2e63d74ca0 |
| cp_251.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | aadadc53bfb6 |
| cp_251_001.jpg | fotografie | 197f67fe344e |
| cp_251_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 6d2487c871af |
| cp_251_001.jpg | archivní karta | 38244d73cb7d |
| cp_251_col.png | kolorovaná odvozenina | f3d4909f3102 |

### Čp. 250: dlouhý nárožní dům s pohřební službou a trafikou

- Nárožní dům Šmeralova náměstí a ulice U Pražské brány na západní straně (Pohřební služba, TABÁK); karty KSPPOP neg. 10.950–10.952 popisují uliční fasádu, nároží z náměstí i celou pravou stranu ulice (250 | 495 | 449). Šířka 25,8 m je zbytek řady po plánových šířkách 449 a 495.
- Prameny: fotografie cp_250_001 (neg. 10.951 nároží z náměstí, neg. 10.952 uliční fasáda od jihu), cp_250,449,495_002 (neg. 10.950 z náměstí), cp_250,449,495_001 (z věže piaristického kostela, 1974), náčrt střech KSPPOP 250/1, GIS půdorys 330
- Střecha: valbová střecha s hřebenem rovnoběžným s ulicí, čtyři volská oka do ulice (náčrt), tři do náměstí (nemodelována); nízký zadní přístavek s pultovou střechou nad hlubší jižní částí půdorysu GIS
- GIS budova 330 (popisek 250); geometrie revize r1, 512 polygonů.
- Hypotézy: výšky (okap 7,5 m) z poměrů šikmých snímků ±0,3 m; polohy os na vzdáleném konci fasády ±0,7 m; šířka 25,8 m místo 27,0 m v GIS – důsledek plánových šířek 449 a 495 (kanonický GIS nezměněn); hlubší jižní část půdorysu GIS jako přístavek 4,9 m – náčrt střech má zadní křídlo naopak u náměstí; třetí osa fasády do náměstí u domu 251 je hypotéza; sklon střechy 40° a hřeben 11,5 m odhad

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| P-000080.jpg | pohlednice | a0652af2f647 |
| P-000080__2.jpg | pohlednice | d5cb6339e151 |
| P-000081.jpg | pohlednice | 31632986f1a8 |
| P-000081__2.jpg | pohlednice | 8ec5eeb5eba8 |
| cp250_a_crop_V.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | aed8ddaf2ff1 |
| cp250_b_crop_V.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 38065f659042 |
| cp250_c_crop_V.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | ef6ba43faa3c |
| cp_244,245,246,247,250,251_001.tif.jpg | fotografie | d79e22187f04 |
| cp_246,247,250,251_001.jpg | fotografie | d822c17be8ad |
| cp_247,250_001.jpg | fotografie | c2e5272d70cd |
| cp_250,251,253,254,255_001.jpg | fotografie | 1c5b387ad44c |
| cp_250,449,495_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | d17affde9a45 |
| cp_250,449,495_001.jpg | archivní karta | c6cf9d080105 |
| cp_250,449,495_001.jpg | fotografie | b460981e4be4 |
| cp_250,449,495_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | c86b49d87831 |
| cp_250,449,495_002.jpg | archivní karta | 51281aefeef9 |
| cp_250,449,495_002.jpg | fotografie | 98f542e7e439 |
| cp_250,449,495_002_col.png | kolorovaná odvozenina | 525a91a660e3 |
| cp_250_001.jpg | archivní karta | 46fb48b2bda8 |
| cp_250_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 57f1a33d968d |
| cp_250_001.jpg | fotografie | 54e51427454b |
| cp_250_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 05413ebeb7f4 |
| cp_250_001.jpg | fotografie | 27a14f64b219 |
| cp_250_001.jpg | archivní karta | 77283147e4b3 |
| cp_250_001.jpg | plán / výkres | 1d4637bca432 |
| cp_250_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | ce979a4d14e4 |
| cp_250_col.png | kolorovaná odvozenina | c2dbcd10e64a |

### Čp. 495: úzký dům s řeznictvím a štítem do ulice

- Úzký jednoosý dům mezi 449 a 250 (bývalé řeznictví T. Töppera); karta KSPPOP neg. 10.953 popisuje uliční fasádu, situace plánu portálu z roku 1930 dává pořadí 250 | 495 | 449. Šířka 5,83 m je z plánu 1930 a zaměření 1972, GIS má 7,6 m.
- Prameny: fotografie cp_495_001 (neg. 10.953, 1974), plán krámského portálu O. Zienerta z 1. 6. 1930 (cp_495_005), zaměření půdorysu O. Horákové z roku 1972 (cp_495_001__3), náčrt střech KSPPOP 495/2, GIS půdorys 331
- Střecha: sedlová střecha s hřebenem kolmo k ulici, štítová zeď do ulice s volským okem, nižší zadní křídlo s pultovou střechou
- GIS budova 331 (popisek 495); geometrie revize r1, 194 polygonů.
- Hypotézy: sklon střechy a výška hřebene (11,3 m) jsou odhad – žádný řez; plán 1930 kreslí v patře tři okna, fotografie z roku 1974 ukazuje dvě – model sleduje fotografii; zadní křídlo podle půdorysu 1972 a náčrtu, bez kót; dva listy ve struktuře patří jiným domům (čp. 268 Minoritská 1885; Friedhofsstraße 1929) a nebyly použity

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_250,449,495_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | d17affde9a45 |
| cp_250,449,495_001.jpg | archivní karta | c6cf9d080105 |
| cp_250,449,495_001.jpg | fotografie | b460981e4be4 |
| cp_250,449,495_002.jpg | fotografie | 98f542e7e439 |
| cp_250,449,495_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | c86b49d87831 |
| cp_250,449,495_002.jpg | archivní karta | 51281aefeef9 |
| cp_250,449,495_002_col.png | kolorovaná odvozenina | 525a91a660e3 |
| cp_495_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | a9323b000e9f |
| cp_495_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 34d74f89c28a |
| cp_495_001.jpg | archivní karta | 9919ae4bf4bf |
| cp_495_001.jpg | plán / výkres | bb4bcee316fd |
| cp_495_001.jpg | fotografie | afe358dbe94d |
| cp_495_001__2.jpg | plán / výkres | a1dd132e9c17 |
| cp_495_001__3.jpg | plán / výkres | b66a4e361220 |
| cp_495_001_col.png | kolorovaná odvozenina | f6ac64e5c6dd |
| cp_495_001_col_cr_front.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 77c26178802a |
| cp_495_001_mult.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 73e4ac6f8ef5 |
| cp_495_002.jpg | plán / výkres | f956a1894f40 |
| cp_495_002__2.jpg | plán / výkres | 4f283da11f2b |
| cp_495_003.jpg | plán / výkres | b3c089ca29b2 |
| cp_495_003__2.jpg | plán / výkres | 68c6c283a080 |
| cp_495_004.jpg | plán / výkres | 1a431bf4662b |
| cp_495_004__2.jpg | plán / výkres | b9a51cf8545d |
| cp_495_005.jpg | plán / výkres | 6043ba8f15e9 |
| cp_495_005__2.jpg | plán / výkres | ab162375b617 |
| cp_495_006.jpg | plán / výkres | 04635132e92a |

### Čp. 449: nárožní dům u Fučíkových sadů s krámy a balkonem

> **Upozornění – částečně hypotéza:** Jižní průčelí je zaměřeno (1974) a fotografováno; uliční fasáda je doložena jen šikmými fotografiemi a projektem 1891 (přízemí = projekt).

- Nárožní dům na západní straně ulice u Fučíkových sadů (parcela 644 na rohu Pragerstraße a Kaiser-Josefs-Promenade). Karty KSPPOP neg. 10.955–10.958 popisují nároží, průčelí ze sadů, dvůr a kůlnu; plán F. Griesbacha z roku 1891 kótuje 15,00 m do ulice a 17,50 m do promenády (GIS má jen 12,0 × 10,9 m).
- Prameny: zaměření V. Nováka 1974 PRŮČELÍ 1:50 (jižní fasáda, cp_449_001__3), plán F. Griesbacha z 24. 10. 1891 (půdorysy, krov, situace), fotografie cp_449_001 (neg. 10.955 nároží, neg. 10.956 ze sadů), cp_249_001 (Šejner ~1965), cp_249,449_001 (~1960), cp_449,545_001/002 (předválečné od knihovny), náčrt střech KSPPOP 449/3
- Střecha: valba s hřebenem rovnoběžným s jižní fasádou nad jižním blokem, hřeben kolmo k ní nad uličním blokem až ke štítové zdi u 495, atikový štít do sadů se dvěma okénky, menší štít s balkonem do ulice, zadní přístavek s plochou lepenkovou střechou, čtyři komíny
- GIS budova 332 (popisek 449); geometrie revize r1, 744 polygonů.
- Hypotézy: šířky 15,0 × 17,5 m podle plánu 1891 místo GIS 12,0 × 10,9 m; rozložení kotví jihovýchodní roh na GIS; přízemí uliční fasády (výkladce a vstup) je podle projektu 1891 – fotografie je nečtou; sklon střech 28° a hřeben 11,1 m ze siluety zaměření; zadní přístavek a dvorek podle náčrtu, bez kót; balustrády, rustika a pilastry jsou textura

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_249,297,449_001.jpg | archivní karta | e9bcf81f7d82 |
| cp_249,449_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 605c5a6236fd |
| cp_249,449_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 2978decc17e5 |
| cp_249,449_001.jpg | plán / výkres | 5d2aeb30b567 |
| cp_249,449_001.jpg | archivní karta | f2f3225c46b7 |
| cp_249,449_001.jpg | fotografie | cb2dbcbda647 |
| cp_249,449_001__2.jpg | fotografie | 3ba849f414cb |
| cp_249,449_001__cp_449_crop.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 0d329cb0ba2d |
| cp_249,449_001_col.png | kolorovaná odvozenina | 7b962da9634b |
| cp_249_002__cp_449_crop.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 1d7a977d0fe8 |
| cp_249_002_col__cp_449_crop.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | ec7e176d3188 |
| cp_250,449,495_001.jpg | archivní karta | c6cf9d080105 |
| cp_250,449,495_001.jpg | fotografie | b460981e4be4 |
| cp_250,449,495_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | d17affde9a45 |
| cp_250,449,495_002.jpg | archivní karta | 51281aefeef9 |
| cp_250,449,495_002.jpg | fotografie | 98f542e7e439 |
| cp_250,449,495_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | c86b49d87831 |
| cp_250,449,495_002_col.png | kolorovaná odvozenina | 525a91a660e3 |
| cp_449,545_001.jpg | fotografie | 1990573ee8db |
| cp_449,545_002.jpg | fotografie | 5197e8b0c962 |
| cp_449_001.jpg | archivní karta | 2c1a583226b3 |
| cp_449_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | d3a6fec8d5bf |
| cp_449_001.jpg | plán / výkres | 8ca519dc9544 |
| cp_449_001.jpg | fotografie | 664639ee37f4 |
| cp_449_001.jpg | archivní karta | 1407aa28428e |
| cp_449_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 8422aa7c95a0 |
| cp_449_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 846ae43187e2 |
| cp_449_001__2.jpg | plán / výkres | ad0e28c91ecb |
| cp_449_001__3.jpg | plán / výkres | 45ba040f4976 |
| cp_449_001_col.png | kolorovaná odvozenina | a844605a9928 |
| cp_449_002.jpg | fotografie | 7e112c98d07b |
| cp_449_002.jpg | plán / výkres | 6198ca30e575 |
| cp_449_002.jpg | archivní karta | 7b7abf7ced05 |
| cp_449_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 809019f33e22 |
| cp_449_002_col.png | kolorovaná odvozenina | 68bf6d4d348a |
| cp_449_003.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 7fa2a48c2748 |
| cp_449_003.jpg | archivní karta | 9917b60e6437 |
| cp_449_003.jpg | fotografie | 3fe6361cbc20 |
| cp_449_003.jpg | plán / výkres | 5f8c4713e0a7 |
| cp_449_004.jpg | archivní karta | 2690fa986b12 |
| cp_449_004.jpg | plán / výkres | d922ede382db |
| cp_449_004.jpg | fotografie | 31531991e3dc |
| cp_449_004.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 23462d6c70ff |
| cp_449_005.jpg | plán / výkres | 2cecb0a02c24 |
| cp_449_006.jpg | plán / výkres | fbd4dd69a5cd |

### Čp. 247: spojený nárožní dům u náměstí s portálem a balkonem

> **Upozornění – částečně hypotéza:** Dům je doložen jen šikmými fotografiemi 1970–74 a náčrtem střech; plány chybějí – výšky, osy a zadní budovy jsou hypotéza.

- Dvě historické části pod jedním číslem na jihovýchodním rohu Šmeralova náměstí: nárožní část k náměstí (Květiny) a jižní část s portálem, balkonem a frontony směrem k 249. Karty KSPPOP (VII a XII 1973, 1974) popisují průhledy náměstím i ulicí a portál; plány domu se nenašly.
- Prameny: fotografie cp_247_001 (XII 1973 průhled ulicí; ~1973 jihovýchodní roh náměstí), cp_247_002 (~1974 portál s balkonem), cp_246,247_001 (VII 1973 nároží z náměstí), cp_247,249_001 (~1970 od Fučíkových sadů), pohlednice III. Platz, náčrt střech KSPPOP 247/1, GIS půdorys 333
- Střecha: valbová střecha s hřebenem rovnoběžným s ulicí přes obě části, nárožní valba k náměstí, křídlo podél náměstí, štítová zeď k 249, pět volských ok do ulice (náčrt), tři do náměstí (nemodelována); zadní patrová budova a pavlače jako nižší objemy
- GIS budova 333 (popisek 247); geometrie revize r1, 1158 polygonů.
- Hypotézy: bez plánů: výšky (okap 8,3 m), osy a krámy přízemí jsou odhad ze šikmých snímků; portál 10,3 m od nároží podle náčrtu střech (balkon); půdorys zjednodušen na hlavní blok 11,95 m a dvě zadní budovy; dvůr za jižní částí je v modelu zastřešen; sklon střechy a hřeben odhad; frontony oken jako geometrie 0,15 m

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| P-000080.jpg | pohlednice | a0652af2f647 |
| P-000080__2.jpg | pohlednice | d5cb6339e151 |
| P-000081.jpg | pohlednice | 31632986f1a8 |
| P-000081__2.jpg | pohlednice | 8ec5eeb5eba8 |
| cp247_a_crop_V.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 04747152e846 |
| cp_242,243,244,245,246,247_001.jpg | fotografie | 3cc8d720e973 |
| cp_244,245,246,247,250,251_001.tif.jpg | fotografie | d79e22187f04 |
| cp_244,245,246,247_001.jpg | fotografie | d4ab5a719216 |
| cp_246,247,250,251_001.jpg | fotografie | d822c17be8ad |
| cp_246,247_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | c9a7050a3433 |
| cp_246,247_001.jpg | fotografie | 73639efffb4e |
| cp_246,247_001.jpg | archivní karta | 0ddcb7e3baf7 |
| cp_247,249_001.jpg | archivní karta | a52a4144afb8 |
| cp_247,249_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 4b95d5eb3c49 |
| cp_247,249_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 01a0e6328f88 |
| cp_247,249_001.jpg | fotografie | 19aa0ca6e218 |
| cp_247,249_001.jpg | plán / výkres | 69e0c9f7ef66 |
| cp_247,249_001__2.jpg | fotografie | e54f806dbde2 |
| cp_247,250_001.jpg | fotografie | c2e5272d70cd |
| cp_247_001.jpg | archivní karta | 5dc7b7aa5b0f |
| cp_247_001.jpg | fotografie | b0d7f2aea5b3 |
| cp_247_001.jpg | archivní karta | 7bd7688c292b |
| cp_247_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 28d69dfcc30d |
| cp_247_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 535316d0c4eb |
| cp_247_001.jpg | fotografie | 8e5b61cf4c73 |
| cp_247_001_col_cr_front.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 979a3a78ec15 |
| cp_247_001_mult.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 774f984a79b0 |
| cp_247_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | c91df40fbd5e |
| cp_247_002.jpg | archivní karta | f3524831e997 |
| cp_247_002.jpg | fotografie | 8c2b7d16fe6f |
| cp_247_002_col.png | kolorovaná odvozenina | ccd42d839c3d |
| cp_247_002_col_cr_front.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | c272340a17bc |
| cp_247_002_mult.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 5e2a6f2ec63f |
| cp_247_b_col.png | kolorovaná odvozenina | e9339474b2ef |

### Čp. 249: třípodlažní nárožní dům u Rybalkovy se třemi štíty

> **Upozornění – částečně hypotéza:** Jižní dvouosá štítová fasáda je zaměřena (1974) a fotografována; uliční fasáda a zadní křídlo jsou odvozeny ze šikmých fotografií a náčrtu – osy a výšky jsou hypotéza.

- Nárožní dům na východní straně ulice u Rybalkovy (Mechanika, Elektroopravna); karty KSPPOP 1965–1975 popisují nároží z Rybalkovy, bok do Rybalkovy i zadní křídlo. Zaměření V. Nováka z roku 1974 kreslí dvouosou štítovou fasádu 7,65 m širokou, GIS dává jižnímu boku 12,46 m – rozpor je zapsán v knize nesouladů.
- Prameny: zaměření V. Nováka 1974 PRŮČELÍ 1:50 (cp_249_012) a půdorys přízemí O. Horákové 1973 (cp_249_006), projekty C. Hinkeho 1898–1928 pro dvorní křídlo, fotografie cp_249_001 (~1974 nároží z Rybalkovy; ~1965 Šejner), cp_249_002 (1974, VI 1975), cp_249_003 (X 1975 detail glazovaných cihel), cp_249,449_001 (~1960), náčrt střech KSPPOP 249/2, GIS půdorys 335
- Střecha: valbová střecha s hřebenem rovnoběžným s ulicí, valba k Rybalkově s velkým volutovým štítem, štítová zeď k 247, malý štít na severním konci a střední štít nad dvouosou částí uliční fasády, třípodlažní dvorní křídlo kolmo vzadu
- GIS budova 335 (popisek 249); geometrie revize r1, 1158 polygonů.
- Hypotézy: Novákova jednotka 7,65 m umístěna od nároží na jižní fasádě a její skladba převzata i pro štítovou část uliční fasády; zbytek jižní stěny (4,8 m) je hypotéza; osy uliční fasády (7) odhad ze šikmých snímků ±0,7 m; tři štíty zjednodušeny na trojúhelníky; voluty a štítová okénka jsou textura; zadní třípodlažní křídlo není v GIS – poloha podle náčrtu, výšky podlaží podle řezů Hinke; sklon střechy 28° a hřeben 14,3 m odhad

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_247,249_001.jpg | plán / výkres | 69e0c9f7ef66 |
| cp_247,249_001.jpg | fotografie | 19aa0ca6e218 |
| cp_247,249_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 01a0e6328f88 |
| cp_247,249_001.jpg | archivní karta | a52a4144afb8 |
| cp_247,249_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 4b95d5eb3c49 |
| cp_247,249_001__2.jpg | fotografie | e54f806dbde2 |
| cp_249,282,283,298,284_001.jpg | archivní karta | 983f1ab80de5 |
| cp_249,297,449_001.jpg | archivní karta | e9bcf81f7d82 |
| cp_249,449_001.jpg | archivní karta | f2f3225c46b7 |
| cp_249,449_001.jpg | fotografie | cb2dbcbda647 |
| cp_249,449_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 2978decc17e5 |
| cp_249,449_001.jpg | plán / výkres | 5d2aeb30b567 |
| cp_249,449_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 605c5a6236fd |
| cp_249,449_001__2.jpg | fotografie | 3ba849f414cb |
| cp_249,449_001_col.png | kolorovaná odvozenina | 7b962da9634b |
| cp_249,735,1107,1153_001.jpg | archivní karta | b0b116ed6ec4 |
| cp_249_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | fa1d4f8d9ff2 |
| cp_249_001.jpg | fotografie | cb357bd81e67 |
| cp_249_001.jpg | archivní karta | e7c275cc1c14 |
| cp_249_001.jpg | archivní karta | da5afc3363d8 |
| cp_249_001.jpg | fotografie | 26d6409a898e |
| cp_249_001.jpg | plán / výkres | 14ebfdce9e3a |
| cp_249_001__2.jpg | plán / výkres | 095392e2be16 |
| cp_249_001_col.png | kolorovaná odvozenina | 2a24c92bb19a |
| cp_249_002.jpg | fotografie | ff93e650870f |
| cp_249_002.jpg | archivní karta | 02a1527b0e77 |
| cp_249_002.jpg | fotografie | 33ec3e3b5f37 |
| cp_249_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 425a7ef653af |
| cp_249_002.jpg | plán / výkres | f2146c22c08d |
| cp_249_002.jpg | archivní karta | eee8d4f372da |
| cp_249_002__2.jpg | plán / výkres | 698e55de4de0 |
| cp_249_002__cp_249_crop.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 4928ddbac884 |
| cp_249_002_col.png | kolorovaná odvozenina | a8a2aeefe409 |
| cp_249_002_col__cp_249_crop.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | be3858988a0c |
| cp_249_003.jpg | archivní karta | d9825e0a8bf8 |
| cp_249_003.jpg | fotografie | 185029b8d208 |
| cp_249_003.jpg | plán / výkres | 44229e112e7b |
| cp_249_003__2.jpg | plán / výkres | 3c181406684b |
| cp_249_004.jpg | plán / výkres | 1e3710184815 |
| cp_249_004__2.jpg | plán / výkres | 1760c0bf1d8d |
| cp_249_005.jpg | plán / výkres | 0b5fc1272b2e |
| cp_249_006.jpg | plán / výkres | e8d2523deb1b |
| cp_249_007.jpg | plán / výkres | cee4a6cbb662 |
| cp_249_008.jpg | plán / výkres | c56d576caa6a |
| cp_249_009.jpg | plán / výkres | 05985ef2f544 |
| cp_249_010.jpg | plán / výkres | e65fcc22daa0 |
| cp_249_011.jpg | plán / výkres | 01a4d4fd9c6a |
| cp_249_012.jpg | plán / výkres | 50b9bebb589f |
| cp_249_013.jpg | plán / výkres | ed33222c3349 |
| cp_249_014.jpg | plán / výkres | 414f72ce6c0f |
| cp_249_015.jpg | plán / výkres | 301cd560bd11 |
| cp_249_016.jpg | plán / výkres | 450bc741db84 |
| cp_249_017.jpg | plán / výkres | 7f6f95bee796 |
| cp_249_018.jpg | plán / výkres | ab76560af4e1 |
| cp_249_019.jpg | plán / výkres | 26ff7221a212 |
| cp_249_020.jpg | plán / výkres | d4ca8a537188 |
