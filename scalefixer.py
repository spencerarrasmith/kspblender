import bpy

def main(craft,cursor_loc,scale):
    scn = bpy.context.scene
    for part in craft.partslist:
        obj = bpy.data.objects[part.part]
        scn.context.active = obj
        obj_loc = obj.location - cursor_loc
        obj_sca = obj.scale
        obj.location = (scale*obj_loc[0],scale*obj_loc[1],scale*obj_loc[2])
        obj.scale = (scale*obj_sca[0],scale*obj_sca[1],scale*obj_sca[2])
        
    bpy.ops.transform.resize()