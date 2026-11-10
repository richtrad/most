import * as THREE from './vendor/three.module.js';
import {OrbitControls} from './vendor/OrbitControls.js';
import {GLTFLoader} from './vendor/GLTFLoader.js';
const $=id=>document.getElementById(id),host=$('canvas');
const renderer=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.outputEncoding=THREE.sRGBEncoding;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=.8;host.appendChild(renderer.domElement);
const scene=new THREE.Scene();scene.background=new THREE.Color('#dddcd2');scene.add(new THREE.HemisphereLight(0xffffff,0x7d8074,1.05));const sun=new THREE.DirectionalLight(0xfff7e8,1);sun.position.set(-12,24,18);scene.add(sun);
const camera=new THREE.PerspectiveCamera(38,1,.01,200),controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=false;
const clay=new THREE.MeshStandardMaterial({color:'#72857b',roughness:.9}),highlight=new THREE.MeshStandardMaterial({color:'#c07038',roughness:.9});
const landmarks=await (await fetch('./evidence/landmarks.json')).json();
const views={hero:{p:[32,21,24],t:[4,4,-8]},axis_front:{p:[3,5,39],t:[3,5,-8]},axis_right:{p:[49,5,-9],t:[3,5,-9]},axis_back:{p:[3,5,-51],t:[3,5,-9]},axis_left:{p:[-44,5,-9],t:[3,5,-9]},roof_front_left:{p:[-28,31,27],t:[3,5,-9]},roof_front_right:{p:[35,31,27],t:[3,5,-9]},roof_back_left:{p:[-28,31,-43],t:[3,5,-9]},roof_back_right:{p:[35,31,-43],t:[3,5,-9]},detail_corner:{p:[17,5,5],t:[12.48,3,0]},detail_roof_frame:{p:[22,17,8],t:[6,7,-7]},detail_chimneys:{p:[15,16,-18],t:[7,9,-10]},detail_damage:{p:[17,1.3,-3.9],t:[12.48,1.3,-3.9]},detail_threshold:{p:[1.8,.6,3],t:[1.8,.25,0]},detail_threshold_below:{p:[1.8,-.3,2],t:[1.8,.15,0]},detail_annex:{p:[-14,9,-5],t:[-3,2.5,-14]}};
const cv=v=>[v[0],v[2],-v[1]];
// Cameras follow the final photograph-oriented coordinate convention.
for(const v of Object.values(views)){v.p[0]=12.48-v.p[0];v.t[0]=12.48-v.t[0];}
views.photo1={p:[-24,10,15],t:[6,4,-8]};
views.detail_threshold={p:[10.7,.8,3],t:[10.7,.48,0]};
views.detail_threshold_below={p:[10.7,.15,3],t:[10.7,.45,0]};
for(const f of landmarks.facades){const M=f.matrix;const point=[M[0][3]+M[0][0]*f.length/2,M[1][3]+M[1][0]*f.length/2,f.height/2],n=[-M[0][1],-M[1][1],0];const dist=Math.max(10,f.length*1.5);views['facade_'+f.id]={p:cv(point.map((q,i)=>q+n[i]*dist)),t:cv(point)};}
for(const o of landmarks.openings){const t=cv(o.world),n=cv(o.normal),d=Math.max(3.4,(o.top-o.bottom)*2.5,o.width*2.5),s=[-n[2],0,n[0]];for(const [name,k]of[['front',0],['left',-.58],['right',.58]])views[`opening_${o.id}_${name}`]={p:t.map((q,i)=>q+n[i]*d+s[i]*d*k+(i===1?.12:0)),t};}
for(const k of Object.keys(views)){const op=document.createElement('option');op.value=k;op.textContent=k;$('view').append(op);}
const model=(await new GLTFLoader().loadAsync('./models/cp257_SOL61.glb')).scene;scene.add(model);model.traverse(o=>{if(o.isMesh){o.userData.original=o.material;for(const m of(Array.isArray(o.material)?o.material:[o.material]))if(m.map)m.map.anisotropy=Math.min(16,renderer.capabilities.getMaxAnisotropy());}});
function render(){renderer.render(scene,camera)}
function resize(){renderer.setSize(host.clientWidth,host.clientHeight);camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();render();}new ResizeObserver(resize).observe(host);
function setView(k){camera.position.fromArray(views[k].p);controls.target.fromArray(views[k].t);controls.update();$('view').value=k;render();}
function surface(mode){model.traverse(o=>{if(o.isMesh){const a=o.userData.original;const gen=(Array.isArray(a)?a:[a]).some(m=>m.userData.generated_unobserved_surface);o.material=mode==='clay'?clay:mode==='hypotheses'&&gen?highlight:a;}});render();}
$('view').onchange=e=>setView(e.target.value);$('surface').onchange=e=>surface(e.target.value);$('source').onclick=()=>$('source-dialog').showModal();$('close-source').onclick=()=>$('source-dialog').close();
document.querySelectorAll('.compare input').forEach(i=>i.oninput=()=>i.parentElement.style.setProperty('--split',i.value+'%'));
window.qa={views,async capture(key,mode='texture'){surface(mode);setView(key);resize();render();return{png:renderer.domElement.toDataURL('image/png'),camera:{position:camera.position.toArray(),target:controls.target.toArray(),fov:camera.fov,aspect:camera.aspect},exposure:renderer.toneMappingExposure,width:renderer.domElement.width,height:renderer.domElement.height};}};
setView('hero');$('status').textContent='SOL 6.1 · čp. 257 · pracovní rekonstrukce G';controls.addEventListener('change',render);
