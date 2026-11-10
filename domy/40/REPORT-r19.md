# Čp. 40 – jemný bump a knihovní krytina r19

Nová lokální varianta přidává procedurální mikroreliéf omítky a keramického povrchu střechy. Tangentové normálové mapy jsou vložené v GLB i v souboru Blender. Barevné textury a UV fasád i geometrie r16 zůstávají stejné. Střecha používá nový podklad a nové UV výběry.

Omítka hlavních stěn je oddělená od zapuštěných oken a ostění podle modelových ploch. Sklo, nápisy a fotografické stíny nebyly použity jako výšková mapa. Střešní normála přidává pouze drobnou zrnitost; tvar tašek nadále tvoří stávající geometrie. Síla je úmyslně malá, nejlépe viditelná při bočním osvětlení a v detailu.

Reliéf je materiálová hypotéza, provisional, locked:false; není měřeným historickým povrchem. Tato změna neopravuje dosavadní neověřenou GIS registraci, zadní obálku ani měkčí podklad boční fasády. Předchozí úplný report je v history_r16/REPORT.md. Starší ilustrační pohledy A/B/rear jsou převzaté z r16; nové rendery corner, detail_left a detail_roof pocházejí ze znovu importovaného GLB r19.

Přepínač Bump zapnout/vypnout umožňuje srovnání stejného modelu a osvětlení. Předchozí varianta načítá zachované r16. Žádná nová obrazová generace ani vzdálený upload.


## Připravená knihovna střech

Použita R002_A z roof_texture_library_v2, varianta pestrého opotřebení pálené oblé krytiny. Barevné vzorky vnitřků jednotlivých tašek se přiřazují fyzickým taškám modelu. Rozměry a spáry určují existující modelované tašky, nikoli nominální údaj 4 × 4 m knihovního obrázku. Střecha má pestřejší keramický povrch bez opakování jediného fleku na každé tašce. Normálová mapa používá samostatné UV, takže změna barevného vzorku nemění měřítko mikroreliéfu.

Knihovní obrázek není schválený jako bezešvá celoplošná textura; zde se celoplošně nedlaždicuje. Vznikl podle jiného domu a dokládá pouze pracovní materiálovou variantu, nikoli historické odstíny čp. 40. Silné poškození a díry do krovu nebyly přidávány. Provenience a hash jsou v roof_provenance.json.

Při detailním pohledu zůstávají na střeše převzaté zlomy geometrických panelů a nepravidelné dořezy tašek. Materiálová úprava je neodstraňuje.
