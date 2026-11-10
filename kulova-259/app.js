import * as THREE from './vendor/three.module.js';
import {OrbitControls} from './vendor/OrbitControls.js';
import {GLTFLoader} from './vendor/GLTFLoader.js';
const $=id=>document.getElementById(id),host=$('canvas');
const renderer=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.outputEncoding=THREE.sRGBEncoding;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=.8;host.appendChild(renderer.domElement);
const scene=new THREE.Scene();scene.background=new THREE.Color('#dddcd2');scene.add(new THREE.HemisphereLight(0xffffff,0x7d8074,1.05));const sun=new THREE.DirectionalLight(0xfff7e8,1);sun.position.set(-12,24,18);scene.add(sun);
const camera=new THREE.PerspectiveCamera(38,1,.01,200),controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=false;
const clay=new THREE.MeshStandardMaterial({color:'#72857b',roughness:.9}),highlight=new THREE.MeshStandardMaterial({color:'#c07038',roughness:.9});
const landmarks=await (await fetch('./evidence/landmarks.json')).json();
const views={hero:{p:[25,16,25],t:[7,4.6,-4]},axis_front:{p:[7,5,30],t:[7,5,-3]},axis_right:{p:[38,5,-5],t:[7,5,-5]},axis_back:{p:[7,5,-38],t:[7,5,-5]},axis_left:{p:[-24,5,-5],t:[7,5,-5]},roof_front_left:{p:[-15,23,20],t:[7,7,-5]},roof_front_right:{p:[29,23,20],t:[7,7,-5]},roof_back_left:{p:[-15,23,-30],t:[7,7,-5]},roof_back_right:{p:[29,23,-30],t:[7,7,-5]},detail_corner:{p:[18,6,5],t:[13.8,4,0]},detail_roof:{p:[21,19,6],t:[8,10,-5]},detail_chimneys:{p:[16,16,-13],t:[10,11,-6]},detail_damage:{p:[11,.8,4],t:[11,.8,0]},detail_cornice:{p:[7,4.5,5],t:[7,4,0]},detail_threshold:{p:[2.38,.8,3],t:[2.38,.18,0]},detail_threshold_below:{p:[2.38,-.16,3],t:[2.38,.13,0]}};
const cv=v=>[v[0],v[2],-v[1]];
for(const o of landmarks.openings){const t=cv(o.world),d=Math.max(3.2,(o.top-o.bottom)*2.5,o.width*2.5);for(const [name,k]of[['front',0],['left',-.58],['right',.58]])views[`opening_${o.id}_${name}`]={p:[t[0]+d*k,t[1]+.06,d],t};}
for(const k of Object.keys(views)){const op=document.createElement('option');op.value=k;op.textContent=k;$('view').append(op);}
const model=(await new GLTFLoader().loadAsync('./models/cp259_SOL61.glb')).scene;scene.add(model);model.traverse(o=>{if(o.isMesh){o.userData.original=o.material;for(const m of(Array.isArray(o.material)?o.material:[o.material]))if(m.map)m.map.anisotropy=Math.min(16,renderer.capabilities.getMaxAnisotropy());}});
const facadeMaterials=new Set();
model.traverse(o=>{if(o.isMesh)for(const m of(Array.isArray(o.userData.original)?o.userData.original:[o.userData.original]))if(m.name==='SOURCE_PHOTO_REGISTERED'&&m.map){m.userData.originalMap=m.map;facadeMaterials.add(m);}});
const hdImage=await new THREE.TextureLoader().loadAsync('./textures/front_regenerated_hd_v2.png');
const hdMaps=new Map();
for(const m of facadeMaterials){const map=m.userData.originalMap.clone();map.source=new THREE.Source(hdImage.image);map.needsUpdate=true;hdMaps.set(m,map);}
let textureVersion='original';
function setTextureVersion(key){if(!['original','hd'].includes(key))throw Error('Unknown texture version');textureVersion=key;for(const m of facadeMaterials){m.map=key==='hd'?hdMaps.get(m):m.userData.originalMap;m.needsUpdate=true;}$('texture-version').value=key;render();}
function render(){renderer.render(scene,camera)}
function resize(){renderer.setSize(host.clientWidth,host.clientHeight);const old=camera.aspect;camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();if(Math.abs(old-camera.aspect)>.001&&$('view').value)setView($('view').value);else render();}new ResizeObserver(resize).observe(host);
function setView(k){camera.position.fromArray(views[k].p);controls.target.fromArray(views[k].t);camera.position.sub(controls.target).multiplyScalar(Math.max(1,1/camera.aspect)).add(controls.target);controls.update();$('view').value=k;render();}
function surface(mode){model.traverse(o=>{if(o.isMesh){const a=o.userData.original;const gen=(Array.isArray(a)?a:[a]).some(m=>m.userData.generated_unobserved_surface);o.material=mode==='clay'?clay:mode==='hypotheses'&&gen?highlight:a;}});render();}
$('view').onchange=e=>setView(e.target.value);$('surface').onchange=e=>surface(e.target.value);$('source').onclick=()=>$('source-dialog').showModal();$('close-source').onclick=()=>$('source-dialog').close();
$('texture-version').onchange=e=>setTextureVersion(e.target.value);
document.querySelectorAll('.compare input').forEach(i=>i.oninput=()=>i.parentElement.style.setProperty('--split',i.value+'%'));
window.qa={views,setTextureVersion,getTextureInfo(){return{version:textureVersion,materials:facadeMaterials.size,sizes:[...facadeMaterials].map(m=>[m.map.image.width,m.map.image.height]),camera:camera.position.toArray(),target:controls.target.toArray()};},async capture(key,mode='texture'){surface(mode);setView(key);resize();render();return{png:renderer.domElement.toDataURL('image/png'),textureVersion,camera:{position:camera.position.toArray(),target:controls.target.toArray(),fov:camera.fov,aspect:camera.aspect},exposure:renderer.toneMappingExposure,width:renderer.domElement.width,height:renderer.domElement.height};}};
setView('hero');$('status').textContent='Čp. 259 · SOL 6.1 · G · pracovní rozsah fasády';controls.addEventListener('change',render);
setTextureVersion(new URLSearchParams(location.search).get('texture')==='original'?'original':'hd');
window.qa.captureExport=async()=>{const exported=(await new GLTFLoader().loadAsync('./models/cp259_SOL61_HD_v2.glb')).scene;exported.traverse(o=>{if(o.isMesh)for(const m of(Array.isArray(o.material)?o.material:[o.material]))if(m.map)m.map.anisotropy=Math.min(16,renderer.capabilities.getMaxAnisotropy());});scene.remove(model);scene.add(exported);setView('hero');resize();render();const png=renderer.domElement.toDataURL('image/png');scene.remove(exported);scene.add(model);render();return png;};
