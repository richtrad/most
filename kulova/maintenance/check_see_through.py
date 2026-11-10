"""See-through check (v5, 19.10.2026; viewpoints outside the bounding circle, roof/footprint coverage): a FIRST hit that lies inside the masonry outline (> 15 cm behind the wall line) and above the wall top = the viewer sees into the attic through a gap (counted as failure);
back-face first hits are reported separately (relevant only for single-sided materials). Original idea: from viewpoints all around a house (pedestrian, eave level, close look-up under the eaves, above), cast rays at the house;
a FIRST hit on the back side of a face (dot(face normal, ray) > 0.05) means the viewer looks into the inside of the building through a gap.
Hits within 3 cm of a boundary edge of a single-sided sheet (roof edge thickness) are tolerated. Works on .blend and .glb.
usage: blender -b --python check_see_through.py -- <out.json> <file> [<file> ...]"""
import bpy, bmesh, json, math, sys
from pathlib import Path
from mathutils import Vector
from mathutils.bvhtree import BVHTree
from mathutils.kdtree import KDTree
args = sys.argv[sys.argv.index('--')+1:]; OUT = Path(args[0]); report = []
def load(f):
    if f.endswith('.blend'): bpy.ops.wm.open_mainfile(filepath=f)
    else: bpy.ops.wm.read_factory_settings(use_empty=True); bpy.ops.import_scene.gltf(filepath=f)
def seg_dist(px, py, a, b):
    ax, ay = a; bx, by = b; dx, dy = bx - ax, by - ay; L = dx*dx + dy*dy or 1e-12; t = max(0, min(1, ((px-ax)*dx + (py-ay)*dy) / L)); return math.hypot(px - ax - t*dx, py - ay - t*dy)
def inside_poly(px, py, poly):
    c = False
    for i in range(len(poly)):
        (x0, y0), (x1, y1) = poly[i], poly[(i+1) % len(poly)]
        if (y0 > py) != (y1 > py) and px < x0 + (py - y0) * (x1 - x0) / (y1 - y0): c = not c
    return c
CT = [None]   # coverings-only BVH of the current file (roofs, wing roofs, dormers, *_Roof boxes)
def in_attic_zone(p, tops):
    for poly, zt in tops:
        if p.z > zt - 0.05 and inside_poly(p.x, p.y, poly) and min(seg_dist(p.x, p.y, poly[i], poly[(i+1) % len(poly)]) for i in range(len(poly))) > 0.15:
            if CT[0] is not None and p.z - zt > 0.1 and CT[0].ray_cast(Vector((p.x, p.y, zt + 0.03)), Vector((0, 0, 1)), p.z - zt - 0.06)[0] is not None: continue   # a covering lies between this wall top and p: p is not in this wall's attic (e.g. a low annex under a wing eave)
            return True
    return False
def interior(p, obj, dirv, tops, tree, owner, fn):
    if not in_attic_zone(p, tops): return False
    if 'Roof' in obj and (fn.z < -0.2 or (fn.z > 0.2 and fn.dot(dirv) > 0)): return True   # the attic side of the roof (underside of a thick roof / back of a sheet) inside the walls
    if 'Roof' in obj: return False                                                         # outer covering
    q = p - dirv * 0.03   # test point 3 cm in front of the hit (on the viewer's side), so a hit exactly in the plane of a roof edge is judged from the outside
    if not in_attic_zone(q, tops): return False
    loc, nor, idx, dist = tree.ray_cast(q + Vector((0, 0, 0.01)), Vector((0, 0, 1)), 100.0)
    return loc is not None and 'Roof' in owner[idx] and dist > 0.02  # the hit point is covered by a roof = inside the attic
