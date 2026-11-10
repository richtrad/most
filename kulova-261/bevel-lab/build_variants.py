from pathlib import Path
import bpy,bmesh,json,math,hashlib,struct
from mathutils import Vector
O=Path(__file__).resolve().parent
for d in ['models','evidence','qa','web']:(O/d).mkdir(parents=True,exist_ok=True)
source=O.parent/'kulova_cp261_v10_2026-09-26/models/cp261_v10.blend'
variants=[('a',.003,.003,.005,2),('b',.005,.005,.008,3),('c',.008,.008,.012,3)]
def digest(o):
 m=o.data
 return hashlib.sha256(json.dumps({'v':[list(v.co) for v in m.vertices],'p':[list(p.vertices) for p in m.polygons],'uv':[[list(l.uv) for l in u.data] for u in m.uv_layers]},sort_keys=True).encode()).hexdigest()
report=[]
for key,sill,step,arch,segments in variants:
 bpy.ops.wm.open_mainfile(filepath=str(source),load_ui=False)
 before={o.name:digest(o) for o in bpy.context.scene.objects if o.type=='MESH'}
 results=[]
 for name,amount,kind,material in [('CP_261_Frames_Sills_And_Cornices',sill,'sill','GENERATED_REVEAL'),('CP_261_Entrance_Three_Steps_PROVISIONAL',step,'steps','GENERATED_REVEAL'),('CP_261_Restored_Original_Arch_Moulding',arch,'arch','GENERATED_PLASTER')]:
  o=bpy.data.objects[name];me=o.data;bm=bmesh.new();bm.from_mesh(me);bm.edges.ensure_lookup_table();bm.edges.index_update();chosen=[]
  for e in bm.edges:
   if not e.is_manifold or not e.is_convex or e.calc_face_angle()<math.radians(45):continue
   pts=[v.co for v in e.verts]
   if kind=='sill':
    # Only the two projecting sill boxes under each window, not jambs or cornices.
    eligible=all(any(lo-1e-5<=v.z<=hi+1e-5 for lo,hi in [(4.285,4.4375),(.695,.8475)]) for v in pts) and min(v.y for v in pts)<-.12
   elif kind=='steps':eligible=min(v.z for v in pts)>.05 and any(f.normal.z>.5 for f in e.link_faces)
   else:eligible=max(v.y for v in pts)<.331
   if eligible:chosen.append(e.index)
  bm.free();assert chosen,(kind,'no edges')
  attribute=me.attributes.get('bevel_weight_edge') or me.attributes.new('bevel_weight_edge','FLOAT','EDGE')
  for i in chosen:attribute.data[i].value=1
  edge_mat=bpy.data.materials[material].copy();edge_mat.name='BEVEL_'+kind.upper();me.materials.append(edge_mat);slot=len(me.materials)-1
  bpy.ops.object.select_all(action='DESELECT');o.select_set(True);bpy.context.view_layer.objects.active=o
  modifier=o.modifiers.new('Selected exposed edges '+str(amount*1000)+'mm','BEVEL');modifier.width=amount;modifier.segments=segments;modifier.limit_method='WEIGHT';modifier.affect='EDGES';modifier.use_clamp_overlap=True;modifier.material=slot;modifier.harden_normals=True
  bpy.ops.object.modifier_apply(modifier=modifier.name)
  me=o.data;uv=me.uv_layers.active;new_faces=0
  for p in me.polygons:
   if p.material_index!=slot:continue
   new_faces+=1;normal=p.normal.normalized();v=Vector((0,0,1))-normal*normal.z
   if v.length<.01:v=Vector((0,1,0))-normal*normal.y
   v.normalize();u=v.cross(normal).normalized()
   if u.x<-.01:u=-u
   span=3.44086 if kind=='arch' else 2.47742
   for li in p.loop_indices:
    co=me.vertices[me.loops[li].vertex_index].co;uv.data[li].uv=(co.dot(u)/span,co.dot(v)/span)
  assert new_faces>0
  bm=bmesh.new();bm.from_mesh(me);nonmanifold=sum(not e.is_manifold for e in bm.edges);bm.free()
  if kind!='sill':assert nonmanifold==0,(kind,nonmanifold)
  me.calc_loop_triangles();bad=0
  for t in me.loop_triangles:
   if t.area<1e-12:continue
   a,b,c=[uv.data[i].uv for i in t.loops]
   if abs((b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x))<1e-15:bad+=1
  assert bad==0,(kind,bad)
  results.append({'object':name,'selected_edges':len(chosen),'offset_m':amount,'segments':segments,'new_faces':new_faces,'nonmanifold_edges':nonmanifold,'degenerate_uv':bad})
 changed=[o.name for o in bpy.context.scene.objects if o.type=='MESH' and digest(o)!=before[o.name]]
 assert len(changed)==3,changed
 bpy.ops.wm.save_as_mainfile(filepath=str(O/'models'/('cp261_bevel_'+key+'.blend')))
 bpy.ops.export_scene.gltf(filepath=str(O/'models'/('cp261_bevel_'+key+'.glb')),export_format='GLB',export_extras=True)
 raw=(O/'models'/('cp261_bevel_'+key+'.glb')).read_bytes();g=json.loads(raw[20:20+struct.unpack_from('<I',raw,12)[0]]);assert all('bufferView' in im for im in g['images'])
 report.append({'id':key,'selected':results,'unchanged_objects':len(before)-3,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'embedded_images':len(g['images']),'visual_passed':False})
(O/'evidence/variants.json').write_text(json.dumps(report,indent=2),'utf8');print('VARIANTS_READY',json.dumps(report),flush=True)
