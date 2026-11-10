// Standalone working studies. Never inserts an unapproved study into the street.
import * as THREE from './vendor/three.module.js';
import {GLTFLoader} from './vendor/GLTFLoader.js';
import {OrbitControls} from './vendor/OrbitControls.js';
const BASE='/most/kulova/';
const en=document.documentElement.lang==='en',tr=(cs,eng)=>en?eng:cs;
const make=(tag,cls,text)=>{const e=document.createElement(tag);if(cls)e.className=cls;if(text)e.textContent=text;return e;};
const [houses,studies]=await Promise.all(['houses.json','textured-studies.json'].map(async f=>{const r=await fetch(BASE+'data/'+f,{cache:'no-cache'});if(!r.ok)throw Error(f+': '+r.status);return r.json();}));
function dispose(root){const gs=new Set(),ms=new Set(),ts=new Set();root.traverse(o=>{if(o.isMesh){gs.add(o.geometry);for(const m of Array.isArray(o.material)?o.material:[o.material]){ms.add(m);for(const v of Object.values(m))if(v?.isTexture)ts.add(v);}}});gs.forEach(g=>g.dispose());ms.forEach(m=>m.dispose());ts.forEach(t=>t.dispose());}
function mount(host){
 const fixed=host.dataset.cp||null;let cp=fixed||new URLSearchParams(location.search).get('preview')||'262';if(!houses[cp])cp='262';
 let surface=host.dataset.surface||new URLSearchParams(location.search).get('model')||'geometry';if(surface!=='textured'||!studies[cp])surface='geometry';
 host.classList.add('k-house-preview');host.id=host.id||'house-preview';
 const title=make('h2','k-preview-title',tr('Dům zblízka','House close-up')),stage=make('div','k-preview-stage');
 const fallback=make('img','k-preview-fallback');fallback.src=BASE+'assets/houses/cp'+cp+'_oblique.jpg';fallback.alt=tr('Náhled geometrie čp. ','Geometry preview of house ')+cp;stage.append(fallback);
 const controls=make('div','k-preview-controls'),label=make('label','',tr('Dům','House')),select=make('select','k-preview-house');select.setAttribute('aria-label',tr('Vyberte dům','Choose a house'));
 for(const n of Object.keys(houses).sort((a,b)=>Number(a)-Number(b)))select.add(new Option(tr('Čp. ','No. ')+n+(studies[n]?tr(' · také s texturami',' · textures available'):''),n));select.value=cp;label.append(select);
 if(!fixed)controls.append(label);
 const buttons=make('div','k-preview-modes');buttons.setAttribute('role','group');buttons.setAttribute('aria-label',tr('Varianta modelu','Model version'));
 const geo=make('button','',tr('Geometrie','Geometry')),tex=make('button','',tr('Texturovaný model','Textured model'));geo.type=tex.type='button';buttons.append(geo,tex);controls.append(buttons);
 const views=make('div','k-preview-views'),front=make('button','',tr('Průčelí','Front')),roof=make('button','',tr('Celý model / střecha','Whole model / roof'));front.type=roof.type='button';views.append(front,roof);
 const status=make('p','k-preview-status');status.setAttribute('role','status');const note=make('p','k-preview-note'),study=make('a','k-preview-study');
 host.append(title,stage,controls,views,status,note,study);
 const renderer=new THREE.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.outputEncoding=THREE.sRGBEncoding;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=.8;
 renderer.domElement.setAttribute('role','img');stage.append(renderer.domElement);
 const scene=new THREE.Scene();scene.background=new THREE.Color('#dddeda');scene.add(new THREE.HemisphereLight(0xffffff,0x777777,.5));const sun=new THREE.DirectionalLight(0xffffff,1.1);sun.position.set(20,50,30);scene.add(sun);
 const camera=new THREE.PerspectiveCamera(40,1,.05,2000),ctl=new OrbitControls(camera,renderer.domElement);ctl.enableDamping=true;ctl.enablePan=true;const loader=new GLTFLoader();let root=null,ticket=0,visible=true;
 const resize=()=>{const w=stage.clientWidth,h=stage.clientHeight;if(!w||!h)return;renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();};new ResizeObserver(resize).observe(stage);
 new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;},{rootMargin:'100px'}).observe(host);
 function fitFront(){if(!root)return;const b=new THREE.Box3().setFromObject(root),dims=surface==='textured'?studies[cp]:null,w=dims?.preview_width_m||houses[cp].width_m||b.max.x-b.min.x,h=dims?.preview_eave_m||houses[cp].eave_m||b.max.y;
  const x=b.min.x+w/2;ctl.target.set(x,h*.62,0);camera.position.set(x+w*.19,h*.62+h*.17,Math.max(w,h)*(camera.aspect<1?2.05:1.65));ctl.update();}
 function fitRoof(){if(!root)return;const b=new THREE.Box3().setFromObject(root),c=b.getCenter(new THREE.Vector3()),s=b.getSize(new THREE.Vector3()),r=Math.max(s.x,s.y,s.z);ctl.target.copy(c);camera.position.copy(c).add(new THREE.Vector3(.7,.8,1).normalize().multiplyScalar(r*1.65));ctl.update();}
 async function load(){const mine=++ticket;host.dataset.ready='loading';tex.disabled=!studies[cp];geo.setAttribute('aria-pressed',String(surface==='geometry'));tex.setAttribute('aria-pressed',String(surface==='textured'));
  const titleText=tr('Čp. ','No. ')+cp;title.textContent=titleText+' · '+(en?(studies[cp]?.title_en||houses[cp].kind):(studies[cp]?.title_cs||houses[cp].kind));fallback.src=BASE+'assets/houses/cp'+cp+'_oblique.jpg';
  const st=studies[cp];note.textContent=surface==='textured'?(en?st.note_en:st.note_cs):tr('Původní geometrická revize; barvy označují materiály. Textury jsou samostatnou pracovní variantou.','Original geometry revision; colours identify materials. Textures are a separate working version.');
  study.textContent=st?tr('Otevřít samostatnou texturovanou studii →','Open standalone textured study →'):tr('Prameny a stránka domu →','Sources and house page →');study.href=BASE+(st?(en?st.study_en:st.study_cs):'cp'+cp+'/');
  status.textContent=tr('Načítání čp. ','Loading house ')+cp+'…';const path=surface==='textured'?st.glb:'models/cp'+cp+'.glb';
  try{const g=await loader.loadAsync(BASE+path);if(mine!==ticket){dispose(g.scene);return;}if(root){scene.remove(root);dispose(root);}root=g.scene;scene.add(root);resize();fitFront();fallback.hidden=true;host.dataset.ready=cp+':'+surface;renderer.domElement.setAttribute('aria-label',titleText+' · '+(surface==='textured'?tr('texturovaný pracovní model','textured working model'):tr('geometrie','geometry')));status.textContent=titleText+' · '+(surface==='textured'?tr('texturovaná pracovní studie','textured working study'):tr('geometrie','geometry'))+' · '+tr('tažením otáčejte','drag to rotate');
  }catch(e){if(mine!==ticket)return;host.dataset.ready='error';status.textContent=tr('Model se nepodařilo načíst. Použijte odkaz na samostatnou stránku.','Could not load model. Use the standalone page link.');console.error(e);}}
 select.onchange=()=>{cp=select.value;if(!studies[cp])surface='geometry';load();};geo.onclick=()=>{surface='geometry';load();};tex.onclick=()=>{if(studies[cp]){surface='textured';load();}};front.onclick=fitFront;roof.onclick=fitRoof;
 renderer.setAnimationLoop(()=>{if(visible){ctl.update();renderer.render(scene,camera);}});resize();load();
}
let hosts=[...document.querySelectorAll('[data-house-preview]')];
if(!hosts.length){const geom=document.querySelector('#canvas[data-mode="house"]'),header=document.querySelector('header.z-wrap');if(geom&&header){const wrap=make('div','k-house-heading');while(header.firstChild)wrap.append(header.firstChild);const preview=make('div');preview.dataset.housePreview='';preview.dataset.cp=geom.dataset.cp;header.append(wrap,preview);header.classList.add('k-house-hero');hosts=[preview];}}
hosts.forEach(mount);
