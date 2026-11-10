# U náhonu (K jatkám, Schlachthausstraße) a Na popravišti: zpráva o 3D modelu ulice a jeho pramenech

Projekt MOST, GRAFIT FIT ČVUT, 9. 11. 2026. Geometrie a stránka: Claude (Anthropic); textury doplňuje Codex. Web: https://grafitctu.github.io/most/u-nahonu/

Stav: ve 3D je 12 z 12 modelovaných budov. Model ulice (GLB) je k dispozici.

## Co kde stálo

Poloha všech domů pochází z GIS vrstvy projektu, která je vektorizací historického plánu města Mostu z roku 1938. Ulice U náhonu (K jatkám) v ní má 15 budov a navazující Na popravišti 11; 19 z nich nese číslo popisné. Na západní straně U náhonu leží nároží Rybalkovy (281) a ulice B. Jablonského (988 a 1818), východní stranu zabírá areál městských jatek. Na jižním konci ulice ústí do Na popravišti, jejíž jihovýchodní řada od nárožního domu 606 končí krajním domem 1068 u volného plácku směrem k Pražské ulici. Kliknutím na dům v mapě otevřete jeho stránku.

Mapa ukazuje půdorysy GIS. Model se od nich tam, kde to prameny dokládají, odchyluje: dvojice 988 a 987 má šířky 11,40 a 12,05 m místo 12,38 a 11,07 m (součet řady podle GIS je zachován), domy 541, 1065 a 1068 mají šířky z kótovaných plánů 12,80, 9,00 a 9,00 m místo 12,15, 10,06 a 8,44 m, stáje 286 jsou blokem 10,30 m podle plánu 1928, kde GIS kreslí jen pás 4,56 m, a dům 281 nemá nárožní pás 3,1 m, který je podle karty terasou nad garážemi. Domek 1886 v GIS chybí a je zakreslen podle náčrtu (viz [Rozpory](#rozpory)).

### Úseky ulice
- Z · západní strana U náhonu (od Rybalkovy k Na popravišti): 281, 286, 987, 988, 1818, 431
- NP · Na popravišti, jihovýchodní řada (od nároží 606 k plácku u Pražské): 606, 1886, 719, 541, 1065, 1068

### Databázové oblasti a co modelováno není

Oblast U náhonu se v databázi Libuše během práce dvakrát přeorganizovala: snapshot z 11. 9. 2026 měl 20 struktur (a duplicitní oblast „U Nahonu“ s kolorovanými odvozeninami), živé načtení 23. 10. 2026 dvanáct a 9. 11. 2026 jen sedm (556, 566, 838, 987, 988, 1697, 1886); oblast Na popravišti má osm struktur. Obě oblasti mají dohromady 15 struktur. Domy 281 (dnes oblast Rybalkova), 286 a 431 (Leninova) a 1818 (Jablonského) jsme načetli z jejich nových oblastí, stejně jako sousední domy jmenované na kartách; všech 554 příloh 29 struktur jsme otevřeli. Domy, které byly zbořeny před pořízením dostupných snímků, jsou předány jako blocked:

| Čp. | Proč není modelován | Přílohy v databázi |
|---|---|---|
| 455 | nárožní domek Na popravišti × U náhonu (GIS 1611); zbořen před pořízením dostupných snímků: na fotografiích ze 70. let je na jeho místě proluka; GIS (plán 1938) budovu ještě vede; jediný plán 455_01 kreslí přístavbu (projektová hypotéza je otázka pro uživatele) | 5 |
| 597 | dům Na popravišti (GIS 1612); zbořen před pořízením dostupných snímků: na fotografiích ze 70. let je na jeho místě proluka; GIS (plán 1938) budovu ještě vede; plán 597_01 je jen dvorní chlév | 6 |
| 697 | dům Na popravišti (GIS 1613); zbořen před pořízením dostupných snímků: na fotografiích ze 70. let je na jeho místě proluka; GIS (plán 1938) budovu ještě vede; plán chybí | 5 |
| 838 | budova správy jatek (GIS 1298); v náčrtu areálu přeškrtnutá, bez snímku | 11 |

Struktury oblasti U náhonu, které modelované nejsou (v sestavě šedé bloky):

| Čp. | Poznámka | Ulice podle GIS | Přílohy |
|---|---|---|---|
| 556 | Všech 16 příloh ukazuje dům čp. 556 v Tyršově ulici; GIS budova 1299 se štítkem 556 v areálu jatek nemá pramen (možná záměna s halou 566) – v sestavě šedý blok | Tyršova (1938 Jahnova), U náhonu (1938 K jatkám) | 16 |
| 566 | hala jatek: jediný šikmý snímek bez měřítka a náčrt areálu; strana a délka nejisté – v sestavě šedý blok | v GIS není | 12 |
| 1697 | bývalá prádelna jatek: jediný snímek, pravděpodobně dvorní strana – v sestavě šedý blok | U náhonu (1938 K jatkám) | 3 |

Jako šedé bloky zůstávají i dům 550, jehož hlavní průčelí patří Leninově ulici, a budova GIS se štítkem 230: pod číslem 230 vede Libuše dům ve Starém městě (oblast Hvězdná), pro budovu u jatek pramen nemá.

## Odkud jsou prameny

### Fotografie ze 70. let

Fasády všech modelovaných domů kromě domku 1886 jsou ze snímků ze 70. let: série ATO119 (řadový snímek 988 a 987 od jihovýchodu, čelní a nárožní záběry, dvorní strany z balkonu sousedního domu) a fotografie s kartami Krajského střediska státní památkové péče a ochrany přírody (KSPPOP), které popisují stanoviště a sousedy. Každý použitý snímek je na stránce domu s červeným rámečkem a ID otvorů. Cílová epocha modelu jsou 70. léta, proto je dům 431 ruinou bez střechy, jak ho ukazuje fotografie, a ne domem podle projektu 1922.

### Stavební plány 1885–1941

Kótované plány dávají šířky, výšky a sklony: nárožní dům 281 (červen 1885, „an Stelle des alten“), dům 719 (1885, přestavba 1928), domy 1065 (říjen 1899, Franz Weitzdorfer) a 1068 (prosinec 1899, C. Hinke), dům 431 (1922, Josef Richter), přestavba stájí 286 (říjen 1928, A. Meixner), dům 541 (kolem 1927, řez 1930) a zaměření domu 606 z roku 1941. Projekt není realizace: neobarokní výzdoba 1068, bosáž 719 a dvojice oken 606 z projektů na fotografiích nejsou a model je nemá.

### Náčrty KSPPOP

Ručně kreslené situační a střešní náčrty ze 70. let určují členění střech, polohu komínů a domy v hloubce bloku; podle náčrtu 606/5 je zakreslen domek 1886, který GIS nezná.

### Chybně zařazené a cizí listy

Listy cp_541_04 a cp_541_05 jsou plány domu 719 (1924). Plány 431 z let 1874–1883 nesou prázdné číslo a jiné rozměry a nebyly použity. Plán dvora 1818 z roku 1933 nese omylem „Nr. 1816“. Všech šestnáct příloh čp. 556 ukazuje dům v Tyršově ulici, ne budovu u jatek.

### Databáze Libuše projektu MOST

Databáze byla použita pouze pro čtení (0 zápisů). Seznam oblastí a přílohy jsme načetli živě 23. 10. a znovu 9. 11. 2026, protože se oblast U náhonu mezitím přeorganizovala. Celkem 554 příloh 29 struktur (oblasti U náhonu a Na popravišti, nové oblasti přesunutých domů Rybalkova, Leninova, Jablonského a Hvězdná a sousední domy jmenované na kartách) jsme otevřeli na kontaktních listech; karty a plány jsme četli v plné velikosti. Oblasti U náhonu a Na popravišti mají 15 struktur a 208 příloh (167 jedinečných).

### Odvozeniny

Kolorované snímky a výřezy v databázi jsou rekonstrukce, ne prameny. O tvaru, otvorech a nápisech rozhoduje původní černobílá fotografie nebo plán.

### GIS a terén

Polohy a natočení domů jsou z GIS vrstvy (vektorizace plánu 1938, místní souřadnice). Šířky se od GIS liší tam, kde je dokládá plán nebo poměr na snímku (viz mapa). Výšky budov v GIS jsou jen zástupný údaj: výšky jsou z řezů a pohledů plánů (281, 286, 541, 606, 1065, 1068), z poměrů na snímcích (987, 988, 1818, 431) nebo odvozené z profilu projektu (719). Terén je plochý (z = 0 u všech domů); historický výškopis nebyl k dispozici.

## Jak vznikla geometrie

- **Rešerše plánů.** Nejdříve jsme prohledali databázi: všech 554 příloh 29 struktur jsme otevřeli na kontaktních listech, karty a plány jsme četli v plné velikosti (titulek, datum, měřítko, stavebník, sousedé). Protože se oblast U náhonu během práce přeorganizovala, hledali jsme přílohy každého čísla popisného ve všech oblastech, kde ho databáze vede.

- **Identita domů.** Pořadí domů na řadových snímcích, popisy stanovišť na kartách a šířky z GIS a z plánů určují, který dům je který: dvě levé osy snímku cp_987_001 patří domu 988, dům 281 má hlavní průčelí do Rybalkovy a k U náhonu jen slepý štít, budova 286 v U náhonu jsou dvorní stáje domu z Leninovy a dům 431 byl v 70. letech ruinou.

- **Fasáda jen z fotografie nebo plánu s domem v rámečku.** Na každém použitém snímku je dům v červeném rámečku a každý otvor má ID (G okna přízemí, M a U okna pater, D dveře, P průjezd, R a B zadní a dvorní strana). Počty otvorů z rámečků kontroluje brána proti plánu modelu; otvory, které pramen neukazuje, jsou přiznané hypotézy.

- **Měřítko.** Šířky jsou z kótovaných plánů (541, 1065, 1068, 286, 281), ze situace 1928 a poměru šířek na řadovém snímku (988 a 987) nebo z GIS. U fotografií jsme fasády rektifikovali na známou šířku; výšky jsou z řezů plánů nebo z poměrů na snímcích. Kde se projekt liší od fotografie, model sleduje fotografii.

- **Střecha.** Členění střech je z náčrtů KSPPOP, plánů a snímků, sklony z řezů; střecha hotového modelu se změří ze sítě. Zvláštní tvary: pultová střecha stájí 286 napříč ulicí za stupňovitou atikou, téměř plochá pultová střecha 541, složená střecha 1818 a ruina 431 bez střechy.

- **Stavba v Blenderu.** Parametrický builder bez okna (`build_house_un2.py`, kopie builderu ulice U Pražské brány s doplňky pro pultové střechy) vyrobí z `geometry_plan.json` BLEND a GLB; ruinu 431 staví vlastní skript. Otvory jsou skutečné niky, materiály jsou jen ID pro pozdější textury.

- **Kontrola.** Brána geometrie (prosvítání podkroví paprsky, nekryté zdivo, střecha nad prázdnem, UV, síť, počty otvorů) a vizuální kontrola: pohledy s materiály a bez barev (čtyři strany, čtyři rohy shora, dva podhledy u okapu, shora), detaily otvorů a záznam kontroly. Opravy po kontrole dostávají novou revizi (988 r4, 286 r5, 541 r3), starší revize zůstávají uložené. Dům se do ulice umístí až po prošlé bráně a prohlédnuté sadě; u ruiny 431 je nekrytá koruna zdí doloženou výjimkou.

- **Sestava ulice.** Registr `street_layout_gis.json` drží polohu, natočení a revizi každého domu (rámec X = východ, Y = sever); okolní budovy z GIS zastupují v sestavě šedé bloky, silnice a chodníky mají šířky jako hypotézu.

Pracovní složka: F:\MOST\output\u_nahonu_street_claude_2026-10-23\ (domy, kontroly, registr poloh; prameny jen ke čtení; stav 9. 11. 2026).

## Rozpory a hypotézy

- **Přeorganizovaná databáze.** Oblast U náhonu měla ve snapshotu z 11. 9. 2026 dvacet struktur, při živém načtení 23. 10. dvanáct a 9. 11. 2026 sedm; přílohy domů se přestěhovaly do oblastí sousedních ulic a přibyly stavební plány. Rozsah rekonstrukce proto určuje GIS ulice 40 a navazující řada Na popravišti, ne databázová oblast.

- **987 a 988: čtyři osy a šířky.** Při prvním čtení měl dům 987 šest os; řadový snímek ATO119_10_9_005 ukazuje, že dvě levé osy snímku cp_987_001 patří domu 988. Situace z roku 1928 na listu stájí 286 a poměr šířek na dvou snímcích dávají 988 šířku 11,40 m a 987 šířku 12,05 m, GIS 12,38 a 11,07 m. Model posouvá jen dělicí zeď o 0,98 m a součet řady 23,45 m podle GIS drží; kanonický GIS zůstává beze změny a rozhodnutí o něm patří uživateli.

- **988: jihozápadní výběžek GIS.** GIS kreslí za domem 988 výběžek v plné výšce; zadní snímek ho zakrývá střechou nízkého domu 790. Model ho má jako přízemní přístavek 3,6 m s valbou (hypotéza).

- **281: průčelí do Rybalkovy a nedokončené nároží.** Dům 281 má podle plánu 1885 a snímku ze 70. let hlavní průčelí se čtyřmi osami do Rybalkovy a k U náhonu jen slepý štít. GIS polygon má k Rybalkově hranu 13,98 m; nárožní pás 3,1 m je podle karty „nedokončené nároží“ s terasou nad garážemi a modelován není.

- **286: pás GIS proti stájím z roku 1928.** GIS kreslí v U náhonu jen pás 4,56 × 26,6 m; plán přestavby stájí z října 1928 a snímky ukazují blok 10,30 m s atikou a pultovou střechou napříč ulicí. Model drží plán; dvorní strana a otvory přízemí jsou hypotéza (štítek).

- **431: ruina ze 70. let proti projektu 1922.** Jediný snímek ze 70. let ukazuje obvodové zdi bez střechy s obloukem průjezdu a vlomenými garážovými vraty. Plán z roku 1922 kreslí dům se sedlovou střechou a obytným podkrovím. Model ukazuje doložený stav epochy (štítek), varianta podle plánu 1922 je otázka pro uživatele.

- **Na popravišti: šířky plánů proti GIS.** Kótované plány dávají domům 541, 1065 a 1068 šířky 12,80, 9,00 a 9,00 m (dohromady 30,80 m), GIS 12,15, 10,06 a 8,44 m (30,65 m). Model drží plány a posouvá dělicí zdi; 606 a 719 mají šířku z GIS.

- **1886: domek bez půdorysu.** GIS domek nezná; náčrt 606/5 ho klade do hloubky bloku za dům 719 a jediný snímek od zahrady je zarostlý. Poloha, velikost i podoba jsou hypotéza (štítek).

- **Štítky GIS bez pramene.** GIS budova 370 se štítkem 230 a budova 1299 se štítkem 556 leží v areálu jatek, ale Libuše vede pod těmito čísly dům ve Starém městě a dům v Tyršově ulici. Náčrt areálu klade na místo GIS 1299 halu 566 (možná záměna 556 ↔ 566); co stálo na místě GIS 370 a 371, zůstává otevřené.

- **Zbořené domy.** Na místě domů 455, 597 a 697 jsou na snímcích ze 70. let proluky a budova správy jatek 838 je v náčrtu přeškrtnutá. GIS (plán 1938) je ještě vede, proto jsou v sestavě šedé bloky a domy jsou předány jako blocked; dům 455 by šel postavit jen jako projektová hypotéza podle jediného plánu.

- **Výšky.** Okapy a hřebeny jsou z řezů plánů (281, 286, 541, 606, 1065, 1068; ±0,3 m), z poměrů na snímcích (987, 988, 1818, 431; ±0,3–0,4 m) nebo odvozené z profilu projektu (719); u 1886 odhad.

- **Dvorní a nedoložené strany** jsou bez otvorů, pokud je žádný pramen neukazuje. Volská oka z náčrtů, která uliční snímky nepotvrzují, modelována nejsou; šambrány, rustika a vlysy jsou textura.

- **Terén** je plochý (z = 0 u všech domů); historický výškopis nebyl k dispozici. Šířky silnice a chodníků jsou hypotéza.

Údaje jsou v datech označené jako `model_hypothesis`, `status: provisional`, `locked: false`.

## Kniha nesouladů pramenů

Případy, kdy si prameny odporují (plán proti fotografii, GIS proti plánu, chybně zařazený list, přeorganizovaná databáze), zapisujeme do interní knihy nesouladů pramenů projektu MOST. Ta se zatím nepublikuje, proto zde uvádíme jen identifikátory případů této ulice (9):
- `2026-11-03_u-nahonu_987-sest-os-vs-ctyri-na-radovem-snimku` – U náhonu 987: dvě levé „osy“ čelního snímku patří sousedu 988 – dům má 4 osy a je o 1 m širší, než udává GIS (dělicí zeď s 988 posunuta)
- `2026-11-03_u-nahonu_988-jz-vybezek-gis-vs-790` – U náhonu 988: jihozápadní výběžek GIS půdorysu vypadal na zadním snímku jako křídlo, karta ale říká, že nízká valbová stavba je čp. 790 ve dvoře 915
- `2026-11-03_u-nahonu_oblast-20-struktur-vs-zivy-get-12` – U náhonu: oblast v Libuši se během práce dvakrát přeorganizovala – 20 struktur (11. 9.) → 12 (23. 10.) → 7 (9. 11. 2026); přílohy domů se přestěhovaly do oblastí sousedních ulic a přibyly stavební plány
- `2026-11-09_na-popravisti_sirky-planu-vs-gis` – Na popravišti: kótované plány dávají 541 = 12,80, 1065 = 9,00 a 1068 = 9,00 m, GIS 12,15 / 10,06 / 8,44 m – součet sedí, posunuté jsou dělicí zdi; dva plány 719 leží u 541
- `2026-11-09_u-nahonu_281-pruceli-do-rybalkovy-nedokoncene-narozi` – U náhonu 281: nárožní dům má hlavní průčelí do Rybalkovy; k U náhonu stojí slepý štít a nároží zůstalo „nedokončené“ – GIS hrana 13,98 m zahrnuje i terasu nad garážemi
- `2026-11-09_u-nahonu_286-gis-pas-4m-vs-staje-1928-10m` – U náhonu: dvorní budova 286 Leninova má v GIS jen pás 4,56 m podél ulice, plán stájí z roku 1928 i snímky ze 70. let ukazují blok 10,30 m s atikou
- `2026-11-09_u-nahonu_431-ruina-70-let-vs-plan-1922` – U náhonu 431: jediný snímek ukazuje ruinu bez střechy s vlomenými garážovými vraty, plán z roku 1922 dům s obytným podkrovím
- `2026-11-09_u-nahonu_455-597-697-838-zboreny-pred-snimky` – U náhonu / Na popravišti: GIS má budovy 455, 597, 697 a 838, ale na snímcích ze 70. let jsou na jejich místě proluky
- `2026-11-09_u-nahonu_gis-stitky-230-556-bez-pramene` – U náhonu: GIS budovy se štítky 230 a 556 nemají v Libuši pramen – archiv vede pod těmito čísly domy ve Starém městě a v Tyršově ulici

## Přehled domů

| Čp. | Úsek | Typ | Štítek | Podlaží | Průčelí × okap (m) | Revize | Přílohy | Stav / textury |
|---|---|---|---|---|---|---|---|---|
| 281 | Z | nárožní dům do Rybalkovy (plán 1885) | – | 2 + podkroví | 10,9 × 9,7 | r1 | 21 | zatím bez textur |
| 286 | Z | dvorní budova (stáje 1928) domu 286 Leninova | Částečně hypotéza | 2 | 10,3 × 4,7 | r5 | 44 | bez textur (Částečně hypotéza – jen prosté materiály) |
| 987 | Z | třípodlažní nájemní dům (4 osy) | – | 3 | 12,1 × 11,3 | r2 | 25 | zatím bez textur |
| 988 | Z | třípodlažní nájemní dům u nároží Jablonského | – | 3 | 11,4 × 11,3 | r4 | 22 | zatím bez textur |
| 1818 | Z | dvoupodlažní dům na nároží Jablonského se složenou střechou | Částečně hypotéza | 2 | 10,7 × 7,3 | r1 | 14 | bez textur (Částečně hypotéza – jen prosté materiály) |
| 431 | Z | ruina domu jako vjezd do garážového dvora (stav 70. let) | Ruina (stav 70. let) | 1 (ruina) | 16,5 × 4,4 | r1 | 17 | bez textur (Ruina (stav 70. let) – jen prosté materiály) |
| 606 | NP | nárožní dům Na popravišti × U náhonu | – | 2 | 9,7 × 6,9 | r1 | 20 | zatím bez textur |
| 1886 | NP | přízemní domek v hloubce bloku (hypotéza) | Hypotéza | 1 | 7,1 × 3,2 | r1 | 3 | bez textur (Hypotéza – jen prosté materiály) |
| 719 | NP | dvoupodlažní dům s průjezdem (přestavba 1928) | – | 2 | 15,8 × 7,8 | r1 | 29 | zatím bez textur |
| 541 | NP | dvoupodlažní dům s průjezdem a téměř plochou střechou | – | 2 | 12,8 × 7,2 | r3 | 18 | zatím bez textur |
| 1065 | NP | dvoupodlažní dům se supraportami (1899) | – | 2 | 9,0 × 8,2 | r1 | 23 | zatím bez textur |
| 1068 | NP | krajní dům řady s holým štítem | – | 2 | 9,0 × 8,3 | r1 | 10 | zatím bez textur |

## Domy jednotlivě

### Čp. 281: nárožní dům do Rybalkovy (plán 1885)

> **Poznámka k identitě a GIS:** GIS 372 má hranu do Rybalkovy 13,98 m; nárožní pás 3,1 m je podle karty terasa nad garážemi, model má 10,9 m

- nárožní dům U náhonu × Rybalkova (1938 Jezdecká, Reitergasse), postavený podle plánu z června 1885 (cp_281_001, „Plan zum Bau eines neuen Wohnhauses an Stelle des alten … No. Cons. 281 am Kasernen-Platz, für die Herrn Peter Stefan’schen Erben“); starší plán 1874 (cp_281_002) kreslí zbořený přízemní dům
- Prameny: plán 1885 (průčelí, řez, půdorysy), fotografie ATO119_10_19_003 (průčelí do Rybalkovy, 70. léta), panoramata cp_281,611,961,1022_001 a cp_281,987_001 se slepým štítem do U náhonu, karty, GIS 372
- Střecha: sedlová, hřeben podél Rybalkovy, štít k U náhonu (slepý, komín ve vrcholu), na západě navazuje 611
- GIS budova 372 (popisek 281); geometrie revize r1, 515 polygonů.
- Hypotézy: šířka 10,9 m (plán + fotografie) místo GIS 13,98 m; hloubka podle GIS 11,93 m místo ≈ 13,3 m z řezu 1885 – kanonický GIS beze změny; nárožní terasa nad garážemi modelována jako nízká substrukce 2,45 m (v 70. letech probořená, za plakátovou ohradou) – tvar a výška hypotéza; výšky otvorů z fotografie při 137 px/m (±0,2 m); atiková okénka 0,4 × 0,4 m odhad; nárožní rizalit s arkýřem z projektu 1885 nebyl postaven – nemodelován; zadní (dvorní) stěna: 4 sloupce oken podle ATO119_10_19_002, polohy a šířky hypotéza; nižší dvorní křídlo na západě bez rozměrů – nemodelováno; pásová rustika přízemí, šambrány, kartuše a zubořez vlysu = mělký detail pro texturu

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_19_002.jpg | fotografie | adaba2c2e29e |
| ATO119_10_19_003.jpg | fotografie | 9868b16a0a34 |
| cp_281,282,611,732,961,1022_001.jpg | fotografie | d484ba0ae356 |
| cp_281,282,611,732,961,1022_001__2.jpg | fotografie | b518209578d0 |
| cp_281,282,611,732,961,1022_001__cp_281_crop.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 2d3ad6ebea6d |
| cp_281,282,611,732,961,1022_001_col.png | kolorovaná odvozenina | f77e597b061f |
| cp_281,282_001.jpg | archivní karta | 142749ed6904 |
| cp_281,611,961,1022_001.jpg | fotografie | d483fb651436 |
| cp_281,611_001.jpg | fotografie | d26ed31c8a7d |
| cp_281,611_001.jpg | archivní karta | f92512da7742 |
| cp_281,987_001.jpg | fotografie | 31c70e771335 |
| cp_281,987_001.jpg | archivní karta | ed4132f77b87 |
| cp_281,987_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 97dea68a7552 |
| cp_281_001.jpg | archivní karta | a3a005db67fe |
| cp_281_001.jpg | fotografie | afafefcfa02e |
| cp_281_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | cda6e24b625d |
| cp_281_001.jpg | plán / výkres | 1a9f67e3c3f4 |
| cp_281_002.jpg | plán / výkres | c75eb379ab45 |
| cp_281_A_front_color_partial_2d3603b4ac.png | kolorovaná odvozenina | 2d3603b4acd2 |
| cp_281_B_front_color_partial_c156f1e5dd.png | kolorovaná odvozenina | c156f1e5dd6f |
| cp_281_mult_d7c7b27c1da2bb50.png | odvozenina bez tagu (kolorovaná / výřez / FRONT) | d7c7b27c1da2 |

### Čp. 286: dvorní budova (stáje 1928) domu 286 Leninova

> **Upozornění – Částečně hypotéza:** Uliční blok podle plánu 1928 a snímků ze 70. let; dvorní strana a otvory přízemí jsou hypotéza, šířka podle plánu (GIS má jen 4,56 m).

> **Poznámka k identitě a GIS:** GIS 1617 kreslí jen pás 4,56 × 26,6 m; model drží blok 10,30 m podle plánu 1928 (délka souhlasí)

- dvorní budova domu čp. 286 Leninova na U náhonu – bývalé stáje (Stallungen), přestavba 10/1928 pro firmu A. Simon & Co. (plán cp_286_03, stavitel A. Meixner, Oberleutensdorf; soused „Wohnhaus K.No. 987 der Fa. Ignaz Glaser“), v 70. letech garáže
- Prameny: plán přestavby 10/1928 (pohled „gegen den Schlachthof“, dvorní pohled, řez A–B, situace), fotografie ATO119_10_9_001 a _002 (= karta cp_286_001), dvorní snímky ATO119_10_19_024 a _028, GIS 1617
- Střecha: řez A–B 1928: pultová střecha za atikou, 6,20 m u zdi 987, 4,70 m na dvorní straně; 4 komíny (Hofansicht)
- GIS budova 1617 (popisek 286); geometrie revize r5, 247 polygonů.
- Hypotézy: šířka 10,30 m podle plánu 1928 místo GIS 4,56 m (fotografie ze 70. let ukazují blok 9,6–10,6 m) – kanonický GIS beze změny; zúžení k západu (plán: 9,4 / 8,5 m, odměřeno) modelováno schodem v polovině hloubky (10,30 → 8,50 m); jižní stěna rovná podél 987 (GIS se k západu lehce stáčí); okno U1 a výška atiky z fotografie ±0,3 m; přízemí do ulice bez otvorů (projekt 1928 kreslí lizény, snímek nečitelný); dvorní fasáda: 4 garážová vrata a 5 malých oken patra – počet podle Hofansicht 1928 a snímků, polohy hypotéza; komíny 4 podle Hofansicht, polohy ±1 m; vrata (dvoukřídlá prkenná) a zeď se zapuštěnými poli: výšky 3,1 / 2,8 m podle plánu, pole = textura; stodola na západním konci (Bestehende Scheuer) není součástí modelu

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_19_018.jpg | fotografie | 1edf7000ee8c |
| ATO119_10_19_019.jpg | fotografie | 840e2f06462a |
| ATO119_10_19_020.jpg | fotografie | d11f7e6d1e77 |
| ATO119_10_19_021.jpg | fotografie | c8aff6253083 |
| ATO119_10_19_022.jpg | fotografie | 0d0d3b9b68df |
| ATO119_10_19_023.jpg | fotografie | 76a6bb1e7ecd |
| ATO119_10_19_024.jpg | fotografie | 7346da32deba |
| ATO119_10_19_025.jpg | fotografie | 8416e2767a79 |
| ATO119_10_19_026.jpg | fotografie | a0ea87ec69e7 |
| ATO119_10_19_027.jpg | fotografie | f7f461fd0213 |
| ATO119_10_19_028.jpg | fotografie | b91966eb2383 |
| ATO119_10_19_029.jpg | fotografie | 616e993a67e0 |
| ATO119_10_19_030.jpg | fotografie | 200af8524b26 |
| ATO119_10_19_031.jpg | fotografie | d40fc2b505dc |
| cp_282,283,298,284,285,286,287,915,297_001.jpg | archivní karta | 727eb8e3203d |
| cp_282,283,298,284,285,286,287,915,297_001.jpg | plán / výkres | dbbba77ed367 |
| cp_282,283,298,284,285,286,287,915,297_001.jpg | fotografie | e988667ef249 |
| cp_282,283,298,284,285,286,287,915,297_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 3fedd3c24978 |
| cp_282,283,298,284,285,286,287,915,297_001_col.png | kolorovaná odvozenina | 8c6b31a67eda |
| cp_282,283,298,284,285,286,287,915_001.jpg | fotografie | e8c883dc2962 |
| cp_282,283,298,284,285,286,287,915_001_col.png | kolorovaná odvozenina | b8d1a4f8201b |
| cp_283,298,284,285,286,287,915_001.jpg | fotografie | 5591b31a5b45 |
| cp_283,298,284,285,286,287,915_001_col.png | kolorovaná odvozenina | 2f04953887cb |
| cp_284,285,286,287,298,915_001.jpg | fotografie | fd1882196e1c |
| cp_284,285,286,287,298,915_001.jpg | archivní karta | 3be6202471bd |
| cp_285,286,287,915,292,1310_001.jpg | fotografie | 95fc692bd2d7 |
| cp_285,286,287,915,292,1310_001_col.png | kolorovaná odvozenina | 03cd86d96a30 |
| cp_285,286_001.jpg | fotografie | 8544e7e8791f |
| cp_285,286_001.jpg | archivní karta | 74f731f92572 |
| cp_286,287,915_001.jpg | archivní karta | 3a172455f203 |
| cp_286,287,915_001.jpg | fotografie | 17398bb1bade |
| cp_286,287,915_002.jpg | archivní karta | c4fa2ce99e07 |
| cp_286,287,915_002.jpg | fotografie | 6cc28a5382c5 |
| cp_286_001.jpg | archivní karta | fd7ddf7211b9 |
| cp_286_001.jpg | fotografie | 1383452d49f3 |
| cp_286_001.jpg | archivní karta | ed85215b780a |
| cp_286_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | b6e3974cc313 |
| cp_286_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 77db7f386c58 |
| cp_286_001.jpg | plán / výkres | afda861af50b |
| cp_286_001__2.jpg | fotografie | ffb7f0bcc4b4 |
| cp_286_01.jpg | plán / výkres | 098368bd1f87 |
| cp_286_02.jpg | plán / výkres | 1061d1a80f62 |
| cp_286_03.jpg | plán / výkres | 0a433416ad49 |
| cp_286_04.jpg | plán / výkres | 09e36b96e5ff |

### Čp. 987: třípodlažní nájemní dům (4 osy)

> **Poznámka k identitě a GIS:** GIS 388 dává průčelí 11,07 m; model 12,05 m (součet řady 988 + 987 = 23,45 m podle GIS zachován)

- Třípodlažní dům na západní straně U náhonu mezi stájemi 286 a domem 988; na situaci 1928 (list cp_286_03) „Wohnhaus K.No. 987 der Fa. Ignaz Glaser“. Řadový snímek ATO119_10_9_005 ukazuje obě průčelí 988 a 987 vedle sebe; dvě levé osy snímku cp_987_001 patří domu 988.
- Prameny: fotografie ATO119_10_9_005 (celá řada), ATO119_10_9_001 (= cp_987_001), ATO119_10_9_002, zadní ATO119_10_9_006 (= cp_987_002), situace 1928 na listu cp_286_03, karty, GIS 388
- Střecha: sedlová, hřeben podél ulice, štít k 988 i k severu (požární štít nad blokem 286 s komínem ve vrcholu: ATO119_10_9_002, panorama cp_281,987_001)
- GIS budova 388 (popisek 987); geometrie revize r2, 562 polygonů.
- Hypotézy: šířka 12,05 m místo GIS 11,07 m – dělicí zeď s 988 posunuta o 0,98 m k severu podle situace 1928 a poměru šířek na dvou snímcích; rozhodnutí o kanonickém GIS na uživateli; výšky podlaží z poměrů na fotografiích při okapu H = 11,3 m (nekótováno, ±0,4 m); okap 987 se na hranici s 988 lehce liší (skok římsy na ATO119_10_9_003); šířka oken 1,05 m, dveří 1,15 m odhad; schodišťový rizalit (2,3 × 1,3 m) a zadní otvory ±0,5 m ze šikmého snímku shora; komíny: severní ve vrcholu štítu (doloženo), střední a jižní poloha ±1 m; pásová rustika, vlys pod římsou a šambrány = mělký detail pro texturu

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_9_001.jpg | fotografie | 1bc39b36950e |
| ATO119_10_9_002.jpg | fotografie | 401fa70b7d86 |
| ATO119_10_9_004.jpg | fotografie | d90e8069ac69 |
| ATO119_10_9_005.jpg | fotografie | f0acd857f49f |
| ATO119_10_9_006.jpg | fotografie | fd3780460020 |
| ATO119_10_9_007.jpg | fotografie | 6e4075f55e93 |
| cp_281,987_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 97dea68a7552 |
| cp_281,987_001.jpg | archivní karta | ed4132f77b87 |
| cp_281,987_001.jpg | fotografie | 31c70e771335 |
| cp_599,987,988_001.jpg | plán / výkres | eaa09a4758cc |
| cp_599,987,988_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | a4fee845b3fd |
| cp_599,987,988_001.jpg | archivní karta | 066ff0cd8f59 |
| cp_599,987,988_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | e1e17fbae503 |
| cp_599,987,988_001.jpg | fotografie | 03c99af3652f |
| cp_915,987,988_001.jpg | archivní karta | 9e70552bceed |
| cp_915,987,988_001.jpg | fotografie | 8339483d9cac |
| cp_987_001.jpg | plán / výkres | 10a0de354fe8 |
| cp_987_001.jpg | archivní karta | a45a96d45075 |
| cp_987_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 8a2536542663 |
| cp_987_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 38ac0871d21d |
| cp_987_001.jpg | fotografie | 2a9e6342b9fc |
| cp_987_002.jpg | archivní karta | 795d0547569d |
| cp_987_002.jpg | fotografie | 46a2e89e9cf3 |
| cp_987_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | e9610616f72a |
| cp_987_002_col.png | kolorovaná odvozenina | 95fa03facfe4 |

### Čp. 988: třípodlažní nájemní dům u nároží Jablonského

> **Poznámka k identitě a GIS:** GIS 387 dává průčelí 12,38 m; model 11,40 m podle situace 1928 a poměru šířek na snímcích

- Třípodlažní dům na západní straně U náhonu u nároží ulice B. Jablonského, mezi 987 a 599; nízká stavba za ním vpravo je podle karty čp. 790. Řadový snímek ATO119_10_9_005 a čelní snímek cp_988_002 ukazují 4 osy (1 | 2 3 | 4) s dveřmi u jižního nároží.
- Prameny: fotografie ATO119_10_9_005, cp_988_002 (= ATO119_10_9_003), cp_599,987,988_001, zadní cp_988_001 (= ATO119_10_9_008), situace 1928 na listu cp_286_03, karty, GIS 387
- Střecha: sedlová, hřeben podél ulice, štíty k 599 i k 987 (štít 988 na řadovém snímku s obrysem střechy 599); 3 komíny na hřebeni (zadní snímek)
- GIS budova 387 (popisek 988); geometrie revize r4, 613 polygonů.
- Hypotézy: výšky podlaží a okapu z rektifikace bez kótovaného plánu (±0,3 m); absolutní měřítko H = 11,3 m odhad podle poměru výška/šířka na cp_988_002; polohy os ±0,3 m (rektifikace cp_988_002, kontrola cp_599,987,988_001); šířka oken 1,05 m, dveří 1,25 m odhad; JZ výběžek GIS půdorysu modelován jako přízemní přístavek s valbou (3,6 m) – na zadním snímku zakryt střechou čp. 790; výška i střecha hypotéza; sklon střechy ~31° (zdvih 4,2 m) odhad ze štítu na řadovém snímku; poloha hřebene uprostřed hloubky; komíny: počet 3 ze zadního snímku, polohy ±1 m; 9.11.2026: šířka 11,40 m místo GIS 12,38 m – dělicí zeď s 987 posunuta o 0,98 m k severu (rozložení dávky, kanonický GIS beze změny; rozhodnutí k potvrzení uživatelem); zadní otvory (3 osy, dveře) ±0,5 m podle šikmého snímku shora – hypotéza

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_9_002.jpg | fotografie | 401fa70b7d86 |
| ATO119_10_9_003.jpg | fotografie | 242daf38a57b |
| ATO119_10_9_004.jpg | fotografie | d90e8069ac69 |
| ATO119_10_9_005.jpg | fotografie | f0acd857f49f |
| ATO119_10_9_007.jpg | fotografie | 6e4075f55e93 |
| ATO119_10_9_008.jpg | fotografie | 53e989e34ce0 |
| cp_599,987,988_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | a4fee845b3fd |
| cp_599,987,988_001.jpg | plán / výkres | eaa09a4758cc |
| cp_599,987,988_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | e1e17fbae503 |
| cp_599,987,988_001.jpg | archivní karta | 066ff0cd8f59 |
| cp_599,987,988_001.jpg | fotografie | 03c99af3652f |
| cp_915,987,988_001.jpg | archivní karta | 9e70552bceed |
| cp_915,987,988_001.jpg | fotografie | 8339483d9cac |
| cp_988_001.jpg | archivní karta | 9a734c65e31e |
| cp_988_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 7d90c74a8f6b |
| cp_988_001.jpg | fotografie | b5b5b2aebbd7 |
| cp_988_002.jpg | archivní karta | 26a60b34f934 |
| cp_988_002.jpg | plán / výkres | 165f7f7fad09 |
| cp_988_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 50ad01dc85d5 |
| cp_988_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 5f9a1554bb73 |
| cp_988_002.jpg | fotografie | b1ca76467ddf |
| cp_988_002_col.png | kolorovaná odvozenina | 4327e70e05cd |

### Čp. 1818: dvoupodlažní dům na nároží Jablonského se složenou střechou

> **Upozornění – Částečně hypotéza:** Dům podle snímků ze 70. let; výšky, tvar zadní střechy, jižní vikýř a severní přístavek garáží jsou odhad.

- U náhonu, západní strana, východní cíp „špalíčku“ v ulici B. Jablonského (s 534 na západě), GIS 1616; v Libuši oblast Jablonského (snímky KSSPPOP a ATO ze 70. let)
- Prameny: fotografie ATO119_10_24_122 a _123 (= cp_1818_002), cp_1818_001 a ATO119_10_24_037/_038 (od severu), náčrt střech 1818/5, plány 1933 (jen uhelné kóje), GIS 1616
- Střecha: složená: přední příčná část (hřeben podél U náhonu) se štítem k severu a valbou na JV nároží, zadní část s hřebenem Z–V a valbou na západě (náčrt 1818/5, ATO 122); nové listy cp_1818_01 (1933) kreslí jen uhelné kóje ve dvoře
- GIS budova 1616 (popisek 1818); geometrie revize r1, 424 polygonů.
- Hypotézy: výška okapu 7,3 m a hřebenu 10,4 m z perspektivy bez kótovaného plánu (±0,3 / ±0,8 m); hloubka přední příčné části 6,8 m odhad; zděný vikýř na jižní střeše: poloha a šířka nejisté (dva snímky dávají s 2,8–8,6 a 4,0–10,5 m), modelován ustoupený za okap, 4,5 m široký; severní přízemní přístavek (garáž, býv. obchod, kůlna) není v GIS – rozměry 9,0 × 6,5 × 3,2 m a otvory odhad ze snímků od severu; parapety jižní stěny o 0,5 m níž než východní – čteno z fotografie, příčina (terén?) neověřena; otvory zadní (západní) stěny a dvora nejsou na žádném snímku – bez otvorů; plán cp_1818_01 (25. 1. 1933) uvádí v titulu „Nr. 1816“, poloha ale odpovídá 1818

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_24_037.jpg | fotografie | 6eac0a55b87f |
| ATO119_10_24_038.jpg | fotografie | c6821c0c66ed |
| ATO119_10_24_122.jpg | fotografie | b122441183bc |
| ATO119_10_24_123.jpg | fotografie | c3d76c37dafd |
| cp_1818_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | a852f2dfbba5 |
| cp_1818_001.jpg | fotografie | e1b966b35624 |
| cp_1818_001.jpg | archivní karta | 956b948754fa |
| cp_1818_002.jpg | fotografie | 92a64f009569 |
| cp_1818_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 3c0b27cf3d4c |
| cp_1818_002.jpg | plán / výkres | 24ef55c84d0d |
| cp_1818_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 533e107a3a1f |
| cp_1818_002.jpg | archivní karta | 4d4e5e407a1a |
| cp_1818_002_col.png | kolorovaná odvozenina | 3e1e030da7b7 |
| cp_1818_01.jpg | plán / výkres | 519e3f229ae0 |

### Čp. 431: ruina domu jako vjezd do garážového dvora (stav 70. let)

> **Upozornění – Ruina (stav 70. let):** Model ukazuje stav na jediném snímku ze 70. let: obvodové zdi bez střechy s průjezdem a garážovými vraty. Dům se střechou a podkrovím podle plánu 1922 není modelován.

- U náhonu, západní strana, GIS 1614 (uliční hrana 16,53 m); průchozí parcela k Leninově, v Libuši dnes v oblasti Leninova. Uliční dům byl v 70. letech ruinou bez střechy a sloužil jako vjezd do garážového dvora (karta P6 „Ulice: U náhonu“, náčrt 431/6)
- Prameny: fotografie cp_431_001__2 (průčelí ruiny z U náhonu) a cp_431_003 (dvorní strana), karta P6 a náčrt 431/6, plán 1922 cp_431_06 (stav se střechou – alternativa), GIS 1614
- Střecha: viz plán modelu
- GIS budova 1614 (popisek 431); geometrie revize r1, 124 polygonů.
- Hypotézy: výška zdí 4,4 m a polohy otvorů z fotografie s GIS šířkou 16,53 m (±0,2 m); plán 1922 dává 17,0–17,3 m; dvorní stěna: oblouk průjezdu, dveře a okénko jen ze šikmého snímku cp_431_003 – polohy hypotéza; garážová vrata jsou pozdější vlomení do zdi (před zřícením střechy nebyla); stav před zřícením (podlažnost, střecha, vikýře podle 1922) nemodelován – rozhodnutí uživatele

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_431_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | b4eaccd0e728 |
| cp_431_001.jpg | plán / výkres | c4fbc50b335b |
| cp_431_001.jpg | fotografie | 59ea0422666b |
| cp_431_001.jpg | archivní karta | e07ad3928213 |
| cp_431_001__2.jpg | archivní karta | c4446cc2ce6d |
| cp_431_001__2.jpg | fotografie | 70b7b1d9111b |
| cp_431_002.jpg | fotografie | ef3111efc8cf |
| cp_431_002.jpg | archivní karta | 4efa6bbce28e |
| cp_431_002_col.png | kolorovaná odvozenina | c54805b137fb |
| cp_431_003.jpg | archivní karta | dd155dee70f8 |
| cp_431_003.jpg | fotografie | 149b5e139283 |
| cp_431_01.jpg | plán / výkres | debfc24549b0 |
| cp_431_02.jpg | plán / výkres | 4093163dd0a0 |
| cp_431_03.jpg | plán / výkres | 78cd40680e8e |
| cp_431_04.jpg | plán / výkres | d2126c1465fe |
| cp_431_05.jpg | plán / výkres | 01be74c11a4b |
| cp_431_06.jpg | plán / výkres | e7a5d28710d7 |

### Čp. 606: nárožní dům Na popravišti × U náhonu

- nárožní dům Na popravišti × U náhonu (SV konec řady); štítová stěna do U náhonu se zubořezem a jediným oknem ve štítu
- Prameny: fotografie cp_606_001 (průčelí, 70. léta), cp_550,606_001 a ATO119_10_9_016 (štít do U náhonu), zaměření 606_02 (9. 4. 1941), projekt 606_01 (nerealizován), náčrt 606/5, GIS
- Střecha: sedlová, hřeben podél Na popravišti, štít do U náhonu, na JZ navazuje vyšší 719
- GIS budova 1626 (popisek 606); geometrie revize r1, 207 polygonů.
- Hypotézy: hřeben 12,6 m odvozen z pohledu 606_02 (střecha ≈ 5,7 m nad římsou, ±0,5 m); okno ve štítu jako tmavá výplň na štítové zdi (není vyříznuto); projekt 606_01 (Franz Wiede, nedatováno) s dvojicemi oken a supraportami nerealizován; obchod z let 1921–41 (606_03) v ose 3 už jako okno; komíny ±1 m (průmět na fotografii); volská oka z náčrtu 606/5 na fotografii neověřena – nemodelována; dvorní pavlač, WC, dřevníky nemodelovány

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_550,606_001.jpg | archivní karta | 4cd0dfb6c0d0 |
| cp_550,606_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 3c5a42648767 |
| cp_550,606_001.jpg | fotografie | 657a4c51b9f2 |
| cp_606,719_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | e7726536bfcb |
| cp_606,719_001.jpg | archivní karta | bd7eade0fc24 |
| cp_606,719_001.jpg | fotografie | 90ce0136d7e5 |
| cp_606,719_001_col.png | kolorovaná odvozenina | 6eeb79f474e8 |
| cp_606_001.jpg | archivní karta | 37a332d1b040 |
| cp_606_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 8f8650d1cd88 |
| cp_606_001.jpg | plán / výkres | 697b555caa05 |
| cp_606_001.jpg | fotografie | 2359624f2fc8 |
| cp_606_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | d4c355acee12 |
| cp_606_001__2.jpg | fotografie | 9959f2d48d7e |
| cp_606_001__2.jpg | archivní karta | 8d22aa6330ac |
| cp_606_002.jpg | archivní karta | 9f2b00d3f607 |
| cp_606_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 7657e3b30836 |
| cp_606_002.jpg | fotografie | d01f03f385c4 |
| cp_606_01.jpg | plán / výkres | e4df609485aa |
| cp_606_02.jpg | plán / výkres | 186697143ad6 |
| cp_606_03.jpg | plán / výkres | 7977e85dd5cf |

### Čp. 1886: přízemní domek v hloubce bloku (hypotéza)

> **Upozornění – Hypotéza:** Domek bez GIS půdorysu: poloha a velikost z náčrtu, podoba odhad podle jediného zarostlého snímku.

> **Poznámka k identitě a GIS:** v GIS chybí; poloha a rozměry ≈ 4,6 × 7,1 m z náčrtu (měřítko podle GIS půdorysu 606)

- přízemní domek se zahrádkou v hloubce bloku JV od nárožního 606 (konec U náhonu), podél hranice parcel 606/719; v GIS chybí
- Prameny: náčrt 606/5 („1886 příz. domek“), fotografie cp_1886_001 od zahrady (fasáda zakryta stromy a plotem), karta
- Střecha: viz plán modelu
- GIS budova None (bez čp.); geometrie revize r1, 99 polygonů.
- Hypotézy: celý model je hypotéza: poloha a rozměry z náčrtu ±15 %, strana s okny zvolena (zahradní strana neověřena); výška 1 podlaží (okap 3,2 m) a sedlová střecha podle snímku, sklon odhad; příčná valbová část s mansardovým podkrovím, zádveří, prádelna a kůlny z náčrtu nemodelovány

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1886_001.jpg | archivní karta | 527058038022 |
| cp_1886_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | a087201aad42 |
| cp_1886_001.jpg | fotografie | 4bccba940e98 |

### Čp. 719: dvoupodlažní dům s průjezdem (přestavba 1928)

- řadový dům Na popravišti mezi 606 a 541 s průjezdem (1928); dvorní kovárna 1893
- Prameny: fotografie cp_719_001 (= ATO119_10_9_017), projekt 719_01 (3/1885, W. Wolf; realizován hladce), přestavba 719_04 (1928), kovárna 719_05 (1893), náčrt 719/4, GIS
- Střecha: sedlová podél ulice; hřeben neodečten (rise 4,0 m hypotéza)
- GIS budova 1625 (popisek 719); geometrie revize r1, 211 polygonů.
- Hypotézy: okap 7,8 m odvozen, hřeben 11,8 m hypotéza; polohy otvorů z rektifikace s šířkou 15,70 (±0,15 m); svislá spára s ≈ 11,3 (přestavba 1928) = textura; volská oka z náčrtu 719/4 na uliční fotografii neověřena – nemodelována (na dvorní straně ATO119_10_9_011); dvorní kovárna a kůlny nemodelovány

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_18_063.jpg | fotografie | 1fd91d824474 |
| ATO119_10_9_011.jpg | fotografie | ac8f487804c7 |
| ATO119_10_9_012.jpg | fotografie | 87c8857d7969 |
| ATO119_10_9_014.jpg | fotografie | ee5d4eb77f98 |
| ATO119_10_9_016.jpg | fotografie | 07477bcc5926 |
| ATO119_10_9_017.jpg | fotografie | 85d1b6dabc97 |
| ATO119_10_9_020.jpg | fotografie | 4afc0cf5dd11 |
| ATO119_10_9_022.jpg | fotografie | 72ee94d6665e |
| ATO119_10_9_023.jpg | fotografie | ac931de09602 |
| cp_541,719_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 5d2a74b977b1 |
| cp_541,719_001.jpg | archivní karta | c5b34ec85f0c |
| cp_541,719_001.jpg | fotografie | 287253fd473e |
| cp_606,719_001.jpg | archivní karta | bd7eade0fc24 |
| cp_606,719_001.jpg | fotografie | 90ce0136d7e5 |
| cp_606,719_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | e7726536bfcb |
| cp_606,719_001_col.png | kolorovaná odvozenina | 6eeb79f474e8 |
| cp_719_001.jpg | fotografie | 31da572d7e58 |
| cp_719_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 8639f9e951a2 |
| cp_719_001.jpg | archivní karta | fea263dbdddb |
| cp_719_001.jpg | plán / výkres | d8adf4f0e280 |
| cp_719_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 06a758fffc63 |
| cp_719_002.jpg | archivní karta | fec418d24ea1 |
| cp_719_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 2b0f799bbdd1 |
| cp_719_002.jpg | fotografie | c3d94ea5d618 |
| cp_719_01.jpg | plán / výkres | dbab3cae83b5 |
| cp_719_02.jpg | plán / výkres | 802fcb99e4c5 |
| cp_719_03.jpg | plán / výkres | 126b40d5d62d |
| cp_719_04.jpg | plán / výkres | 3e433a247408 |
| cp_719_05.jpg | plán / výkres | 38f23cfd7ecc |

### Čp. 541: dvoupodlažní dům s průjezdem a téměř plochou střechou

> **Poznámka k identitě a GIS:** GIS dává průčelí 12,15 m; model 12,80 m podle kótovaného plánu

- dvoupodlažní dům Na popravišti mezi 719 a 1065 s průjezdem; dvorní stavby 1927–31 (Orglmeister, Wettstein, Kny) pro Marii Nehtl
- Prameny: fotografie cp_541_001 (= ATO119_10_9_015), plán 541_01 (≈ 1927, Orglmeister), řez 541_06 (9/1930), náčrt 541/3; listy cp_541_04 a _05 jsou plány čp. 719 zařazené u 541
- Střecha: téměř plochá pultová střecha klesající do dvora (náčrt 541/3, řez 1930)
- GIS budova 1624 (popisek 541); geometrie revize r3, 210 polygonů.
- Hypotézy: šířka 12,80 m podle plánu místo GIS 12,15 m – dělicí zeď s 1065 posunuta o 0,65 m; zadní pravá část (GIS do hl. 13,4 m) jako nižší přístavek 5,4 m s pultovou stříškou – výška hypotéza; listy cp_541_04 a 541_05 jsou plány čp. 719 (Kuzebauch 1924) chybně zařazené u 541; komín: poloha podle náčrtu, neověřena

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_18_063.jpg | fotografie | 1fd91d824474 |
| ATO119_10_9_014.jpg | fotografie | ee5d4eb77f98 |
| ATO119_10_9_015.jpg | fotografie | e9f80f1b3b2d |
| cp_541,719_001.jpg | fotografie | 287253fd473e |
| cp_541,719_001.jpg | archivní karta | c5b34ec85f0c |
| cp_541_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 30517481d6a0 |
| cp_541_001.jpg | archivní karta | 1f7be8145616 |
| cp_541_001.jpg | plán / výkres | d14987a921d4 |
| cp_541_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 9bfa1fa7e032 |
| cp_541_001.jpg | fotografie | 6860ef7dc500 |
| cp_541_01.jpg | plán / výkres | 703e9be076ad |
| cp_541_02.jpg | plán / výkres | c92e221d7c48 |
| cp_541_03.jpg | plán / výkres | 184141656988 |
| cp_541_04.jpg | plán / výkres | 714fd56cb780 |
| cp_541_05.jpg | plán / výkres | d653b006d98e |
| cp_541_06.jpg | plán / výkres | 08f861b9bb29 |
| cp_541_07.jpg | plán / výkres | 10de08bf3829 |
| cp_541_08.jpg | plán / výkres | 80371c968dcf |

### Čp. 1065: dvoupodlažní dům se supraportami (1899)

> **Poznámka k identitě a GIS:** GIS dává průčelí 10,06 m; model 9,00 m podle plánu 1899

- dvoupodlažní dům Na popravišti mezi 541 a 1068, novostavba 10/1899 (Franz Weitzdorfer) pro Franze a Annu Maierovy
- Prameny: fotografie cp_1065_001 (čelně), plán 1065_01 (10/1899, F. Weitzdorfer, 1:100), dvorní plány 1908–24, náčrt, GIS
- Střecha: sedlová podél ulice, 2 komíny na hřebeni (1065_01)
- GIS budova 1623 (popisek 1065); geometrie revize r1, 262 polygonů.
- Hypotézy: šířka 9,00 m podle plánu místo GIS 10,06 m – dělicí zdi posunuty (1065 začíná o 0,65 m dál, 1068 o 0,41 m blíž); zazděný obchodní otvor os 3–4 = textura (modelováno jen okno G3); volská oka (projekt 1899, náčrt) a štítový vikýř do dvora (zadní snímek) nemodelovány – na uliční fotografii neověřeny; zadní křídlo jako přízemní přístavek 3,6 m (dvorní stavby 1908–24) – výška hypotéza

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_18_063.jpg | fotografie | 1fd91d824474 |
| ATO119_10_18_064.jpg | fotografie | 5511ced157ee |
| ATO119_10_9_016.jpg | fotografie | 07477bcc5926 |
| ATO119_10_9_018.jpg | fotografie | afe2186a387e |
| ATO119_10_9_021.jpg | fotografie | f350d11e284b |
| ATO119_10_9_023.jpg | fotografie | ac931de09602 |
| cp_1065,1068_001.jpg | fotografie | ea2e07aacfc4 |
| cp_1065,1068_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 9b1b1c9c9336 |
| cp_1065,1068_001.jpg | archivní karta | 05e2028b46fc |
| cp_1065,1068_001_col.png | kolorovaná odvozenina | 819c92ffe37c |
| cp_1065_001.jpg | fotografie | 55d90803a0f3 |
| cp_1065_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | c530a3a32da6 |
| cp_1065_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 936a0daca1f6 |
| cp_1065_001.jpg | plán / výkres | 755a7f8507c2 |
| cp_1065_001.jpg | archivní karta | b4c654f281e0 |
| cp_1065_002.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | fac9667f5ddb |
| cp_1065_002.jpg | fotografie | cf4e2e1844ee |
| cp_1065_002.jpg | archivní karta | bac5e27fadc1 |
| cp_1065_01.jpg | plán / výkres | c2fbb5b43de1 |
| cp_1065_02.jpg | plán / výkres | 7b8956a2ba6c |
| cp_1065_03.jpg | plán / výkres | 49eb91ca5cde |
| cp_1065_04.jpg | plán / výkres | 4328dfbd15c6 |
| cp_1065_05.jpg | plán / výkres | 9554527cc83f |

### Čp. 1068: krajní dům řady s holým štítem

> **Poznámka k identitě a GIS:** GIS dává průčelí 8,44 m; model 9,00 m podle plánu

- krajní dům řady Na popravišti; vpravo (JZ) volný plácek k nároží Pražské (karta 1068)
- Prameny: fotografie cp_1068_001 (od jihozápadu), projekt 1068_01 (12/1899, C. Hinke; neobarokní výzdoba nerealizována), karta, náčrt, GIS
- Střecha: sedlová podél ulice, holý štít k plácku (zubořez)
- GIS budova 1622 (popisek 1068); geometrie revize r1, 214 polygonů.
- Hypotézy: šířka 9,00 m podle plánu (GIS 8,44) – štít o 0,15 m dál do plácku než GIS; okap 8,3 / hřeben 12,05 m odvozeny z profilu projektu (±0,3); zadní přízemní křídlo (kůlny, dřevník, prádelna) 3,0 m – výška hypotéza; volská oka (náčrt) a štítový vikýř do dvora nemodelovány

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| ATO119_10_18_063.jpg | fotografie | 1fd91d824474 |
| ATO119_10_18_064.jpg | fotografie | 5511ced157ee |
| cp_1065,1068_001.jpg | fotografie | ea2e07aacfc4 |
| cp_1065,1068_001.jpg | archivní karta | 05e2028b46fc |
| cp_1065,1068_001.jpg | odvozenina bez tagu (kolorovaná / výřez / FRONT) | 9b1b1c9c9336 |
| cp_1065,1068_001_col.png | kolorovaná odvozenina | 819c92ffe37c |
| cp_1068_001.jpg | archivní karta | 23b06277dec2 |
| cp_1068_001.jpg | plán / výkres | 7f02344485ad |
| cp_1068_001.jpg | fotografie | 48cd73e11f05 |
| cp_1068_01.jpg | plán / výkres | 22fc5e1db810 |
