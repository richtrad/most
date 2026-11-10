# Kulová čp. 263 — pracovní model G

Vytvořen samostatný model, lokální web, původní podklady, plán, pracovní deník a vizuální kontrola. Předchozí čp. 261 a jeho veřejný web se nemění.

**Stav: pracovní hypotéza k prohlédnutí, nikoli schválený model pro uliční sestavu.** Přesné poškození a některé detaily generované fasády nelze potvrdit proti neostrému zdroji. Proto povinné historické brány nejsou označeny jako splněné; `batch.json` zůstává blokovaný pro propagaci. Technický a vizuální průchod tím není zaměňován za historickou validaci.

## Výsledek a zásadní rozhodnutí

Zamítnut starší chybně přiřazený FRONT 263 i agregovaný starý GLB. Identitu nízkého domu se třemi horními okny dokládá přehledový snímek s číslem 263, návaznost na čp. 262 a popsaný plán. Uživatel ponechal rozhodnutí agentovi. Dům má šířku 10,28 m podle plánu, hloubku 18,8 m, římsu 6,45 m a vzepětí střechy 5,7 m; nesouhlas se starším GIS odhadem 10,63 m je přiznán. Smíšené datování podkladů není vyřešené.

Výchozí G: geometrie pěti oken, dveří a niky se registruje k pracovní fasádě. Varianta T nebyla objednána ani vytvořena. Samostatné ostění, rámy, příčky, parapety, mělký práh, okapy, komín a dvě střešní formy. Vybrané hrany mají střídmé zaoblení 8–12 mm. Tři schody z jiného domu nebyly automaticky přeneseny.

## Kontroly a nalezené opravy

Uloženo 78 pohledů s kamerami plus snímek skutečného kliknutí na zdroje. Každé okno, dveře a nika má čelní a oba šikmé pohledy s texturou i bez ní. Dále čtyři osy, čtyři střešní rohy, detaily římsy, poškození, nároží, prahu, okapů a vikýřů. Viz `qa/visual_qa.json` a `qa/contact_*.jpg`.

Opraveno nespojité UV vikýře, doplněny skutečné okenní příčky, odstraněn nedoložený lem menšího střešního otvoru a vyřazena čtvercová záplata vzniklá nesouladem měřítka chráněného vzorku a generovaného okolí. Chráněný kompozit měl nulovou pixelovou odchylku mimo masku, přesto vizuálně neprošel. Finální doplňkové materiály jsou celé syntetické a jsou tak označeny. Obraz původní fasády nebyl pixelově zachován; ostré praskliny, rozbité tabulky a prkna jsou hypotéza.

BLEND znovu otevřen v Blenderu, pět textur zabaleno; GLB otevřen v Edge/Three.js. 4 886 trojúhelníků, 5,48 MB GLB, nulové degenerované UV trojúhelníky. Čelní mapa 1582 × 994, opakované materiály 512 × 512. To není rozlišení původní fotografie. Velké nedoložené stěny jsou bez vymyšlených otvorů; pravidelnost opakované textury a zjednodušený směr tašek na křivkách zůstávají omezení.

## Prohlížení a reprodukce

Spusťte `start_viewer.ps1`, potom http://127.0.0.1:8803/web/. Lze také v této složce spustit `python -m http.server 8803 --bind 127.0.0.1`. Web vyžaduje HTTP, ne file://. Obsahuje posuvníky ČB/barevná reference, před/po opravě UV a textura/clay, volbu kamer, skrytí okapů a zdrojový dialog.

Hotové modely: `models/cp263_G.blend`, `models/cp263_G.glb`. Zachován i první neúspěšný GLB pro srovnání. Pro reprodukci ze zachovaných obrazových výstupů: `extract_materials.py`, Blender `-b --python build.py`, `audit_blend.py`, poté `node render.cjs` a `contact_sheets.py`. Skripty mají lokální cesty k Blenderu/Pythonu/Playwrightu; při přenosu je upravte. `prepare.py`, `correct_identity.py` a `composite.py` jsou záznamy dřívějších fází, nespouštějte je přes finální výstupy. Regenerace obrazového modelu není deterministická. Finální materiály vybírá `extract_materials.py`.

## Využití účtu

| Fáze | Zbývá |
|---|---:|
| start_before_inventory | 94 % |
| after_inventory_and_plan | 93 % |
| after_identity_audit_and_rejected_cleanup_generation | 93 % |
| after_correct_identity_and_facade_generation | 92 % |
| after_uv_generation_and_geometry_export | 92 % |
| after_first_visual_qa_uv_fix_and_viewer | 91 % |
| after_final_geometry_and_material_review | 90 % |
| final_before_delivery | 89 % |

Rozdíly jsou celé procentní body společného týdenního limitu, nikoli počet tokenů této práce. Nejvyšší dosud pozorovaný rozdíl jedné měřené fáze je 1 bod; shodně u přípravy, nové fasády a iterací QA. Rozlišení neumožňuje určit jednoho vítěze. Hodnota 0 neznamená nulovou spotřebu. Tři volání obrazového modelu (1 zamítnutá editace, 1 fasáda, 1 atlas) nelze z těchto údajů samostatně ocenit. Souběžná práce na účtu může ovlivnit výsledek. Poslední vzorek je v `usage.json`.

## Co zbývá před propagací do ulice

Přesnější registrace a historicky věrný FRONT se zachováním skutečných detailů, pokud možno z kolmějšího a ostřejšího snímku; ověření epochy a půdorysu; znovu všechny vizuální kontroly po případné změně. Tento balík se automaticky nenahrává jako ověřený databázový FRONT. Živé API Libuše bylo nedostupné (timeout), žádné vzdálené záznamy se neměnily.

Finální měření: zbývá 89 % proti 94 % na začátku, tedy rozdíl 5 procentních bodů společného limitu. Závěrečná kontrola, oprava materiálů a dokumentace tvoří poslední přibližně jednobodový interval.
