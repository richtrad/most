# Kulová čp.259 — pracovní rekonstrukce SOL6.1, 2.10.2026

Zpracována jedna fasáda podle fotografické reference s11 otvory (9oken,2vstupy), vlastními ostěními, prahy a parapety. Editovatelná scéna a GLB mají lokální zaoblení C8mm/3segmenty, uzavřenou pracovní střechu a dva komíny. Předešlé domy zůstaly zachovány.

## Prameny a důležitá omezení

Prvním krokem byla živá rešerše všech příloh oblasti, cílového domu a sousedů. Metadata Libuše ověřena GET2.10.2026. První síťová chyba byla blokace lokálního socketu, nikoli výpadek serveru; povolený read-only GET uspěl. Pět plánů258 bylo otevřeno: nízký magazín1888 a dvorní křídlo1910 nejsou uliční průčelí. Proto vybráno259.

Otevřeny oba plány259. List1871 ukazuje čtyři osy, dvě podlaží, vstup třetí zleva, půdorys a řez. List1874 navrhuje další podlaží; fotografie kolem1968 je dvoupodlažní a má jiné otvory. Návrh není důkaz provedení. Přesný rozměrový vztah a rozsah domu za pravým okrajem fotografie nejsou vyřešeny. Zvolená pracovní šířka14m a hloubka10m nejsou zaměření. Zadní stěny jsou bez domyšlených otvorů; hypotetická skořepina nesmí být zaměněna za doložený dvorní objekt.

Starý databázový CR FRONT259 se třemi okny ve štítu je v rozporu s ručním označením259 napravo na archivní kartě. V této práci byl odmítnut, archivní upload ani metadata se nepřepisovaly. Nové albedo vzniklo rektifikací barevné fotografie řady. Jeho známé části se nepřegenerovaly. Dřívější kolorování odstranilo stromy a doplnilo zakrytá místa: také tato místa jsou hypotéza. Zdrojový malý výřez nedovoluje ostré historické detaily,1536×1200 pouze zvětšuje existující obsah.

## G a materiály

Každý otvor má uložené čtyři pixelové hrany a vlastní souřadnice. Žádné stejné rozměry oken nebo počet schodů nejsou zkopírovány z261. Photografická výplň je v hloubce0.285m, rám a ostění mají skutečný objem. Vnitřní kresba výplně zůstává fotografická, nejde o detailní rekonstrukci všech okenních příček a interiéru. Varianta T nevznikla.

Vestavěný imagegen skutečně doplnil UV atlas ze zdrojových materiálových pásů. Uložen terč, binární maska, plný prompt, surová generace a deterministický kompozit. Maximální chyba mimo masku0. Materiálová kresba doplněných ploch je provisional/unlocked. Barevná pracovní volba ochre/charcoal se eviduje samostatně od starého přiřazenícream/clayred; do databáze barev se nezapisovalo.

První browser kontrola odhalila levitující komíny, příliš světlé parapety a opakování omítky na velkých bocích. Komíny protaženy dovnitř střechy; parapety dostaly fotografické čelo a tmavší boční materiál. První model i jeho snímky jsou v models/initial a qa/initial. Velké boky dostávají samostatné souvislé doplnění; malé ostění používá původní atlas. Práh má vlastní plný podklad; neověřené schodiště se automaticky nevymýšlí. Samostatný svod není doložen ani přidán. Jednoduchý přední žlab je pracovní hypotéza; albedo průčelí začíná pod ním.

## Kontrola a stav předání

Skutečný GLB otevřen v Edge/Three.js. Každé okno a dveře zepředu/zleva/zprava, stejné kamery clay,4osy,4střešní rohy, detaily římsy, nároží, poškození, komínů a prahu včetně spodku. Parametry kamer a hashGLB v qa/cameras.json. Výsledky v qa/visual_qa.json. Opětovné otevření BLEND ověřilo vložené obrazové soubory; GLB obsahuje vlastní vložené textury. Web má posuvníky fotografie/kolorování, textura/clay a materiál před/po. Obrázky pro článek jsou ve figures.

Historická geometrie zůstává **blocked**: přesné pokračování za fotografickým okrajem, shoda čtyřosého plánu s dnešním výřezem a dvorní rozsah. Model se nepropaguje do celé ulice ani do fotografické databáze. Jde o kompletně předanou pracovní verzi, nikoli finálně doložený celý dům. Toto je zásadní omezení hodnocení kvality. Jiný dům než Astra není kontrolovaný A/B test.

Využití účtu průběžně v evidence/usage.json. Zaokrouhlená účtová procenta neříkají přesné tokeny jednotlivých etap. Obrazové generování, Blender a browser GPU práce nejsou totéž co textové tokeny.

## Obnova

Spustitbuild.py vBlender4.5 z uložených textures; žádná nová generace se tím neprovádí. render.cjs vNode sPlaywrightEdge vytvoří celou sadu snímků. finish_materials.py reprodukuje původní malý atlas ze surového obrazového výstupu; runtime vyžadujePython/Pillow/NumPy. Žádné tajné tokeny nejsou součástí balíku.

Závěrečné výsledky:7344trojúhelníků, GLB6.41MB,6vložených obrazových textur,92kamerových pohledů+3klikové kontroly pramenů. Web7posuvníků, kontrolované odkazy a mobilní rozložení. Dva skutečné imagegen editační běhy; oba kompozity zachovaly chráněné pixely s chybou0. Všechny zaokrouhlené odečty účtového využití66%; z této přesnosti nelze určit tokenově nejnáročnější etapu.
