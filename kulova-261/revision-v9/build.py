from pathlib import Path
import bpy,bmesh,sys,math,json,hashlib
from mathutils import Vector
O=Path(__file__).resolve().parent;sys.path.insert(0,str(O));import architecture as A
bpy.ops.wm.open_mainfile(filepath=str(O.parent/'kulova_cp261_v8_2026-09-26/models/cp261_v8.blend'),load_ui=False)
root=bpy.data.objects['CP_261'];plaster=bpy.data.materials['GENERATED_PLASTER'];stone=bpy.data.materials['GENERATED_REVEAL'];dark=bpy.data.materials['DARK_UNOBSERVED_INTERIOR']
for name in ['CP_261_Roof_Dormers','CP_261_Entrance_Three_Steps_PROVISIONAL']:
 bpy.data.objects.remove(bpy.data.objects[name],do_unlink=True)
x=13.746*.53;y=.42;h=7.1;k=4.4/6.9;z0=h+k*.45;width=1.35
outer=A.outline(A.opening(x,width,h+k*y-.045,z0+2.02,.40))
inner=A.outline(A.opening(x,width*.67,z0+.08,z0+1.75,.40))
dorm=A.Mesh('CP_261_Roof_Dormers',root,[plaster,dark]);fall=.12
# Each boundary vertex ends at the actual roof intersection, slightly buried.
front=[(xx,y,zz) for xx,zz in outer]
rear=[]
for xx,zz in outer:
 yy=(zz+fall*y-h+.06)/(k+fall)
 rear.append((xx,yy,zz-fall*(yy-y)))
for i in range(len(outer)):
 j=(i+1)%len(outer)
 dorm.face([front[i],front[j],rear[j],rear[i]])
 dorm.face([front[i],(inner[i][0],y,inner[i][1]),(inner[j][0],y,inner[j][1]),front[j]])
 dorm.face([(inner[i][0],y,inner[i][1]),(inner[i][0],.615,inner[i][1]),(inner[j][0],.615,inner[j][1]),(inner[j][0],y,inner[j][1])])
dorm.face(rear[::-1]);dorm.face([(xx,.615,zz) for xx,zz in inner],1)
ob=dorm.done(roof_intersection=True,rear_cap=True,front_closed=True,hidden_geometry='provisional roof junction; no new archive evidence')
# One watertight stair profile. Bottom below z=0 avoids coincident house base.
step=A.Mesh('CP_261_Entrance_Three_Steps_PROVISIONAL',root,[stone]);cx=13.746*.09
profile=[(-1.02,-.045),(.33,-.045),(.33,.48),(-.46,.48),(-.46,.32),(-.74,.32),(-.74,.16),(-1.02,.16)]
left=[(cx-.66,yy,zz) for yy,zz in profile];right=[(cx+.66,yy,zz) for yy,zz in profile]
step.face(left[::-1]);step.face(right)
for i in range(len(profile)):
 j=(i+1)%len(profile);step.face([left[i],left[j],right[j],right[i]])
so=step.done(step_count=3,riser_m=.16,tread_m=.28,base_z_m=-.045,status='provisional',locked=False)
checks={}
for o in [ob,so]:
 me=o.data;uv=me.uv_layers.active
 for p in me.polygons:
  normal=p.normal.normalized();v=Vector((0,0,1))-normal*normal.z
  if v.length<.01:v=Vector((0,1,0))-normal*normal.y
  v.normalize();u=v.cross(normal).normalized()
  if u.x<-.01:u=-u
  span=3.44086 if o==ob else 2.47742
  for li in p.loop_indices:
   q=me.vertices[me.loops[li].vertex_index].co;uv.data[li].uv=(q.dot(u)/span,q.dot(v)/span)
 bm=bmesh.new();bm.from_mesh(me)
 checks[o.name]={'boundary_edges':sum(e.is_boundary for e in bm.edges),'non_manifold_edges':sum(not e.is_manifold for e in bm.edges),'volume':bm.calc_volume(signed=False)}
 assert checks[o.name]['non_manifold_edges']==0,checks[o.name]
 bm.free()
 me.calc_loop_triangles();bad=0
 for t in me.loop_triangles:
  a,b,c=[uv.data[i].uv for i in t.loops]
  if t.area>1e-10 and abs((b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x))<1e-14:bad+=1
 assert bad==0,(o.name,bad)
 checks[o.name]['degenerate_uv_triangles']=bad
for im in bpy.data.images:
 if im.users and im.source=='FILE':assert im.packed_file,im.name
bpy.ops.wm.save_as_mainfile(filepath=str(O/'models/cp261_v9.blend'))
bpy.ops.export_scene.gltf(filepath=str(O/'models/cp261_v9.glb'),export_format='GLB',export_extras=True)
(O/'evidence/geometry_checks.json').write_text(json.dumps({'objects':checks,'rear_termination':'roof intersection minus 0.06m','stair_bottom':-.045,'unchanged':'all source textures, front openings, gutters, roof and v8 colour correction','historical_status':'model_hypothesis','visual_passed':False},indent=2))
print('BUILD_V9_OK',checks,flush=True)
