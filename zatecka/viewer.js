// GLB viewer for /most/zatecka/ (street and house pages). Data attributes on #canvas: data-model, data-mode=street|house, data-base.
import * as THREE from './vendor/three.module.js';
import {OrbitControls} from './vendor/OrbitControls.js';
import {GLTFLoader} from './vendor/GLTFLoader.js';
const el = document.getElementById('canvas'); const mode = el.dataset.mode || 'house'; const base = el.dataset.base || './';
const en = document.documentElement.lang === 'en'; const T = (cs, e) => en ? e : cs;
const status = document.getElementById('status'); const info = document.getElementById('info');
const renderer = new THREE.WebGLRenderer({antialias: true}); renderer.setPixelRatio(Math.min(devicePixelRatio, 2)); el.appendChild(renderer.domElement);
const scene = new THREE.Scene(); scene.background = new THREE.Color(0xdfe3e8);
const cam = new THREE.PerspectiveCamera(40, 1, 0.3, 6000); const ctl = new OrbitControls(cam, renderer.domElement); ctl.enableDamping = true;
scene.add(new THREE.HemisphereLight(0xffffff, 0x8a8f7a, 2.0)); const sun = new THREE.DirectionalLight(0xffffff, 2.4); sun.position.set(-300, 420, 260); scene.add(sun);
const clay = new THREE.MeshStandardMaterial({color: 0xd2d0c8, roughness: 0.9});
let root, houses = {}, roots = {}, views = {};
function fitBox(box, dir, dist = 1.6) {
  const c = box.getCenter(new THREE.Vector3()), s = box.getSize(new THREE.Vector3()), r = Math.max(s.x, s.y, s.z);
  ctl.target.copy(c); cam.position.copy(c).add(new THREE.Vector3(...dir).normalize().multiplyScalar(r * dist)); cam.near = r / 500; cam.far = r * 40; cam.updateProjectionMatrix(); ctl.update();
}
function boxOf(list) { const b = new THREE.Box3(); list.forEach(cp => roots[cp] && b.expandByObject(roots[cp])); return b; }
function applySurface() {
  const clayOn = document.getElementById('surface')?.value === 'clay'; const hyp = document.getElementById('hyp')?.checked;
  root.traverse(o => { if (!o.isMesh) return; o.material = clayOn ? clay : o.userData.orig;
    if (!clayOn && hyp && o.userData.cp && houses[o.userData.cp]?.placement !== 'GIS') { const m = o.userData.orig.clone(); m.emissive = new THREE.Color(0xb35a00); m.emissiveIntensity = 0.35; o.material = m; } });
}
function show(cp) {
  const h = houses[cp]; if (!h || !info) return; info.hidden = false;
  info.innerHTML = `<h3>${T('Čp.', 'No.')} ${cp}</h3><p>${h.kind}<br>${T('Strana', 'Side')}: ${h.side_cs} · ${T('or. č.', 'orient. no.')} ${h.orient}<br>${T('Poloha', 'Position')}: ${h.placement === 'GIS' ? T('GIS půdorys', 'GIS footprint') : T('odhad (sekvence)', 'estimate (sequence)')}<br>${T('Prameny', 'Sources')}: ${h.n_photo} ${T('fotografií', 'photos')}, ${h.n_plan} ${T('náčrt', 'sketch')}, ${h.n_card} ${T('karet', 'cards')}</p><p><a href="${base}cp${cp}/">${T('Stránka domu: prameny a model →', 'House page: sources and model →')}</a></p><button type="button" id="info-close">${T('Zavřít', 'Close')}</button>`;
  document.getElementById('info-close').onclick = () => { info.hidden = true; };
}
const ray = new THREE.Raycaster(); let down = null;
renderer.domElement.addEventListener('pointerdown', e => { down = [e.clientX, e.clientY]; });
renderer.domElement.addEventListener('pointerup', e => {
  if (mode !== 'street' || !down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 5) return;
  const r = renderer.domElement.getBoundingClientRect(); ray.setFromCamera(new THREE.Vector2((e.clientX - r.left) / r.width * 2 - 1, -(e.clientY - r.top) / r.height * 2 + 1), cam);
  for (const hit of ray.intersectObject(root, true)) if (hit.object.userData.cp) { show(hit.object.userData.cp); break; }
});
async function main() {
  if (mode === 'street') houses = await (await fetch(base + 'data/houses.json')).json();
  const gltf = await new GLTFLoader().loadAsync(el.dataset.model, ev => { if (status && ev.total) status.textContent = T('Načítání ', 'Loading ') + Math.round(ev.loaded / ev.total * 100) + ' %'; });
  root = gltf.scene; scene.add(root);
  root.traverse(o => { const m = (o.name || '').match(/^CP_(\d+)_root/); if (m) roots[m[1]] = o; });
  root.traverse(o => { if (o.isMesh) { o.userData.orig = o.material; let p = o; while (p) { const m = (p.name || '').match(/^CP_(\d+)_root/); if (m) { o.userData.cp = m[1]; break; } p = p.parent; } } });
  const all = new THREE.Box3().setFromObject(root);
  if (mode === 'street') views = {
    overview: [T('Celá ulice', 'Whole street'), () => fitBox(all, [0.25, 1.0, 0.55], 0.75)],
    brewery: [T('Konec u pivovaru', 'Brewery end'), () => fitBox(boxOf(['437', '110', '774', '699', '453', '1006']), [0.6, 0.75, 0.9], 1.0)],
    corner: [T('Nároží R. Luxemburkové', 'Corner with R. Luxemburkové'), () => fitBox(boxOf(['699', '770', '453']), [0.9, 0.35, 0.6], 1.2)],
    villas: [T('Vilová řada (poloha odhadem)', 'Villa row (estimated position)'), () => fitBox(boxOf(['1918', '1906', '1907', '1914', '1915', '1903', '1904', '1899', '1901', '1867', '1872']), [1.0, 0.7, 0.2], 0.9)],
    school: [T('Gymnázium / muzeum 1360', 'Grammar school / museum 1360'), () => fitBox(boxOf(['1360']), [0.5, 0.6, -0.8], 1.1)] };
  else { const s = all.getSize(new THREE.Vector3()); views = {
    oblique: [T('Šikmo zepředu', 'Front oblique'), () => fitBox(all, [0.7, 0.55, 1.0], 1.35)],
    front: [T('Průčelí', 'Front'), () => fitBox(all, [0, 0.25, 1], 1.5)],
    back: [T('Zezadu', 'Rear'), () => fitBox(all, [-0.6, 0.55, -1.0], 1.35)],
    roof: [T('Střecha shora', 'Roof from above'), () => fitBox(all, [0.2, 1.0, 0.35], 1.3)] };
    // houses are exported in their local frame: facade plane is z=0 in glTF (Blender y=0); the street side is +z
  }
  const sel = document.getElementById('view'); if (sel) { for (const [k, [label]] of Object.entries(views)) sel.add(new Option(label, k)); sel.onchange = () => views[sel.value][1](); }
  Object.values(views)[0][1](); applySurface(); ['surface', 'hyp'].forEach(id => document.getElementById(id)?.addEventListener('change', applySurface));
  if (status) status.textContent = T('Načteno. Tažením otáčejte, kolečkem přibližujte', 'Loaded. Drag to rotate, scroll to zoom') + (mode === 'street' ? T(', klikem vyberte dům.', ', click a house to select it.') : '.');
}
function resize() { const w = el.clientWidth, h = el.clientHeight; if (renderer.domElement.width !== Math.round(w * renderer.getPixelRatio()) || renderer.domElement.height !== Math.round(h * renderer.getPixelRatio())) { renderer.setSize(w, h, false); cam.aspect = w / h; cam.updateProjectionMatrix(); } }
renderer.setAnimationLoop(() => { resize(); ctl.update(); renderer.render(scene, cam); });
main().catch(e => { if (status) status.textContent = T('Model se nepodařilo načíst: ', 'Could not load the model: ') + e.message; console.error(e); });
