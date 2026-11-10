# Čp. 259 — nová alternativa fasádní textury

2. 10. 2026. Původní model, fotografie, textura, QA a ZIP zůstaly zachované.

## Co vzniklo

Vestavěný image_gen.imagegen provedl **pět skutečných editací**: celé průčelí podle původní registrované textury, plánu 1871 a vzorku omítky; následně čtyři samostatné detailové výřezy. Plné prompty: [prompts.json](prompts.json). Surové výstupy, terče, překryvové masky a registrační souřadnice jsou v této složce.

První generace byla nativně 1419 × 1109 px, nikoli požadované 4K. Detailové výřezy jsou přibližně 1410 × 1115 px; překryvové složení poskytuje **2688 × 2100 px**, 5,64 milionu pixelů oproti původním 1,84 milionu. Neoznačujeme interpolaci za nativní 4K. Jemnější kresba skutečně vznikla generací v jednotlivých výřezech. Nízkofrekvenční barva se sladila s první celkovou generací.

Pozice všech jedenácti otvorů byly lokální plynulou registrací vráceny k původním UV souřadnicím. Geometrie, UV, hloubka ostění, prahy, parapety, bevel a střecha se nemění. Nejde o alternativu T řešící historický nesoulad místo G: toto je uživatelem požadovaná syntetická materiálová alternativa na zachované G geometrii. Zdroje ani databázový FRONT nebyly přepsány.

## Přepínání

Nad interaktivním modelem je **Fasáda: Regenerovaná HD / Původní fotografická textura**. Přepnutí nemění kameru ani světlo. HD je výchozí; parametr ?texture=original otevře původní vzhled. Nový posuvník porovnává samotné textury. Exporty jsou models/cp259_SOL61_HD_v2.blend a .glb; staré názvy zůstávají původní verzí.

Test přepínače odhalil sdílení Source při Three.js Texture.clone(): při prvním zapojení se přepsal i obraz původní mapy v paměti. Oprava používá samostatný THREE.Source pro HD; test nyní výslovně kontroluje obě rozlišení, zachování kamery i návrat po clay režimu.

## Interpretace a omezení

confidence=model_hypothesis; status=provisional; locked=false. Nová kresba, množství drobného poškození, zpracování křídel a profilů jsou syntetická interpretace, nikoli informace získaná z archivu. Generátor zejména zjednodušil vnitřní členění nejširšího horního okna a přidal dekorativní kresbu dveří. Varianta slouží k porovnání vizuální kvality; pro archivní přesnost zůstává dostupná fotografická textura.

Plán 1871 má čtyři osy a jiné přízemí; jeho profily byly inspirací, nepřenesli jsme celý plán do pěti fotografických os. Historická blokace přesného rozsahu a identity z předchozího REPORT.md trvá. Detailnější textura ji neřeší a model nebyl propagován do potvrzené uliční sestavy ani nahrán jako archivní fotografie.

Kontroly: celá nová sada 92 browser renderů, všech 11 otvorů zepředu a obou šikmých stran, osy, střešní rohy, detaily a clay. Důkazy a komentáře: qa/hd_v2/. Výsledek této texturové kontroly se uvádí odděleně od historického schválení domu.
