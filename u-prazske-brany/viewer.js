// GLB viewer for /most/u-prazske-brany/ (street and house pages), adapted from /most/kulova/viewer.js (25. 10. 2026).
// #canvas data attributes: data-mode=street|house, data-model (GLB), data-base, data-cp (house key, e.g. 574 or 413_a).
// Street page: if data-model is empty or fails to load, the street is composed from the house GLBs and the transforms in data/houses.json
// (layout frame X east, Y north, Z up -> glTF: position (x, z, -y), rotation about Y = rotation_z). House roots are named CP_<key>_root as in the street GLB.
// Codex textures: data/textures.json maps key -> {glb: 'models/textured/cp<key>.glb' | null}; listed GLBs add the surface option "Textury (Codex)".
import * as THREE from './vendor/three.module.js';
import {OrbitControls} from './vendor/OrbitControls.js';
import {GLTFLoader} from './vendor/GLTFLoader.js';
const KEY = /^CP_(G?[0-9]+(?:_[a-z])?)_root/;   // 26.10.2026: G<id> = GIS building without cp
const el = document.getElementById('canvas'); const mode = el.dataset.mode || 'house'; const base = el.dataset.base || './'; const houseCp = el.dataset.cp || null;
const en = document.documentElement.lang === 'en'; const T = (cs, e) => en ? e : cs; const cap = s => s ? s[0].toUpperCase() + s.slice(1) : s;
const status = document.getElementById('status'); const info = document.getElementById('info'); const surf = document.getElementById('surface');
const renderer = new THREE.WebGLRenderer({antialias: true}); renderer.setPixelRatio(Math.min(devicePixelRatio, 2)); renderer.outputColorSpace = THREE.SRGBColorSpace; el.appendChild(renderer.domElement);
const scene = new THREE.Scene(); scene.background = new THREE.Color(0xdfe3e8);
const cam = new THREE.PerspectiveCamera(40, 1, 0.3, 6000); const ctl = new OrbitControls(cam, renderer.domElement); ctl.enableDamping = true;
scene.add(new THREE.HemisphereLight(0xffffff, 0x8a8f7a, 1.15)); const sun = new THREE.DirectionalLight(0xffffff, 1.6); sun.position.set(-300, 420, 260); scene.add(sun);
const clay = new THREE.MeshStandardMaterial({color: 0xd2d0c8, roughness: 0.9});
const loader = new GLTFLoader(); let root, houses = {}, textures = {}, roots = {}, views = {}, texLoaded = {};
function fitBox(box, dir, dist = 1.6) {
  if (box.isEmpty()) return;
  const c = box.getCenter(new THREE.Vector3()), s = box.getSize(new THREE.Vector3()), r = Math.max(s.x, s.y, s.z);
  ctl.target.copy(c); cam.position.copy(c).add(new THREE.Vector3(...dir).normalize().multiplyScalar(r * dist)); cam.near = r / 500; cam.far = r * 40; cam.updateProjectionMatrix(); ctl.update();
}
function boxOf(list) { const b = new THREE.Box3(); list.forEach(k => roots[k] && b.expandByObject(roots[k])); return b; }
function frontDir(list) {   // average outward facade normal of the listed houses (house front = -Y local in Blender = +Z local in glTF)
  let x = 0, z = 0; list.forEach(k => { const h = houses[k]; if (h && roots[k]) { const a = h.rot_deg * Math.PI / 180; x += Math.sin(a); z += Math.cos(a); } });
  const l = Math.hypot(x, z) || 1; return [x / l, 0.75, z / l];
}
async function compose() {
  const g = new THREE.Group(); g.name = 'u_prazske_brany_composed'; const list = Object.entries(houses).filter(([k, h]) => h.glb && h.origin); let done = 0;
  await Promise.all(list.map(async ([k, h]) => {
    const r = new THREE.Group(); r.name = 'CP_' + k + '_root'; const a = h.rot_deg * Math.PI / 180, adj = h.origin_adjust_m || 0;
    r.position.set(h.origin[0] + adj * Math.cos(a), h.origin[2] || 0, -(h.origin[1] + adj * Math.sin(a))); r.rotation.y = a;
    const m = await loader.loadAsync(base + h.glb); r.add(m.scene); g.add(r); done++;
    if (status) status.textContent = T('Skládání ulice z domů: ', 'Composing the street from houses: ') + done + ' / ' + list.length;
  }));
  const b = new THREE.Box3().setFromObject(g), s = b.getSize(new THREE.Vector3()), c = b.getCenter(new THREE.Vector3());
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(s.x * 1.4 + 40, s.z * 1.4 + 40), new THREE.MeshStandardMaterial({color: 0x5c5b56, roughness: 1}));
  ground.rotation.x = -Math.PI / 2; ground.position.set(c.x, -0.03, c.z); ground.name = 'Ground_Context'; g.add(ground); return g;
}
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
    if (!o.isMesh || o.userData.texmesh || !o.userData.orig) return;
    const texOn = tex && ((o.userData.cp && texLoaded[o.userData.cp]) || (mode !== 'street' && texLoaded[houseCp]));
    o.visible = !texOn; o.material = v === 'clay' ? clay : o.userData.orig;
    if (v === 'mat' && hyp && o.userData.cp && houses[o.userData.cp] && houses[o.userData.cp].has_presentation) { const m = o.userData.orig.clone(); m.emissive = new THREE.Color(0xb35a00); m.emissiveIntensity = 0.35; o.material = m; }
  });
  Object.values(texLoaded).forEach(s => { s.visible = tex; });
  if (status && tex) status.textContent = wanted.length ? T('Textury Codexu: ' + wanted.length + ' (ostatní domy bez textur).', 'Codex textures: ' + wanted.length + ' (other houses untextured).') : T('Pro tento výběr zatím nejsou textury.', 'No textures yet for this selection.');
}
function show(cp) {
  const h = houses[cp]; if (!h || !info) return; info.hidden = false;
  const lab = T(h.label_cs, h.label_en), disc = T(h.disclosure_cs, h.disclosure_en), gn = T(h.gis_note_cs, h.gis_note_en);   // presentation label must always be shown
  info.innerHTML = '<h3>' + (h.label.startsWith('GIS') ? T('Budova', 'Building') : T('Čp.', 'No.')) + ' ' + h.label + (h.label.startsWith('GIS') ? T(' (bez čp.)', ' (no house number)') : '') + '</h3>' + (lab ? '<p class="k-disclosure"><strong>' + cap(lab) + ':</strong> ' + disc + '</p>' : '')
    + (gn ? '<p class="k-disclosure"><small>' + gn + '</small></p>' : '') + '<p>' + T(h.kind, h.kind_en) + '<br>' + T(h.section_cs, h.section_en) + ' · ' + T('revize', 'revision') + ' ' + h.rev
    + '<br>' + T('Přílohy v databázi', 'Database attachments') + ': ' + (h.label.startsWith('GIS') ? T('žádná struktura (budova bez čp.)', 'no structure (no house number)') : h.n_atts) + '<br>' + T('Textury', 'Textures') + ': ' + h.tex + '</p><p><a href="' + base + 'cp' + cp + '/">'
    + T('Stránka domu: prameny a model →', 'House page (Czech): sources and model →') + '</a></p><button type="button" id="info-close">' + T('Zavřít', 'Close') + '</button>';
  document.getElementById('info-close').onclick = () => { info.hidden = true; };
}
const ray = new THREE.Raycaster(); let down = null;
renderer.domElement.addEventListener('pointerdown', e => { down = [e.clientX, e.clientY]; });
renderer.domElement.addEventListener('pointerup', e => {
  if (mode !== 'street' || !root || !down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 5) return;
  const r = renderer.domElement.getBoundingClientRect(); ray.setFromCamera(new THREE.Vector2((e.clientX - r.left) / r.width * 2 - 1, -(e.clientY - r.top) / r.height * 2 + 1), cam);
  for (const hit of ray.intersectObject(root, true)) { if (!hit.object.visible) continue; let p = hit.object; while (p && !KEY.test(p.name || '')) p = p.parent; if (p) { show(p.name.match(KEY)[1]); break; } }
});
function resize() { const w = el.clientWidth, h = el.clientHeight; if (renderer.domElement.width !== Math.round(w * renderer.getPixelRatio()) || renderer.domElement.height !== Math.round(h * renderer.getPixelRatio())) { renderer.setSize(w, h, false); cam.aspect = w / h; cam.updateProjectionMatrix(); } }
async function main() {
  try { textures = await (await fetch(base + 'data/textures.json', {cache: 'no-cache'})).json(); } catch (e) { textures = {}; }
  if (mode === 'street') houses = await (await fetch(base + 'data/houses.json', {cache: 'no-cache'})).json();
  const anyTex = Object.entries(textures).some(([cp, t]) => t.glb && (mode === 'street' || cp === houseCp));
  if (surf && anyTex) surf.add(new Option(T('Textury (Codex)', 'Textures (Codex)'), 'tex'));
  const prog = ev => { if (status && ev.total) status.textContent = T('Načítání ', 'Loading ') + Math.round(ev.loaded / ev.total * 100) + ' %'; };
  if (el.dataset.model) { try { root = (await loader.loadAsync(el.dataset.model, prog)).scene; } catch (e) { if (mode !== 'street') throw e; console.warn('street GLB not available, composing', e); } }
  if (!root) root = await compose();
  scene.add(root);
  root.traverse(o => { const m = (o.name || '').match(KEY); if (m) roots[m[1]] = o; });
  root.traverse(o => { if (o.isMesh) { o.userData.orig = o.material; let p = o; while (p) { const m = (p.name || '').match(KEY); if (m) { o.userData.cp = m[1]; break; } p = p.parent; } } });
  const all = new THREE.Box3(); Object.values(roots).forEach(r => all.expandByObject(r)); if (all.isEmpty()) all.setFromObject(root);
  if (mode === 'street') {
    views = {overview: [T('Celá ulice', 'Whole street'), () => fitBox(all, [0.2, 0.9, 0.6], 0.85)]};
    const secs = {}; Object.entries(houses).forEach(([k, h]) => { if (roots[k]) (secs[h.section] = secs[h.section] || []).push(k); });
    Object.keys(secs).sort().forEach(s => { const ks = secs[s], h = houses[ks[0]]; views[s] = [T(h.section_cs, h.section_en), () => fitBox(boxOf(ks), frontDir(ks), 1.15)]; });
    views.top = [T('Shora', 'From above'), () => fitBox(all, [0.0, 1.0, 0.02], 0.8)];
  } else views = {
    oblique: [T('Šikmo zepředu', 'Front oblique'), () => fitBox(all, [0.7, 0.55, 1.0], 2.0)],
    front: [T('Průčelí', 'Front'), () => fitBox(all, [0, 0.25, 1], 2.1)],
    back: [T('Zezadu', 'Rear'), () => fitBox(all, [-0.6, 0.55, -1.0], 2.0)],
    roof: [T('Střecha shora', 'Roof from above'), () => fitBox(all, [0.2, 1.0, 0.35], 1.9)] };
  const sel = document.getElementById('view'); if (sel) { for (const [k, [label]] of Object.entries(views)) sel.add(new Option(label, k)); sel.onchange = () => views[sel.value][1](); }
  Object.values(views)[0][1](); await applySurface(); ['surface', 'hyp'].forEach(id => { const x = document.getElementById(id); if (x) x.addEventListener('change', applySurface); });
  if (status && (!surf || surf.value !== 'tex')) status.textContent = T('Načteno. Tažením otáčejte, kolečkem přibližujte', 'Loaded. Drag to rotate, scroll to zoom') + (mode === 'street' ? T(', klikem vyberte dům.', ', click a house to select it.') : '.');
}
renderer.setAnimationLoop(() => { resize(); ctl.update(); renderer.render(scene, cam); });
main().catch(e => { if (status) status.textContent = T('Model se nepodařilo načíst: ', 'Could not load the model: ') + e.message; console.error(e); });
