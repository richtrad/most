# MOST: FRONT, UV inpainting a 3D model celé ulice

Verze postupu 1.0, 5. září 2026. Referenční výsledek:
[Kulová v5](../output/kulova_front_inpaint_v5_2026-09-05/README.md).
V této referenci byl novou metodou dokončen materiál čp. 262, okolní domy byly
převzaty. Tento postup rozšiřuje stejné zpracování na jednotlivé domy celé ulice.

## Spuštění dedikovaného agenta

V úloze otevřené v projektu MOST napiš například:

> Použij $most-street-texturer a zpracuj celou ulici [název ulice] postupem
> Kulová v5. Použij ověřené kolorované FRONTy z databáze, geometrii, text
> a poškození kontroluj podle původních fotografií. Doplň skryté plochy
> skutečným UV inpaintingem, vytvoř modely domů i celé ulice a odevzdej
> Blender, GLB, prohlížeč, porovnání a evidenci. Existující verze zachovej.
> Po vlastní kontrole pilotu pokračuj všemi bezpečně zpracovatelnými domy.

Registrovaný specialista se jmenuje `most_street_texturer`; má projektovou
konfiguraci `.codex/agents/most-street-texturer.toml`. Postup lze vyvolat
také přímo přes skill `$most-street-texturer` v
`.agents/skills/most-street-texturer/`. Přebírá model a oprávnění úlohy.
Nevytváří automatický časový plán ani běh bez zadání konkrétní ulice.

