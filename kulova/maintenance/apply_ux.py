"""Idempotent UX layer for the published Kulova HTML exports.

Run after prepare.py / fix_paths.py when refreshing the publication bundle.
Only changes presentation pages and shared CSS/JS; never model/source data.
"""
from pathlib import Path
import re, html, shutil, argparse
from PIL import Image

parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path)
ROOT=parser.parse_args().root or (Path(__file__).resolve().parents[3] if Path(__file__).parent.name=='maintenance' else Path(__file__).resolve().parents[1]/'kulova_publish_20261002/ux-repo')
houses=['257','259','261','263','264']
def nav(route,en=False,lab=False):
    suffix='en/' if en else ''
    links=[('/most/'+suffix,'GRAFIT / MOST'),('/most/kulova/'+suffix,'Kulová')]+[('/most/kulova-'+n+'/'+suffix,('House ' if en else 'Čp. ')+n) for n in houses]
    s='<nav class="kulova-nav" aria-label="'+('Street navigation' if en else 'Domy v ulici')+'">'
    for url,title in links:
        active=route.replace('-264-original','-264')==url or ('-261/' in url and lab)
        s+=f'<a href="{url}"'+(' aria-current="page"' if active else '')+f'>{title}</a>'
    if not lab:
        other=route[:-3] if en else route+'en/'
        s+=f'<a class="ux-language" href="{other}" lang="'+('cs' if en else 'en')+'">'+('Česky' if en else 'English')+'</a>'
    return s+'</nav>'

