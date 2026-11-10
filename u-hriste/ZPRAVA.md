# U hřiště (1938 Seligerova): zpráva o 3D modelu ulice a jeho pramenech

Projekt MOST, GRAFIT FIT ČVUT, 26. 10. 2026. Geometrie a stránka: Claude (Anthropic); textury doplňuje Codex. Web: https://grafitctu.github.io/most/u-hriste/

Stav: ve 3D je 36 z 36 modelovaných budov. Model ulice (GLB) je k dispozici.

## Co kde stálo

Poloha všech domů pochází z GIS vrstvy projektu, která je vektorizací historického plánu města Mostu z roku 1938. Ulice v ní vede jako Seligerova (v roce 1964 U hřiště) s 36 budovami: 28 z nich mají číslo popisné (27 různých čísel, čp. 523 má dvě budovy), 8 čísla nemají (dvůr paláce SHD a areál bývalé plynárny). Kliknutím na zelený nebo oranžový dům v mapě otevřete jeho stránku.

Čísla v mapě jsou podle pramenů, ne podle popisků GIS: budova 635 je 574 a budova 634 je 630 (v GIS mají popisky prohozené, viz [Rozpory](#rozpory)). Dílny 413 a a 413 b jsou hypotéza identity na budovách GIS bez čísla. Budovy bez čísla popisného (GIS 1526–1531 v areálu plynárny a GIS 1638) jsou označené „GIS“ a modelované jako hypotézy.

### Úseky ulice
- S1 · jižní strana VSV ramene: 626, 625, 630, 574, 772
- S2 · severozápadní strana VSV ramene: 823, 831, 653, 659, 666, 673, 671
- S3 · bývalá plynárna: 523 a, GIS 1530, 523 b, GIS 1529, GIS 1531, GIS 1527, GIS 1526
- S4 · JZ rameno od Husova náměstí: 1733, 413 a, 413 b, 1313, 410
- S5 · rameno k nám. Dvouletky: 415, 475, 416, 439, 417
- S6 · domy čelem k nám. Dvouletky: 586, 1230, 1186, 1188, 1178, 1192, GIS 1638

### Databázová oblast „U hřiště“ a co modelováno není

Oblast U hřiště v databázi Libuše obsahuje 35 struktur. Dvě zbořené dvorní stavby nemají v GIS půdorys, a proto se nemodelují (blocked):

| Čp. | Proč není modelováno | Přílohy |
|---|---|---|
| 627 | dvorní stavba hostince „Zur Linde“ (772), na skice cp_772_001 vyznačená jako zbořená; v databázi jen plány, v GIS bez půdorysu | 8 |
| 742 | dvorní stavba za 625 a 630, na skicách KSPPOP vyznačená jako zbořená; jeden plán, v GIS bez půdorysu | 1 |

Dalších pět struktur obsahuje jen pohlednice nebo leží podle GIS v jiných ulicích; jejich přílohy jsme načetli a prohlédli, modelovány nejsou:

| Čp. | Poznámka | Ulice podle GIS | Přílohy |
|---|---|---|---|
| 452 | jen pohlednice (sdílené panoramy), není domem této ulice | v GIS není | 2 |
| 459 | jen pohlednice (sdílená), není domem této ulice | v GIS není | 1 |
| 540 | podle GIS v ulicích Gassmanova / Nádražní, jiná ulice | Mánesova (1938 Gassmanova), Nádražní | 2 |
| 552 | pohlednice Václavského a Husova náměstí, mimo rozsah ulice | v GIS není | 2 |
| 740 | podle GIS v ulicích Nádražní / Okružní, jiná ulice | Nádražní, Okružní | 2 |

## Odkud jsou prameny

### Dvě fotografické kampaně

Ulici zachycují dvě kampaně fotodokumentace: „Komplet: Starý Most“ (karty MNV s datem 28. 11. 1967, domy ještě stojí) a fotodokumentace KSPPOP Ústí nad Labem z 60.–70. let (karty s razítkem a skici parcel s čísly sousedních domů; část domů je na nich už zbořena a v prolukách stojí garáže). Cílová epocha modelu jsou 60. léta: pro každý dům používáme snímek z roku 1967 nebo z KSPPOP, na kterém dům ještě stojí. Ručně psané texty karet a skici určují, co snímek ukazuje a kdo jsou sousedé.

### Stavební plány 1871–1940

K většině domů existují stavební plány z let 1871–1940. Pro jižní řadu jsou klíčové pohledy „Ansicht“ 1 : 100 z roku 1931 (starý stav a renovace fasády) pro Brüxer Kohlen-Bergbau-Gesellschaft, které kreslí domy 574, 630, 625 a 626 vedle sebe a dávají jejich výšky. Projekt ale není realizace: u domů 625, 659, 671, 673, 772, 410 a 1733 se plány a fotografie liší a model sleduje fotografii (viz [Rozpory](#rozpory)). Míry na starých listech v sázích převádíme vídeňským sáhem 1,8965 m.

### Databáze Libuše projektu MOST

Seznamy příloh jsme načetli živě 25. 10. 2026, pouze pro čtení (0 zápisů). Oblast U hřiště má 35 struktur a 516 příloh (437 různých souborů podle SHA-256): 130 plánů a výkresů, 113 fotografií, 101 archivních karet, 21 pohlednic, 2 kolorované odvozeniny a 149 příloh bez tagu. Netagované přílohy jsou nízkorozlišené kopie (1920 × 1080, černé okraje) z dřívější duplicitní oblasti, která v databázi živě už neexistuje; u domů 417, 1230, 1186, 1188, 1178 a 1192 jsou jediným obrazovým pramenem fasády. Proti staršímu snímku databáze z 11. září zmizelo 33 struktur s pohlednicemi a přibyla struktura 410. Ze sousední oblasti Náměstí Dvouletky jsme načetli struktury 596, 740 a 1193 (soused domu 1192). Každou přílohu jsme otevřeli; náhledy jsou na stránkách domů a seznam s kontrolními součty SHA-256 je ve [zprávě](ZPRAVA.md).

### Odvozeniny

Kolorované snímky v databázi (u čp. 523) jsou rekonstrukce, ne prameny. O tvaru, otvorech a nápisech rozhoduje původní černobílá fotografie.

### GIS a terén

Polohy, natočení a šířky průčelí jsou z GIS vrstvy (vektorizace plánu 1938, místní souřadnice). Výšky budov v GIS jsou jen náhodný zástupný údaj: výšky domů odhadujeme z plánů a rektifikovaných fotografií. Terén je zatím plochý (výška ulice z = 0 u všech domů), protože jsme pro ulici neotevřeli žádný historický výškopis; je to provizorní hypotéza.

## Jak vznikla geometrie

- **Rešerše plánů.** Nejdříve jsme prohledali databázi stavebních plánů: všech 516 příloh oblasti a 13 příloh sousední oblasti jsme otevřeli na kontaktních listech a listy použité pro geometrii četli v plném rozlišení (titulek, datum, měřítko, uliční nebo dvorní objekt, sousedé). Plány se našly u všech položek dávky.

- **Identita a pořadí domů.** Skici parcel KSPPOP s čísly sousedů a popsané fotografie určují, který dům je který. Tak vyšlo najevo, že GIS má u domů 574 a 630 prohozené popisky a že dílny 413 nemají v GIS vlastní budovu.

- **Fasáda jen z fotografie s domem v rámečku.** Na každém použitém snímku je dům v červeném rámečku a každý otvor má ID (například G pro okna přízemí, U pro okna patra, D pro dveře, DW pro okna vikýřů). Počty otvorů z rámečků kontroluje brána proti plánu modelu; rámečky jsou na stránce každého domu.

- **Rektifikace a měřítko.** Fotografie průčelí jsou rektifikovány na šířku průčelí z GIS. Svislé měřítko dávají plány (řezy a pohledy z let 1881 až 1932), jinde odhad podle dveří a podlaží. Kde se projekt liší od realizace, model sleduje fotografii.

- **Střecha.** Silueta střechy je z fotografie, výšky z řezu nebo pohledu; střecha hotového modelu se změří ze sítě a porovná s pramenem.

- **Stavba v Blenderu.** Parametrický builder bez okna (`build_house_20261025.py`, odvozený z builderu Rudolfovy a Kulové) vyrobí z `geometry_plan.json` BLEND a GLB. Otvory jsou skutečné niky, vikýře otevírají krytinu, materiály jsou jen ID pro pozdější textury.

- **Kontrola.** Brána geometrie (prosvítání podkroví paprsky, nekryté zdivo, střecha nad prázdnem, UV, síť, počty otvorů) a vizuální kontrola: pohledy s materiály a bez barev (čtyři strany, čtyři rohy shora, dva podhledy u okapu, shora), detaily otvorů a záznam kontroly. Dům se do ulice umístí až po prošlé bráně a prohlédnuté sadě.

- **Sestava ulice.** Registr `street_layout_gis.json` drží polohu, natočení a revizi každého domu (rámec X = východ, Y = sever); domy, které ještě nejsou hotové, zastupují v sestavě šedé bloky z GIS.

Pracovní složka: F:\MOST\output\u_hriste_street_claude_2026-10-25\ (domy, kontroly, registr poloh; prameny jen ke čtení).

## Rozpory a hypotézy

- **574 a 630: prohozené popisky v GIS.** GIS budovy 634 a 635 nesou popisky 574 a 630, ale čtyři skici KSPPOP (574, 630, 625/626, 772) i popsané fotografie dávají od ulice pořadí 772 | 574 | 630 | 625 | 626: na fotografii 574 je vpravo obloukový průjezd 630, na fotografii 630 je vlevo 574. Budova 635 je proto 574 (dveře vlevo, tři vikýře) a budova 634 je 630 (obloukový průjezd vlevo). Rozhodl uživatel 25. 10. 2026: podle pramenů. Kanonický GIS ani registr poloh se nemění.

- **413: dílny bez budovy v GIS (hypotéza identity).** Struktura 413 (dvorní kotelna a dílny, fotografie z 28. 11. 1967 a KSPPOP) nemá v GIS budovu s tímto číslem. Skica parcel ji klade do dvora mezi palác 1733 a ulici, kde GIS vede dvě budovy bez čísla (1113 a 1114). Modelujeme je jako 413 a a 413 b se štítkem „hypotéza identity“ (rozhodnutí uživatele 25. 10. 2026).

- **523: bývalá plynárna, doložená jen zčásti.** GIS vede pod čp. 523 dvě budovy. Fotografie dokládají jen část fasád: delší budova 1136 je na snímku asi v délce 26 m z 36,7 m a její přiřazení je hypotéza. Obě budovy nesou štítek „částečně hypotéza“. Další budovy ulice bez čísla (v areálu plynárny 1529, 1530, 1531 a kruhové 1526 a 1527, snad plynojemy; dále 1638) jsou jen šedý kontext.

- **772: dva projekty, realizace neodpovídá přesně žádnému.** Pro Franze Siegla existují projekty z let 1885 (nárožní dům s pěti osami) a 1890 (čtyři osy, vrata pod třetí osou, tři vikýře). Fotografie odpovídá rozvrhu z roku 1890, ale všechny osy patra jsou dvojice oken, nad nimi je atikový vlys s okénky a vikýře chybějí. Model sleduje fotografii.

- **823 a 831: dvě čísla, jedna fasáda.** Karta KSPPOP popisuje 831–823 jako dvojdům se společnou fasádou a vchodem. Hranici domů určuje svod na rektifikované fotografii, asi 0,2 m od hranice parcel v GIS; společný vchod patří do 831.

- **439 a 417: chalupy u trhu.** GIS je vede pod Seligerovou, ale na chalupě 439 visí v 60. letech cedule ulice Na dobytčím trhu. Plán z roku 1911 u čp. 439 zobrazuje dvorní sklad s garážemi, ne chalupu. U 417 existují jen nízkorozlišené kopie fotografií; dřevem obložený štít může patřit domu, nebo stáji z roku 1923 (štítek „částečně hypotéza“).

- **Domy čelem k nám. Dvouletky (S6).** GIS vede domy 586 až 1192 pod Seligerovou, skici KSPPOP ale ukazují, že průčelím hledí na náměstí Dvouletky. U 1230, 1186, 1188, 1178 a 1192 existují jen netagované kopie fotografií 1920 × 1080 z dřívější duplicitní oblasti, originály chybějí; všechny nesou štítek „částečně hypotéza“. Dům 586 má původní fotografie.

- **410, 653 a 1733: plán a realizace.** Projekt nástavby patra u 410 (Stockwerksaufbau) nebyl proveden, fotografie z roku 1975 ukazují dvě podlaží a pět vikýřů. U 653 vysvětluje plán z roku 1932 třetí řadu oken: je v nastavené uliční stěně s pokoji v podkroví, takže průčelí (11,0 m) je vyšší než zadní okap (8,4 m). Palác 1733 má na pohlednici stejné členění jako projekt z roku 1930, ale jiné proporce; model drží osy z pohlednice a výšky podlaží z projektu.

- **Plynárna bez čísel popisných: stav kolem 1938.** GIS plán 1938 zakresluje v areálu plynárny dva kruhové plynojemy a provozní budovy bez čísla popisného. Na žádost uživatele (26. 10. 2026) jsou domodelované jako výslovné hypotézy: plynojem 2150 m³ (budova GIS 1526) podle plánu firmy N. Rella & Neffe z roku 1903, plynojem 800 m³ (GIS 1527) podle nádrže z roku 1872, budovy GIS 1529 a 1531 jen jako objemy podle půdorysu. Karta KSPPOP ale uvádí, že plynárna byla za války zříceninou a potom zbořena – v 60. letech tu tyto stavby pravděpodobně už nestály, proto nesou štítek „hypotéza – stav kolem 1938“. Malá budova GIS 1530 u vjezdu je pracovně vrátnice, kterou fotografie 60. let ukazují; dvorní stavba GIS 1638 u nám. Dvouletky nemá žádný pramen.

- **627 a 742: zbořené dvorní stavby.** Na skicách KSPPOP jsou vyznačené jako zbořené a v GIS nemají půdorys; nemodelují se (blocked).

- **Výšky a terén.** Výšky podlaží, říms a střech jsou odhady z rektifikací a plánů. Terén je plochý (z = 0), protože historický výškopis ulice nebyl k dispozici; je to provizorní hypotéza.

- **Dvorní a nedoložené strany** jsou bez otvorů, pokud je žádný pramen neukazuje.

Údaje jsou v datech označené jako `model_hypothesis`, `status: provisional`, `locked: false`.

## Kniha nesouladů pramenů

Případy, kdy si prameny odporují (plán proti fotografii, GIS proti skice, kopie místo originálu), zapisujeme do interní knihy nesouladů pramenů projektu MOST. Ta se zatím nepublikuje, proto zde uvádíme jen identifikátory případů této ulice (11):
- `2026-10-25_u-hriste_1733-projekt-1930-vs-realizace` – U hřiště 1733: palác SHD – projekt 1930 má jiné proporce než realizace na pohlednici
- `2026-10-25_u-hriste_410-nastavba-nerealizovana` – U hřiště 410: projekt nástavby patra (Stockwerksaufbau) se neuskutečnil – fotografie 1975 ukazují dvě podlaží
- `2026-10-25_u-hriste_413-dilny-bez-gis` – U hřiště 413: dílny ve dvoře SHD mají fotografie i skicu, ale v GIS nemají budovu s tímto čp.
- `2026-10-25_u-hriste_439-417-chalupy-trh` – U hřiště 439 a 417: chalupy nesou ceduli „Ul. Na dobytčím trhu“ a plány u jejich čísel patří dvorním stavbám
- `2026-10-25_u-hriste_574-630-gis-popisky` – U hřiště 574 a 630: GIS má u dvou sousedních domů prohozené popisky čísel popisných
- `2026-10-25_u-hriste_653-nastavba-1932` – U hřiště 653: nastavený uliční štít s pokoji v podkroví (1932) – průčelí vyšší než zadní okap
- `2026-10-25_u-hriste_772-dva-projekty` – U hřiště 772: dva projekty pro téhož stavebníka (1885 a 1890), realizace odpovídá žádnému z nich přesně
- `2026-10-25_u-hriste_823-831-dvojdum` – U hřiště 823 a 831: dvě čísla popisná, jedna fasáda – hranici domů prozradí jen svod a GIS
- `2026-10-25_u-hriste_nizke-strechy-sparka-stitu` – Metodika: u nízkých střech proklouznou šikmé paprsky 1 cm spárou mezi štítem a krytinou
- `2026-10-25_u-hriste_plynarna-epocha-1938` – U hřiště, areál plynárny: budovy GIS bez čp. jsou stav kolem 1938 – v 60. letech už plynárna nestála
- `2026-10-25_u-hriste_s6-jen-kopie-nizkeho-rozliseni` – U hřiště, nám. Dvouletky (1230, 1186, 1188, 1178, 1192, 417): fotografie jen jako netagované kopie 1920×1080

## Přehled domů

| Čp. | Úsek | Typ | Štítek | Podlaží | Průčelí × okap (m) | Revize | Přílohy | Stav / textury |
|---|---|---|---|---|---|---|---|---|
| 626 | S1 | řadový patrový dům v ohybu ulice | – | 2 | 8,5 × 8,4 | r2 | 28 | zatím bez textur |
| 625 | S1 | řadový patrový dům | – | 2 | 8,9 × 8,4 | r2 | 26 | zatím bez textur |
| 630 | S1 | patrový dům s obloukovým průjezdem a třemi vikýři | – | 2 + vikýře | 9,1 × 8,9 | r3 | 14 | zatím bez textur |
| 574 | S1 | patrový dům se třemi vikýři | – | 2 + vikýře | 9,9 × 8,3 | r3 | 21 | zatím bez textur |
| 772 | S1 | bývalý hostinec „Zur Linde“ na konci řady | – | 2 + atikový vlys | 18,5 × 9,2 | r1 | 20 | zatím bez textur |
| 823 | S2 | nárožní dům dvojdomu 823 | 831 | – | 2 | 9,2 × 7,5 | r2 | 12 | zatím bez textur |
| 831 | S2 | pravá polovina dvojdomu 823 | 831 | – | 2 | 10,5 × 7,5 | r1 | 8 | zatím bez textur |
| 653 | S2 | dům s nikou se sochou a nastaveným uličním štítem | – | 2 + pokoj v nastaveném štítu | 9,5 × 11,0 | r4 | 12 | zatím bez textur |
| 659 | S2 | patrový dům podle plánu z roku 1882 | – | 2 | 10,3 × 8,6 | r3 | 9 | zatím bez textur |
| 666 | S2 | nízký patrový dům | – | 2 | 9,4 × 7,6 | r1 | 18 | zatím bez textur |
| 673 | S2 | patrový dům s modernizovanou fasádou | – | 2 | 10,5 × 7,3 | r1 | 8 | zatím bez textur |
| 671 | S2 | dvoupatrový dům na konci řady | – | 3 | 17,2 × 11,8 | r2 | 25 | zatím bez textur |
| 523 a | S3 | budova bývalé plynárny podél ulice u 772 | částečně hypotéza | 1 (okna pod okapem) | 21,6 × 5,8 | r2 | 47 | bez textur (částečně hypotéza – jen prosté materiály) |
| GIS 1530 | S3 | malá budova u vjezdu do plynárny (pracovně vrátnice) | hypotéza podle GIS | 1 (hypotéza) | 14,8 × 3,0 | r3 | 0 | bez textur (částečně hypotéza – jen prosté materiály) |
| 523 b | S3 | dlouhá přízemní budova bývalé plynárny | částečně hypotéza | 1 | 36,7 × 5,0 | r2 | 47 | bez textur (částečně hypotéza – jen prosté materiály) |
| GIS 1529 | S3 | dlouhá provozní budova plynárny podél ulice | hypotéza – stav kolem 1938 | 1 (hypotéza) | 43,5 × 5,5 | r1 | 0 | bez textur (částečně hypotéza – jen prosté materiály) |
| GIS 1531 | S3 | provozní budova ve dvoře plynárny | hypotéza – stav kolem 1938 | 1 (hypotéza) | 23,1 × 6,0 | r1 | 0 | bez textur (částečně hypotéza – jen prosté materiály) |
| GIS 1527 | S3 | plynojem 800 m³ (1872) | hypotéza – stav kolem 1938 | – | 16,0 × 6,8 | r1 | 0 | bez textur (částečně hypotéza – jen prosté materiály) |
| GIS 1526 | S3 | plynojem 2150 m³ (projekt 1903) | hypotéza – stav kolem 1938 | – | 17,3 × 11,3 | r1 | 0 | bez textur (částečně hypotéza – jen prosté materiály) |
| 1733 | S4 | správní budova Brüxer Kohlen-Bergbau-Gesellschaft (palác SHD) | – | 4 + atika | 38,8 × 16,4 | r2 | 31 | zatím bez textur |
| 413 a | S4 | dílna ve dvoře SHD (struktura 413) | hypotéza identity | 1 | 11,1 × 3,6 | r1 | 23 | bez textur (částečně hypotéza – jen prosté materiály) |
| 413 b | S4 | dílna / garáž ve dvoře SHD (struktura 413) | hypotéza identity | 1 | 8,4 × 3,5 | r4 | 23 | bez textur (částečně hypotéza – jen prosté materiály) |
| 1313 | S4 | kino (Kinematographen-Theater Franze Gutha) | – | 1 + promítací věž | 20,5 × 4,3 | r3 | 17 | zatím bez textur |
| 410 | S4 | velký patrový dům na Husově náměstí | – | 2 + vikýře | 18,7 × 9,5 | r1 | 18 | zatím bez textur |
| 415 | S5 | dvoupatrový dům se čtyřmi osami a frontony | – | 3 | 12,0 × 11,3 | r1 | 36 | zatím bez textur |
| 475 | S5 | úzký dvoupatrový dům s obchodem | – | 3 | 7,5 × 11,0 | r1 | 23 | zatím bez textur |
| 416 | S5 | vyšší dvoupatrový dům s frontony a zubořezem | – | 3 (vyvýšené přízemí) | 10,4 × 13,1 | r2 | 23 | zatím bez textur |
| 439 | S5 | přízemní chalupa s cedulí „Ul. Na dobytčím trhu“ | – | 1 | 13,6 × 3,2 | r1 | 25 | zatím bez textur |
| 417 | S5 | malá chalupa (Ziegelgasse, plán 1892) | částečně hypotéza | 1 | 5,0 × 2,3 | r1 | 7 | bez textur (částečně hypotéza – jen prosté materiály) |
| 586 | S6 | přízemní dům za zahradní zdí na nároží k U hřiště | – | 1 | 19,1 × 3,6 | r1 | 18 | zatím bez textur |
| 1230 | S6 | patrový dům se středním rizalitem a zakřiveným štítem | částečně hypotéza | 2 | 10,2 × 8,9 | r3 | 4 | bez textur (částečně hypotéza – jen prosté materiály) |
| 1186 | S6 | patrový dům se dvěma vikýři | částečně hypotéza | 2 + vikýře | 10,6 × 8,7 | r2 | 5 | bez textur (částečně hypotéza – jen prosté materiály) |
| 1188 | S6 | patrový dům se zkoseným nárožím | částečně hypotéza | 2 | 9,1 × 7,5 | r2 | 7 | bez textur (částečně hypotéza – jen prosté materiály) |
| 1178 | S6 | patrový dům s atikovým štítem | částečně hypotéza | 2 | 10,8 × 7,7 | r2 | 6 | bez textur (částečně hypotéza – jen prosté materiály) |
| 1192 | S6 | patrový dům s arkýřem a věžičkou | částečně hypotéza | 2 | 12,7 × 8,0 | r2 | 7 | bez textur (částečně hypotéza – jen prosté materiály) |
| GIS 1638 | S6 | dvorní stavba bez čp. u nám. Dvouletky | hypotéza podle GIS | 1 (hypotéza) | 21,4 × 3,2 | r1 | 0 | bez textur (částečně hypotéza – jen prosté materiály) |

## Domy jednotlivě

### Čp. 626: řadový patrový dům v ohybu ulice

- Krajní dům jižní řady u ohybu ulice. Skica KSPPOP (625 | 626, vpravo kino 1313), popisky na fotografii z roku 1967 i GIS budova 632 s popiskem 626 se shodují. Na fotografii má tři zabedněná okna v přízemí, dveře vpravo a čtyři okna v patře; jihozápadní štít je holý.
- Prameny: skica KSPPOP cp_626_001, fotografie cp_625,626_003 a cp_626_002 (karta P2-1), Ansicht alter Bestand 1931 (cp_574_007, 1 : 100) pro výšky, GIS půdorys 632
- Střecha: společná sedlová střecha s 625 bez vikýřů, štít k vyššímu 630, obnažený jihozápadní štít
- GIS budova 632 (popisek 626); geometrie revize r2, 190 polygonů.
- Hypotézy: zabedněná okna přízemí jsou modelována jako okna, bednění patří do textury; výšky (okap 8,4 m, hřeben 12,6 m) jsou převzaty z Ansicht 1931; jihozápadní štít je bez otvorů podle fotografie cp_626_002; dvorní průčelí je bez otvorů (nedoloženo)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_625,626_001.jpg | archivní karta | 73d60025b21f |
| cp_625,626_001.jpg | plán / výkres | 293c10b0e1f0 |
| cp_625,626_001.jpg | kopie bez tagu (1920 × 1080) | 649fa291ffb8 |
| cp_625,626_001.jpg | fotografie | 44ced66b73c3 |
| cp_625,626_002.jpg | fotografie | 6120a7c8dacc |
| cp_625,626_002.jpg | kopie bez tagu (1920 × 1080) | 03c378303338 |
| cp_625,626_002.jpg | archivní karta | 6c4a0784a217 |
| cp_625,626_002_01.jpg | plán / výkres | 9dd428e26797 |
| cp_625,626_002_02.jpg | plán / výkres | e1cca88f29f7 |
| cp_625,626_003.jpg | kopie bez tagu (1920 × 1080) | 56203a814dc1 |
| cp_625,626_003.jpg | plán / výkres | 650609e1579a |
| cp_625,626_003.jpg | archivní karta | 2ebd95fb0666 |
| cp_625,626_003.jpg | fotografie | 03df5632a9bb |
| cp_625,626_003.jpg | kopie bez tagu (1920 × 1080) | fc7477bf2404 |
| cp_625,626_003__2.jpg | plán / výkres | 84b1c8d26791 |
| cp_625,626_004.jpg | fotografie | dc220270cf59 |
| cp_625,626_004.jpg | plán / výkres | a254e229e633 |
| cp_625,626_004.jpg | archivní karta | fc4624ff3ebb |
| cp_625,626_004.jpg | kopie bez tagu (1920 × 1080) | 57aa29515d56 |
| cp_625,626_005.jpg | plán / výkres | edccb2289560 |
| cp_626_001.jpg | plán / výkres | a2cfae20d42c |
| cp_626_001.jpg | kopie bez tagu (1920 × 1080) | 20521c0026e0 |
| cp_626_001.jpg | fotografie | 77f636464cce |
| cp_626_001.jpg | archivní karta | af5b0c5ea0fc |
| cp_626_001.jpg | kopie bez tagu (1920 × 1080) | dcc66293ed40 |
| cp_626_002.jpg | fotografie | 3b5414b829fe |
| cp_626_002.jpg | kopie bez tagu (1920 × 1080) | a3177145570e |
| cp_626_002.jpg | archivní karta | 35b2af3ef251 |

### Čp. 625: řadový patrový dům

- Dům mezi 630 a 626: pořadí 630 | 625 | 626 dává skica KSPPOP i popisky na fotografii, GIS budova 633 s popiskem 625 souhlasí. Na fotografii z 60. let má dveře vlevo u 630, tři okna v přízemí a čtyři v patře. Ansicht z roku 1931 kreslí ve druhé ose výkladní dveře, fotografie tam ukazuje okno.
- Prameny: skica KSPPOP cp_625,626_003, fotografie cp_625,626_003, Ansicht 1931 (levá polovina dvojice 625 | 626), GIS půdorys 633
- Střecha: společná sedlová střecha s 626 bez vikýřů, štít k vyššímu 630
- GIS budova 633 (popisek 625); geometrie revize r2, 185 polygonů.
- Hypotézy: výšky jsou převzaty z Ansicht 1931; fotografie ukazuje shodný okap a kordonovou římsu asi o 0,4 m níž (nejisté); poloha komínu je odhadnuta z perspektivy fotografie; dvorní průčelí je bez otvorů; dvorní fotografie cp_625_001/002 jsou jen orientační

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_625,626_001.jpg | plán / výkres | 293c10b0e1f0 |
| cp_625,626_001.jpg | archivní karta | 73d60025b21f |
| cp_625,626_001.jpg | fotografie | 44ced66b73c3 |
| cp_625,626_001.jpg | kopie bez tagu (1920 × 1080) | 649fa291ffb8 |
| cp_625,626_002.jpg | archivní karta | 6c4a0784a217 |
| cp_625,626_002.jpg | fotografie | 6120a7c8dacc |
| cp_625,626_002.jpg | kopie bez tagu (1920 × 1080) | 03c378303338 |
| cp_625,626_002_01.jpg | plán / výkres | 9dd428e26797 |
| cp_625,626_002_02.jpg | plán / výkres | e1cca88f29f7 |
| cp_625,626_003.jpg | archivní karta | 2ebd95fb0666 |
| cp_625,626_003.jpg | fotografie | 03df5632a9bb |
| cp_625,626_003.jpg | plán / výkres | 650609e1579a |
| cp_625,626_003.jpg | kopie bez tagu (1920 × 1080) | 56203a814dc1 |
| cp_625,626_003.jpg | kopie bez tagu (1920 × 1080) | fc7477bf2404 |
| cp_625,626_003__2.jpg | plán / výkres | 84b1c8d26791 |
| cp_625,626_004.jpg | plán / výkres | a254e229e633 |
| cp_625,626_004.jpg | fotografie | dc220270cf59 |
| cp_625,626_004.jpg | archivní karta | fc4624ff3ebb |
| cp_625,626_004.jpg | kopie bez tagu (1920 × 1080) | 57aa29515d56 |
| cp_625,626_005.jpg | plán / výkres | edccb2289560 |
| cp_625_001.jpg | archivní karta | 82112663bf3d |
| cp_625_001.jpg | kopie bez tagu (1920 × 1080) | a47ec4580c08 |
| cp_625_001.jpg | fotografie | 289e0681a6a4 |
| cp_625_002.jpg | kopie bez tagu (1920 × 1080) | dd19b8d7d8df |
| cp_625_002.jpg | fotografie | 46d1098cd2c5 |
| cp_625_002.jpg | archivní karta | 5415087a6322 |

### Čp. 630: patrový dům s obloukovým průjezdem a třemi vikýři

> **Poznámka k identitě a GIS:** GIS má u tohoto domu popisek 574: popisky 574 a 630 jsou v GIS u sousedních budov 634 a 635 prohozené. Model se řídí prameny (skici KSPPOP a popsané fotografie): 635 = 574, 634 = 630, rozhodnutí uživatele 25. 10. 2026. Kanonický GIS ani registr poloh se nemění.

- Skici KSPPOP (cp_630_001, cp_574_001, cp_625,626_003) a fotografie domu 574, na které je vpravo vidět obloukový průjezd, dávají od ulice pořadí 772 | 574 | 630 | 625 | 626. GIS budova 634 je proto 630, přestože nese popisek 574. Fotografie (karta P4) ukazuje obloukový průjezd vlevo, v přízemí 2 + 1 okna, v patře 1 + 2 + 1 a tři vikýře se segmentovým záklenkem, prostřední dvojitý.
- Prameny: fotografie cp_630_001 (karta P4, rektifikovaná 9,06 × 8,93 m), skici KSPPOP cp_630_001, cp_574_001 a cp_625,626_003, Ansicht alter Bestand 1931 (cp_574_007), GIS půdorys 634
- Střecha: sedlová střecha s hřebenem podél ulice (Ansicht 1931, hřeben 13,9 m), vyšší než 574 a 625, takže štíty nad sousedy jsou obnažené
- GIS budova 634 (popisek 574); geometrie revize r3, 437 polygonů.
- Hypotézy: šířka 9,06 m je podle GIS; Ansicht 1931 dává podle měřítka 9,35–9,64 m; spodní část oken vikýřů zakrývá římsa (fotografie zdola); poloha a výška komínu jsou odhad, na fotografii ani na Ansicht nejsou vidět; sklepní okénka v soklu patří do textury; dvorní průčelí je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_630,674_001.jpg | fotografie | 8e148f38f3b5 |
| cp_630,674_001.jpg | kopie bez tagu (1920 × 1080) | 6d3fa74c2649 |
| cp_630,674_001.jpg | archivní karta | 158812a9e19c |
| cp_630_001.jpg | archivní karta | 55df15a63656 |
| cp_630_001.jpg | kopie bez tagu (1920 × 1080) | d210e997eec4 |
| cp_630_001.jpg | fotografie | 62e3410e64b9 |
| cp_630_001.jpg | plán / výkres | ed447c5fcae5 |
| cp_630_001.jpg | kopie bez tagu (1920 × 1080) | 73f80fc564e0 |
| cp_630_001__2.jpg | plán / výkres | dd4149c2e139 |
| cp_630_002.jpg | fotografie | 778f38612a76 |
| cp_630_002.jpg | kopie bez tagu (1920 × 1080) | 12978909554a |
| cp_630_002.jpg | archivní karta | b50d657be61e |
| cp_630_002.jpg | plán / výkres | 438d90be7d48 |
| cp_630_003.jpg | plán / výkres | 46cbfb9cf408 |

### Čp. 574: patrový dům se třemi vikýři

> **Poznámka k identitě a GIS:** GIS má u tohoto domu popisek 630: popisky 574 a 630 jsou v GIS u sousedních budov 634 a 635 prohozené. Model se řídí prameny (skici KSPPOP a popsané fotografie): 635 = 574, 634 = 630, rozhodnutí uživatele 25. 10. 2026. Kanonický GIS ani registr poloh se nemění.

- Podle skic KSPPOP a popsaných fotografií (pořadí od ulice 772 | 574 | 630 | 625 | 626) je GIS budova 635 domem 574, přestože nese popisek 630. Fotografie (karta P5) ukazuje dveře vlevo, v přízemí 2 + 1 okna, v patře 1 + 2 + 1 a tři vikýře, prostřední dvojitý; vpravo je vidět obloukový průjezd domu 630. Plán Wenzla Pampla kreslí 574 a 630 jako jeden dělitelný dům široký 19 m; Ansicht k renovaci fasády z roku 1931 odpovídá fotografii.
- Prameny: fotografie cp_574_001 (karta P5, rektifikovaná 9,94 × 8,35 m), skici KSPPOP cp_574_001, cp_630_001, cp_625,626_003 a cp_772_001, plán W. Pampla (cp_574_001__2: šířka 19,00 m, hloubka 12,70 m, podlaží 3,80 / 3,75 m), Ansicht 1931 (1 : 100), GIS půdorys 635
- Střecha: sedlová střecha se štíty k sousedům 772 a 630, hřeben 12,8 m podle Ansicht alter Bestand 1931
- GIS budova 635 (popisek 630); geometrie revize r3, 287 polygonů.
- Hypotézy: výška římsy 8,35 m je z rektifikace fotografie při šířce 9,94 m; projekt uvádí 9,5–9,7 m, model sleduje realizaci; hřeben 12,8 m je změřen na Ansicht 1931, z fotografie není vidět; komín vpředu u levého vikýře je z fotografie, jeho výška (13,0 m) je odhad; dvorní průčelí je bez otvorů; dvorní fotografie cp_574_002/003 jsou jen orientační; sklepní okénka, lizény a rámy oken patří do textury

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_574_001.jpg | kopie bez tagu (1920 × 1080) | 247065d01bbd |
| cp_574_001.jpg | fotografie | 9dd3e565fd0b |
| cp_574_001.jpg | archivní karta | a8dfbb522038 |
| cp_574_001.jpg | plán / výkres | 19d065129d6f |
| cp_574_001.jpg | kopie bez tagu (1920 × 1080) | 0eb7ed6597f9 |
| cp_574_001__2.jpg | plán / výkres | fc37920ba7d6 |
| cp_574_002.jpg | archivní karta | 6e6719d7652f |
| cp_574_002.jpg | kopie bez tagu (1920 × 1080) | 2b3443775e15 |
| cp_574_002.jpg | plán / výkres | 0a675baa7b20 |
| cp_574_002.jpg | fotografie | 4187e781ea55 |
| cp_574_003.jpg | plán / výkres | de3fb197863f |
| cp_574_003.jpg | archivní karta | 73fb0e57d0b4 |
| cp_574_003.jpg | fotografie | f57672c28551 |
| cp_574_003.jpg | kopie bez tagu (1920 × 1080) | a8132564c591 |
| cp_574_004.jpg | archivní karta | 0ac108f1c449 |
| cp_574_004.jpg | plán / výkres | 9c5743ec58f7 |
| cp_574_004.jpg | kopie bez tagu (1920 × 1080) | 781cfe175103 |
| cp_574_004.jpg | fotografie | 057ec9aa4bbf |
| cp_574_005.jpg | plán / výkres | 20ccabee56db |
| cp_574_006.jpg | plán / výkres | 00bed354ab17 |
| cp_574_007.jpg | plán / výkres | a4647131699b |

### Čp. 772: bývalý hostinec „Zur Linde“ na konci řady

- Patrový dům na volném východním konci jižní řady. Skica KSPPOP (772 | 574), situace projektu z roku 1885 (novostavba Siegl | 574 | 630 | 625) i GIS budova 636 s popiskem 772 se shodují. Pro Franze Siegla existují dva projekty, z let 1885 a 1890; fotografie odpovídá rozvrhu z roku 1890, ale všechny čtyři osy patra jsou dvojice oken, nad nimi je atikový vlys s okénky a vikýře chybějí.
- Prameny: fotografie cp_772_001 (karta P6, rektifikovaná 18,51 m), plán 1890 (cp_627,772_002, 1 : 100) pro svislé měřítko, projekt 1885 (cp_627,772_004) se situací sousedů, skica KSPPOP cp_772_001, dvorní fotografie cp_772_003/004, GIS půdorys 636
- Střecha: valba k volnému východnímu konci, štít k nižšímu 574, bez vikýřů (projekt 1890 měl tři vikýře; nerealizováno nebo později odstraněno)
- GIS budova 636 (popisek 772); geometrie revize r1, 654 polygonů.
- Hypotézy: svislé měřítko je z plánu 1890 (výšky oken), ne přímo z fotografie; vzepětí hřebene 4,3 m a sklon střechy jsou odhad, na fotografii je střecha zkrácená; polohy konzol římsy jsou z fotografie přibližné; segmentové frontony nad prostředními páry oken jsou modelovány jako jeden fronton nad párem; zadní křídlo má podle GIS půdorysu stejnou výšku jako hlavní dům; dvorní fotografie jsou jen orientační; boční východní fasáda je bez otvorů, není doložena; bosáž přízemí, vlys a šambrány patří do textury

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_627,772_001.jpg | plán / výkres | c801eb6a7628 |
| cp_627,772_002.jpg | plán / výkres | c04425e0a615 |
| cp_627,772_003.jpg | plán / výkres | 0500352167c8 |
| cp_627,772_004.jpg | plán / výkres | 15a0bd04ff88 |
| cp_627,772_005.jpg | plán / výkres | b90cb15773a1 |
| cp_627,772_006.jpg | plán / výkres | e59aec7a25fe |
| cp_772_001.jpg | archivní karta | e5bdc169c8df |
| cp_772_001.jpg | plán / výkres | 6b3c4c32ca81 |
| cp_772_001.jpg | kopie bez tagu (1920 × 1080) | fec7f941253e |
| cp_772_001.jpg | fotografie | 770c73ed817a |
| cp_772_001.jpg | kopie bez tagu (1920 × 1080) | b4c0443bedc6 |
| cp_772_002.jpg | archivní karta | 84c701080977 |
| cp_772_002.jpg | kopie bez tagu (1920 × 1080) | 96c8e5d15cc5 |
| cp_772_002.jpg | fotografie | 8ed8019d5d02 |
| cp_772_003.jpg | fotografie | 8d4937cc3f59 |
| cp_772_003.jpg | kopie bez tagu (1920 × 1080) | 1291d3dfd5a6 |
| cp_772_003.jpg | archivní karta | 1a6f8cf48ee5 |
| cp_772_004.jpg | fotografie | 5bd19932ff9c |
| cp_772_004.jpg | kopie bez tagu (1920 × 1080) | ee809fc9ea5a |
| cp_772_004.jpg | archivní karta | eabc309dbd68 |

### Čp. 823: nárožní dům dvojdomu 823 | 831

- Nárožní dům u odbočky ramene k nám. Dvouletky. Karta KSPPOP popisuje 831–823 jako dvojdům se společnou fasádou a vchodem; skica (586 | 823 roh | 831) i GIS budova 1121 s popiskem 823 souhlasí. Hranici obou domů na společné fasádě určuje svod (asi 0,2 m od hranice parcel v GIS); společný vchod hned vpravo od svodu patří do 831. Projekt z 30. let ukazuje jiné rozmístění otvorů, model se drží fotografie.
- Prameny: fotografie cp_831_002 (celá fasáda dvojdomu, rektifikovaná 19,67 m), fotografie boční fasády cp_823_001 (10,35 m), fotografie cp_823,671_001 a cp_586,823_001, skica KSPPOP cp_823_001, karta cp_831_002, plán Tusl z 30. let (řez, Rückansicht), GIS půdorys 1121
- Střecha: valbová střecha nad nárožím, hřeben podél ulice pokračuje nad 831; sklon asi 36° podle řezu plánu Tusl (provizorně)
- GIS budova 1121 (popisek 823); geometrie revize r2, 256 polygonů.
- Hypotézy: výška okapu 7,45 m a hřebene 11,35 m je z rektifikace obou fasád, svislé měřítko je odhad; zazděný otvor v boční fasádě patří do textury (lícuje s omítkou), není modelován jako otvor; poloha komínu na dělicí zdi s 831 je odvozena z perspektivy dvou fotografií; dvorní průčelí je bez otvorů; Rückansicht plánu je jen orientační; bosáž přízemí, nadokenní římsy patra a nápis „…EL“ v pásu patří do textury

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_586,823_001.jpg | kopie bez tagu (1920 × 1080) | a29675292eac |
| cp_586,823_001.jpg | fotografie | 0816ed4d134d |
| cp_586,823_001.jpg | archivní karta | d96645e711f7 |
| cp_823,671_001.jpg | fotografie | 5b5c32c06362 |
| cp_823,671_001.jpg | kopie bez tagu (1920 × 1080) | af74a3a8ac4f |
| cp_823,671_001.jpg | archivní karta | 8eb35b578bce |
| cp_823_001.jpg | plán / výkres | 5961eb47ead8 |
| cp_823_001.jpg | kopie bez tagu (1920 × 1080) | 9e0457b7f1d8 |
| cp_823_001.jpg | archivní karta | 152d808a1d02 |
| cp_823_001.jpg | fotografie | ee009dcebd93 |
| cp_823_001.jpg | kopie bez tagu (1920 × 1080) | 4fe3751a43b1 |
| cp_823_001__2.jpg | plán / výkres | 62009b6c1bf6 |

### Čp. 831: pravá polovina dvojdomu 823 | 831

- Dům mezi 823 a 653 (skica KSPPOP 823 | 831 | 653, GIS budova 1122 s popiskem 831). Se sousedním 823 má společnou fasádu; na fotografii je v přízemí společný vchod u svodu, okno a rozšířené výkladní okno, v patře čtyři okna a vpravo asi 2,2 m slepé zdi u 653.
- Prameny: fotografie cp_831_002 (rektifikovaná 19,67 m pro celý dvojdům), fotografie dvora cp_831_001, skica a karta KSPPOP cp_831_002, GIS půdorys 1122
- Střecha: sedlová střecha společná s 823, vpravo štít a požární zeď k vyššímu 653
- GIS budova 1122 (popisek 831); geometrie revize r1, 173 polygonů.
- Hypotézy: výška okapu a hřebene je převzata z 823 (společná fasáda, provizorně); výkladní okno G2 je stav 60.–70. let (rozbité, rozšířené), původní okna nejsou známa; dvorní průčelí je bez otvorů; fotografie dvora je jen orientační; bosáž přízemí patří do textury

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_831_001.jpg | fotografie | 50b1afb153c2 |
| cp_831_001.jpg | archivní karta | 9cfad74c6d0c |
| cp_831_001.jpg | kopie bez tagu (1920 × 1080) | 3748a60911b6 |
| cp_831_002.jpg | plán / výkres | c6484d6b1df2 |
| cp_831_002.jpg | kopie bez tagu (1920 × 1080) | 5f3582af06b4 |
| cp_831_002.jpg | fotografie | f75131fd3eeb |
| cp_831_002.jpg | kopie bez tagu (1920 × 1080) | 87d8bebe05af |
| cp_831_002.jpg | archivní karta | fd4f1a0068bc |

### Čp. 653: dům s nikou se sochou a nastaveným uličním štítem

- Dům mezi 831 a 659 (skica KSPPOP 831 | 653 | 659, GIS budova 1123 s popiskem 653); plány z let 1931 a 1932 nesou adresu Nr. 653 Seligerstraße. Fotografie ukazuje v přízemí zabedněné okno, portál se třemi schody a dvě okna, v 1. patře dvě okna, niku se sochou a dvě okna, nahoře dvě okna v nastaveném uličním štítu.
- Prameny: fotografie cp_653_001 (rektifikovaná 9,51 × 11,0 m), plány 1931 a 1932 (cp_653_001__2, 002–004; řez 1932 s podlažími 3,30 / 3,30 m), skica KSPPOP cp_653_001, GIS půdorys 1123
- Střecha: podle plánu 1932 (cp_653_004) nastavený uliční štít s pokojem v podkroví (Dachzimmer), nízký přední sklon k hřebeni a strmý zadní sklon k římse 1. patra; z ulice střecha není vidět
- GIS budova 1123 (popisek 653); geometrie revize r4, 263 polygonů.
- Hypotézy: přední výška 11,0 m je z rektifikace při šířce GIS 9,51 m (svislé měřítko ±0,4 m); zadní okap 8,4 m a hřeben 11,9 m jsou z řezu 1932, měřítko listu je odhad; socha v nice patří do textury, samostatně není modelována; sklepní okénka patří do textury; dvorní průčelí je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_653_001.jpg | kopie bez tagu (1920 × 1080) | 8dd20df3789d |
| cp_653_001.jpg | plán / výkres | 972f13b88a2f |
| cp_653_001.jpg | archivní karta | 795a94cf3f62 |
| cp_653_001.jpg | kopie bez tagu (1920 × 1080) | ee5d6f151460 |
| cp_653_001.jpg | fotografie | 0c55b155ee82 |
| cp_653_001__2.jpg | plán / výkres | 74b239278278 |
| cp_653_002.jpg | plán / výkres | 9e2beab6894b |
| cp_653_003.jpg | plán / výkres | 11415f9e3437 |
| cp_653_004.jpg | plán / výkres | 21afeede3fc9 |
| cp_659,653_001.jpg | kopie bez tagu (1920 × 1080) | 3727282b7a97 |
| cp_659,653_001.jpg | archivní karta | bbe4a0ddb8b5 |
| cp_659,653_001.jpg | fotografie | 7180bc4d75a7 |

### Čp. 659: patrový dům podle plánu z roku 1882

- Dům mezi 653 a 666 (skica KSPPOP 653 | 659 | 666, GIS budova 1124 s popiskem 659). Fotografie odpovídá pohledu z plánu 1882: v přízemí pár oken, dveře se dvěma schody a pár zazděných oken, v patře pár, jedno okno a pár.
- Prameny: fotografie cp_659_001 a cp_659,653_001 (rektifikace 10,62 × 8,55 m), plán 1882 (cp_659_001__2: 8,55 m k hlavní římse, podlaží 3,45 m), skica KSPPOP cp_659_001, GIS půdorys 1124
- Střecha: sedlová střecha s hřebenem podél ulice, vzepětí asi 4,2 m (plán 1882); vikýřové okénko z pohledu 1882 na fotografii 60.–70. let není, proto není modelováno
- GIS budova 1124 (popisek 659); geometrie revize r3, 224 polygonů.
- Hypotézy: zazděná okna G3 a G4 jsou modelována jako otvory, zazdívka patří do textury; polohy komínů jsou z fotografie, výšky jsou odhad; sklepní okénka patří do textury; šířka je přední hrana GIS 10,35 m (plán 10,00–10,23 m)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_659,653_001.jpg | fotografie | 7180bc4d75a7 |
| cp_659,653_001.jpg | archivní karta | bbe4a0ddb8b5 |
| cp_659,653_001.jpg | kopie bez tagu (1920 × 1080) | 3727282b7a97 |
| cp_659_001.jpg | kopie bez tagu (1920 × 1080) | eaefc4e408fc |
| cp_659_001.jpg | fotografie | 2ff231935c0b |
| cp_659_001.jpg | kopie bez tagu (1920 × 1080) | b74645f685e6 |
| cp_659_001.jpg | plán / výkres | 9516c0d52a87 |
| cp_659_001.jpg | archivní karta | 86dda2047e88 |
| cp_659_001__2.jpg | plán / výkres | 6726f46a2649 |

### Čp. 666: nízký patrový dům

- Dům mezi 659 a 673 (skica KSPPOP 659 | 666 | 673, GIS budova 1132 s popiskem 666). Na fotografii má v přízemí pár oken, dveře a pár oken, v patře pár, jedno okno a pár.
- Prameny: fotografie cp_666_001 (rektifikovaná 9,44 × 7,6 m), skica KSPPOP cp_666_001, GIS půdorys 1132
- Střecha: nízká sedlová střecha s hřebenem podél ulice, bez vikýřů (fotografie)
- GIS budova 1132 (popisek 666); geometrie revize r1, 217 polygonů.
- Hypotézy: výška okapu 7,6 m je z rektifikace (svislé měřítko ±0,4 m); vzepětí střechy 3,9 m je odhad; sklepní okénka patří do textury; dvorní průčelí je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_666_001.jpg | kopie bez tagu (1920 × 1080) | 4d172eb8f620 |
| cp_666_001.jpg | kopie bez tagu (1920 × 1080) | 225af9d8a119 |
| cp_666_001.jpg | fotografie | 8005355f413e |
| cp_666_001.jpg | plán / výkres | 6714238b11ab |
| cp_666_001.jpg | archivní karta | f6629c839aa8 |
| cp_666_001__2.jpg | plán / výkres | e0344d3d8bdd |
| cp_666_002.jpg | fotografie | ae0d31bf9afe |
| cp_666_002.jpg | kopie bez tagu (1920 × 1080) | 37c6497373eb |
| cp_666_002.jpg | archivní karta | a25c9d7fb518 |
| cp_666_003.jpg | kopie bez tagu (1920 × 1080) | 99b0193486df |
| cp_666_003.jpg | fotografie | d1f40fb4e3d9 |
| cp_666_003.jpg | archivní karta | 12de442e2331 |
| cp_666_004.jpg | kopie bez tagu (1920 × 1080) | 14f394a95b1e |
| cp_666_004.jpg | fotografie | 556357415c6c |
| cp_666_004.jpg | archivní karta | 5dfbac3b0997 |
| cp_666_005.jpg | fotografie | 77fe815c0831 |
| cp_666_005.jpg | kopie bez tagu (1920 × 1080) | e0c75caf162d |
| cp_666_005.jpg | archivní karta | bab2c5c66e4a |

### Čp. 673: patrový dům s modernizovanou fasádou

- Dům mezi 666 a 671 (skica KSPPOP 666 | 673 | 671, GIS budova 1133 s popiskem 673). Fotografie ukazuje hladkou modernizovanou fasádu: v přízemí okno, dveře a okno, v patře dvě široká okna a okénko. Plán J. Lienerta z roku 1883 a skica J. Herdy z roku 1934 zachycují starší stav a pro fasádu použity nejsou.
- Prameny: fotografie cp_673_001 (rektifikovaná 10,49 × 7,3 m), skica KSPPOP cp_673_001, GIS půdorys 1133; plány 1883 a 1934 jen pro srovnání
- Střecha: sedlová střecha s hřebenem podél ulice (fotografie)
- GIS budova 1133 (popisek 673); geometrie revize r1, 146 polygonů.
- Hypotézy: výška okapu 7,3 m je z rektifikace (svislé měřítko nejisté); vzepětí střechy 3,6 m je odhad; dvorní průčelí je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_673_001.jpg | plán / výkres | 02d6a796af95 |
| cp_673_001.jpg | kopie bez tagu (1920 × 1080) | 2d45bdaf3bb4 |
| cp_673_001.jpg | kopie bez tagu (1920 × 1080) | 8db548b2961e |
| cp_673_001.jpg | fotografie | b191c939fe77 |
| cp_673_001.jpg | archivní karta | 60dd52cd16dc |
| cp_673_001__2.jpg | plán / výkres | ad22d1ab123f |
| cp_673_002.jpg | plán / výkres | 292cc8c7e8e4 |
| cp_673_003.jpg | plán / výkres | 890c9d9310f8 |

### Čp. 671: dvoupatrový dům na konci řady

- Poslední dům severozápadní řady (skica KSPPOP 673 | 671, GIS budova 1134 s popiskem 671); k domu patří plány Roberta Nacheho (Tischlerwerkstätte, Gasgasse). Fotografie ukazují šest os: v přízemí dveře vlevo a pět oken s mřížemi, ve dvou patrech po šesti oknech a atikový pás s malovaným nápisem. Na severovýchodní boční stěně jsou u nároží dvě osy ve třech řadách a za svodem a komínem tři osy v horních řadách.
- Prameny: fotografie cp_671_001 a cp_671_002 (rektifikovaná 17,24 × 11,8 m), plán 1881 (cp_671_003: výška 11,80 m, Profil), plány R. Nacheho, skica KSPPOP cp_671_001, GIS půdorys 1134
- Střecha: nízká sedlová střecha podle Profilu 1881, z ulice není vidět; štíty na bočních stěnách
- GIS budova 1134 (popisek 671); geometrie revize r2, 485 polygonů.
- Hypotézy: rektifikace šikmého snímku má svislou nejistotu ±0,3 m; plán 1881 měl rovnoměrné osy po 2,85 m, model sleduje realizaci podle fotografie; polohy bočních oken jsou ze šikmého snímku odhadnuty; vzepětí střechy 2,6 m je z Profilu 1881; schodišťový rizalit vzadu je z GIS, jeho výška je hypotéza; malovaný nápis v atikovém pásu patří do textury

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_671_001.jpg | archivní karta | 882dc41389c5 |
| cp_671_001.jpg | kopie bez tagu (1920 × 1080) | 6f7d2c442e58 |
| cp_671_001.jpg | kopie bez tagu (1920 × 1080) | c62eb171fe52 |
| cp_671_001.jpg | plán / výkres | 8463f52eb7ef |
| cp_671_001.jpg | fotografie | 145b28605ce8 |
| cp_671_001__2.jpg | plán / výkres | d3b9c7e6ab3d |
| cp_671_002.jpg | kopie bez tagu (1920 × 1080) | 8b61ac7f586d |
| cp_671_002.jpg | plán / výkres | 7ece844c976f |
| cp_671_002.jpg | fotografie | 39eb3c04dd09 |
| cp_671_002.jpg | archivní karta | a37d41bf6b99 |
| cp_671_003.jpg | fotografie | ad0122dcc115 |
| cp_671_003.jpg | kopie bez tagu (1920 × 1080) | d4de47c6745b |
| cp_671_003.jpg | archivní karta | 497da586b5d7 |
| cp_671_003.jpg | plán / výkres | addb422af2e2 |
| cp_671_004.jpg | fotografie | 88affd3ab342 |
| cp_671_004.jpg | kopie bez tagu (1920 × 1080) | 7d1e32b4db69 |
| cp_671_004.jpg | archivní karta | 86a0e3c4710e |
| cp_671_004.jpg | plán / výkres | 7e47514bbfc2 |
| cp_671_005.jpg | plán / výkres | f8316062d40c |
| cp_671_006.jpg | plán / výkres | 7378818c75ad |
| cp_671_007.jpg | plán / výkres | 8741b4a4addc |
| cp_671_008.jpg | plán / výkres | 4ad61f75582b |
| cp_823,671_001.jpg | archivní karta | 8eb35b578bce |
| cp_823,671_001.jpg | kopie bez tagu (1920 × 1080) | af74a3a8ac4f |
| cp_823,671_001.jpg | fotografie | 5b5c32c06362 |

### Čp. 523 a: budova bývalé plynárny podél ulice u 772

> **Upozornění – částečně hypotéza:** Jen část domu je doložena fotografií; zbytek je odvozen z plánu nebo ze sousedního domu.

- Karta KSPPOP popisuje stavení na pozemku bývalé plynárny při pohledu z ulice, vpravo se štítem domu 772; skica ukazuje dlouhou budovu podél U hřiště u 772. GIS vede pod čp. 523 dvě budovy, tato odpovídá budově 1135. Fotografie ukazuje pásová okna v přízemí, malá okna pod okapem a plochý štít na severovýchodním konci.
- Prameny: karta a skica KSPPOP cp_523_002, fotografie cp_523_002 (projektivní fit podle výšky stěny na obou koncích), GIS půdorys 1135
- Střecha: nízká sedlová střecha se štíty, vzepětí 1,8 m je odhad
- GIS budova 1135 (popisek 523); geometrie revize r2, 200 polygonů.
- Hypotézy: délka fasády je podle GIS 21,55 m, okap 5,8 m podle měřítka na blízkém rohu; zahradní zeď před severovýchodní částí není modelována; štít u 772 na fotografii patří zadnímu křídlu domu 772 (podle karty)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_523_001.jpg | plán / výkres | e29d58fcdd7c |
| cp_523_001.jpg | fotografie | 5cae12868a0d |
| cp_523_001.jpg | kopie bez tagu (1920 × 1080) | 6b0be886c54a |
| cp_523_001.jpg | archivní karta | 6b2a8b2c384d |
| cp_523_001_col.png | kolorovaná odvozenina | 63dcb3eba179 |
| cp_523_001_col_clean.png | kolorovaná odvozenina | 1141f66aae91 |
| cp_523_002.jpg | plán / výkres | 4b184ad5d1e4 |
| cp_523_002.jpg | kopie bez tagu (1920 × 1080) | 9c9602917890 |
| cp_523_002.jpg | kopie bez tagu (1920 × 1080) | 5da009b5bc5a |
| cp_523_002.jpg | fotografie | 966e0b41040f |
| cp_523_002.jpg | archivní karta | 5e822ead6dbb |
| cp_523_002__2.jpg | plán / výkres | a2220fce3fdc |
| cp_523_003.jpg | fotografie | cd1a47742da3 |
| cp_523_003.jpg | plán / výkres | f3ee3d71c602 |
| cp_523_003.jpg | archivní karta | c68fee22fe27 |
| cp_523_003.jpg | kopie bez tagu (1920 × 1080) | af426d4580d2 |
| cp_523_004.jpg | plán / výkres | 811f3636e277 |
| cp_523_004.jpg | kopie bez tagu (1920 × 1080) | 5427abbcd17c |
| cp_523_004.jpg | fotografie | 1ed03a57ad00 |
| cp_523_004.jpg | archivní karta | c40f45b3d6b4 |
| cp_523_005.jpg | archivní karta | 9f245d9a68ff |
| cp_523_005.jpg | kopie bez tagu (1920 × 1080) | 7a6fe6267e30 |
| cp_523_005.jpg | plán / výkres | 1ab15d0fb05c |
| cp_523_005.jpg | fotografie | c69563038b3e |
| cp_523_006.jpg | kopie bez tagu (1920 × 1080) | 312126eb167d |
| cp_523_006.jpg | archivní karta | d33ef11d1a2f |
| cp_523_006.jpg | fotografie | e220dd1c2b9a |
| cp_523_006.jpg | plán / výkres | 4b81bf2b10ce |
| cp_523_007.jpg | fotografie | 493768e0b479 |
| cp_523_007.jpg | plán / výkres | 0aa279d924c7 |
| cp_523_007.jpg | archivní karta | d7bfdd0090bb |
| cp_523_007.jpg | kopie bez tagu (1920 × 1080) | 3ae7e38eea0f |
| cp_523_008.jpg | archivní karta | 9888b9fb3422 |
| cp_523_008.jpg | plán / výkres | cf9533bf2e08 |
| cp_523_008.jpg | fotografie | c19810ecf908 |
| cp_523_008.jpg | kopie bez tagu (1920 × 1080) | 83904c2fc2bb |
| cp_523_009.jpg | plán / výkres | 92df64c6cda7 |
| cp_523_009.jpg | archivní karta | f872a562e8e6 |
| cp_523_009.jpg | kopie bez tagu (1920 × 1080) | d940a97a06eb |
| cp_523_009.jpg | fotografie | 8533a60c6285 |
| cp_523_010.jpg | fotografie | f1032b7991de |
| cp_523_010.jpg | plán / výkres | 6b217ed473dd |
| cp_523_010.jpg | kopie bez tagu (1920 × 1080) | 315afa02bceb |
| cp_523_010.jpg | archivní karta | edeb51d4ff12 |
| cp_523_011.jpg | plán / výkres | 5a3c427f5634 |
| cp_523_012.jpg | plán / výkres | 2db6e61ff22b |
| cp_523_013.jpg | plán / výkres | cf69cc83c2a8 |

### Budova GIS 1530 (bez čp.): malá budova u vjezdu do plynárny (pracovně vrátnice)

> **Upozornění – hypotéza podle GIS:** Malá budova bez čísla popisného u vjezdu do bývalé plynárny podle GIS plánu 1938, pracovně vrátnice. Fotografie KSPPOP ukazuje bok vrátnice, ale její přiřazení k této budově GIS ani orientace nejsou jisté. Výška a střecha jsou odhad, otvory nemodelovány.

- Malá budova bez čísla popisného u ulice mezi 523 a a 523 b, jen v GIS plánu 1938. Karty KSPPOP (cp_523_007, cp_523_009) zmiňují vjezdovou vrátnici, kterou v 60.–70. letech používaly Státní statky; fotografie cp_523_009 ukazuje její bok. Přiřazení vrátnice k této budově GIS je hypotéza.
- Prameny: GIS půdorys 1530; fotografie a karta KSPPOP cp_523_009 (bok vjezdové vrátnice ze strany plynárny)
- Střecha: nízká sedlová střecha (vzepětí 0,9 m) podle fotografie
- GIS budova 1530 (bez čp.); geometrie revize r3, 86 polygonů.
- Hypotézy: přiřazení k vrátnici je hypotéza; orientace fotografie k budově není určena, otvory proto nejsou modelovány; výška 3,0 m je odhad

### Čp. 523 b: dlouhá přízemní budova bývalé plynárny

> **Upozornění – částečně hypotéza:** Jen část domu je doložena fotografií; zbytek je odvozen z plánu nebo ze sousedního domu.

- Fotografie KSPPOP ze struktury 523 ukazuje dlouhou přízemní budovu bývalé plynárny s vraty se segmentovým záklenkem, segmentovými okny a druhými dveřmi. Přiřazení k druhé GIS budově čp. 523 (1136, fasáda 36,7 m) je hypotéza: snímek zachycuje jen asi 26 m fasády.
- Prameny: fotografie cp_523_003 (projektivní fit), GIS půdorys 1136
- Střecha: nízká sedlová střecha se štíty, vzepětí 2,2 m je odhad
- GIS budova 1136 (popisek 523); geometrie revize r2, 288 polygonů.
- Hypotézy: viditelná délka asi 25,7 m při okapu 5,0 m; zbytek fasády budovy GIS 1136 (asi 26–36 m) je bez doložení a bez otvorů; zadní křídlo budovy GIS 1136 má stejnou výšku

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_523_001.jpg | plán / výkres | e29d58fcdd7c |
| cp_523_001.jpg | fotografie | 5cae12868a0d |
| cp_523_001.jpg | kopie bez tagu (1920 × 1080) | 6b0be886c54a |
| cp_523_001.jpg | archivní karta | 6b2a8b2c384d |
| cp_523_001_col.png | kolorovaná odvozenina | 63dcb3eba179 |
| cp_523_001_col_clean.png | kolorovaná odvozenina | 1141f66aae91 |
| cp_523_002.jpg | plán / výkres | 4b184ad5d1e4 |
| cp_523_002.jpg | kopie bez tagu (1920 × 1080) | 9c9602917890 |
| cp_523_002.jpg | kopie bez tagu (1920 × 1080) | 5da009b5bc5a |
| cp_523_002.jpg | fotografie | 966e0b41040f |
| cp_523_002.jpg | archivní karta | 5e822ead6dbb |
| cp_523_002__2.jpg | plán / výkres | a2220fce3fdc |
| cp_523_003.jpg | fotografie | cd1a47742da3 |
| cp_523_003.jpg | plán / výkres | f3ee3d71c602 |
| cp_523_003.jpg | archivní karta | c68fee22fe27 |
| cp_523_003.jpg | kopie bez tagu (1920 × 1080) | af426d4580d2 |
| cp_523_004.jpg | plán / výkres | 811f3636e277 |
| cp_523_004.jpg | kopie bez tagu (1920 × 1080) | 5427abbcd17c |
| cp_523_004.jpg | fotografie | 1ed03a57ad00 |
| cp_523_004.jpg | archivní karta | c40f45b3d6b4 |
| cp_523_005.jpg | archivní karta | 9f245d9a68ff |
| cp_523_005.jpg | kopie bez tagu (1920 × 1080) | 7a6fe6267e30 |
| cp_523_005.jpg | plán / výkres | 1ab15d0fb05c |
| cp_523_005.jpg | fotografie | c69563038b3e |
| cp_523_006.jpg | kopie bez tagu (1920 × 1080) | 312126eb167d |
| cp_523_006.jpg | archivní karta | d33ef11d1a2f |
| cp_523_006.jpg | fotografie | e220dd1c2b9a |
| cp_523_006.jpg | plán / výkres | 4b81bf2b10ce |
| cp_523_007.jpg | fotografie | 493768e0b479 |
| cp_523_007.jpg | plán / výkres | 0aa279d924c7 |
| cp_523_007.jpg | archivní karta | d7bfdd0090bb |
| cp_523_007.jpg | kopie bez tagu (1920 × 1080) | 3ae7e38eea0f |
| cp_523_008.jpg | archivní karta | 9888b9fb3422 |
| cp_523_008.jpg | plán / výkres | cf9533bf2e08 |
| cp_523_008.jpg | fotografie | c19810ecf908 |
| cp_523_008.jpg | kopie bez tagu (1920 × 1080) | 83904c2fc2bb |
| cp_523_009.jpg | plán / výkres | 92df64c6cda7 |
| cp_523_009.jpg | archivní karta | f872a562e8e6 |
| cp_523_009.jpg | kopie bez tagu (1920 × 1080) | d940a97a06eb |
| cp_523_009.jpg | fotografie | 8533a60c6285 |
| cp_523_010.jpg | fotografie | f1032b7991de |
| cp_523_010.jpg | plán / výkres | 6b217ed473dd |
| cp_523_010.jpg | kopie bez tagu (1920 × 1080) | 315afa02bceb |
| cp_523_010.jpg | archivní karta | edeb51d4ff12 |
| cp_523_011.jpg | plán / výkres | 5a3c427f5634 |
| cp_523_012.jpg | plán / výkres | 2db6e61ff22b |
| cp_523_013.jpg | plán / výkres | cf69cc83c2a8 |

### Budova GIS 1529 (bez čp.): dlouhá provozní budova plynárny podél ulice

> **Upozornění – hypotéza – stav kolem 1938:** Budova bez čísla popisného v areálu bývalé plynárny jen podle GIS plánu 1938; fotografie ani plán k ní nebyly nalezeny. Plynárna byla po válce zbořena, v 60. letech tu budova pravděpodobně nestála. Výška a střecha jsou odhad, otvory nemodelovány.

- Areál bývalé plynárny (Gasanstalt / städtisches Gaswerk, Gasgasse). Budova nemá číslo popisné, je jen v GIS plánu 1938. Podle karty KSPPOP u snímku cp_523_003 byla plynárna za války zříceninou a potom zbořena, fotografie 60.–70. let ukazují volný dvůr – jde tedy o stav kolem roku 1938, ne o 60. léta. Na Lageplanu z roku 1945 odpovídá dlouhé stupňovité budově podél ulice.
- Prameny: GIS půdorys 1529, Lageplan 1945 (cp_523_010); typově plány provozních budov plynárny (cp_523_012 z roku 1872, cp_523_003 z roku 1892)
- Střecha: sedlová střecha, vzepětí 2,5 m – odhad
- GIS budova 1529 (bez čp.); geometrie revize r1, 65 polygonů.
- Hypotézy: výška 5,5 m a střecha jsou odhad podle typu provozních budov; otvory nejsou modelovány (žádná fotografie); drobný schod půdorysu GIS je vynechán

### Budova GIS 1531 (bez čp.): provozní budova ve dvoře plynárny

> **Upozornění – hypotéza – stav kolem 1938:** Budova bez čísla popisného v areálu bývalé plynárny jen podle GIS plánu 1938; fotografie ani plán k ní nebyly nalezeny. Plynárna byla po válce zbořena, v 60. letech tu budova pravděpodobně nestála. Výška a střecha jsou odhad, otvory nemodelovány.

- Areál bývalé plynárny (Gasanstalt / städtisches Gaswerk, Gasgasse). Budova nemá číslo popisné, je jen v GIS plánu 1938. Podle karty KSPPOP u snímku cp_523_003 byla plynárna za války zříceninou a potom zbořena, fotografie 60.–70. let ukazují volný dvůr – jde tedy o stav kolem roku 1938, ne o 60. léta.
- Prameny: GIS půdorys 1531, Lageplan 1945 (cp_523_010)
- Střecha: sedlová střecha, vzepětí 3,0 m – odhad
- GIS budova 1531 (bez čp.); geometrie revize r1, 50 polygonů.
- Hypotézy: výška 6,0 m a střecha jsou odhad; otvory nejsou modelovány (žádná fotografie)

### Budova GIS 1527 (bez čp.): plynojem 800 m³ (1872)

> **Upozornění – hypotéza – stav kolem 1938:** Plynojem bývalé plynárny podle GIS plánu 1938 a stavebního plánu. Podle karty KSPPOP byla plynárna za války zříceninou a potom zbořena – v 60. letech tu plynojem pravděpodobně už nestál. Poloha zvonu, výška a vodicí konstrukce jsou odhad.

- Areál bývalé plynárny (Gasanstalt / städtisches Gaswerk, Gasgasse). Budova nemá číslo popisné, je jen v GIS plánu 1938. Podle karty KSPPOP u snímku cp_523_003 byla plynárna za války zříceninou a potom zbořena, fotografie 60.–70. let ukazují volný dvůr – jde tedy o stav kolem roku 1938, ne o 60. léta. Kruh GIS 1527 (průměr 16,0 m) je starší plynojem 800 m³, který plán z roku 1903 uvádí jako stávající, blíž k ulici.
- Prameny: plán nádrže „Gaasometer Bassein“ (komise 14. 6. 1872, příloha cp_523_006): průměr 46 vídeňských stop = 14,54 m, hloubka 4,95 m; situační plán plynárny 1872 (cp_523_007); situace 1903 (cp_523_005); GIS půdorys 1527
- Střecha: kopulovitá koruna zvonu (odhad 0,6 m)
- GIS budova 1527 (bez čp.); geometrie revize r1, 769 polygonů.
- Hypotézy: zvon a vodicí konstrukce (8 sloupů do 6,2 m) jsou typová hypotéza – plán zvonu z roku 1872 nebyl nalezen; v 60. letech plynojem pravděpodobně už nestál

### Budova GIS 1526 (bez čp.): plynojem 2150 m³ (projekt 1903)

> **Upozornění – hypotéza – stav kolem 1938:** Plynojem bývalé plynárny podle GIS plánu 1938 a stavebního plánu. Podle karty KSPPOP byla plynárna za války zříceninou a potom zbořena – v 60. letech tu plynojem pravděpodobně už nestál. Poloha zvonu, výška a vodicí konstrukce jsou odhad.

- Areál bývalé plynárny (Gasanstalt / städtisches Gaswerk, Gasgasse). Budova nemá číslo popisné, je jen v GIS plánu 1938. Podle karty KSPPOP u snímku cp_523_003 byla plynárna za války zříceninou a potom zbořena, fotografie 60.–70. let ukazují volný dvůr – jde tedy o stav kolem roku 1938, ne o 60. léta. Kruh GIS 1526 (průměr 17,3 m) odpovídá projektovanému teleskopickému plynojemu 2150 m³ z roku 1903: na situaci plánu leží dál od ulice než starší plynojem.
- Prameny: plán teleskopického plynojemu 2150 m³ pro Imperial Continental Gas Association (N. Rella & Neffe, Vídeň, 20. 2. 1903, příloha cp_523_005 u čp. 523): zvon 16,0 m, nádrž 16,92 m, koruna 0,76 m, 12 příhradových sloupů vodicí konstrukce; Lageplan plynárny z února 1945 (cp_523_010); GIS půdorys 1526
- Střecha: kopulovitá koruna zvonu (vzepětí 0,76 m podle plánu)
- GIS budova 1526 (bez čp.); geometrie revize r1, 841 polygonů.
- Hypotézy: zvon je zobrazen v poloze s jednou vysunutou sekcí – skutečná poloha se měnila podle zásoby plynu; výška vodicí konstrukce (asi 10,7 m nad okrajem nádrže) je odečtena z plánu 1 : 50; příhradování sloupů a diagonály patří do textury; v 60. letech plynojem pravděpodobně už nestál

### Čp. 1733: správní budova Brüxer Kohlen-Bergbau-Gesellschaft (palác SHD)

- Velká správní budova mezi Husovým náměstím, Nádražní a U hřiště (GIS budova 1112 s popiskem 1733). Plány „Verwaltungsgebäude“ Brüxer Kohlen-Bergbau-Gesellschaft (Lossow & Kühne, 1930) a pohlednice ukazují 11 os, obloukově zaklenutá okna přízemí, portál se třemi poli, balkon ve 3. podlaží přes pět středních os a vyvýšenou atiku s pěti kruhovými okny.
- Prameny: pohlednice P-000114 (realizace) a P-000018, P-000073, P-000237, P-000584, Hauptansicht 1930 (cp_1733_004, 1 : 100: podlaží 4,35 / 4,05 / 4,05 / 3,60 m, římsa 16,4 m, atika 18,0 m), Ansicht Bahnhofstraße (cp_1733_002: 7 os ve 4 podlažích), plány cp_1733_005–007, fotografie cp_410,1733_001 (1975), GIS půdorys 1112
- Střecha: plochá nebo nízká valbová střecha za atikou (pohlednice), v modelu nízká valba 1,2 m, která sleduje šikmou západní stěnu půdorysu
- GIS budova 1112 (popisek 1733); geometrie revize r2, 1237 polygonů.
- Hypotézy: šířka os 3,15 m je z pohlednice; projekt 1930 má užší osy, model sleduje realizaci; kruhová okna atiky, sochy a nadokenní římsy patří do textury; zadní a dvorní strany jsou bez otvorů (půdorysy z plánů nepoužity); atika je modelována jako předsazený blok ve výšce 15,9–18,0 m; východní strana k U hřiště (dvůr SHD) je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| P-000018.jpg | pohlednice | 42b170ae334c |
| P-000018__2.jpg | pohlednice | 3538117aa864 |
| P-000073.jpg | pohlednice | e06f0132735c |
| P-000073__2.jpg | pohlednice | 3a530ec0e7ef |
| P-000114.jpg | pohlednice | dbe60e55323d |
| P-000114__2.jpg | pohlednice | dd94593d90d2 |
| P-000237.jpg | pohlednice | 85fa118efea5 |
| P-000237__2.jpg | pohlednice | dcc99c653b73 |
| P-000584.jpg | pohlednice | 02c4e61bda0a |
| P-000587.jpg | pohlednice | facc05031402 |
| cp_1733_001.jpg | plán / výkres | 00131abf0a9c |
| cp_1733_001.jpg | archivní karta | e4064a9c40bd |
| cp_1733_002.jpg | archivní karta | bfea5a35a094 |
| cp_1733_002.jpg | plán / výkres | bdc75c3c5b19 |
| cp_1733_003.jpg | plán / výkres | 5b962e4da48a |
| cp_1733_004.jpg | plán / výkres | 0dd7c4e9ec63 |
| cp_1733_005.jpg | plán / výkres | 3532fa47faa0 |
| cp_1733_006.jpg | plán / výkres | 880036396b8a |
| cp_1733_007.jpg | plán / výkres | 873027e897a2 |
| cp_1733_008.jpg | plán / výkres | 340a0620f247 |
| cp_410,1733_001.jpg | fotografie | 4f98a0a15944 |
| cp_510,1733_001.jpg | archivní karta | 30ffd852f320 |
| cp_510,542,1733,592,594,614_001.jpg | fotografie | b6b5325db019 |
| cp_510,542,1733_001.jpg | archivní karta | fe017291d418 |
| cp_510,542,1733_001__2.jpg | fotografie | 30768a164386 |
| cp_510,542,1733_002.jpg | archivní karta | 54e8e45b6efe |
| cp_552,555,1733_001.jpg | fotografie | ba0a304f0b81 |
| cp_552,555,1733_001.jpg | kopie bez tagu (1920 × 1080) | 770120dbe15a |
| cp_552,555,1733_001.jpg | archivní karta | ee85f262f85b |
| cp_552,555,1733_001.jpg | kopie bez tagu (1920 × 1080) | b87121c16130 |
| cp_552,555,1733_001.jpg | plán / výkres | 7abf8416cccb |

### Čp. 413 a: dílna ve dvoře SHD (struktura 413)

> **Upozornění – hypotéza identity:** Přiřazení čísla popisného k budově GIS je odvozeno ze skici a fotografií, GIS budovu s tímto čp. nevede.

> **Poznámka k identitě a GIS:** Hypotéza identity: GIS budovu s čp. 413 nevede. Přiřazení struktury 413 k budovám GIS 1113 a 1114 (bez čp.) ve dvoře mezi palácem 1733 a ulicí je odvozeno ze skici KSPPOP a fotografií; rozhodnutí uživatele 25. 10. 2026.

- Struktura 413 (dvorní kotelna a dílny, fotografie „Komplet: Starý Most“ z 28. 11. 1967 a KSPPOP) nemá v GIS budovu s tímto číslem. Skica parcel KSPPOP ji klade do dvora mezi palác 1733 a ulici U hřiště, kde GIS vede dvě budovy bez čp. Tato část je modelována na budově GIS 1113: fotografie ukazuje přízemní dílnu s proskleným dvoukřídlým vstupem, dvěma dvojitými okny a plochou střechou se světlíky.
- Prameny: skica KSPPOP cp_413_002, fotografie cp_413_001 (Komplet: Starý Most, 28. 11. 1967), GIS půdorys 1113 (bez čp.)
- Střecha: plochá střecha se světlíky (světlíky nejsou modelovány)
- GIS budova 1113 (bez čp.); geometrie revize r1, 111 polygonů.
- Hypotézy: měřítko je odvozeno z čelní fotografie; světlíky patří do textury, nejsou modelovány; půdorys ve tvaru L je z GIS, zadní část má stejnou výšku

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_413_001.jpg | kopie bez tagu (1920 × 1080) | cacf23db405c |
| cp_413_001.jpg | fotografie | c3fc3dd9aa6e |
| cp_413_001.jpg | archivní karta | 5c325454455f |
| cp_413_002.jpg | kopie bez tagu (1920 × 1080) | 940b084a580d |
| cp_413_002.jpg | fotografie | d711d2714d34 |
| cp_413_002.jpg | kopie bez tagu (1920 × 1080) | e7381b449c47 |
| cp_413_002.jpg | plán / výkres | 8c3c5aa6418b |
| cp_413_002.jpg | archivní karta | 15777f421605 |
| cp_413_003.jpg | fotografie | d3c9102b56c9 |
| cp_413_003.jpg | kopie bez tagu (1920 × 1080) | c6c97d321b42 |
| cp_413_003.jpg | archivní karta | 91555d8789a0 |
| cp_413_004.jpg | fotografie | 46e71d4b2b9f |
| cp_413_004.jpg | kopie bez tagu (1920 × 1080) | 1395181bbdce |
| cp_413_004.jpg | archivní karta | 017cdffdbae2 |
| cp_413_005.jpg | kopie bez tagu (1920 × 1080) | 1dc8cd31cf71 |
| cp_413_005.jpg | archivní karta | 8f1fbfab1782 |
| cp_413_005.jpg | fotografie | 4e800c75bc97 |
| cp_413_006.jpg | kopie bez tagu (1920 × 1080) | 4317f95ab8b4 |
| cp_413_006.jpg | fotografie | 7c85fc2c5f41 |
| cp_413_006.jpg | archivní karta | a0f4e0d703c7 |
| cp_413_007.jpg | kopie bez tagu (1920 × 1080) | 91bce48a7a51 |
| cp_413_007.jpg | fotografie | b1dff425bd8a |
| cp_413_007.jpg | archivní karta | da1de8f7d687 |

### Čp. 413 b: dílna / garáž ve dvoře SHD (struktura 413)

> **Upozornění – hypotéza identity:** Přiřazení čísla popisného k budově GIS je odvozeno ze skici a fotografií, GIS budovu s tímto čp. nevede.

> **Poznámka k identitě a GIS:** Hypotéza identity: GIS budovu s čp. 413 nevede. Přiřazení struktury 413 k budovám GIS 1113 a 1114 (bez čp.) ve dvoře mezi palácem 1733 a ulicí je odvozeno ze skici KSPPOP a fotografií; rozhodnutí uživatele 25. 10. 2026.

- Druhá budova přiřazená ke struktuře 413 (GIS 1114, bez čp.). Fotografie ukazuje dvoje vrata, prosklený vstup vpravo a plochou střechu se třemi světlíky.
- Prameny: skica KSPPOP cp_413_002, fotografie cp_413_006, GIS půdorys 1114 (bez čp.)
- Střecha: plochá střecha se třemi světlíky (světlíky nejsou modelovány)
- GIS budova 1114 (bez čp.); geometrie revize r4, 95 polygonů.
- Hypotézy: měřítko je odvozeno z výšky vrat; zadní šikmá část je z GIS a má stejnou výšku; šikmá zadní hrana půdorysu je v modelu nahrazena přímkou (zjednodušení obrysu)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_413_001.jpg | kopie bez tagu (1920 × 1080) | cacf23db405c |
| cp_413_001.jpg | fotografie | c3fc3dd9aa6e |
| cp_413_001.jpg | archivní karta | 5c325454455f |
| cp_413_002.jpg | kopie bez tagu (1920 × 1080) | 940b084a580d |
| cp_413_002.jpg | fotografie | d711d2714d34 |
| cp_413_002.jpg | kopie bez tagu (1920 × 1080) | e7381b449c47 |
| cp_413_002.jpg | plán / výkres | 8c3c5aa6418b |
| cp_413_002.jpg | archivní karta | 15777f421605 |
| cp_413_003.jpg | fotografie | d3c9102b56c9 |
| cp_413_003.jpg | kopie bez tagu (1920 × 1080) | c6c97d321b42 |
| cp_413_003.jpg | archivní karta | 91555d8789a0 |
| cp_413_004.jpg | fotografie | 46e71d4b2b9f |
| cp_413_004.jpg | kopie bez tagu (1920 × 1080) | 1395181bbdce |
| cp_413_004.jpg | archivní karta | 017cdffdbae2 |
| cp_413_005.jpg | kopie bez tagu (1920 × 1080) | 1dc8cd31cf71 |
| cp_413_005.jpg | archivní karta | 8f1fbfab1782 |
| cp_413_005.jpg | fotografie | 4e800c75bc97 |
| cp_413_006.jpg | kopie bez tagu (1920 × 1080) | 4317f95ab8b4 |
| cp_413_006.jpg | fotografie | 7c85fc2c5f41 |
| cp_413_006.jpg | archivní karta | a0f4e0d703c7 |
| cp_413_007.jpg | kopie bez tagu (1920 × 1080) | 91bce48a7a51 |
| cp_413_007.jpg | fotografie | b1dff425bd8a |
| cp_413_007.jpg | archivní karta | da1de8f7d687 |

### Čp. 1313: kino (Kinematographen-Theater Franze Gutha)

- Kino na východní straně jihozápadního ramene, podél U hřiště (skica KSPPOP: 1313 podél ulice, promítací kabina a terasa u 410; GIS budova 631 s popiskem 1313). Fotografie ukazuje dlouhý sál se dvěma dveřmi (východy z plánu), vyšší promítací věž s nápisem KINO a přízemní foyer s přesahující stříškou a skleněnými dveřmi. Plán pro Franze Gutha kreslí sál se dvěma východy; věž a foyer jsou pozdější, snad z 30. let.
- Prameny: fotografie cp_1313_001, skica KSPPOP cp_1313_002, plán „Plan zum Bau eines Kinematographen-Theaters für Herrn Franz Guth“, GIS půdorys 631
- Střecha: sedlová střecha nad sálem (okap 4,3 m, hřeben 7,0 m); zadní části z GIS mají plochou střechu (hypotéza)
- GIS budova 631 (popisek 1313); geometrie revize r3, 235 polygonů.
- Hypotézy: délky částí (sál 20,5 m, věž 5,0 m, foyer 5,85 m) jsou odhad ze šikmé fotografie; výšky (sál 4,3 m, hřeben 7,0 m, věž 8,5 m, foyer 4,3 m) jsou z fotografie s měřítkem podle dveří; okna věže nad 4,3 m nejsou vyříznuta, patří do textury; zadní části z GIS mají plochou střechu (hypotéza); šikmá zadní část a jižní výstupek půdorysu GIS jsou v modelu zjednodušeny; nápis KINO / BIO patří do textury

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1313_001.jpg | fotografie | 0fce91c6fded |
| cp_1313_001.jpg | kopie bez tagu (1920 × 1080) | 76219cc57860 |
| cp_1313_001.jpg | archivní karta | 87d8bb63e284 |
| cp_1313_001.jpg | plán / výkres | b98d25c497a7 |
| cp_1313_002.jpg | plán / výkres | 345db2578596 |
| cp_1313_002.jpg | plán / výkres | 6056c1fc360d |
| cp_1313_002.jpg | archivní karta | 6a05d62d0553 |
| cp_1313_002.jpg | fotografie | 9de02e43c737 |
| cp_1313_002.jpg | kopie bez tagu (1920 × 1080) | c1be4b9f81b0 |
| cp_1313_002.jpg | kopie bez tagu (1920 × 1080) | dd7b644ce723 |
| cp_1313_003.jpg | fotografie | 69d16d2db605 |
| cp_1313_003.jpg | plán / výkres | deb1aab0e7c2 |
| cp_1313_003.jpg | kopie bez tagu (1920 × 1080) | f33830051a67 |
| cp_1313_003.jpg | archivní karta | ad0836660bfb |
| cp_1313_004.jpg | kopie bez tagu (1920 × 1080) | a3fa60367185 |
| cp_1313_004.jpg | archivní karta | 7f71d3a9cf40 |
| cp_1313_004.jpg | fotografie | a4c3af409260 |

### Čp. 410: velký patrový dům na Husově náměstí

- Dům na severní straně Husova náměstí, jehož severozápadní štít hledí ke kinu 1313 a do U hřiště (skica KSPPOP 1313 | 410, karta kina zmiňuje vpravo velký dům čp. 410, GIS budova 619 s popiskem 410). Fotografie z roku 1975 ukazuje sedm os (pár | jedno | dvojité okno se vstupem | jedno | pár), dvě podlaží a střechu s pěti vikýři. Projekt nástavby dalšího patra (Stockwerksaufbau) realizován nebyl.
- Prameny: fotografie cp_410,1733_001 (1975) a cp_1313_001, plány cp_410_001 a cp_410_003 (řezy původního stavu), cp_410_002 (Stockwerksaufbau, nerealizováno), cp_410_004 (sondážní práce), skica KSPPOP cp_1313_002, GIS půdorys 619
- Střecha: hřeben podél hlavní fasády; severozápadní konec štít nad kinem 1313 (fotografie), jihovýchodní konec valba (hypotéza)
- GIS budova 619 (popisek 410); geometrie revize r1, 432 polygonů.
- Hypotézy: osy jsou symetrizovány, fotografie je mírně šikmá; výšky (okap 9,5 m, hřeben 13,7 m) jsou z fotografie 1975; jihovýchodní boční stěna k Husovu náměstí je bez otvorů (nedoloženo); polohy vikýřů jsou z fotografie přibližné

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_410,1733_001.jpg | fotografie | 4f98a0a15944 |
| cp_410,510,911_001.jpg | fotografie | c493c2139938 |
| cp_410,911,938,949,1260_001.jpg | fotografie | 764a18fc491f |
| cp_410,911,938,949,1260_002.jpg | fotografie | ac95af7aa090 |
| cp_410,911,938,949,1260_003.jpg | fotografie | b7a0e9c6ca55 |
| cp_410,911,938,949,1260_004.jpg | fotografie | 913c0f1d1ca5 |
| cp_410,911,938,949,1260_005.jpg | fotografie | 1b16811dc506 |
| cp_410,911,938,949,1260_006.jpg | fotografie | 7596bfc71b2b |
| cp_410,911,938,949,1260_007.jpg | fotografie | ecb8a5f3acdd |
| cp_410,911,938,949,1260_008.jpg | fotografie | 821d1c2f5131 |
| cp_410,911,938,949,1260_009.jpg | fotografie | 5a41109aa13d |
| cp_410,911,938,949,1260_010.jpg | fotografie | 40d7d0898246 |
| cp_410,911,938,949,944,912,904,903,939_001.jpg | fotografie | 014b65f6fadf |
| cp_410,911,938,949,944,912,904,903,939_002.jpg | fotografie | 725ab5ef741d |
| cp_410_001.jpg | plán / výkres | 7f32380ce1e3 |
| cp_410_002.jpg | plán / výkres | 6101f61d3b3e |
| cp_410_003.jpg | plán / výkres | c07899a96441 |
| cp_410_004.jpg | plán / výkres | 5ea0950de554 |

### Čp. 415: dvoupatrový dům se čtyřmi osami a frontony

- První dům řady 415 | 475 | 416 v rameni k nám. Dvouletky (skica KSPPOP, karta domu 475 uvádí vlevo dům 415 a vpravo 416, GIS budova 1115). Fotografie z 28. 11. 1967 ukazuje čtyři osy: v přízemí široký výkladní otvor, okno, dveře a okno, v 1. patře čtyři okna s frontony (krajní trojúhelníkové, prostřední segmentové), ve 2. patře čtyři okna.
- Prameny: fotografie cp_415_003 (28. 11. 1967, rektifikovaná 12,04 × 11,4 m), fotografie řady cp_415,475,416_002, skica KSPPOP cp_415,475,416_001, plán cp_415_001, GIS půdorys 1115
- Střecha: valba vlevo k volnému konci u proluky u dvora SHD, štít k 475 (fotografie)
- GIS budova 1115 (popisek 415); geometrie revize r1, 300 polygonů.
- Hypotézy: výška 11,3 m je z rektifikace při šířce GIS; poměr šířek 415 : 475 je na fotografii 1,48, v GIS 1,60 (rozdíl asi 0,4 m ponechán); frontony nad okny 1. patra patří do textury (předsazení pod 0,1 m), nadokenní římsy 2. patra jsou geometrie; vzepětí střechy 4,0 m je odhad; zadní schodišťový rizalit je z GIS a sahá do výšky okapu; dvorní průčelí je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| P-000584.jpg | pohlednice | 02c4e61bda0a |
| cp_415,475,416_001.jpg | kopie bez tagu (1920 × 1080) | 81ddd1f9c913 |
| cp_415,475,416_001.jpg | fotografie | 7eae58ae39dc |
| cp_415,475,416_001.jpg | plán / výkres | 8cdeb535d9e2 |
| cp_415,475,416_001.jpg | archivní karta | e90bbee4ff1d |
| cp_415,475,416_001.jpg | kopie bez tagu (1920 × 1080) | 202ceff31d4d |
| cp_415,475,416_002.jpg | archivní karta | 5b1b74cf21c9 |
| cp_415,475,416_002.jpg | fotografie | 2c43df97b755 |
| cp_415,475,416_002.jpg | kopie bez tagu (1920 × 1080) | 06f9c3699651 |
| cp_415,475,416_003.jpg | fotografie | 9f5f6a619190 |
| cp_415,475,416_003.jpg | kopie bez tagu (1920 × 1080) | 054013d9e430 |
| cp_415,475,416_003.jpg | archivní karta | f13b310434af |
| cp_415,475_001.jpg | archivní karta | 6c400567bd85 |
| cp_415,475_001.jpg | fotografie | abf94b799649 |
| cp_415,475_001.jpg | kopie bez tagu (1920 × 1080) | 3473cfdb1387 |
| cp_415_001.jpg | fotografie | 203096938828 |
| cp_415_001.jpg | kopie bez tagu (1920 × 1080) | e4f60bef24c2 |
| cp_415_001.jpg | plán / výkres | d224bac9de85 |
| cp_415_001.jpg | archivní karta | 3d7c03fea257 |
| cp_415_002.jpg | archivní karta | 9d06aaf48fdb |
| cp_415_002.jpg | fotografie | fd0cd81a2fd6 |
| cp_415_002.jpg | kopie bez tagu (1920 × 1080) | 6b81691016c0 |
| cp_415_003.jpg | fotografie | f7c14f36593a |
| cp_415_003.jpg | kopie bez tagu (1920 × 1080) | 9f3489a02e96 |
| cp_415_003.jpg | archivní karta | 16b989b32102 |
| cp_415_004.jpg | fotografie | 17d7f6e7c7b6 |
| cp_415_004.jpg | kopie bez tagu (1920 × 1080) | cf6c90a61b30 |
| cp_415_004.jpg | archivní karta | 623407c0ef9d |
| cp_415_005.jpg | kopie bez tagu (1920 × 1080) | 504d6ec99001 |
| cp_415_005.jpg | fotografie | 159b8f04aedf |
| cp_415_005.jpg | archivní karta | efee77374080 |
| cp_415_006,007.jpg | archivní karta | 398c517df9af |
| cp_415_006.jpg | fotografie | b281144db52d |
| cp_415_006.jpg | kopie bez tagu (1920 × 1080) | c7c484fdfc3b |
| cp_415_007.jpg | fotografie | 2e8251c1cfbd |
| cp_415_007.jpg | kopie bez tagu (1920 × 1080) | b5cc4af74f88 |

### Čp. 475: úzký dvoupatrový dům s obchodem

- Prostřední dům řady 415 | 475 | 416 (karta L3R: vlevo dům 415, vpravo 416; GIS budova 1116). Fotografie ukazuje tři osy: v přízemí obchod s nápisem Lebensmittel Siegl (dveře a výloha) a dveře domu, ve dvou patrech po třech oknech.
- Prameny: fotografie cp_475_001 (rektifikovaná 7,52 × 11,0 m), karta L3R, skica KSPPOP cp_415,475,416_001, plány cp_475_001/002, GIS půdorys 1116
- Střecha: sedlová střecha, štíty k 415 a k vyššímu 416
- GIS budova 1116 (popisek 475); geometrie revize r1, 209 polygonů.
- Hypotézy: výška 11,0 m je z rektifikace; nápis Lebensmittel patří do textury; zadní přístavek je z GIS a sahá do výšky okapu; dvorní průčelí je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_415,475,416_001.jpg | plán / výkres | 8cdeb535d9e2 |
| cp_415,475,416_001.jpg | archivní karta | e90bbee4ff1d |
| cp_415,475,416_001.jpg | fotografie | 7eae58ae39dc |
| cp_415,475,416_001.jpg | kopie bez tagu (1920 × 1080) | 202ceff31d4d |
| cp_415,475,416_001.jpg | kopie bez tagu (1920 × 1080) | 81ddd1f9c913 |
| cp_415,475,416_002.jpg | archivní karta | 5b1b74cf21c9 |
| cp_415,475,416_002.jpg | kopie bez tagu (1920 × 1080) | 06f9c3699651 |
| cp_415,475,416_003.jpg | archivní karta | f13b310434af |
| cp_415,475,416_003.jpg | fotografie | 9f5f6a619190 |
| cp_415,475,416_003.jpg | kopie bez tagu (1920 × 1080) | 054013d9e430 |
| cp_415,475_001.jpg | archivní karta | 6c400567bd85 |
| cp_415,475_001.jpg | fotografie | abf94b799649 |
| cp_415,475_001.jpg | kopie bez tagu (1920 × 1080) | 3473cfdb1387 |
| cp_475,416_001.jpg | kopie bez tagu (1920 × 1080) | b39670f480b9 |
| cp_475,416_001.jpg | plán / výkres | 3bb76f8f5444 |
| cp_475,416_001.jpg | archivní karta | afa88b898ac6 |
| cp_475,416_001.jpg | kopie bez tagu (1920 × 1080) | fb30bc6d113e |
| cp_475,416_001.jpg | fotografie | 87b00240c2f1 |
| cp_475_001.jpg | fotografie | 8d7322112371 |
| cp_475_001.jpg | kopie bez tagu (1920 × 1080) | 4626b460766d |
| cp_475_001.jpg | archivní karta | fbad6e558311 |
| cp_475_001.jpg | plán / výkres | 61a76937a64d |
| cp_475_002.jpg | plán / výkres | ec134c661819 |

### Čp. 416: vyšší dvoupatrový dům s frontony a zubořezem

- Poslední a nejvyšší dům řady 415 | 475 | 416 (fotografie cp_416_001, karta L4R, GIS budova 1117). Fotografie ukazuje čtyři osy, vyvýšené přízemí se vstupem ve 3. ose, v 1. patře okna s frontony (segment | trojúhelník | trojúhelník | segment), ve 2. patře okna s nadokenními římsami na konzolách a zubořezový vlys.
- Prameny: fotografie cp_416_001 (rektifikovaná 10,41 × 12,55 m k vlysu, hlavní římsa 13,1 m), fotografie řady cp_415,475,416_002 a dvora cp_475,416_001, skica KSPPOP cp_415,475,416_001, plány cp_416_001–004, GIS půdorys 1117
- Střecha: valba vpravo k volnému konci u chalupy 439, štít a požární zeď k nižšímu 475
- GIS budova 1117 (popisek 416); geometrie revize r2, 605 polygonů.
- Hypotézy: výška 13,1 m je z rektifikace při šířce GIS 10,41 m; dvorní křídlo má plnou výšku s valbou na konci (GIS, orientační fotografie dvora); zadní stěna dvorního křídla je v modelu narovnána (zjednodušení šikmého půdorysu GIS); reliéfy frontonů, bosáž a zubořez patří do textury; frontony a nadokenní římsy jsou geometrie; sklepní okénka patří do textury; dvorní průčelí je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_415,475,416_001.jpg | plán / výkres | 8cdeb535d9e2 |
| cp_415,475,416_001.jpg | kopie bez tagu (1920 × 1080) | 202ceff31d4d |
| cp_415,475,416_001.jpg | kopie bez tagu (1920 × 1080) | 81ddd1f9c913 |
| cp_415,475,416_001.jpg | fotografie | 7eae58ae39dc |
| cp_415,475,416_001.jpg | archivní karta | e90bbee4ff1d |
| cp_415,475,416_002.jpg | fotografie | 2c43df97b755 |
| cp_415,475,416_002.jpg | kopie bez tagu (1920 × 1080) | 06f9c3699651 |
| cp_415,475,416_002.jpg | archivní karta | 5b1b74cf21c9 |
| cp_415,475,416_003.jpg | kopie bez tagu (1920 × 1080) | 054013d9e430 |
| cp_415,475,416_003.jpg | archivní karta | f13b310434af |
| cp_415,475,416_003.jpg | fotografie | 9f5f6a619190 |
| cp_416_001.jpg | kopie bez tagu (1920 × 1080) | 82ce909f43fe |
| cp_416_001.jpg | archivní karta | 994749cbce66 |
| cp_416_001.jpg | fotografie | 67bbfc63da08 |
| cp_416_001.jpg | plán / výkres | 75777f3c5eaf |
| cp_416_002.jpg | plán / výkres | e078ec3994a7 |
| cp_416_003.jpg | plán / výkres | d8db1a7ba764 |
| cp_416_004.jpg | plán / výkres | a9aae6c16b7d |
| cp_475,416_001.jpg | kopie bez tagu (1920 × 1080) | b39670f480b9 |
| cp_475,416_001.jpg | kopie bez tagu (1920 × 1080) | fb30bc6d113e |
| cp_475,416_001.jpg | plán / výkres | 3bb76f8f5444 |
| cp_475,416_001.jpg | archivní karta | afa88b898ac6 |
| cp_475,416_001.jpg | fotografie | 87b00240c2f1 |

### Čp. 439: přízemní chalupa s cedulí „Ul. Na dobytčím trhu“

- GIS vede chalupu pod Seligerovou (budova 1118 s popiskem 439), ale na domě visí v 60. letech cedule ulice Na dobytčím trhu (Viehmarkt); uliční strana je dlouhá severovýchodní fasáda s oknem, cedulí a dvojími dveřmi. Na jihovýchodním konci je příčný štít s obloukovým otvorem a pultovou stříškou. Plán z roku 1911 u tohoto čísla zobrazuje dvorní sklad s garážemi, ne chalupu.
- Prameny: fotografie cp_439_001 a cp_439_002 (KSPPOP), skica KSPPOP cp_439_004 ((439) mezi (416) a (417)), GIS půdorys 1118; plán 1911 (Magazin- und Stallgebäude) pro chalupu nepoužit
- Střecha: valbová střecha s hřebenem podél ulice, na jihovýchodním konci příčný štít (v modelu zjednodušen jako štítový vikýř)
- GIS budova 1118 (popisek 439); geometrie revize r1, 142 polygonů.
- Hypotézy: výšky jsou z fotografie odhadem (okap 3,2 m, hřeben 6,2 m); příčný štít je zjednodušen jako štítový vikýř na lícní stěně; pultová stříška nad oknem je modelována jako římsa; jihozápadní a dvorní strana jsou bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| P-000588.jpg | pohlednice | ed4118ea6b64 |
| cp_439_001.jpg | kopie bez tagu (1920 × 1080) | e285f69e306c |
| cp_439_001.jpg | archivní karta | aa30bef109c2 |
| cp_439_001.jpg | plán / výkres | 2810da27897d |
| cp_439_001.jpg | fotografie | 215481158037 |
| cp_439_002.jpg | archivní karta | 09fa32297564 |
| cp_439_002.jpg | fotografie | 68ef2da77136 |
| cp_439_002.jpg | kopie bez tagu (1920 × 1080) | 11db331cd19f |
| cp_439_003.jpg | kopie bez tagu (1920 × 1080) | 82963ce474e8 |
| cp_439_003.jpg | archivní karta | 7b7cbe31c96b |
| cp_439_003.jpg | fotografie | 645a38966801 |
| cp_439_004.jpg | fotografie | fef547f25f46 |
| cp_439_004.jpg | kopie bez tagu (1920 × 1080) | da8b45888a46 |
| cp_439_004.jpg | kopie bez tagu (1920 × 1080) | 8000771f438a |
| cp_439_004.jpg | plán / výkres | 479437a4ceed |
| cp_439_004.jpg | archivní karta | f47fcadb4b59 |
| cp_439_005.jpg | archivní karta | 6dd8af9b301d |
| cp_439_005.jpg | kopie bez tagu (1920 × 1080) | 979731ee843b |
| cp_439_005.jpg | fotografie | 45561efdc56d |
| cp_439_006.jpg | fotografie | e2e68e5f5c22 |
| cp_439_006.jpg | kopie bez tagu (1920 × 1080) | f9b2f1e7c301 |
| cp_439_006.jpg | archivní karta | 5ff89a4926da |
| cp_439_007.jpg | fotografie | d95132cfa9a6 |
| cp_439_007.jpg | kopie bez tagu (1920 × 1080) | 53d4944fb4b9 |
| cp_439_007.jpg | archivní karta | db750d1f9edc |

### Čp. 417: malá chalupa (Ziegelgasse, plán 1892)

> **Upozornění – částečně hypotéza:** Fasáda je doložena jen nízkorozlišenou kopií fotografie; výšky a detaily jsou odvozeny z plánu a sousedů.

- Chalupa vedle 439 (skica KSPPOP: (417) vedle (439); Planskizze 1892: Haus Nr. 417 v Ziegelgasse; GIS budova 1119 s popiskem 417). Fasáda je doložena jen nízkorozlišenou kopií fotografie (1920 × 1080): k ulici štít s oknem a dveřmi, obložený prkny. Není jisté, zda štít na kopii patří domu 417, nebo stáji z roku 1923.
- Prameny: nízkorozlišená kopie fotografie cp_417_003 (další kopie cp_417_001, 002 a 004 orientačně), skica KSPPOP cp_439_004, Planskizze 1892, GIS půdorys 1119; plány 1923 (Stall, Abort, Schupfen) se týkají dvorních staveb
- Střecha: sedlová střecha se štítem k ulici (severovýchodní strana 7,5 m)
- GIS budova 1119 (popisek 417); geometrie revize r1, 74 polygonů.
- Hypotézy: existují jen nízkorozlišené kopie fotografií, polohy otvorů a výšky jsou odhad; není jisté, zda štít na kopii cp_417_003 patří domu 417, nebo stáji z roku 1923; okénko ve štítu patří do textury; uliční štít je v modelu boční fasádou (místní průčelí modelu je kratší jihovýchodní strana)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_417_001.jpg | kopie bez tagu (1920 × 1080) | 2ae03daa5b7a |
| cp_417_001.jpg | plán / výkres | a53c2dbba371 |
| cp_417_002.jpg | kopie bez tagu (1920 × 1080) | cfdeb8c88631 |
| cp_417_002.jpg | plán / výkres | 02d0f3ad719c |
| cp_417_003.jpg | kopie bez tagu (1920 × 1080) | 4522b817ebe1 |
| cp_417_003.jpg | plán / výkres | 938f23f8e054 |
| cp_417_004.jpg | kopie bez tagu (1920 × 1080) | 4110faa56a53 |

### Čp. 586: přízemní dům za zahradní zdí na nároží k U hřiště

- Dům na východní straně nám. Dvouletky na nároží k U hřiště, za domy 823 a 831 (skica KSPPOP s přeškrtnutým číslem 568 opraveným na 586, vlevo 1230; GIS budova 1125 s popiskem 586). Fotografie ukazuje přízemní dům za zahradní zdí: horní části tří oken, dvě volská oka a střešní okna; valba k nároží U hřiště.
- Prameny: fotografie cp_586_001 a cp_586,823_001, skica KSPPOP cp_586_001, plány cp_586_001__2–006, GIS půdorys 1125
- Střecha: sedlová střecha s valbou na severovýchodním konci, vlevo štít pod požární zdí 1230
- GIS budova 1125 (popisek 586); geometrie revize r1, 184 polygonů.
- Hypotézy: dolní části oken zakrývá zeď, parapety jsou odhad; výška okapu 3,6 m je z měřítka fotografie; zahradní zeď před domem není modelována (není budovou GIS); dvorní strana je bez otvorů

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_586,1230_001.jpg | kopie bez tagu (1920 × 1080) | bf5344cd899a |
| cp_586,823_001.jpg | fotografie | 0816ed4d134d |
| cp_586,823_001.jpg | kopie bez tagu (1920 × 1080) | a29675292eac |
| cp_586,823_001.jpg | archivní karta | d96645e711f7 |
| cp_586_001.jpg | plán / výkres | f6f65c1512ff |
| cp_586_001.jpg | kopie bez tagu (1920 × 1080) | b30fb7e89fd6 |
| cp_586_001.jpg | archivní karta | fdd50c048c56 |
| cp_586_001.jpg | kopie bez tagu (1920 × 1080) | be14f5b745ed |
| cp_586_001.jpg | fotografie | be7f56cf2505 |
| cp_586_001__2.jpg | plán / výkres | c5d9acf77b2a |
| cp_586_002.jpg | kopie bez tagu (1920 × 1080) | e89072fbbcab |
| cp_586_002.jpg | archivní karta | 0e9033bdfb62 |
| cp_586_002.jpg | plán / výkres | c443d8f9ea0f |
| cp_586_002.jpg | fotografie | df9456b17b9e |
| cp_586_003.jpg | plán / výkres | 7e092862f561 |
| cp_586_004.jpg | plán / výkres | de7f4e80f719 |
| cp_586_005.jpg | plán / výkres | ed49d0a32c87 |
| cp_586_006.jpg | plán / výkres | 1c1f0da2d750 |

### Čp. 1230: patrový dům se středním rizalitem a zakřiveným štítem

> **Upozornění – částečně hypotéza:** Fasáda je doložena jen nízkorozlišenou kopií fotografie; výšky a detaily jsou odvozeny z plánu a sousedů.

- Dům čelem k nám. Dvouletky mezi 586 a 1186 (skica 1186 | 1230 s arkýřem, GIS budova 1126). Fasáda je doložena jen nízkorozlišenou kopií fotografie: tři osy, střední rizalit se zakřiveným štítem a oválným oknem, v přízemí okno, široký otvor a dveře. Požární štít k nižšímu 586 nese malovaného jelena.
- Prameny: nízkorozlišené kopie fotografií cp_1230_001 a cp_586,1230_001, skica cp_1230_001, pohled na řadu cp_1178,1188,1192,1193_002 (sousední oblast Náměstí Dvouletky), plán cp_1230_001, GIS půdorys 1126
- Střecha: valba vlevo, požární štít k nižšímu 586
- GIS budova 1126 (popisek 1230); geometrie revize r3, 289 polygonů.
- Hypotézy: jen nízkorozlišená kopie fotografie (1920 × 1080, bez tagu): polohy a výšky otvorů jsou odhad z měřítka šířky GIS; střecha je z kopie fotografie a z pohledu na řadu cp_1178,1188,1192,1193_002 (orientačně); štuk, bosáž a šambrány patří do textury; dvorní průčelí je bez otvorů; střední rizalit je předsazený blok 0,35 m; zakřivený štít rizalitu je zjednodušen jako barokní vikýř; zadní přístavek z GIS je zastřešen pultovou střechou

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1230_001.jpg | plán / výkres | a5e1a3a25ab7 |
| cp_1230_001.jpg | kopie bez tagu (1920 × 1080) | d66f2beb67ba |
| cp_1230_001.jpg | kopie bez tagu (1920 × 1080) | 20013631e385 |
| cp_586,1230_001.jpg | kopie bez tagu (1920 × 1080) | bf5344cd899a |

### Čp. 1186: patrový dům se dvěma vikýři

> **Upozornění – částečně hypotéza:** Fasáda je doložena jen nízkorozlišenou kopií fotografie; výšky a detaily jsou odvozeny z plánu a sousedů.

- Dům čelem k nám. Dvouletky mezi 1188 a 1230 (skica 1188 | 1186 | 1230, GIS budova 1127). Fasáda je doložena jen nízkorozlišenou kopií fotografie: tři osy, v přízemí obloukově zaklenutá okna a portál, v patře tři okna, na střeše dva vikýře (levý štítový, prostřední barokní s obloukovým oknem).
- Prameny: nízkorozlišená kopie fotografie cp_1186_001, skica cp_1186_001, pohled na řadu cp_1178,1188,1192,1193_002 (sousední oblast Náměstí Dvouletky), plány cp_1186_001/002, GIS půdorys 1127
- Střecha: sedlová střecha s vikýři, štíty k sousedům
- GIS budova 1127 (popisek 1186); geometrie revize r2, 324 polygonů.
- Hypotézy: jen nízkorozlišená kopie fotografie (1920 × 1080, bez tagu): polohy a výšky otvorů jsou odhad z měřítka šířky GIS; střecha je z kopie fotografie a z pohledu na řadu cp_1178,1188,1192,1193_002 (orientačně); štuk, bosáž a šambrány patří do textury; dvorní průčelí je bez otvorů; zadní rizalit z GIS je zastřešen pultovou střechou

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1186_001.jpg | plán / výkres | 7ace873a377c |
| cp_1186_001.jpg | kopie bez tagu (1920 × 1080) | 85073fb6b2c4 |
| cp_1186_001.jpg | kopie bez tagu (1920 × 1080) | e0d9ef3dae4d |
| cp_1186_002.jpg | plán / výkres | 308a6582849a |
| cp_740,1186,1188,1482_001.jpg | kopie bez tagu (1920 × 1080) | 60557265bbcb |

### Čp. 1188: patrový dům se zkoseným nárožím

> **Upozornění – částečně hypotéza:** Fasáda je doložena jen nízkorozlišenou kopií fotografie; výšky a detaily jsou odvozeny z plánu a sousedů.

- Dům čelem k nám. Dvouletky mezi 1178 a 1186 (skica 1178 | 1188 | 1186, GIS budova 1128). Fasáda je doložena jen nízkorozlišenou kopií fotografie: zkosené nároží vlevo s párem oken v obou podlažích a hlavní průčelí se třemi osami a portálem.
- Prameny: nízkorozlišená kopie fotografie cp_1188_001, skica cp_1188_001, pohled na řadu cp_1178,1188,1192,1193_002 (sousední oblast Náměstí Dvouletky), plán cp_1188_001, GIS půdorys 1128
- Střecha: valbová střecha se střešními okny (kopie fotografie, pohled na řadu)
- GIS budova 1128 (popisek 1188); geometrie revize r2, 218 polygonů.
- Hypotézy: jen nízkorozlišená kopie fotografie (1920 × 1080, bez tagu): polohy a výšky otvorů jsou odhad z měřítka šířky GIS; střecha je z kopie fotografie a z pohledu na řadu cp_1178,1188,1192,1193_002 (orientačně); štuk, bosáž a šambrány patří do textury; dvorní průčelí je bez otvorů; zkosená stěna 4,82 m je samostatná fasáda, střecha nad ní sleduje boční linii půdorysu; zadní část z GIS je zastřešena pultovou střechou

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1178,1188,1192,1193_001.jpg | kopie bez tagu (1920 × 1080) | ed0e03049848 |
| cp_1178,1188,1192,1193_002.jpg | kopie bez tagu (1920 × 1080) | 2a0b23de6fdc |
| cp_1178,1188,1192,1193_003.jpg | kopie bez tagu (1920 × 1080) | c72693c09c3b |
| cp_1188_001.jpg | kopie bez tagu (1920 × 1080) | a54720295ac9 |
| cp_1188_001.jpg | kopie bez tagu (1920 × 1080) | 5507c59ea783 |
| cp_1188_001.jpg | plán / výkres | 15c37ca3ddfb |
| cp_740,1186,1188,1482_001.jpg | kopie bez tagu (1920 × 1080) | 60557265bbcb |

### Čp. 1178: patrový dům s atikovým štítem

> **Upozornění – částečně hypotéza:** Fasáda je doložena jen nízkorozlišenou kopií fotografie; výšky a detaily jsou odvozeny z plánu a sousedů.

- Dům čelem k nám. Dvouletky mezi 1192 a 1188 (skica 1192 | 1178 | 1188, GIS budova 1129). Fasáda je doložena jen nízkorozlišenou kopií fotografie: tři osy, v přízemí okno, portál a okno, v patře tři okna (prostřední s trojúhelníkovým frontonem), atikový štít s obloukovým oknem.
- Prameny: nízkorozlišená kopie fotografie cp_1178_001, skica cp_1178_001, pohled na řadu cp_1178,1188,1192,1193_002 (sousední oblast Náměstí Dvouletky), plán cp_1178_001, GIS půdorys 1129
- Střecha: sedlová střecha, štíty k sousedům
- GIS budova 1129 (popisek 1178); geometrie revize r2, 277 polygonů.
- Hypotézy: jen nízkorozlišená kopie fotografie (1920 × 1080, bez tagu): polohy a výšky otvorů jsou odhad z měřítka šířky GIS; střecha je z kopie fotografie a z pohledu na řadu cp_1178,1188,1192,1193_002 (orientačně); štuk, bosáž a šambrány patří do textury; dvorní průčelí je bez otvorů; zadní rizalit z GIS je zastřešen pultovou střechou

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1178,1188,1192,1193_001.jpg | kopie bez tagu (1920 × 1080) | ed0e03049848 |
| cp_1178,1188,1192,1193_002.jpg | kopie bez tagu (1920 × 1080) | 2a0b23de6fdc |
| cp_1178,1188,1192,1193_003.jpg | kopie bez tagu (1920 × 1080) | c72693c09c3b |
| cp_1178_001.jpg | kopie bez tagu (1920 × 1080) | a85c367d0c12 |
| cp_1178_001.jpg | plán / výkres | 184d13f57e27 |
| cp_1178_001.jpg | kopie bez tagu (1920 × 1080) | dd65f76eaa75 |

### Čp. 1192: patrový dům s arkýřem a věžičkou

> **Upozornění – částečně hypotéza:** Fasáda je doložena jen nízkorozlišenou kopií fotografie; výšky a detaily jsou odvozeny z plánu a sousedů.

- Dům čelem k nám. Dvouletky mezi 1193 a 1178 (skica 1193 | 1192 | 1178, GIS budova 1130; soused 1193 patří do oblasti Náměstí Dvouletky). Fasáda je doložena jen nízkorozlišenou kopií fotografie: v přízemí tři okna a vrata vpravo, v patře dvě okna, arkýř s balkonem a věžičkou s kupolí a dvě okna.
- Prameny: nízkorozlišená kopie fotografie cp_1192_001, skica cp_1192_001, pohled na řadu cp_1178,1188,1192,1193_002 (sousední oblast Náměstí Dvouletky), plán cp_1192_001, GIS půdorys 1130
- Střecha: sedlová střecha, věžička nad arkýřem (kupole zjednodušena jako jehlan)
- GIS budova 1130 (popisek 1192); geometrie revize r2, 264 polygonů.
- Hypotézy: jen nízkorozlišená kopie fotografie (1920 × 1080, bez tagu): polohy a výšky otvorů jsou odhad z měřítka šířky GIS; střecha je z kopie fotografie a z pohledu na řadu cp_1178,1188,1192,1193_002 (orientačně); štuk, bosáž a šambrány patří do textury; dvorní průčelí je bez otvorů; arkýř 2,1 × 0,6 m má jehlanovou stříšku místo kupole (zjednodušení); zadní rizalit z GIS je zastřešen pultovou střechou (preventivně podle 1230, 1186 a 1178)

| Příloha | Typ | SHA-256 (12 znaků) |
|---|---|---|
| cp_1178,1188,1192,1193_001.jpg | kopie bez tagu (1920 × 1080) | ed0e03049848 |
| cp_1178,1188,1192,1193_002.jpg | kopie bez tagu (1920 × 1080) | 2a0b23de6fdc |
| cp_1178,1188,1192,1193_003.jpg | kopie bez tagu (1920 × 1080) | c72693c09c3b |
| cp_1192,1193_001.jpg | kopie bez tagu (1920 × 1080) | 9e1d5f7c2502 |
| cp_1192_001.jpg | kopie bez tagu (1920 × 1080) | 2e41a6578c1f |
| cp_1192_001.jpg | plán / výkres | 158b4e0c3618 |
| cp_1192_001.jpg | kopie bez tagu (1920 × 1080) | 0bfb7ab51a87 |

### Budova GIS 1638 (bez čp.): dvorní stavba bez čp. u nám. Dvouletky

> **Upozornění – hypotéza podle GIS:** Dvorní stavba bez čísla popisného jen podle GIS plánu 1938; žádná fotografie ani plán nebyly nalezeny. Tvar, výška a střecha jsou odhad.

- Dvorní stavba bez čísla popisného na severozápadní straně ulice za domy u nám. Dvouletky, jen v GIS plánu 1938. Fotografie ani plán k ní nebyly nalezeny.
- Prameny: GIS půdorys 1638
- Střecha: nízká sedlová střecha – odhad
- GIS budova 1638 (bez čp.); geometrie revize r1, 48 polygonů.
- Hypotézy: tvar, výška 3,2 m i střecha jsou odhad (kůlna nebo garáže); otvory nejsou modelovány