Instalace používá samostatný TOML s `name`, `description` a instrukcemi a
projektový skill podle [oficiální dokumentace agentů](https://learn.chatgpt.com/docs/agent-configuration/subagents)
a [lokálních skills](https://learn.chatgpt.com/docs/build-skills). Pokud se nově
přidaný skill ve výběru neobjeví, znovu otevři úlohu nebo restartuj aplikaci.

## 1. Inventura celé ulice a důkaz identity

Agent nejprve najde existující výstupy a stav dávky, přečte `AGENTS.md`,
[kolorizační postup](../color_reference/COLORIZATION_WORKFLOW.md), databázi
barev a přiřazení pro ulici. Inventura zahrnuje všechna zadaná čp., i ta bez
modelu nebo vhodného snímku. Převzatý okolní dům není dokončením nové metody.

Živým GET z Libuše ověří oblast, strukturu, konkrétní přílohu a její obsah.
Zapíše UUID, jméno, datum, SHA-256 a zdroj. Jméno souboru ani databázová vazba
samy neurčují, který dům či stěna jsou na snímku. Rozhoduje porovnání
architektury, popis fotografie, další bezpečně identifikované snímky a plány.
Snímek označený `PLANE,BW` se nekoloruje; plán může podpořit geometrii.

Každý dům může mít více samostatně doložených fasád. U rohového domu agent
porovná obě uliční stěny a clay rendery nejméně ze čtyř hlavních stran.
U každé fasády uloží zvolenou stranu, normálu, lokální souřadnice a obrazové
důkazy. Bez potvrzení nechá stranu neurčenou. Modelový CR FRONT a hypotetický
GIS FRONT zůstanou rozlišeny i v přehledu výsledků.

Pokud FRONT chybí, vznikne podle navazujícího projektu pro extrakci FRONTů,
po jeho vlastním QA. Pokud chybí model, agent při zadání rekonstrukce celé
ulice vytvoří doložený základ v Blenderu; rozměrové odhady označí. Pokud
chybí důkaz identity či půdorysu, pozastaví konkrétní dům s uvedením důvodu.

## 2. Zachování zdrojů, období a materiálů

Nová dávka má vlastní adresář `output/<ulice>_front_inpaint_<verze>/`.
Zdrojové fotografie, FRONTy i vstupní modely jsou neměnné. Každý dům má
vlastní adresář, vlastní konfiguraci a checkpointy. Sdílené fotografie
se zbytečně negenerují znovu; evidují se jejich ověřené vazby na domy.

Materiálová ID musí odpovídat databázi a stejnému období. Uzamčená přiřazení
se nemění bez důvodu a příslušného oprávnění. Neznámé barvy, skryté plochy,
odhadnutá geometrie a generativní doplnění mají `confidence: model_hypothesis`,
`status: provisional`, `locked: false`. Smíšené datace ulice jsou přiznané.

Agent nezačne drahým generováním všech domů současně. Vybere jeden typický
dům a případně druhý rohový, dokončí vlastní QA a pak pokračuje dávkou.
Nežádá znovu o souhlas, který zadání už poskytlo. Existující oprávnění pro
upload archivních kolorovaných snímků a CR FRONT/_mult platí po jejich QA
a následném `verify`; syntetické UV atlasy a GLB nejsou archivní fotografie.

## 3. Geometrie a přesná registrace FRONTu

Databázový kolorovaný FRONT dodává barevný obraz. Původní černobílá fotografie
je rozhodující pro doložené poškození, otvory, písmo a architektonické tvary.
Generovaný FRONT není neomylná ortofotografie: může změnit nadokenní tvar,
vynechat ceduli nebo zjednodušit komíny. Agent tyto rozdíly identifikuje;
v nové vrstvě je opraví podle zdrojového důkazu, případně popíše omezení.

Pro každou fasádu vytvoří mapu kotev: obě hrany všech oken a dveří, parapety,
římsy, okap, rohy a změny podlaží. Jediná transformace celé stěny ani středy
oken obvykle nestačí. Použije po částech definovanou registraci s návazností
mezi podlažími a zkontroluje overlay hraničních linií. Nezavádí nové otvory,
ani nepřekresluje dokumentované poruchy za účelem snadnějšího mapování.

Čelní omítka, ostění, rámy, sklo, kov, dřevo a střecha musí mít správné
materiálové oddělení. Omítka nesmí vytvořit světlý lem přes úzký dřevěný rám.
Pro rámy se používá vhodný zdrojový výřez dřeva a jeho fyzické měřítko.

Nápisy se uchovají jako samostatné RGBA vrstvy skutečných fotografovaných
písmen. OCR může pomoci se čtením; generované či nově vysázené písmo nenahrazuje
historický obraz. Chybějící nápis ve FRONTu se přenese z původní fotografie.
Nečitelná písmena se nedoplňují domněnkou.

## 4. Doplnění skrytých ploch inpaintingem

1. Rozdělit polygony na doložené čelní plochy a nedoložené návratové plochy:
   boky pilastrů, ostění, parapety, spodky říms, výstupky, rámy a další části.
   Přední projekce na kolmém boku zkolabuje; každý bok dostane skutečné
   dvourozměrné UV podle lokální tečné báze a rozměru v metrech.
2. Připravit materiálové terče s viditelným fotografickým kontextovým pásem,
   místem pro pokračování a ochrannými mezerami mezi ostrůvky. Uložit binární
   masku **0 = zachovat, 255 = doplnit**, materiálová ID, měřítko a orientaci.
3. Prohlédnout terč a provést skutečnou editaci vestavěným obrazovým modelem.
   Na jeden terč jeden výstup. Prompt požaduje pokračování konkrétního
   materiálu, stáří, trhlin, šmouh a směru stékání; zakazuje nové stavební
   prvky, nápisy, perspektivu a osvětlení kreslené do atlasu.
4. Uložit úplný prompt, vstup, masku, původní generaci i použitý nástroj.
   Přesně uvést, zda běžel vestavěný imagegen nebo jiný skutečně spuštěný
   nástroj. V5 vychází z principu [StableGen](https://github.com/sakalond/StableGen),
   ale sama plugin StableGen ani ComfyUI nepoužila.
5. Model může změnit kontext nebo velikost výstupu. Generaci zarovnat a
   přes masku deterministicky vložit do původního terče. Mimo masku musí
   být maximální pixelová chyba **0**. Při změně proporcí zastavit a
   zkontrolovat registraci, nikoli slepě deformovat obsah.
6. Doplnění přenést na skutečné UV plochy, sjednotit návaznost na chráněných
   hranách a zapečit atlasy s gutterem. Jemný detail a směr materiálu
   přizpůsobit fyzickému měřítku. Oddělit sRGB barvu a nebarevná PBR data.

Povrch má zůstat omšelý podle fotografie: chybějící omítka, špína, ohoření,
vyražené tabulky, prázdné otvory a poškozené rámy. Skryté opotřebení lze
věrohodně doplnit, ale jeho přesný průběh není doložený. Z jasové fotografie
se nesmí bez kontroly vyrábět reliéf světel/stínů. Výsledek s fotografickými
stíny není čistý PBR sken a nemá být tak popisován.

Vzor čp. 262 měl 16+4 kontextové dlaždice, dva 4096² atlasy a gutter 6 px.
Pro další domy jsou to výchozí vodítka, ne pevná čísla. Texturové rozlišení
má odpovídat zdroji, požadovanému detailu a naměřenému chování prohlížeče.

## 5. Fronta, obnova a kontrolní stavy

Nástroj [batch.py](../tools/most_street_texturer/batch.py) spravuje jeden
záznam na dům a více fasád uvnitř. Detailní formát, příkazy i důkazy jsou v
[BATCH_FORMAT.md](../tools/most_street_texturer/BATCH_FORMAT.md).

Posloupnost je `ready → front_mapped → inpainted → baked → qa_passed → complete`.
Každý přechod vyžaduje pojmenovanou kontrolu, čas, kontrolujícího a existující
artefakty. Hashy chrání zdroje, checkpointy i důkazy. JSON samotný kvalitu
neposuzuje; agent musí snímky a modely opravdu otevřít. Vizuálně nejasná
položka je `blocked`, nepříslušná položka `not_applicable` s důvodem.
Chybějící zdroj není důvod obejít kontrolu jako „nepříslušný“.

Při obnově: kompaktní `status`, potom `verify`, potom `next`. Skript sám
nespouští obrazové generování ani Blender a neprovádí API zápisy. Pokračování
z existujících generací je oddělené od nového generování. Jeden proces
zapisuje společný manifest; Blender a GPU běží po jedné úloze.

Pokud obrazový nástroj není dostupný, agent připraví masky a prompty a
zaznamená konkrétní blokaci; nevydává procedurální šum za hotový inpainting.
Při změně již použitého zdroje vzniká nová verze. Při chybě uploadu se
zastaví dotčený zápis a ověří stav API.

## 6. Vizuální a technické QA

### Povinná sada skutečných vizuálních testů

Každý dům se před označením `qa_passed` otevře v reálném prohlížeči nebo
renderu a projde touto sadou. Sada se provádí nad texturovaným modelem i nad
jedním clay/no-texture průchodem, aby se oddělila chyba geometrie od chyby UV
mapování. U rohového domu se v každém relevantním pohledu kontrolují obě
uliční fasády.

1. `axis_front`, `axis_right`, `axis_back`, `axis_left`: čtyři hlavní osy,
   zhruba z výšky chodce, s celým domem a okolními hranami.
2. `roof_oblique_front_left`, `roof_oblique_front_right`,
   `roof_oblique_back_left`, `roof_oblique_back_right`: šikmé pohledy z výšky
   nad okapem, ve kterých jsou čitelné roviny střechy, okna ve střeše, komíny,
   hřebeny, úžlabí, okapy a napojení štítu.
3. `detail_facade_*`: detailní výřezy každé vybrané fasády; minimálně okno,
   dveře, nároží/ostění, římsa nebo okap a každý zachovávaný nápis či výrazné
   poškození. Detail musí umožnit rozeznat, zda fotografie neleze přes rám,
   sousední stěnu nebo střechu.
4. `identity_source_click`: v interaktivním náhledu se klikne na každý pilotní
   dům a ověří se správné čp., fotografie/FRONT a plán v inspektoru zdrojů.

Povinné pohledy se ukládají s názvem, polohou/orientací kamery, časem a
poznámkou `pass`/`fail`. V manifestu je musí být možné dohledat například
v poli `visualQa.views[]`; chybějící snímek není implicitní průchod. Kontrola
musí výslovně posoudit: (a) natažení, zrcadlení a přetečení textury mezi
plochami, (b) měřítko a směr materiálu, (c) zarovnání oken, dveří, ostění,
říms, nápisů a poškození, (d) geometrii střechy a střešních otvorů a (e)
rozdíl mezi modelovou chybou a chybou textury. Technické `GLB loaded`, hash,
počet trojúhelníků ani nulové degenerace tuto kontrolu nenahrazují.

Pokud se v jediném povinném pohledu objeví výrazný texture bleed, nesmyslné
UV, chybějící střešní detail, nesedící otvor nebo hrubá geometrie, výsledek
se označí `qa_failed` nebo `blocked`, zapíše se konkrétní nález a dům se
nesmí skládat do ulice ani vydávat za porovnávací vítěznou variantu. Starší
verze zůstávají zachované pro porovnání.

| Kontrola | Co musí být doloženo |
|---|---|
| Identita a období | Správné čp., správné průčelí, zdroje a přiznané rozdíly datace |
| Přední pohled | Hrany všech otvorů sedí; žádná omítka přes rámy; přesný text |
| Levý a pravý šikmý pohled | Boky pilastrů, hloubka ostění, parapety a spodky říms bez tažení a švů |
| Detaily | Zachované poruchy a špína, rozbitá okna; žádná náhodná nová ornamentika |
| Inpainting | Uložený skutečný editační výstup; pixelová shoda mimo masku; žádné zbytky maskovací barvy |
| Geometrie | Neměnná proti schválenému vstupu, nebo konkrétní doložené změny; žádné nové náhodné otvory |
| UV a export | Nenulová geometrie nemá zhroucené UV; žádné čekající materiály; všechny používané mapy jsou v GLB |
| Chodníky a vozovky | U každé hotové dlaždice zobrazit vedle 1 × 1 také opakování 3 × 3; člověk kontroluje švy i nápadné opakování kamenů, skvrn a poruch. Samotná shoda hran nebo hashů nestačí. |
| Prohlížeč | Otevřené skutečné exporty, přepnutí materiálu/clay/generovaných ploch, čitelné zdroje a funkční stažení |
| Celá ulice | Správné polohy, měřítko, souřadné osy a spojení domů, jasné vyznačení nehotových částí |

Maskované složení a UV kontroly lze automatizovat. Fotografie, text a detaily
ostění vyžadují vizuální kontrolu. LOD se měří a kontroluje samostatně;
fungující velký GLB neprokazuje výkon na mobilu. Množství polygonů ani počet
souborů nenahrazují zprávu o skutečně dokončených domech a fasádách.

## 7. Předání celé ulice

### Povinná kontrola vstupů a zdvojených prvků (oprava čp. 261)

- Vikýře kontrolovat také v detailu zezadu, z boku a shora: uzavřený plášť,
  skutečné napojení do střešní roviny a souvislé čelo kolem otvoru. Pevně
  uříznutá extruze bez uzávěru není hotový vikýř. Neviděné konstrukční
  napojení označit jako hypotézu; technickou uzavřenost ověřit na hranách
  sítě a vizuálně v texturovaném i clay exportu.
- Schody a podstavu prohlédnout také zespodu při otáčení. Odstranit vnitřní
  překryvy a souběžné totožné plochy způsobující z-fighting; samotný klidový
  pohled zepředu tuto chybu neodhalí. Uložit detail spodního spoje a rotační
  kontrolu.

- U každých dveří zkontrolovat detail zepředu, oba šikmé pohledy a clay:
  spodní hranu křídla, práh, schody a návaznost na chodník. Schody se nesmějí
  mapovat na svislé dveřní křídlo; soklová římsa ani dolní část rámu nesmí
  procházet průchodem. Počet stupňů, výšku a nášlap odvodit ze zdrojů;
  při zakrytém vstupu uvést konkrétní pracovní hypotézu, nikoli historický fakt.
- Porovnat fasádu s geometrií zapnutou i skrytou: svody, žlaby, držáky,
  kabely, rámy a jiné samostatně modelované prvky nesmějí zůstávat podruhé
  nakreslené na zdi. Kontrolovat také fotografický stín a přidružené tmavé
  stopy. Samostatný 3D prvek zachovat; jeho obraz a související stopy odstranit
  skutečným maskovaným inpaintingem v odvozené textuře. Nesouvisející doložené
  poškození chránit a archivní zdroj neměnit.
- Uložit masku, skutečný výstup editace, pixelovou shodu mimo masku a stejné
  detailní kamery před/po. QA musí obsahovat `entrance_steps_reviewed` a
  `no_duplicate_geometry_in_albedo`, včetně nálezů pro každý vybraný vstup
  a svod. Chybějící detail není průchod. Dřívější úspěšná technická kontrola
  neomlouvá zdvojený svod nebo chybné schody; takový nález vrací model k opravě.

- Editovatelná `.blend` scéna s vloženými texturami a jednotlivými domy.
- GLB každého dokončeného domu a celé ulice, přiměřený LOD.
- Prohlížeč se zdrojovým inspektorem a zvýrazněním generovaných ploch.
- Přední i šikmá porovnání s fotografiemi, detaily poškození a oken.
- Manifest zdrojů, materiálových ID, hypotéz, použitých nástrojů, promptů
  a hashů; QA, přehled hotových/pozastavených/vynechaných domů a fasád.
- Obnovovací skript z uložených podkladů a ověřený ZIP bez chybějících souborů.

Celou ulici označit za hotovou až po kontrole sestavy. Pokud některé domy
nelze dokončit, odevzdat užitečnou částečnou sestavu a uvést přesné pokrytí
i potřebný chybějící podklad. Domy převzaté ze starší scény pojmenovat zvlášť.

## 8. Závěrečné sladění omítek mezi fasádami

Doplněno na přání uživatele 8. září 2026. Po kontrole geometrie, textu a
poškození přidej samostatný volitelný krok barevného sladění fasád téhož domu.
Předchozí podklady a modelové verze ponech jako dostupné alternativy.

1. Porovnej dominantní omítku na několika čistých plochách každé fasády.
   Vynech stíny, odkryté zdivo, nápisy, okna, dřevo, kov a barevně odlišné
   architektonické články. Stejné materiálové ID samo nezaručuje stejný odstín
   v generovaných obrázcích. Slaď stejný materiál jednoho domu, nikoli různé
   historické domy do jedné barvy. Respektuj doložené rozdíly nátěrů a epoch.
2. Použij referenční fasádu nebo uzamčené materiálové přiřazení. Pokud jde
   pouze o barevný rozdíl, výchozí metodou je deterministická úprava barevných
   kanálů, bez nového obrazového generování. Zaznamenej výběrové plochy a
   parametry transformace. Pracovní barva zůstává hypotézou.
3. Úpravu aplikuj jen do explicitní masky omítky. Vhodnou variantou jsou
   násobné korekce lineárních RGB kanálů s normalizací jasu každého pixelu.
   Zachovej lokální patinu, špínu, trhliny, chybějící omítku a fotografické
   stíny; nevyhlazuj ani neregeneruj texturu. Nezvyšuj sytost mimo přirozenou
   materiálovou rodinu a kontroluj ořez barev do gamutu.
4. Ulož vstup, výstup, masku, parametry a SHA-256. Mimo masku a ve zvlášť
   chráněných materiálech vyžaduj pixelovou shodu. Změř rozdíl reprezentativní
   chromatičnosti před/po a změnu jasu; taková metrika není dokladem historické
   správnosti ani celkové kvality rekonstrukce.
5. Znovu prohlédni oba FRONTy, detail hrany masky a společný nárožní render
   při stejném osvětlení. Při barevném švu, přebarveném rámu, změně písma nebo
   ztrátě patiny vrať krok k opravě masky či síly korekce. Teprve po tomto
   návratu ulož novou `.blend`/GLB verzi s vloženými opravenými texturami a
   ověř skutečný export. Geometrie a UV se tímto krokem nemění.

První lokální aplikace na čp. 42 a 191, včetně masek a měření, je v
[`libuse_corner_followup_v4_2026-09-08`](../output/libuse_corner_followup_v4_2026-09-08/).
Předchozí text postupu je zachovaný v této dávce jako
`MOST_STREET_TEXTURING_WORKFLOW_before_alignment.md`.

## 9. Kontrola registrace každého otvoru (čp. 261, 26. září 2026)

Předchozí kontrola bevel variant čp. 261 přehlédla zbytky fotografovaných
rámů vedle skutečných otvorů. Úspěšná kontrola zaoblení proto není důkazem
správné registrace fasády. Pro další domy je povinná následující kontrola:

1. Očíslovat všechna okna a dveře po podlažích zleva. U každého změřit
   levou, pravou, horní a dolní hranici fotografované výplně i 3D otvoru.
   Rozlišit vnější minerální šambránu, dřevěný rám a čistý otvor; samotný
   střed okna ani symetrický předpoklad nejsou dostatečné kotvy.
2. Otevřít každý otvor v detailu zepředu a zleva/zprava přibližně pod
   25–40 stupni. Celý rám, nadpraží i parapet musí být v záběru. Hledat
   zejména druhý bílý sloupek, přerušené příčky vedle ostění, dveřní
   výplň na zdi, zdvojený parapet a chybně ukončený fotografický stín.
   Kontaktní tabule slouží jako přehled; podezřelý detail otevřít plný.
3. Doplnit clay průchod a kontrolu hran otvorů proti UV overlay. Ukládat
   per-opening nález, obě strany, kameru, verzi GLB a výsledek. Chybějící
   pohled není průchod. Číselná odchylka je pomůcka, nikoli automatické QA.
4. Rozhodnout podle původní fotografie: při geometrické chybě společně
   upravit otvor ve zdi, ostění, rámy, skla a parapet. Čelní UV přepočítat
   v souřadnicích fasády, aby se textura neposunula spolu s geometrií.
   Započítat šířku předního lemu: čistý otvor není střednice profilu.
5. Při zachované geometrii odstranit přesahující obraz výplně skutečným
   maskovaným inpaintingem odvozeného albeda; chránit okolní poškození.
   Generátor nesmí znovu vytvořit bílé rámy či vymyslet novou šambránu.
   Lze připravit širší materiálový donor, ale na model přenést pouze
   explicitní opravnou masku a ověřit nulovou změnu mimo ni.
6. Znovu prohlédnout všechny otvory, sousedy, schody a římsy ze stejných
   kamer. Zachovat předchozí verzi a porovnání G (geometrie) / T (textura).
   Generovaný FRONT není měřický důkaz; odvozené rozměry zůstávají hypotézou.

Referenční experiment: `output/kulova_cp261_opening_lab_2026-09-26/`.
Volba vítězné varianty a propagace do celé ulice jsou samostatné rozhodnutí.