def update(p):
    route='/'+p.parent.relative_to(ROOT).as_posix()+'/'
    en=route.endswith('/en/');lab='-lab/' in route
    text=p.read_text(encoding='utf-8')
    # The CSS is last so the original theme and all historic figures remain usable.
    if '/most/kulova/ux.css' not in text:
        assets='<link rel="stylesheet" href="/most/kulova/ux.css?v=20261003"><script defer src="/most/kulova/ux.js?v=20261003"></script>'
        if '</head>' in text:text=text.replace('</head>',assets+'</head>',1)
        else:text=re.sub(r'(<(?:nav|header)\b)',assets+r'\1',text,count=1)
    if 'class="kulova-nav"' in text:
        text=re.sub(r'<nav class="kulova-nav".*?</nav>',nav(route,en,lab),text,count=1,flags=re.S)
    else:text=text.replace('<header>',nav(route,en,lab)+'<header>',1)
    # Language switching lives in the same place on every page.
    text=re.sub(r'<p><a href="[^"]+">(?:English overview / EN|Česky / CS)</a></p>','',text)
    # Static section IDs and absolute page anchors work with the EN <base> tag.
    text=re.sub(r'<details class="ux-toc">.*?</details>','',text,flags=re.S)
    main_start=text.index('<main>');main_end=text.index('</main>',main_start)
    content=text[main_start:main_end]
    if 'kulova-264/' in route:
        sections=list(re.finditer(r'<section\b.*?</section>',content,re.S))
        if len(sections)>1 and re.search(r'<h2[^>]*>[^<]*(?:Narovnan|Straighten)',sections[0][0],re.I):
            a,b=sections[:2];content=content[:a.start()]+b[0]+content[a.end():b.start()]+a[0]+content[b.end():]
    count=0;chapters=[]
    def heading(m):
        nonlocal count
        count+=1;attrs=m[1];title=m[2];idmatch=re.search(r'id="([^"]+)"',attrs)
        ident=idmatch[1] if idmatch else f'chapter-{count}'
        # Heading anchors avoid relying on parent sections with divergent CS/EN IDs.
        if not idmatch:attrs+=f' id="{ident}"'
        label=html.unescape(re.sub('<[^>]*>','',title)).strip()
        chapters.append((ident,label))
        return f'<h2{attrs}>{title}</h2>'
    content=re.sub(r'<h2([^>]*)>(.*?)</h2>',heading,content,flags=re.S)
    text=text[:main_start]+content+text[main_end:]
    if 'class="ux-toc"' not in text:
        toc='<details class="ux-toc"><summary>'+('On this page: photographs, materials and repairs' if en else 'Obsah stránky: fotografie, materiály a opravy')+'</summary><ol>'
        toc+=f'<li><a href="{route}#canvas">'+('Interactive 3D model' if en else 'Interaktivní 3D model')+'</a></li>'
        toc+=''.join(f'<li><a href="{route}#{id}">{html.escape(label)}</a></li>' for id,label in chapters)+'</ol></details>'
        text=text.replace('<div class="toolbar">',toc+'<div class="toolbar">',1)
    if 'class="ux-skip"' not in text:
        text=text.replace(nav(route,en,lab),f'<a class="ux-skip" href="{route}#canvas">'+('Skip to model' if en else 'Přejít k modelu')+'</a>'+nav(route,en,lab),1)
    if 'class="ux-viewer-help"' not in text:
        help='<p class="ux-viewer-help">'+('Drag to rotate · scroll or pinch to zoom. Choose a viewpoint to return to a saved camera. Compare images by dragging the divider or using the slider and arrow keys.' if en else 'Tažením otáčejte · kolečkem nebo dvěma prsty přibližujte. Výběrem pohledu se vrátíte k uložené kameře. Obrázky porovnávejte tažením dělicí čáry nebo posuvníkem a šipkami na klávesnici.')+'</p>'
        if '<div id="canvas"></div>' in text:text=text.replace('<div id="canvas"></div>','<div id="canvas"></div>'+help,1)
        elif '</div><p class="caption">' in text:text=text.replace('</div><p class="caption">','</div>'+help+'<p class="caption">',1)
        else:text=text.replace('</div><main>','</div>'+help+'<main>',1)
    if 'class="ux-footer"' not in text:
        footer='<div class="ux-footer"><a href="/most/kulova/'+('en/' if en else '')+'">'+('← All houses in Kulová' if en else '← Všechny domy v Kulové')+'</a> · <a href="/most/kulova-261/bevel-lab/">'+('Edge rounding: A / B / C' if en else 'Zaoblení hran: A / B / C')+'</a> · <a href="/most/kulova-261/opening-lab/">'+('Opening registration: G / T' if en else 'Registrace otvorů: G / T')+'</a></div>'
        text=text.replace('<dialog ',footer+'<dialog ',1)
    if lab:
        text=text.replace('no variant is yet the standard workflow.','variant C was selected for the subsequent workflow.')
        text=text.replace('Vybranou variantu teprve použijeme jako základ dalšího postupu.','Jako základ dalšího postupu byla zvolena varianta C.')
        text=text.replace('První kandidát k posouzení: B. A je velmi jemná; C zvýrazňuje hranu více. / Initial candidate for review: B. A is very subtle; C gives a stronger edge.','Zvolená varianta pro další postup: C. A a B zůstávají jemnějšími alternativami pro porovnání. / Selected for subsequent work: C. A and B remain subtler comparison alternatives.')
        text=text.replace('Výchozí kandidát pro další test: B. A je velmi jemná; C zvýrazňuje hranu více. / Initial candidate for review: B. A is very subtle; C gives a stronger edge.','Zvolená varianta pro další postup: C. A a B zůstávají jemnějšími alternativami pro porovnání. / Selected for subsequent work: C. A and B remain subtler comparison alternatives.')
        text=text.replace('Vybranou variantu teprve použijeme pro další postup; zatím se žádná nestává automatickým standardem. / The selected variant will inform the next workflow; no variant is yet the standard.','Pro další postup byla zvolena varianta C (8 / 12 mm). Původní v10 i A a B zůstávají k porovnání. / Variant C (8 / 12 mm) was selected for subsequent work. Original v10, A and B remain available for comparison.')
        text=text.replace('Doporučený směr: G. Výběr zůstává otevřený; hlavní v10 ani původní C se nemění. / Suggested direction: G. Selection remains open; main v10 and original C are unchanged.','Výchozí postup pro další domy: G po ověření původních pramenů. T je srovnávací alternativa pouze na výslovné zadání. Hlavní v10 a původní C zůstávají zachované. / Default workflow for subsequent houses: G after checking the original sources. T is a comparison alternative only when explicitly requested. Main v10 and original C remain preserved.')
        if 'ux-lab-note' not in text:
            note='<p class="ux-note ux-lab-note">Experimentální porovnání / Experimental comparison. '+('Zvolený směr: C, střídmé lokální zaoblení. / Selected: C, restrained local rounding.' if 'bevel-lab' in route else 'Výchozí oprava: G upravuje geometrii k ověřené textuře. T upravuje texturu při zachování geometrie. / Default: G aligns geometry to the verified texture. T edits the texture while retaining geometry.')+' Modely hlavní prezentace se tímto přehledem nemění. / The main presentation models are unchanged.</p>'
            text=text.replace('</header>',note+'</header>',1)
    if 'kulova-264-original' in route and 'ux-archive-note' not in text:
        note='<p class="ux-note ux-archive-note">'+('Archived version before shopfront straightening. ' if en else 'Archivovaná verze před narovnáním výkladnice. ')+f'<a href="/most/kulova-264/'+('en/' if en else '')+'">'+('Open the updated model →' if en else 'Přejít na upravený model →')+'</a></p>'
        text=text.replace('</header>',note+'</header>',1)
    p.write_text(text,encoding='utf-8')

