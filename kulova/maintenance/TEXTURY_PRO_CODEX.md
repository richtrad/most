# Kulová – jak doplnit texturovaný dům (pro Codex)

Stránka `/most/kulova/` ukazuje základní geometrii všech 15 domů. Od 18. 10. 2026 má také samostatný horní náhled a pět texturovaných studií čp. 111, 261, 262, 265 a 266. Samostatné pracovní studie nejsou automaticky schválené pro vložení do celé ulice.

## Samostatná pracovní studie – současný bezpečný postup

- Záznam patří do `data/textured-studies.json`; obsahuje cestu GLB, náhled, českou/anglickou poznámku, SHA-256 a výslovné `historical_qa_passed: false`, `street_approved: false`, dokud neproběhne příslušné schválení.
- `data/textures.json` používá `study_glb` a `study_url`, ale `glb` ponechá `null`. Tím se pracovní revize nepropaguje do ulice. Starší čp. 262 a čtyřosé čp. 266 jsou záměrně oddělené varianty.
- `house-preview.js` doplňuje horní výběr domu / geometrie / textur, včetně přiznané nedostupnosti u ostatních domů. `house-preview.css` je oddělený od původních stylů.
- U čp. 265 jde o G5/textured_v3, nikoli původní široký pětiosý odhad. `preview_width_m` a `preview_eave_m` v registru studií řídí pouze kameru samostatné texturované varianty; nemění GIS ani rozměry základní uliční sestavy. Šířka/půdorys a datace poškození střechy zůstávají neověřené.
- Po spuštění původního generátoru Claude **vždy spusť také** `python most/kulova/maintenance/render_textured_studies.py` z kořene webového repozitáře. Alternativně zadej `--site-root <cesta-k-most/kulova>`. Tento verzovaný generátor obnoví vložení komponent, aktualizuje stavové texty a znovu vytvoří CS/EN studie. Je idempotentní; modely ani polohy v ulici nemění.
- Webové kopie mohou překódovat barevné mapy do JPEG při zachované geometrii, UV, rozměrech obrázků, průhlednosti a datových mapách. Původní pracovní model se nepřepisuje. Ověř skutečný GLB v prohlížeči, ne pouze hash.

## Vložení do celé ulice – až po geometrickém a historickém QA

Následující starší rozhraní `glb` platí pouze pro model schválený k vložení do sestavy, nikoli automaticky pro zveřejněnou studii.

## 1. Model
- Vycházej z geometrické revize uvedené u domu v `data/textures.json` (`geometry_revision`, geometrie je i v `geometry_glb`).
  Pracovní BLEND revizí jsou ve složkách `kulova_geo_qa_claude_2026-10-18` (261 r5, 111 r6, 258 r4, 1608 r6),
  `kulova_geo_qa_claude_2026-10-17` (262 r6) a `kulova_5houses_claude_G_2026-10-16` (ostatní).
- Zachovej místní souřadnice domu (průčelí v rovině y = 0 v Blenderu, osa x podél průčelí) a jména objektů `CP_<čp>_*`.
  Neposouvej ani neotáčej celý dům: v ulici se texturovaný model vkládá pod uzel `CP_<čp>_root` sestavy.
- Export glTF binární (`.glb`), výchozí osa Y nahoru, textury vložené. Rozumná velikost: do 8 MB na dům,
  textury nejvýš 2048 px (JPEG nebo WebP).

## 2. Soubor
- Ulož jako `most/kulova/models/textured/cp<čp>.glb`.

## 3. Záznam v `most/kulova/data/textures.json`
```json
"262": {"status": "published", "label": "Codex: textury na revizi r6, QA ...", "glb": "models/textured/cp262.glb",
        "geometry_revision": "r6", "geometry_glb": "models/cp262.glb", "updated": "RRRR-MM-DD", "by": "Codex", "qa": "odkaz nebo popis kontroly"}
```
- `glb` je cesta relativní k `/most/kulova/`. Dokud je `glb` `null`, prohlížeč textury nenabízí.
- `label` se zobrazuje v informačním panelu ulice. Tabulky na stránkách se přegenerují při příští aktualizaci stránky.

## 4. Kontrola
- Stránka domu `/most/kulova/cp<čp>/`: v nabídce *Povrch* je *Textury (Codex)* a texturovaný dům překryje geometrii.
- Stránka ulice `/most/kulova/`: volba *Textury (Codex)* vloží dům na jeho místo v ulici; ostatní domy zůstanou geometrické.
- Pokud se texturovaný dům v ulici posune nebo pootočí, nesouhlasí místní souřadnice s geometrickou revizí (bod 1).
- Do souborů nepatří adresa API databáze, UUID ani uživatelská ID.

Generátor stránky (Claude): `F:\MOST\output\grafit_kulova_street_publish_20261018\gen\`. Soubor `data/textures.json`
generátor jen čte; po prvním vytvoření ho nepřepisuje.

## Kontrola uzavřeného podkroví – povinná od 19. 10. 2026

Ve studii čp. 265 byla vidět škvíra pod střechou. Claude proto 19. 10. 2026 doplnil do pěti studií
(111, 261, 262, 265, 266) uzavírací geometrii: podkrovní blok až pod krytinu a uzávěry podbití pod okapy
(objekty `*_AtticClosure*` a `*_EaveClosure_*`, tmavý jednobarevný materiál). Existující sítě, UV a všechny
obrázky zůstaly bajtově stejné; záznam je v `data/textured-studies.json` u klíče `geometry_patch`.

- Před každým nahráním modelu nebo studie spusť z kořene repozitáře:
  `blender -b --python most/kulova/maintenance/check_see_through.py -- vysledek.json model.glb`
  Publikuj jen při `passed: true` (nejvýš 3 vlasové zásahy, nekryté zdivo ≤ 0,5 m², střecha nad prázdnem ≤ 1 m²).
  Doložené díry ve střeše zapiš jako výjimku s pramenem.
- Nové geometrie 19. 10. 2026 mají tuto úpravu přímo z builderu: `F:\MOST\output\kulova_eave_fix_claude_2026-10-19\`
  (předávka `CODEX_HANDOFF_20261019.md`). Čp. 265 r5 má čtyři osy (4 okna nahoře, 3 dole, obloukové dveře vpravo);
  Codexova studie na r5 je publikovaná od 19. 10. 2026 (zdroj `kulova_handoff_intake_2026-10-19`).
- Základní sestava ulice na webu je návrh r14: 111 13,30 m, 265 12,70 m, 266 11,85 m (GIS 11,43 / 15,23 / 11,19 m).
  Kanonický registr se nemění; rozhodnutí o šířkách je otevřené.
