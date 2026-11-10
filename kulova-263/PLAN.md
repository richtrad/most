# Kulová: další dům — čp. 263

Zadání 27. září 2026: naplánovat a provést jeden další dům, dokumentovat
práci a měřit využití na hranicích etap. Výchozí oprava otvorů G, bevel C
jen na vybraných hranách. Předchozí modely zůstávají nedotčené.

## Plán a kontrolní body

1. **Inventura a identita:** plán označený čp. 263, původní skupinové foto,
   lokální databázový FRONT a starší model. Uložit hashe a původ. Živý GET
   Libuše byl zkusen, po povolení síťového přístupu timeout; zdroje jsou
   místní snapshot ze září 2026, nikoli dnes živě ověřený stav.
2. **Registrace a rozbor:** očíslovat skutečné otvory, slepé plochy neotvírat,
   zachovat chybějící okenní výplně, poškození a původní obraz nápisů.
   Samostatně změřit hranice otvorů a fasády. Rozměry plánu a staršího GIS
   nejsou bez ověření zaměnitelné; odhady a skryté dvorní části přiznat.
3. **Materiály:** archivní FRONT nechat beze změny. V nové vrstvě maskovaně
   odstranit zdvojený okap/svod; vygenerovat materiálové pokračování pro
   ostění, parapety a nedoložené plochy. Mimo masku nulová změna pixelů.
4. **Geometrie G:** otvory odvodit jednotlivě, vytvořit hloubku ostění,
   oddělit výplně a tmavé prázdné otvory; skutečný práh/schody bez fotografie
   schodů na dveřích. Vytvořit pět doložených oblých střešních otvorů se
   souvislým uzavřeným pláštěm a napojením do střechy. Zachovat jemné profily.
5. **UV a export:** vlastní nenulové UV pro kolmé plochy, rozlišení podle
   zdroje, jemný bevel vybraných parapetů/stupňů. Export .blend a GLB.
6. **Vizuální QA a opravy:** čtyři osy, čtyři střešní rohy, každý otvor
   zepředu/zleva/zprava, clay osy a podezřelé detaily, nápisy, patina,
   okap s/bez geometrie, spodky schodů/podstava. Kontrolní klik identity.
   Každou vadu zapsat; při kritické geometrii upozornit, neukrýt ji T.
7. **Předání:** místní web s modelem, zdroji, procesem a porovnáním,
   manifesty, QA, obnovovací skripty a ZIP. Kompletní dům označit až po QA.

## Měření náročnosti

Základ: 6 % spotřebováno / 94 % zbývá v týdenním okně (10080 minut),
reset Unix 1791062590. `usage.json` ukládá měření po inventuře, přípravě
materiálů, obrazové generaci, geometrii/exportu, vizuálním QA/opravách a
bezprostředně před závěrem. Rozdíly jsou procentní body sdíleného účtového
limitu, ne přesné počty tokenů; nelze je automaticky připsat obrazovému
modelu či této úloze při souběžných úlohách. Malé etapy může zakrýt
celočíselné zaokrouhlení. Výpočet Blenderu sám není spotřeba LLM tokenů.

## První pozorování

Čp. 263 má pět horních skutečných otvorů, slepé zdobené plochy,
poškozené/vyjmuté výplně, obloukový vstup a pět nízkých oblých vikýřů.
Generovaný nápis není autoritativní: zachovat obraz písmen z původní fotografie,
nikoli generátorův přepis. Počet a provedení vstupů ověřit lokálně.
Plán obsahuje rozměr průčelí 10,28 m, starší GIS odhad 10,63 m; jde o
zdokumentovaný rozdíl podkladů, nikoli důvod deformovat archivní plán.

## Revize po kontrole identity

Původní předpoklad pěti vikýřů a nápisu byl chybný: převzatý FRONT patří jiné fasádě. Zjištěno před stavbou, uživatel informován a pověřil samostatným rozhodnutím. Čp. 263 je nízký tříosý dům bez tohoto nápisu; nový podklad vychází z ČB fotografie a plánu. Starší FRONT, jeho editace a původní agregovaný GLB jsou odmítnuté reference. Podrobnosti a obrazové důkazy: evidence/identity_resolution.json. Dva střešní otvory doložené přehledovým snímkem nahradí chybný předpoklad pěti; jejich hloubka a zadní napojení jsou hypotéza.

## Revize po kontrole identity

Původní předpoklad pěti vikýřů a nápisu byl chybný: převzatý FRONT patří jiné fasádě. Zjištěno před stavbou, uživatel informován a pověřil samostatným rozhodnutím. Čp. 263 je nízký tříosý dům bez tohoto nápisu; nový podklad vychází z ČB fotografie a plánu. Starší FRONT, jeho editace a původní agregovaný GLB jsou odmítnuté reference. Podrobnosti a obrazové důkazy: evidence/identity_resolution.json. Dva střešní otvory doložené přehledovým snímkem nahradí chybný předpoklad pěti; jejich hloubka a zadní napojení jsou hypotéza.

## Dodatek: povinná rešerše plánů — 27. září 2026

Před každou další modelací začít vyhledáním stavebních plánů cílového domu, sousedů a ulice v databázi. Pro tuto řadu dodatečně porovnány plány 1910, 1939 a zaměření 1964/1965; viz `../kulova_identity_plans_2026-09-27/REPORT.md` a `plan_search.json`. Nízký 263 je identifikován, jeho půdorys je však členitější než pracovní obal modelu. Sporný FRONT 263 pracovně odpovídá 264; přesné hranice výřezu nejsou potvrzené. Tento audit nemění uložený model ani původní ZIP a nepředstírá, že rešerše celé sady proběhla před jeho stavbou.
