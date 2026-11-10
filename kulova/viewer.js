// GLB viewer for /most/kulova/ (street and house pages). Data attributes on #canvas: data-model, data-mode=street|house, data-base, data-cp (house pages).
// Codex textures: data/textures.json maps cp -> {glb: 'models/textured/cpN.glb' | null, ...}. If a GLB is listed, the surface menu offers "Textury (Codex)":
// on house pages the textured house replaces the geometry model; in the street, textured houses are attached under their CP_<cp>_root node (same local frame).
import * as THREE from './vendor/three.module.js';
import {OrbitControls} from './vendor/OrbitControls.js';
import {GLTFLoader} from './vendor/GLTFLoader.js';
const el = document.getElementById('canvas'); const mode = el.dataset.mode || 'house'; const base = el.dataset.base || './'; const houseCp = el.dataset.cp || null;
const en = document.documentElement.lang === 'en'; const T = (cs, e) => en ? e : cs;
const status = document.getElementById('status'); const info = document.getElementById('info'); const surf = document.getElementById('surface');
const renderer = new THREE.WebGLRenderer({antialias: true}); renderer.setPixelRatio(Math.min(devicePixelRatio, 2)); renderer.outputColorSpace = THREE.SRGBColorSpace; el.appendChild(renderer.domElement);
const scene = new THREE.Scene(); scene.background = new THREE.Color(0xdfe3e8);
const cam = new THREE.PerspectiveCamera(40, 1, 0.3, 6000); const ctl = new OrbitControls(cam, renderer.domElement); ctl.enableDamping = true;
scene.add(new THREE.HemisphereLight(0xffffff, 0x8a8f7a, 1.15)); const sun = new THREE.DirectionalLight(0xffffff, 1.6); sun.position.set(-300, 420, 260); scene.add(sun);
const clay = new THREE.MeshStandardMaterial({color: 0xd2d0c8, roughness: 0.9});
const loader = new GLTFLoader(); let root, houses = {}, textures = {}, roots = {}, views = {}, texLoaded = {};
function fitBox(box, dir, dist = 1.6) {
  const c = box.getCenter(new THREE.Vector3()), s = box.getSize(new THREE.Vector3()), r = Math.max(s.x, s.y, s.z);
  ctl.target.copy(c); cam.position.copy(c).add(new THREE.Vector3(...dir).normalize().multiplyScalar(r * dist)); cam.near = r / 500; cam.far = r * 40; cam.updateProjectionMatrix(); ctl.update();
}
function boxOf(list) { const b = new THREE.Box3(); list.forEach(cp => roots[cp] && b.expandByObject(roots[cp])); return b; }
async function loadTextured(cp) {
  if (texLoaded[cp]) return texLoaded[cp];
  const t = textures[cp]; if (!t || !t.glb) return null;
  const g = await loader.loadAsync(base + t.glb); g.scene.traverse(o => { if (o.isMesh) o.userData.texmesh = true; });
  if (mode === 'street') roots[cp].add(g.scene); else scene.add(g.scene);
  texLoaded[cp] = g.scene; return g.scene;
}
async function applySurface() {
  const v = surf ? surf.value : 'mat'; const hypEl = document.getElementById('hyp'); const hyp = hypEl ? hypEl.checked : false; const tex = v === 'tex';
  const wanted = tex ? Object.keys(textures).filter(cp => textures[cp].glb && (mode === 'street' ? roots[cp] : cp === houseCp)) : [];
  if (tex && status) status.textContent = T('Načítání textur…', 'Loading textures…');
  for (const cp of wanted) { try { await loadTextured(cp); } catch (e) { console.error(e); } }
  root.traverse(o => {
    if (!o.isMesh || o.userData.texmesh) return;
    const texOn = tex && ((o.userData.cp && texLoaded[o.userData.cp]) || (mode !== 'street' && texLoaded[houseCp]));
    o.visible = !texOn; o.material = v === 'clay' ? clay : o.userData.orig;
    if (v === 'mat' && hyp && o.userData.cp && houses[o.userData.cp] && houses[o.userData.cp].wholly_hyp) { const m = o.userData.orig.clone(); m.emissive = new THREE.Color(0xb35a00); m.emissiveIntensity = 0.35; o.material = m; }
  });
  Object.values(texLoaded).forEach(s => { s.visible = tex; });
  if (status && tex) status.textContent = wanted.length ? T('Textury Codexu: ' + wanted.length + ' (ostatní domy bez textur).', 'Codex textures: ' + wanted.length + ' (other houses untextured).') : T('Pro tento výběr zatím nejsou textury.', 'No textures yet for this selection.');
}
function show(cp) {
  const h = houses[cp]; if (!h || !info) return; info.hidden = false;
  const disc = T(h.disclosure_cs, h.disclosure_en);   // 20.10.2026: project / hypothesis must always be stated
  info.innerHTML = '<h3>' + T('Čp.', 'No.') + ' ' + cp + '</h3>' + (disc ? '<p class="k-disclosure"><strong>' + T('Upozornění:', 'Note:') + '</strong> ' + disc + '</p>' : '') + '<p>' + h.kind + '<br>' + T('Strana', 'Side') + ': ' + h.side_cs + ' · ' + T('revize', 'revision') + ' ' + h.rev
    + '<br>' + T('Přílohy v databázi', 'Database attachments') + ': ' + h.n_atts + '<br>' + T('Textury', 'Textures') + ': ' + h.tex + '</p><p><a href="' + base + 'cp' + cp + '/">'
    + T('Stránka domu: prameny a model →', 'House page: sources and model →') + '</a></p><button type="button" id="info-close">' + T('Zavřít', 'Close') + '</button>';
  document.getElementById('info-close').onclick = () => { info.hidden = true; };
}
const ray = new THREE.Raycaster(); let down = null;
renderer.domElement.addEventListener('pointerdown', e => { down = [e.clientX, e.clientY]; });
renderer.domElement.addEventListener('pointerup', e => {
  if (mode !== 'street' || !down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 5) return;
  const r = renderer.domElement.getBoundingClientRect(); ray.setFromCamera(new THREE.Vector2((e.clientX - r.left) / r.width * 2 - 1, -(e.clientY - r.top) / r.height * 2 + 1), cam);
  for (const hit of ray.intersectObject(root, true)) { if (!hit.object.visible) continue; let p = hit.object; while (p && !/^CP_(\d+)_root/.test(p.name || '')) p = p.parent; if (p) { show(p.name.match(/^CP_(\d+)_root/)[1]); break; } }
});
function resize() { const w = el.clientWidth, h = el.clientHeight; if (renderer.domElement.width !== Math.round(w * renderer.getPixelRatio()) || renderer.domElement.height !== Math.round(h * renderer.getPixelRatio())) { renderer.setSize(w, h, false); cam.aspect = w / h; cam.updateProjectionMatrix(); } }
async function main() {
  try { textures = await (await fetch(base + 'data/textures.json', {cache: 'no-cache'})).json(); } catch (e) { textures = {}; }
  if (mode === 'street') houses = await (await fetch(base + 'data/houses.json')).json();
  const anyTex = Object.entries(textures).some(([cp, t]) => t.glb && (mode === 'street' || cp === houseCp));
  if (surf && anyTex) surf.add(new Option(T('Textury (Codex)', 'Textures (Codex)'), 'tex'));
  const gltf = await loader.loadAsync(el.dataset.model, ev => { if (status && ev.total) status.textContent = T('Načítání ', 'Loading ') + Math.round(ev.loaded / ev.total * 100) + ' %'; });
  root = gltf.scene; scene.add(root);
  root.traverse(o => { const m = (o.name || '').match(/^CP_(\d+)_root/); if (m) roots[m[1]] = o; });
  root.traverse(o => { if (o.isMesh) { o.userData.orig = o.material; let p = o; while (p) { const m = (p.name || '').match(/^CP_(\d+)_root/); if (m) { o.userData.cp = m[1]; break; } p = p.parent; } } });
  const all = new THREE.Box3().setFromObject(root);
  if (mode === 'street') views = {
    overview: [T('Celá ulice', 'Whole street'), () => fitBox(all, [0.15, 0.9, 0.75], 0.8)],
    north_w: [T('Severní řada: 260 až 264', 'North row: 260 to 264'), () => fitBox(boxOf(['260', '261', '262', '263', '264']), [0.0, 0.75, 1.0], 1.1)],
    north_e: [T('Severní řada: 111 až 267', 'North row: 111 to 267'), () => fitBox(boxOf(['111', '265', '266', '267']), [0.0, 0.75, 1.0], 1.15)],
    south: [T('Jižní řada: 259 až 257', 'South row: 259 to 257'), () => fitBox(boxOf(['259', '258', '1608', '1712', '257']), [0.0, 0.75, -1.0], 1.1)],
    k262: [T('Čp. 262 zblízka', 'House 262 close-up'), () => fitBox(boxOf(['262']), [0.25, 0.3, 1.0], 1.2)],
    top: [T('Shora', 'From above'), () => fitBox(all, [0.0, 1.0, 0.02], 0.75)] };
  else views = {
    oblique: [T('Šikmo zepředu', 'Front oblique'), () => fitBox(all, [0.7, 0.55, 1.0], 1.35)],
    front: [T('Průčelí', 'Front'), () => fitBox(all, [0, 0.25, 1], 1.5)],
    back: [T('Zezadu', 'Rear'), () => fitBox(all, [-0.6, 0.55, -1.0], 1.35)],
    roof: [T('Střecha shora', 'Roof from above'), () => fitBox(all, [0.2, 1.0, 0.35], 1.3)] };
  const sel = document.getElementById('view'); if (sel) { for (const [k, [label]] of Object.entries(views)) sel.add(new Option(label, k)); sel.onchange = () => views[sel.value][1](); }
  Object.values(views)[0][1](); await applySurface(); ['surface', 'hyp'].forEach(id => { const x = document.getElementById(id); if (x) x.addEventListener('change', applySurface); });
  if (status && (!surf || surf.value !== 'tex')) status.textContent = T('Načteno. Tažením otáčejte, kolečkem přibližujte', 'Loaded. Drag to rotate, scroll to zoom') + (mode === 'street' ? T(', klikem vyberte dům.', ', click a house to select it.') : '.');
}
renderer.setAnimationLoop(() => { resize(); ctl.update(); renderer.render(scene, cam); });
main().catch(e => { if (status) status.textContent = T('Model se nepodařilo načíst: ', 'Could not load the model: ') + e.message; console.error(e); });
