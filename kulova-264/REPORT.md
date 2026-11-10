# Kulová: pracovní čp. 264, varianta G

27. září 2026. Nová samostatná verze; žádný starší dům, archivní snímek ani vzdálená databázová vazba nebyly přepsané.

## Výsledek a hranice spolehlivosti

Model představuje úzký dům s obchodní výkladnicí, třemi skutečnými horními okny, jedním slepým panelem a pravým vstupem. Obsahuje skutečné ostění, oddělené výplně a rámy, vystupující dřevěnou výkladnici, parapety, nízký práh, levý svod a tři pracovní střešní otvory. Exponované hrany parapetů, prahu a obchodní římsy mají zaoblení 8 mm, tři segmenty. Výchozí strategie G; varianta T nebyla vytvořena.

**Jde o pracovní rekonstrukci, nikoli historicky schválený dům pro uliční sestavu.** Kritickým omezením zůstává nepřímé přiřazení přesné fotografické hranice k čp. 264 a kombinace plánů různých let. Boční a zadní fasády nejsou fotograficky doložené; jejich otvory nejsou vymyšlené. Zadní zastřešení, přesné výšky, hloubky ostění a konstrukce střešních otvorů jsou odhady. Komín nelze bezpečně přiřadit v pozdější fotografii; model jej zatím nepředstírá jako doložený.

## Rešerše před stavbou

Prohledán místní databázový snapshot Libuše pro 261, 262, 263, 264, 111 a 265. Čp. 264 má tři plánové záznamy, z toho historický list 1887 a zaměření 1965 byly skutečně otevřeny. Pro 111 a 265 snapshot neobsahuje PLANE přílohy; to není důkaz jejich neexistence jinde. Podrobnosti, UUID a hashe: [plan_search.json](evidence/plan_search.json).

- List **264 / 1887**: šířka uliční části přibližně 7,4 m, úzká podélná dispozice. Nakreslené průčelí vpravo je označeno *Hintergebäude*: nesmí se zaměnit s uliční stranou.
- List **264 / 1965**: půdorys přízemí a sklepa. Ručně odečtený vnější obrys je uložen v landmarks.json v souřadnicích zmenšeného zobrazení 1862 × 1312 px; převod do metrů používá šířku 1887. Tato kombinace není přesným geodetickým zaměřením jedné epochy.
- **263 / 1910**, situační mapa: posloupnost 262–263–264–111.
- Originály **cp_111,263,264_001.jpg** a **cp_261,262,263_001.jpg**: návaznost na zdobený 262, nízký 263 a další úzké obchodní průčelí.

## Revize předchozího přiřazení

Předchozí audit pracovně přiřadil celý široký FRONT s nápisem k 264, ale ponechal neověřený levý pás. Podrobnější kontrola ukazuje, že tento FRONT není bezpečnou hranicí jediné budovy: obsahuje část obchodního průčelí a širokou sousední fasádu. Rozsah širokého celku neodpovídá úzkému půdorysu 264. Tento model proto odděluje užší obchodní průčelí. Sousední nápis se nepřenáší, jeho čp. se zde definitivně neurčuje a databáze se nepřejmenovává.

Oranžový obrys v [identity_boundaries.jpg](evidence/identity_boundaries.jpg) je pracovní interpretace. Pro konečné historické schválení je potřeba přímo označený uliční pohled nebo spolehlivá registrace dobové mapy a fotografií. Zpráva nezaměňuje opakovaný název souboru za nezávislý důkaz.

## Textura, geometrie a inpainting

