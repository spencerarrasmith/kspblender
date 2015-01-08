import bpy

scn = bpy.context.scene
kill = bpy.context.selected_objects

for obj in kill:
    if obj.parent == None:
        scn.objects.active = obj
        queue = [obj]

        while queue:
            current = queue.pop(0)
            current.select = True
            if not current.is_visible(scn):
                scn.objects.active = current
                current.hide = False
                current.select = True
            for child in current.children:
                queue.append(child)
                
        #bpy.ops.object.delete(use_global = False)