from pathlib import Path
import bpy,json,sys,hashlib
from mathutils import Vector
O=Path(__file__).resolve().parent
sys.path.insert(0,str(O.parent/'kulova_cp261_v7_2026-09-26'))
import architecture as A
rows=json.loads((O/'evidence/openings.json').read_text());W,H,N=13.746,7.1,2048
source=O.parent/'kulova_cp261_bevel_lab_2026-09-26/models/cp261_bevel_c.blend'
def digest(o):
 m=o.data
 return hashlib.sha256(json.dumps({'v':[list(v.co) for v in m.vertices],'p':[list(p.vertices) for p in m.polygons],'uv':[[list(l.uv) for l in u.data] for u in m.uv_layers]},sort_keys=True).encode()).hexdigest()
def save(key):
 bpy.ops.wm.save_as_mainfile(filepath=str(O/'models'/('cp261_openings_'+key+'.blend')))
 bpy.ops.export_scene.gltf(filepath=str(O/'models'/('cp261_openings_'+key+'.glb')),export_format='GLB',export_extras=True)
report={}
for key in ['geometry','inpaint']:
 bpy.ops.wm.open_mainfile(filepath=str(source),load_ui=False)
 before={o.name:digest(o) for o in bpy.context.scene.objects if o.type=='MESH'}
 if key=='geometry':
  new=[]
  for row in rows:
   o=row['old'].copy();l,t,r,b=row['target_px']
   if row['change']:o.update(cx=(l+r)/2/N*W,width=(r-l)/N*W,top=(1-t/N)*H)
   new.append(o)
  # Rebuild front voids and reveals; retain the existing footprint and other materials.
  name='CP_261_Masonry_With_Openings';ob=bpy.data.objects[name];parent=ob.parent;front=bpy.data.materials['SOURCE_FRONT_PROTECTED'];plaster=bpy.data.materials['GENERATED_PLASTER']
  bpy.data.objects.remove(ob,do_unlink=True)
  mesh=A.Mesh(name,parent,[front,plaster]);A.facade(mesh,W,H,new)
  fp=[(0,0),(W,0),(13.574,13.8),(0,13.8)]
  for a,b in zip(fp[1:],fp[2:]+fp[:1]):mesh.face([(a[0],a[1],0),(b[0],b[1],0),(b[0],b[1],H),(a[0],a[1],H)],1)
  mesh.face([(x,y,0) for x,y in fp[::-1]],1);wall=mesh.done()
  for p in wall.data.polygons:
   uv=wall.data.uv_layers.active;normal=p.normal
   if normal.y<-.8 and max(wall.data.vertices[i].co.y for i in p.vertices)<.01:
    p.material_index=0
    for li in p.loop_indices:
     q=wall.data.vertices[wall.data.loops[li].vertex_index].co;uv.data[li].uv=(q.x/W,q.z/H)
   else:
    p.material_index=1;v=Vector((0,0,1))-normal*normal.z
    if v.length<.01:v=Vector((0,1,0))-normal*normal.y
    v.normalize();u=v.cross(normal).normalized()
    for li in p.loop_indices:
     q=wall.data.vertices[wall.data.loops[li].vertex_index].co;uv.data[li].uv=(q.dot(u)/3.44086,q.dot(v)/3.44086)
  for name in ['CP_261_Frames_Sills_And_Cornices','CP_261_Timber_Frames','CP_261_Individual_Photographic_Panes','CP_261_Glazing_And_Doors']:
   ob=bpy.data.objects[name];me=ob.data
   for vertex in me.vertices:
    q=vertex.co
    for row,nw in zip(rows,new):
     old=row['old']
     if not row['change']:continue
     if old['bottom']-.18-1e-5<=q.z<=old['top']+.10 and abs(q.x-old['cx'])<=old['width']/2+.17:
      q.x=nw['cx']+(q.x-old['cx'])*nw['width']/old['width']
      if q.z>=old['bottom']:q.z=old['bottom']+(q.z-old['bottom'])*(nw['top']-old['bottom'])/(old['top']-old['bottom'])
      break
   me.update()
   # Front projection remains registered in world facade coordinates, not stretched with the trim.
   if 'Frames_Sills' in name:
    for p in me.polygons:
     if me.materials[p.material_index].name=='SOURCE_FRONT_PROTECTED':
      for li in p.loop_indices:
       q=me.vertices[me.loops[li].vertex_index].co;me.uv_layers.active.data[li].uv=(q.x/W,q.z/H)
 else:
  im=bpy.data.images.get('registered_facade.png');assert im
  im.unpack(method='REMOVE');im.filepath=str(O/'textures/facade_inpaint.png');im.reload();im.pack()
 changed=[o.name for o in bpy.context.scene.objects if o.type=='MESH' and digest(o)!=before[o.name]]
 if key=='inpaint':assert not changed,changed
 report[key]={'changed_objects':changed,'unchanged_objects':len(before)-len(changed),'visual_passed':False}
 save(key)
(O/'evidence/build_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('DONE',report)