1. Černobílá a již existující kolorovaná fotografie byly samostatně perspektivně narovnány; jejich transformace jsou v [registration.json](evidence/registration.json). Zdrojová fotografie má v této části jen stovky skutečných pixelů. Výstup 1400 × 1420 je převzorkování, nikoli nově získaný detail.
2. Barevný podklad již rekonstruuje sloupem zakrytou část. Je použit jako materiálová hypotéza, ne jako přesný fotografický důkaz každé skvrny. Tři okna, slepý panel a vstup byly porovnány s ČB originálem.
3. Nový obrazový běh vytvořil doplnění svodu a UV materiály. Změny fasády jsou omezené binární maskou; mimo masku zůstávají pixely barevného podkladu přesně shodné. Kompozice zahrnuje normalizaci jasu generované oblasti a přechod pouze uvnitř povolené oblasti. Nejde o důkaz shody starší kolorace s každým poškozením ČB fotografie.
4. První boční omítka měla zřetelné hranice ostrovů. Byla vyřazena a druhým obrazovým během nahrazena čistým pokračováním materiálu; kontext vlevo je pixelově chráněný. Periodická úprava dvacetipixelového okraje se týká pouze kompletně syntetické dlaždice. [Zkouška 3 × 3](evidence/plaster_repeat_3x3.jpg).
5. Výplně se skutečně nacházejí za stěnou. Plochy rámů a skel jsou rozdělené, takže za 3D příčkou neleží druhá celá fotografie okna. Čelní UV se nepoužívají na kolmých plochách. Strany bílých rámů mají barvu nátěru, nikoli tmavé dřevo nebo omítku.
6. Výkladnice sleduje polygon odečtený z obrazu; fotografie neleží jen na celé rovné zdi. Přesná prostorová konstrukce za zavřenou výkladnicí není doložená.
7. Svod je samostatný 3D díl. Pod ním se odstranil fotografický dvojník v úzkém pásu. Ostatní historické kotevní prvky ponechané v barevném podkladu nejsou současně zdvojené 3D objekty.

Barvy, skryté povrchy a konstrukční doplnění: `confidence: model_hypothesis`, `status: provisional`, `locked: false`. Nové materiálové atlasy nejsou nahrávány do databáze historických fotografií.

## Kontroly a nalezené opravy

První skutečný render v prohlížeči odhalil obrácenou normálu jedné samostatné okenní tabule a mřížku švů boční omítky. Zachované důkazy jsou v qa/initial/. Byla opravena orientace oddělených čelních ploch, barva boků rámů, rozdělení příček, opakování omítky a polygon vystupující obchodní římsy.

Závěrečné snímky a kamery jsou v [cameras.json](qa/cameras.json), jednotlivá zjištění v [visual_qa.json](qa/visual_qa.json). Technické načtení, vložené textury a nenulové UV jsou samostatná kontrola a nenahrazují vizuální ani historickou shodu.

## Obnova a využití

`build.py` v Blenderu obnoví BLEND a GLB. `render.cjs` otevře model v Edge/Three.js a uloží kamerové snímky; `start_viewer.ps1` spustí lokální web. Kopie zdrojů, editační terče, masky a oba obrazové výstupy jsou součástí složky.

Měření v [usage.json](evidence/usage.json): začátek 13 % využito / 87 % zbývá, po rešerši stále 13 %, po modelu, dvou obrazových editacích a prvních opravách 15 %. Jde o sdílený celočíselný účtový limit; nelze z něj odvodit přesné tokeny jednotlivé činnosti nebo oddělit souběžnou práci jiných úloh.

Další kontrola clay odhalila obrácený štítový list; jeho normály byly opraveny. U střešních otvorů se UV nově řídí délkou oblouku, tenké hrany mají vlastní metrické UV a boky se zapouštějí pod krytinu. Drobné přerušení fáze tašek na rozhraní zůstává materiálovým omezením.

## Závěrečný technický stav

Model má 4 509 trojúhelníků a čtyři vložené bitmapy. Uloženo 73 kamerových renderů a doklad kliknutí na zdroje. Vizuální kontroly provedeny, historické schválení zůstává zablokované. Poslední geometrická oprava odděluje spodek prahu o 5 mm od podstavy domu. Platný stav dodané verze sleduje `batch_final.json`; dřívější vývojový checkpoint je označen jako překonaný.

Poslední měření před předáním: **16 % využito / 84 % zbývá**, tedy změna o 3 procentní body od začátku této úlohy. Naměřené bloky: rešerše 0 bodů v rozlišení měřidla, model + dvě obrazové editace + první opravy 2 body, závěrečné QA/web/dokumentace 1 bod. Nelze je vydávat za přesné tokenové náklady oddělených operací.
