# Aktualizace celého domu174 – r29

Opraven směr řádků krytiny na590 plochách: UV nyní sleduje lokální okap a směr stoupání jednotlivých střešních rovin, nikoli globální osuX.32 svislých štítových ploch dostalo existující materiál omítky. Geometrie celého modelu zůstala přesně shodná; žádná nová generace. Fresh GLB13 obrazů,10462 trojúhelníků,0kolapsůUV,odchylka0. Nové pohledy celého domu jsou součástí tohoto balíku.

## Oprava předchozího závěru GIS

Původní porovnání17,411/10,552m s plnými GIS hranami nebylo srovnatelné: modelové délky vynechávaly zkosené nároží. Průsečík prodloužených fasád dává plné délky12,333 a19,347m. To samo neprokazuje významný rozměrový nesoulad. Předchozí zpráva níže zůstává jako historie, tento odstavec má přednost.

Nově je doložen kandidátní afinní fit nároží a obou konců uličních stěn k GIS69/čp174. Vazbu podporuje GIS ulice28 (Široká / Zd.Nejedlého) a poloha sousedních175/176/22. Singulární měřítka0,95455 a1,05968; kontrola protějšího virtuálního rohu dává0,632m. Průsečík není fyzický roh zkosené budovy a tři použité body nejsou nezávislá validace. Konvexní obal v překryvu také nedokládá vnitřní dvorní členění.

Model zatím nebyl přepsán do souřadnic GIS. Registrace je kontrolovatelný návrh se stavem provisional,locked:false, nikoli schválená poloha. Další krok je ověřit protější skutečný roh/dvorní rozsah v historickém plánu a přesný stav střechy. Výškový proxy GIS se nepoužil. Celých historicky a GIS validovaných domů stále0; pracovní balík174 není důvod pro opakování již hotových ostění.

---

# Čp. 174 – celý dům, lokální pracovní varianta r27b

Zpracováno 2026-09-09T10:48:48.460085+00:00. Výstup je společná pracovní varianta celého domu, nikoli schválená historická rekonstrukce. Kompletní plán všech rohových domů není hotový.

## Co obsahuje

- Obě uliční fasády se zachovanými dřívějšími opravami otvorů a 218 ostěními A/B/arkýře.
- Dva zdrojově registrované oblouky arkýře a pracovní konzolu; jemná ornamentika zůstává částečně v textuře.
- Novou variantu poškozené střechy: 590 původních střešních ploch sníženo, 36 ploch vzdáleného štítu ponecháno. Dvě fotograficky vedené atikové části, otvorové výplně zapuštěné o 0,10 m.
- Skrytou krytinu a omítku ze skutečného maskovaného builtin doplnění. V tomto dokončovacím běhu 1 editace, ve v5 celkem 20. Známé pixely mimo masku shodné. Hloubka atikových stěn 0,18 m, skryté stěny a střešní sklon jsou model_hypothesis / provisional / locked:false.
- Závěrečné sjednocení B omítek RGB násobky 1,015 / 1,005 / 0,995 v masce světlé teplé omítky. Generovaná skrytá omítka tónově ztmavena. Bez prostorových změn a bez přegenerování fasád; masky a přesné parametry v plaster_channel_qa.json. Pro čp. 174 není historická žlutá doložena, reference zůstává teplá šedokrémová.
- GLB, editovatelný Blender, čtyři pohledy, nový import, fotografie A/B, lokální 3D prohlížeč s přepnutím předchozí verze, mapa okolí a úplný GIS záznam.

## Kontroly a skutečné omezení

Fresh import GLB: **13 obrazů, 10 462 texturovaných trojúhelníků, 0 kolapsů UV, odchylka vrcholů 0**. První export r27 odhalil 8 numerických trojúhelníků do 9,5e-8 m²; r27b odstraňuje pouze přesně spárované trojúhelníky, ostatní smyčky UV zachovává. 1036 dřívějších samostatných objektů otvorů/ostění/arkýře má nezměněnou geometrii, UV a přiřazení materiálů.

Vizuálně prohlédnuty nároží, A, B, zadní strany a opětovný import. R26 ukázal nevhodný průhled atikovými otvory na krytinu, r27 jej nahradil původními fotografickými výplněmi. Prohlížeč načetl nový i předchozí GLB. Technické QA nepotvrzuje přesnou historickou geometrii. Zadní fasády nejsou doložené fotografie, jejich materiál a chybějící detaily zůstávají hypotézou. Jemné zbytky zděděných říms a návaznost atikových segmentů vyžadují další geometrické posouzení; nízký sklon krytiny je pracovní varianta, nikoli měření.

**GIS není uzavřen:** lokální snapshot obsahuje čp. 174 / objekt 69 s obdélníkovým půdorysem 239 m²; hrany 18,65 / 12,45 / 19,08 / 12,90 m. Model má členitější půdorys a použité fasádní délky 17,411 / 10,552 m. Samotný rozdíl délek ani shoda čp. neprokazují chybu historického GIS. Není doložena společná soustava kontrolních bodů ani přesná příslušnost všech modelových částí. **Model nebyl naslepo zvětšen ani vložen do mapy.** Mapa zobrazuje zdrojový GIS samostatně; source EPSG:5514, origin i zpětný převod ověřeny, výškový proxy 9,5 m nepoužit. Potřebné navázání: ověřit nároží a konce obou uličních stěn proti historickému plánu a sousedům 175/22, poté rozhodnout o rozsahu dvorní části, transformaci a výšce.

Závěr revize: **celý dům je zabalen a prohlédnut, ale nelze jej zatím započítat mezi plně validované domy**. Stav plně uzavřených domů zůstává 0. Další práce na 174 se má týkat nedoložené geometrie/registrace, nikoli opakování hotových ostění nebo další inventury.

## Použití a zachování dat

V této složce spusť `python serve.py` a otevři `http://127.0.0.1:8769/`. Server poslouchá pouze na localhost a zpřístupňuje pouze tuto složku. Všechny potřebné knihovny prohlížeče jsou přibalené. Model lze otevřít také přímo v Blenderu.

Původní data a varianty zůstaly zachovány. Ověřeno 741 hashových položek dřívějších checkpointů (741 unikátních souborů). Žádný upload ani zápis do živé Libuše. Nový balík je pracovní lokální výstup; contains no authenticated API configuration.
