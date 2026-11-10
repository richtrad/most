from pathlib import Path
from PIL import Image,ImageDraw
import json
O=Path(__file__).resolve().parent
W,H,N=13.746,7.1,2048
old=json.loads((O.parent/'kulova_cp261_v7_2026-09-26/evidence/landmarks.json').read_text())['model_openings']
# Measured outer timber boundary in the registered facade, not outer stone surround.
bounds=[None,None,(797,207,964,774),(1120,207,1280,774),(1536,207,1700,774),(1756,207,1923,774),(100,1268,279,1910),(380,1272,544,1805),(786,1272,965,1805),(1107,1272,1284,1805),(1626,1272,1801,1805)]
rows=[]
im=Image.open(O.parent/'kulova_cp261_v8_2026-09-26/textures/registered_facade.png').convert('RGB')
mask=Image.new('L',im.size,0);md=ImageDraw.Draw(mask);overlay=im.copy();od=ImageDraw.Draw(overlay)
for i,(o,b) in enumerate(zip(old,bounds)):
 l=(o['cx']-o['width']/2)/W*N;r=(o['cx']+o['width']/2)/W*N;t=(1-o['top']/H)*N;bt=(1-o['bottom']/H)*N
 baseline=[l,t,r,bt]
 if b is None:b=baseline
 # Keep sill/threshold heights: only adjust side boundaries and head where needed.
 target=[b[0]-8,b[1]-8,b[2]+8,bt] if i>=2 else baseline
 rows.append({'id':('U'+str(i+1)) if i<6 else ('D1' if i==6 else 'G'+str(i-6)),'old':o,'baseline_px':baseline,'photo_px':list(b),'target_px':target,'change':i>=2})
 od.rectangle(baseline,outline='cyan',width=2);od.rectangle(target,outline='red',width=2)
 if i<2:continue
 outer=[min(l,b[0])-4,min(t,b[1])-4,max(r,b[2])+4,max(bt,b[3])+4]
 md.rectangle(outer,fill=255)
 # Protect deep inside aperture, leave enough hidden gutter for reliable inpaint.
 md.rectangle([l+10,t+10,r-10,bt-10],fill=0)
mask.save(O/'evidence/inpaint_mask.png');overlay.save(O/'evidence/registration_overlay.png')
guide=im.copy();guide.paste((255,0,255),(0,0,*im.size),mask);guide.save(O/'evidence/inpaint_target.png')
im.save(O/'textures/facade_original.png')
(O/'evidence/openings.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('prepared',len(rows),'openings')
