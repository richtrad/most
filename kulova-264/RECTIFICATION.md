# Konstrukční narovnání výkladnice

Nová varianta podle výslovného rozhodnutí uživatele. Původní výkladnice kopírovala deformaci registrované fotografie příliš doslova.

1. Zachován původní model a originální fotografie.
2. Horní a spodní hrana hlavní římsy obchodu jsou vodorovné, těleso výkladnice pravoúhlé. Patrová římsa má sjednocenou výšku.
3. Stejnou změnu sleduje spojitá registrace textury. Narovnány také hlavní vodorovné příčky dřevěných polí. Počet polí, materiál a poškození zachovány. Nejde o inpainting varianty T: upravena je současně geometrie i registrace.
4. Horní okna, dveřní otvor, půdorys, střecha, práh a samostatný svod zůstávají zachovány. Přechod u dveří je lokální; veškeré mapování je monotónní bez převrácených oblastí.
5. Příčina zkreslení není kalibračně prokázána; může kombinovat perspektivu, registraci a dřívější kolorování. Tato varianta předpokládá původně rovné truhlářské konstrukce. Není historickým důkazem přesných rozměrů.

Identita čp. a skryté části zůstávají pracovní hypotézou jako v předchozí zprávě. Starší REPORT popisuje výchozí verzi; tento dokument zaznamenává změnu.

## Kontrola výsledku

Uloženo a prohlédnuto 73 snímků skutečného GLB v Edge/Three.js (osy, střešní rohy, všechny otvory zepředu a z obou stran, clay, detaily). Čelo římsy má samostatnou texturu z čelní roviny fotografie; fotografický bok se na čelo nepřenáší. Původní model má nezměněný hash. Jemné nepravidelnosti malby a dřívější omezení střechy zůstávají přiznané. Model je pracovní varianta; do schválené ulice není propagován.

Sestavení: nejprve `refine_registration.py`, poté Blender `--background --python build.py`. Pět bitmap je zabaleno v BLEND i GLB. Přehled parametrů registrace je v `evidence/rectification.json`.
