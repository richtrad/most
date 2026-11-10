from pathlib import Path
import bpy,json,hashlib,struct
O=Path(__file__).resolve().parent
def geom(o):
 m=o.data
 return hashlib.sha256(json.dumps({'v':[list(v.co) for v in m.vertices],'p':[list(p.vertices) for p in m.polygons],'uv':[[list(l.uv) for l in u.data] for u in m.uv_layers]},sort_keys=True).encode()).hexdigest()
def snapshot(path):
 bpy.ops.wm.open_mainfile(filepath=str(path),load_ui=False)
 objects={o.name:geom(o) for o in bpy.context.scene.objects if o.type=='MESH'}
 used={n.image.name for o in bpy.context.scene.objects if o.type=='MESH' for m in o.data.materials if m and m.use_nodes for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image}
 images={i.name:hashlib.sha256(i.packed_file.data).hexdigest() for i in bpy.data.images if i.packed_file and i.name in used}
 bad=[]
 for o in bpy.context.scene.objects:
  if o.type!='MESH':continue
  me=o.data;me.calc_loop_triangles();uv=me.uv_layers.active
  for t in me.loop_triangles:
   if t.area<1e-12:continue
   a,b,c=[uv.data[i].uv for i in t.loops]
   if abs((b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x))<1e-15:bad.append([o.name,t.polygon_index])
 return objects,images,bad
b,bi,bb=snapshot(O.parent/'kulova_cp261_bevel_lab_2026-09-26/models/cp261_bevel_c.blend');report={}
for k in ['geometry','inpaint']:
 o,im,bad=snapshot(O/'models'/f'cp261_openings_{k}.blend')
 changed=[n for n in b if b[n]!=o[n]];changed_im=[n for n in bi if bi[n]!=im[n]]
 assert not bad,bad
 if k=='geometry':assert not changed_im
 else:assert not changed and changed_im==['registered_facade.png']
 raw=(O/'models'/f'cp261_openings_{k}.glb').read_bytes();g=json.loads(raw[20:20+struct.unpack_from('<I',raw,12)[0]])
 assert all('bufferView' in x for x in g['images'])
 report[k]={'changed_objects':changed,'unchanged_objects':len(b)-len(changed),'changed_images':changed_im,'degenerate_uv_triangles':len(bad),'glb_sha256':hashlib.sha256(raw).hexdigest(),'embedded_images':len(g['images'])}
(O/'evidence/audit.json').write_text(json.dumps(report,indent=2))
print('AUDIT',report)
