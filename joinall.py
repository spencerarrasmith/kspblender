import bpy


def main(ship):
    scn = bpy.context.scene
    mergelist = []

    for obj in scn.objects:
        print(obj.name)
        if obj.type == 'MESH' and "KSP" not in obj.name:
            if obj['ship'] == ship and not obj.hide:
                mergelist.append(obj)
        else:
            print("Skipped ", obj.name)

    while len(mergelist) > 1:
        bpy.ops.object.select_all(action='DESELECT')
        merge1 = mergelist.pop()
        merge2 = mergelist.pop()
        scn.objects.active = merge1
        merge1.select = True
        bpy.ops.object.modifier_add(type='BOOLEAN')
        merge1.modifiers[0].operation = 'UNION'
        merge1.modifiers[0].object = merge2
        modname = merge1.modifiers[0].name
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modname)
        mergelist.append(bpy.context.active_object)

    result = bpy.context.active_object
    result.select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.remove_doubles(threshold=0.001)
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.parent_clear(type='CLEAR')
    result.name = "RESULT"
    result.scale = (10, 10, 10)


def alt(ship):
    scn = bpy.context.scene
    mergelist = []

    for obj in scn.objects:
        print(obj.name)
        if obj.type == 'MESH' and "KSP" not in obj.name:
            if obj['ship'] == ship and not obj.hide:
                mergelist.append(obj)
        else:
            print("Skipped ", obj.name)

    bpy.ops.object.select_all(action='DESELECT')
    for obj in mergelist:
        obj.select = True

    bpy.ops.object.join()
    bpy.ops.object.parent_clear(type='CLEAR')
    result.name = "RESULT"
    result.scale = (10, 10, 10)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.remove_doubles(threshold=0.001)
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode='OBJECT')


alt('Kerbal 2X')