for f in args[1:]:
    load(f); dg = bpy.context.evaluated_depsgraph_get(); bm = bmesh.new(); owner = []; kd_pts = []
    for o in [o for o in bpy.context.scene.objects if o.type == 'MESH' and o.visible_get() and not o.name.startswith(('Ground', 'Street_'))]:
        m = o.evaluated_get(dg).to_mesh(); t = bmesh.new(); t.from_mesh(m); t.transform(o.matrix_world); o.evaluated_get(dg).to_mesh_clear()
        bmesh.ops.remove_doubles(t, verts=t.verts, dist=1e-4)
        for e in t.edges:
            if e.is_boundary:
                a, b = e.verts[0].co, e.verts[1].co; n = max(1, int((b - a).length / 0.01))
                kd_pts += [a.lerp(b, i / n) for i in range(n + 1)]
        tm = bpy.data.meshes.new('tmp'); t.to_mesh(tm); t.free(); n0 = len(bm.faces); bm.from_mesh(tm); bpy.data.meshes.remove(tm); owner += [o.name] * (len(bm.faces) - n0)
    tops = []   # masonry footprint polygons at the wall top (upward faces at the highest level of each *Masonry* object)
    SKIP = ('Roof', 'Chimney', 'Downpipe', 'Gable', 'Surround', 'Pilaster', 'Threshold', 'Sill', 'Pediment', 'Cornice', 'Closure', 'Dormer', 'Gutter', 'Keystone', 'Console')
    def wall_block(o):   # masonry or a ground-standing wall box (e.g. 262 Right_Strip) at least 2.5 m high and 1 m wide
        if 'Masonry' in o.name: return True
        if any(k in o.name for k in SKIP): return False
        bb = [o.matrix_world @ Vector(c) for c in o.bound_box]; z0 = min(v.z for v in bb); z1 = max(v.z for v in bb)
        return z0 <= 0.05 and z1 - z0 >= 2.5 and max(v.x for v in bb) - min(v.x for v in bb) >= 1.0 and max(v.y for v in bb) - min(v.y for v in bb) >= 1.0
    for o in [o for o in bpy.context.scene.objects if o.type == 'MESH' and wall_block(o)]:
        t = bmesh.new(); t.from_mesh(o.data); t.transform(o.matrix_world); bmesh.ops.remove_doubles(t, verts=t.verts, dist=1e-4); zt = max(v.co.z for v in t.verts)
        for fc in t.faces:
            if fc.normal.z > 0.9 and abs(fc.calc_center_median().z - zt) < 0.05: tops.append(([(v.co.x, v.co.y) for v in fc.verts], zt))
        t.free()
    import re
    covn = lambda n: (re.search(r'_Roof(\.\d+)?$', n) or '_WingRoof_' in n or '_Dormer_' in n) and 'Closure' not in n   # coverings only (no closures, gables, attic block)
    cb = bmesh.new(); cb.from_mesh(bpy.data.meshes.new('cov_tmp'))
    for o in [o for o in bpy.context.scene.objects if o.type == 'MESH' and covn(o.name)]:
        t = bmesh.new(); t.from_mesh(o.evaluated_get(dg).to_mesh()); t.transform(o.matrix_world); o.evaluated_get(dg).to_mesh_clear(); tm = bpy.data.meshes.new('tmp'); t.to_mesh(tm); t.free(); cb.from_mesh(tm); bpy.data.meshes.remove(tm)
    ctree = BVHTree.FromBMesh(cb) if len(cb.faces) else None; cb.free(); CT[0] = ctree
    bm.faces.ensure_lookup_table(); tree = BVHTree.FromBMesh(bm); kd = KDTree(max(1, len(kd_pts)))
    for i, p in enumerate(kd_pts): kd.insert(p, i)
    kd.balance()
    mn = Vector((min(v.co[i] for v in bm.verts) for i in range(3))); mx = Vector((max(v.co[i] for v in bm.verts) for i in range(3))); C = (mn + mx) / 2; S = max(mx.x - mn.x, mx.y - mn.y)
    eave = mn.z + 0.62 * (mx.z - mn.z)
    views = []
    for k in range(24):
        a = 2 * math.pi * k / 24; d = Vector((math.cos(a), math.sin(a), 0))
        R0 = 0.5 * math.hypot(mx.x - mn.x, mx.y - mn.y)   # every viewpoint outside the bounding circle of the house
        for h, dist in ((1.6, R0 + 8), (eave, R0 + 8), (eave + 0.4, R0 + 8), (mx.z + 4, R0 + 10), (1.6, R0 + 2.5)):
            views.append(Vector((C.x, C.y, 0)) + d * dist + Vector((0, 0, h)))
    hits = []; back = []; n_rays = 0
    for v in views:
        for i in range(36):
            for j in range(24):
                tgt = Vector((mn.x + (mx.x - mn.x) * (i + 0.5) / 36, mn.y + (mx.y - mn.y) * ((i * 7 + j) % 24 + 0.5) / 24, mn.z + (mx.z - mn.z) * (j + 0.5) / 24))
                dirv = (tgt - v).normalized(); n_rays += 1; loc, nor, idx, dist = tree.ray_cast(v, dirv, 500.0)
                if loc is None: continue
                fn = bm.faces[idx].normal
                if interior(loc, owner[idx], dirv, tops, tree, owner, fn): hits.append(dict(kind='interior', obj=owner[idx], loc=[round(c, 2) for c in loc], view=[round(c, 1) for c in v]))
                elif fn.dot(dirv) > 0.05 and (kd.find(loc)[2] if kd_pts else 9.0) > 0.03: back.append(dict(obj=owner[idx], loc=[round(c, 2) for c in loc]))
    # 19.10.2026: roof/footprint consistency on a 0.25 m grid. uncovered = masonry top with no roof above it;
    # unsupported = roof surface farther than 1.0 m outside every masonry outline (roof hanging over nothing, e.g. 263 r4).
    unc = 0; uns = 0; g = 0.25; unc_pts = []; uns_pts = []
    nx_, ny_ = int((mx.x - mn.x) / g) + 1, int((mx.y - mn.y) / g) + 1
    for ix in range(nx_):
        for iy in range(ny_):
            x, y = mn.x + (ix + 0.5) * g, mn.y + (iy + 0.5) * g
            ins = [(poly, zt) for poly, zt in tops if inside_poly(x, y, poly)]
            if ins:
                zt = max(z for _, z in ins); loc = ctree.ray_cast(Vector((x, y, zt - 0.02)), Vector((0, 0, 1)), 100.0)[0] if ctree else None
                if loc is None: unc += 1; unc_pts.append((round(x, 2), round(y, 2)))
            else:
                loc = ctree.ray_cast(Vector((x, y, mx.z + 1)), Vector((0, 0, -1)), 200.0)[0] if ctree else None
                if loc is not None and all(min(seg_dist(x, y, poly[i], poly[(i+1) % len(poly)]) for i in range(len(poly))) > 1.0 for poly, _ in tops): uns += 1; uns_pts.append((round(x, 2), round(y, 2)))
    uncovered_m2 = round(unc * g * g, 2); unsupported_m2 = round(uns * g * g, 2)
    by = {}
    for h in hits: by[h['obj']] = by.get(h['obj'], 0) + 1
    bb = {}
    for h in back: bb[h['obj']] = bb.get(h['obj'], 0) + 1
    r = dict(file=f, rays=n_rays, masonry_tops=len(tops), see_through_hits=len(hits), backface_hits_info=len(back), backface_by_object=bb, by_object=dict(sorted(by.items(), key=lambda kv: -kv[1])), samples=hits[:25], uncovered_masonry_top_m2=uncovered_m2, unsupported_roof_m2=unsupported_m2, uncovered_samples=unc_pts[:40], unsupported_samples=uns_pts[:40],
             passed=len(hits) <= 3 and uncovered_m2 <= 0.5 and unsupported_m2 <= 1.0)   # <= 3 hairline hits (1 cm joints) tolerated
    report.append(r); bm.free(); print('SEETHROUGH', Path(f).name, 'rays', n_rays, 'tops', len(tops), 'INTERIOR hits', len(hits), dict(list(r['by_object'].items())[:6]), '| backface info', len(back), '| uncovered m2', uncovered_m2, '| unsupported m2', unsupported_m2, '| PASS' if r['passed'] else '| FAIL')
OUT.write_text(json.dumps(report, indent=1)); print('SEETHROUGH DONE')
