# Čp. 40 – celý pracovní model r9

Výstupy pouze lokální, původní soubory a starší varianty zachované. Model není dosud plně historicky a metricky validovaný.

## Opravy a uzavřené výrobní kroky

- Dlouhá A: šest horních oken, sedm přízemních/suterénních otvorů; krátká B: dvě horní okna a dva portály; podkroví A: dvě okna. Celkem 19 otvorů, 177 ploch fotografického průčelí a výplní, 84 ploch ostění a říms. Hloubky 0,12–0,18 m a římsy 0,055 m jsou hypotézy, jemná profilace rámů je převážně fotografická textura.
- První široká rectifikace B obsahovala tři okna sousedního domu. Výkres průčelí čp.40, půdorys a fotografie cp_40_002 vedly k vyřazení této části. Neplatnou pětiosou verzi r7 zachováváme jako doklad neúspěšné validační smyčky, nikoli doporučený model. Starší generované FRONTy nejsou geometrická pravda.
- A vychází z rectifikované původní fotografie s fotografickou luminancí a místně registrovanou barvou. B rovněž zachovává originální luminanci. Původní nápisy, poškození a zrna nebyly přegenerovány. Perspektivní zkreslení a rozostření fotografie se tím automaticky nestávají přesnou ortofotografií.
- Jedna skutečná builtin editace UV atlasu; při skládání přesně chráněné známé pixely, žádná zbývající magenta. Využito 84 ze 100 připravených návratových polí; zbytek se po opravě hranice domu nepoužívá. Střecha, skrytá omítka a komín mají vygenerované materiály. Kamenitý povrch komína je pracovní doplněk, nikoli doložená skladba.
- Střecha po kontrole výkresu změněna z chybného podélného hřebene na hřeben v hloubkovém směru, s přední valbou nad dvěma podkrovními okny. Výška hřebene 12 m, komína 12,9 m a skrytý průběh střechy jsou pracovní parametry. Zděděné zadní zalomení je ponechané, s povrchovou hypotézou; není rekonstruován doložený interiér.
- Závěrečné maskované RGB sladění zelené omítky podle vlastní krátké fasády, bez nové obrazové generace. Viz colour_match.json; všechny materiálové hypotézy provisional, locked:false. R7 měla barevný vzorek z přesahu sousední stěny, konečná r9 jej nahrazuje vlastním B.
- R7 renderovací názvy kolidovaly s externími A/B texturami. V r8/r9 mají rendery příponu _render, textury byly obnoveny z původních mezivýstupů; finální Blender používá vložené obrazy. Starý r7 není předávací model.

## Kontroly

Nový import GLB: 7 vložených obrazů, 1110 texturovaných trojúhelníků, 0 kolapsů UV, maximální vzdálenost vrcholů 0.0 m. Technické QA potvrzuje export, nikoli historickou správnost. Čtyři rendery a nový import zkontrolovány samostatně.

## GIS a neuzavřené důkazy

Kandidát objekt105 / čp.40, Horova–Úzká. Model A17,538 m / B8,978 m, mapové kandidátní hrany22,606 /8,683 m. Tříbodový afinní fit má měřítka1,289 /0,967; není nezávislé ověření. Transformace do modelu nebyla aplikována a náhradní náhodná výška GIS nebyla použita. Zpětný převod místních souřadnic a EPSG:5514 ověřený. Předběžné čtení měřítka výkresu 1972 naznačuje A kolem16m a B kolem8,5m; přesné odečtení vyžaduje kalibraci skenu, ne slepé natažení na GIS.

Výkresy cp_40_003 až006 jsou skutečné plány, nekolorovány. cp_40_002 a širší cp_40_001 jsou fotografie; chybné starší označení PLANE u fotografie je opravené pouze v lokální evidenci. Sdílený snímek cp_39,40 ukazuje jinou epochu obchodních portálů; cp_457,40 zachycuje dvorní zástavbu s nejistou příslušností stěn. Proto bez automatického přenosu do pozdní uliční varianty.

K plnému uzavření zbývá nezávisle potvrdit délku a majetkovou hranici v GIS, kalibrovat výkres a střechu, určit zadní stěny a epochu dvorních zdrojů. Celkový plán rohových domů není hotový; plně validovaných domů stále0. Hotové uliční plochy není nutné vyrábět znovu.

## Otevření

Spustit python serve.py, otevřít http://127.0.0.1:8774/. Balík má lokální Three.js, původní i nový model, zdroje a validační podklady. Uploady a změny živé Libuše:0.
