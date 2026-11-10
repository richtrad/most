"""Idempotent publication generator: run AFTER the existing Claude base generator.

Reads only the public registries. Never changes a GLB or the street placement.
Default site root is the parent of this maintenance directory.
"""
from pathlib import Path
import json,re,html,argparse
def main():
 p=argparse.ArgumentParser();p.add_argument('--site-root',type=Path,default=Path(__file__).resolve().parents[1]);args=p.parse_args();S=args.site_root
 studies=json.loads((S/'data/textured-studies.json').read_text(encoding='utf-8'));houses=json.loads((S/'data/houses.json').read_text(encoding='utf-8'));tex=json.loads((S/'data/textures.json').read_text(encoding='utf-8'));E=html.escape
 ids=list(studies);cs_ids=', '.join(ids[:-1])+' a '+ids[-1];en_ids=', '.join(ids[:-1])+' and '+ids[-1]
 assets='<link rel="stylesheet" href="/most/kulova/house-preview.css?v=20261018-studies-2"><script type="module" src="/most/kulova/house-preview.js?v=20261018-studies-2"></script>'
 for cp,s in studies.items():
  label='Codex: samostatná texturovaná pracovní studie'+(' – starší geometrie, čeká na revizi'if cp=='262'else'')
  tex[cp].update(status='standalone_study',label=label,study_glb=s['glb'],study_url=s['study_cs'],by='Codex',updated=s['updated'],qa=s['study_cs'],street_approved=False)
  # No final-street approval: the existing viewer must not silently replace it.
  tex[cp]['glb']=None;houses[cp]['tex']=label
 (S/'data/textures.json').write_text(json.dumps(tex,ensure_ascii=False,indent=1),encoding='utf-8');(S/'data/houses.json').write_text(json.dumps(houses,ensure_ascii=False,indent=1),encoding='utf-8')
 def cards(en=False):
  parts=[]
  for cp,s in studies.items():
   title=s['title_en'if en else'title_cs'];note=s['note_en'if en else'note_cs'];url=s['study_en'if en else'study_cs'];name=('No. 'if en else'Čp. ')+cp
   parts.append(f'<a class="k-study-card" href="/most/kulova/{url}"><img src="/most/kulova/{s["thumbnail"]}" alt="{E(name+" – "+title)}" loading="lazy" width="1000" height="563"><div><strong>{E(name)} · {E(title)}</strong><small>{E(note)}</small><span class="k-tex work">{"Working textured study"if en else"Pracovní texturovaná studie"}</span></div></a>')
  title='New standalone textured studies'if en else'Nové samostatné texturované studie'
  note=f'{len(studies)} existing Codex studies, kept separate from the untextured street assembly. Their appearance has been reviewed; this is not final historical approval. Older studies below remain unchanged.'if en else f'{len(studies)} již vytvořených studií Codexu, oddělených od základní geometrické sestavy ulice. Vzhled prošel pracovní kontrolou, nejde o finální historické schválení. Starší studie níže zůstávají beze změny.'
  return '<!-- BEGIN CODEX TEXTURED STUDIES --><section id="texturovane-studie" class="k-textured-studies"><h2>'+title+'</h2><p>'+note+'</p><div class="z-cards">'+''.join(parts)+'</div></section><!-- END CODEX TEXTURED STUDIES -->'
 def attach(s):
  s=s.replace('20261018-studies-1','20261018-studies-2')
  return s if'house-preview.js'in s else s.replace('</head>',assets+'</head>')
 def refresh_rows(s):
  def row(m):
   r=m.group();c=re.search(r'href="(?:\.\./)?cp(\d+)/"',r)
   if c and c[1]in studies:
    cp=c[1];label=E(tex[cp]['label'])
    if '<span class="k-tex'in r:r=re.sub(r'<span class="k-tex[^\"]*">.*?</span>',f'<span class="k-tex work">{label}</span>',r)
    elif 'lang="cs"'in r:r=re.sub(r'<td lang="cs">[^<]*</td></tr>$',f'<td lang="cs">{label}</td></tr>',r)
   return r
  s=re.sub(r'<tr>.*?</tr>',row,s,flags=re.S)
  def card(m):
   cp=m[1];r=m.group()
   if cp in studies:r=re.sub(r'<span class="k-tex[^\"]*">.*?</span>',f'<span class="k-tex work">{E(tex[cp]["label"])}</span>',r)
   return r
  return re.sub(r'<a href="cp(\d+)/"><img.*?</a>',card,s,flags=re.S)
 for file in [S/'index.html',S/'en/index.html']+list(S.glob('cp*/index.html')):
  s=file.read_text(encoding='utf-8');s=attach(s);en='<html lang="en"'in s
  s=s.replace('Geometrie je bez textur: barvy jsou jen materiálová ID. Texturované domy doplňuje Codex postupně.','Základní sestava ukazuje geometrii; texturované pracovní studie jsou dostupné samostatně. Barvy a skryté části nejsou historicky schválené.')
  s=s.replace('The geometry is untextured: colours are material IDs. Codex adds textured houses one by one.','The base street assembly shows geometry; textured working studies are available separately. Colours and hidden parts are not historically approved.')
  s=refresh_rows(s)
  if file==S/'index.html':
   s=s.replace('Stránka ukazuje, co kde stálo, odkud každý údaj pochází a jak vznikla geometrie. Model je zatím bez textur: texturované domy bude postupně doplňovat Codex a v prohlížeči se objeví jako volba <em>Textury (Codex)</em>.','Stránka ukazuje, co kde stálo, odkud každý údaj pochází a jak vznikla geometrie. Vpravo lze vybrat kterýkoli z 15 domů a přepnout hotové pracovní textury čp. 111, 261, 262 a 266. Základní sestava celé ulice níže zůstává geometrická; texturované studie jsou oddělené varianty.')
   s=re.sub(r'<img src="assets/houses/cp262_oblique.jpg"[^>]*>', '<div data-house-preview><noscript><img src="assets/houses/cp262_oblique.jpg" alt="Geometrie čp. 262"></noscript></div>',s,count=1)if'data-house-preview'not in s else s
   s=re.sub(r'hotové pracovní textury čp\. [\d, a]+\.',f'hotové pracovní textury čp. {cs_ids}.',s)
   newp=f'Čp. {cs_ids} už mají samostatné pracovní texturované studie. Otevřete je v horním přepínači nebo v <a href="#texturovane-studie">samostatných studiích níže</a>. Jejich přesné revize a omezení uvádí <a href="data/textured-studies.json">registr studií</a>. Nejsou automaticky vložené do celé ulice: zejména čp. 262, 265 a 266 mají odlišné geometrické revize a vyžadují další kontrolu.'
   s=re.sub(r'(<section id="textury"><h2>Textury \(Codex\)</h2>\s*)<p>.*?</p>',lambda m:m[1]+'<p>'+newp+'</p>',s,count=1,flags=re.S)
  elif file==S/'en/index.html':
   s=s.replace('The geometry is untextured; Codex adds textured houses one by one, and they appear in the viewer as the surface option “Textures (Codex)”.','The street assembly is untextured. Four existing textured working studies (111, 261, 262 and 266) can be switched on in the separate preview below; they are not automatically inserted into the street.')
   if'data-house-preview'not in s:s=s.replace('</header>','</header><div class="z-wrap z-hero"><div><h2>Explore individual houses</h2><p>Choose any of the 15 houses. Four already have a separate textured working version. Colours, hidden parts and historical accuracy remain provisional.</p><p><a href="#texturovane-studie">Standalone textured studies ↓</a></p></div><div data-house-preview></div></div>',1)
   s=re.sub(r'\b(?:Four|\d+) existing textured working studies \([\d, and]+\)',f'{len(studies)} existing textured working studies ({en_ids})',s)
   s=re.sub(r'\b(?:Four|\d+) already have a separate textured working version\.',f'{len(studies)} already have a separate textured working version.',s)
  cp=file.parent.name.removeprefix('cp')
  if cp in studies:
   s=re.sub(r'(<p id="tex-status">).*?(</p>)',lambda m:m[1]+'<span class="k-tex work">'+E(tex[cp]['label'])+'</span>'+m[2],s,flags=re.S)
   s=s.replace('Až Codex dodá texturovaný model, objeví se v prohlížeči nahoře volba <em>Textury (Codex)</em>.',f'Hotový pracovní model lze přepnout v horním náhledu. <a href="/most/kulova/{studies[cp]["study_cs"]}">Otevřít samostatnou texturovanou studii čp. {cp}</a>. Původní geometrický model níže zůstává dostupný beze změny.')
  if file in [S/'index.html',S/'en/index.html']:
   if'<!-- BEGIN CODEX TEXTURED STUDIES -->'in s:s=re.sub(r'<!-- BEGIN CODEX TEXTURED STUDIES -->.*?<!-- END CODEX TEXTURED STUDIES -->',cards(en),s,flags=re.S)
   elif not en:s=s.replace('<section id="starsi">',cards(False)+'<section id="starsi">',1)
   else:s=s.replace('</main>',cards(True)+'</main>',1)
  file.write_text(s,encoding='utf-8')
 for cp,st in studies.items():
  for en in [False,True]:
   url=st['study_en'if en else'study_cs'];rel='../../../'if en else'../../';title=('No. 'if en else'Čp. ')+cp+' · '+st['title_en'if en else'title_cs'];note=st['note_en'if en else'note_cs'];other=st['study_cs'if en else'study_en'];name='Standalone textured study'if en else'Samostatná texturovaná studie';lang='en'if en else'cs'
   body=f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)} – GRAFIT / MOST</title><meta name="description" content="{E(name+": "+note)}"><link rel="canonical" href="https://grafitctu.github.io/most/kulova/{url}"><link rel="stylesheet" href="/most/kulova/street.css?v=20261018n">{assets}<script type="importmap">{{"imports":{{"three":"/most/kulova/vendor/three.module.js"}}}}</script><link rel="icon" href="data:,"></head><body><nav class="street-nav"><a href="/most/">GRAFIT / MOST</a><a href="/most/kulova/">Kulová</a><a href="/most/kulova/{"en/"if en else""}#texturovane-studie">{"All textured studies"if en else"Všechny texturované studie"}</a><a href="/most/kulova/cp{cp}/">{"House sources and geometry"if en else"Prameny a geometrie domu"}</a><a class="ux-language" href="/most/kulova/{other}">{"Česky"if en else"English"}</a></nav><header class="z-wrap"><p>GRAFIT / MOST · CODEX · 18. 10. 2026</p><h1>{E(title)}</h1><p>{name}</p></header><main class="z-wrap"><p class="ux-note">{E(note)} {"Working reconstruction, not a historical survey or final street approval."if en else"Pracovní rekonstrukce, nikoli historické zaměření či finální schválení do ulice."}</p><div class="k-study-full" data-house-preview data-cp="{cp}" data-surface="textured"></div><section><h2>{"Model and provenance"if en else"Model a původ"}</h2><p>{"The preview switches between the original public geometry and the standalone textured working version. These may be different geometry revisions; no new historical detail was created for this publication."if en else"Náhled přepíná mezi původní veřejnou geometrií a samostatnou texturovanou pracovní variantou. Jde případně o rozdílné geometrické revize; při tomto zveřejnění nevznikal nový historický detail."}</p><ul><li><a href="/most/kulova/{st["glb"]}" download>{"Textured GLB"if en else"Texturované GLB"} · {st["web_bytes"]/1e6:.1f} MB</a></li><li><a href="/most/kulova/models/cp{cp}.glb" download>{"Original public geometry GLB"if en else"Původní veřejné geometrické GLB"}</a></li><li><a href="/most/kulova/data/textured-studies.json">{"Study registry and SHA-256"if en else"Registr studií a SHA-256"}</a></li></ul><p>{"Web copies retain geometry, UV and texture dimensions. Only colour images were re-encoded as JPEG; original source models remain unchanged."if en else"Webové kopie zachovávají geometrii, UV i rozměry textur. Pouze barevné mapy byly překódované do JPEG; původní zdrojové modely zůstaly beze změny."}</p><p><code>model_hypothesis · provisional · locked: false</code></p></section></main><footer class="ux-footer"><p>GRAFIT FIT ČVUT · MOST · {"Geometry: Claude; textures and web studies: Codex."if en else"Geometrie: Claude; textury a webové studie: Codex."}</p></footer></body></html>'
   body=body.replace('Geometrie: Claude; textury a webové studie: Codex.','Geometrický základ: Claude; pracovní revize, textury a webové studie: Codex.').replace('Geometry: Claude; textures and web studies: Codex.','Geometry base: Claude; working revisions, textures and web studies: Codex.')
   # The import map must precede module scripts in the standalone pages.
   body=body.replace(assets,'',1).replace('</head>',assets+'</head>',1)
   out=S/url/'index.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(body,encoding='utf-8')
 print('Rendered',len(studies),'CS + EN standalone studies; 15 house previews; 2 index galleries. Street model untouched.')
if __name__=='__main__':main()