for route in ['kulova-'+n for n in houses]+['kulova-264-original']:
    for lang in ['', 'en/']:update(ROOT/'most'/route/lang/'index.html')
for lab in ['bevel-lab','opening-lab']:update(ROOT/'most/kulova-261'/lab/'index.html')

assets=ROOT/'most/kulova/assets';assets.mkdir(exist_ok=True)
for n in houses:
    image=Path(__file__).parent/'before'/f'kulova-{n}_hero.png'
    if image.exists():
        im=Image.open(image).convert('RGB');im.thumbnail((720,500));im.save(assets/f'house-{n}.jpg',quality=85,optimize=True)
descriptions={
'257':('Torzo domu a otevřený krov. Fotografie více stěn, plány a kontrola otvorů.','House remains and exposed roof frame. Multiple facade photographs, plans and opening checks.'),
'259':('Fotografická textura proti regenerované HD. Přepínání materiálů přímo na modelu.','Photographic texture versus regenerated HD. Switch materials directly on the model.'),
'261':('Kompletní vývoj: fotografie, omítka, ostění, schody a okapy. Porovnání C a G/T.','The complete development: photographs, plaster, window returns, steps and gutters. C and G/T comparisons.'),
'263':('Ověření identity domu, opravený FRONT, dva vikýře a kontrola mapování.','House identification, corrected FRONT reference, two dormers and texture mapping checks.'),
'264':('Narovnání výkladnice a porovnání geometrie. Původní verze zůstává dostupná.','Shopfront straightening and geometry comparisons. The original version remains available.')}
for en in [False,True]:
    suffix='en/' if en else '';route='/most/kulova/'+suffix
    title='Kulová: models and reconstruction process' if en else 'Kulová: modely a postup rekonstrukce'
    intro='Explore a house in 3D, compare the original and colourized photographs, then follow the materials and detail corrections. Each page keeps its sources and limitations.' if en else 'Prohlédněte si dům ve 3D, porovnejte původní a kolorovanou fotografii a pokračujte k materiálům a opravám detailů. Každý dům má vlastní prameny a zapsaná omezení.'
    note='These are provisional reconstructions. Colours and hidden surfaces are hypotheses, not historical confirmation. G means adjusting geometry to a source-verified texture; T edits the texture and is an explicitly requested alternative. FRONT is a derived frontal material reference, not an exact surveyed facade.' if en else 'Jde o pracovní rekonstrukce. Barvy a skryté plochy jsou hypotézy, nikoli historické potvrzení. G znamená úpravu geometrie k textuře ověřené podle pramenů; T je úprava textury, kterou volíme jen na výslovné zadání. FRONT je odvozená čelní materiálová reference, ne přesné zaměření fasády.'
    text=f'<!doctype html><html lang="'+('en' if en else 'cs')+f'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — GRAFIT / MOST</title><meta name="description" content="{intro}"><link rel="stylesheet" href="/most/kulova/ux.css?v=20261003"><link rel="canonical" href="https://grafitctu.github.io{route}"></head><body><a class="ux-skip" href="{route}#ux-main">'+('Skip to houses' if en else 'Přejít k domům')+'</a>'+nav(route,en)+'<div class="ux-index"><header><p>GRAFIT / MOST · KULOVÁ</p><h1>'+title+'</h1><p>'+intro+'</p></header><main id="ux-main">'
    for n in houses:
        url='/most/kulova-'+n+'/'+suffix
        text+=f'<article><a href="{url}" tabindex="-1" aria-hidden="true"><img src="/most/kulova/assets/house-{n}.jpg" alt="" width="720" height="500"'+(' loading="lazy"' if n!='257' else '')+'></a><div class="ux-card-copy"><h2>Kulová '+n+'</h2><p>'+descriptions[n][en]+'</p><a href="'+url+'">'+('Model and process' if en else 'Model a postup tvorby')+' <span aria-hidden="true">→</span></a></div></article>'
    text+='<aside class="ux-note">'+note+'</aside></main><div class="ux-footer"><p>'+('Method comparisons: ' if en else 'Metodická porovnání: ')+'<a href="/most/kulova-261/bevel-lab/">'+('Edge rounding A / B / C' if en else 'Zaoblení hran A / B / C')+'</a> · <a href="/most/kulova-261/opening-lab/">'+('Geometry G / texture T' if en else 'Geometrie G / textura T')+'</a></p><p>GRAFIT / MOST · 3. 10. 2026</p></div></div></body></html>'
    p=ROOT/'most/kulova'/suffix/'index.html';p.write_text(text,encoding='utf-8')
