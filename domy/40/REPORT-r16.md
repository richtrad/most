# Čp.40 – oprava textur a UV r16

Oprava reaguje na dva uživatelské detaily r13. Nulový počet kolabovaných UV neprokazoval vizuální kvalitu: na fasádě byly roztažené pásy, zlomy omítky a neostrý fotografický podklad.

## Příčina a změny

- Dlouhá fasáda A: dřívější silně perspektivně transformovaná fotografie měla nízké efektivní rozlišení vlevo. Lokální registrace otvorů dále lámala okolní omítku. Varianta r16 používá existující ostřejší FRONT z místní zálohy, v již uložené zelené variantě fronts_r4. Původní fotografický nápis je v tomto FRONTu přenesen ze zdroje; nebyl nově vygenerován ani vysázen.
- Nové mapování je navázané na celé hrany otvorů a souvislé římsy. Měřítko a rozměry domu z r13 zůstaly zachované; fasádní trojúhelníky byly pouze rozděleny pro UV. První pokus s hladkým spline r14 byl zamítnut: nezlepšil zdrojovou neostrost a obsahoval přehnutí. r15 s novým FRONTem byl mezikrok, štít ještě nebyl dostatečný.
- Štít C: omítka a dvě okenní výplně mají samostatné mapování. Omítka používá monotónní lichoběžníkové UV, takže se již nenatahuje mezi oknem a okrajem střechy. Okna zůstala v původních modelových otvorech; pravé poškozené okno nebylo zazděno ani doplněno novou příčkou.
- Jeden skutečný builtin image_gen edit doplnil pouze dvě obdélníkové části podkladové omítky pod samostatnými okny. Maska, prompt, surová generace, zarovnání a složený atlas jsou v balíku. Mimo masku je pixelová změna přesně 0. To neznamená historické potvrzení doplněných míst.
- Krátká fasáda B, střešní tašky, komín a zadní pracovní obálka se v této opravě neměnily. Barvy omítek přebírají stávající neuzamčenou zelenou hypotézu; nové globální přebarvení ani doostření fotografie neproběhlo.

## Vizuální a technická kontrola

V prohlížeči byl otevřen skutečný GLB a zkontrolován detail levé fasády i štítu. Zmizel roztažený pás nad podkrovními okny; dlouhá fasáda je čitelnější. Rendery před/po používají stejné kamery. Prohlédnuty byly také nároží, boční a zadní pohled. Boční fasáda je nadále měkčí než odvozený FRONT A; zadní obálka má pracovní opakovanou texturu a švy. Tyto převzaté části nejsou nově vizuálně schválené jako dokončené.

Fresh GLB: 7 vložených textur, 61 230 texturovaných trojúhelníků, 0 kolapsů UV, odchylka geometrie při exportu 0 m. Kontrolní triangulace mapování FRONTu měla 830/170 platných buněk A/C bez přehnutí; finální omítka C používá ještě jednodušší nezávislé mapování.

## Význam a omezení ostřejšího FRONTu

FRONT je odvozená generovaná reference, nikoli ortofotografie. Je ostřejší, ale některé jemné tvary rámů a průběh oprýskání jsou její interpretací. Tato varianta proto zlepšuje vzhled a mapování, nikoli prokázanou historickou přesnost. Detailní patina FRONTu ani dvě nově doplněné části omítky nejsou novým historickým důkazem. Původní fotografie i r13 zůstávají dostupné pro srovnání. Veškeré doplnění: model_hypothesis, provisional, locked:false.

GIS kandidát 105 stále neodpovídá ruční kalibraci plánu. Model není georeferencovaný; střešní rozměry, zadní půdorys a podrobnosti krytiny zůstávají pracovní. Počet úplně historicky/metricky validovaných domů se nemění.

## Obnova a porovnání

Přepínač Předchozí varianta r13 načítá její nezměněný GLB. Původní soubory a pokusy r14/r15 jsou zachované. Plný prompt této jedné nové obrazové editace je v prompt.txt. Vše pouze lokálně, žádný upload do Libuše.
