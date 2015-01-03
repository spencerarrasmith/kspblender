import bpy, time

class DeletePartOperator(bpy.types.Operator):
    bl_idname = "object.delete_part"
    bl_label = "Delete Part"
    
    def execute(self, context):
        scn = bpy.context.scene
        obj = bpy.context.active_object
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
                
        bpy.ops.object.delete(use_global = False)
        return {'FINISHED'}


bpy.utils.register_class(DeletePartOperator)

#obj = bpy.context.active_object
#bpy.ops.object.delete_part()

class CustomMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_CustomMenu"
    bl_label = "Custom Menu"
    
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.shade_smooth", text="Shade Smooth")
        layout.operator("object.shade_flat", text="Shade Flat")
        layout.separator()
        layout.operator_menu_enum("object.modifier_add", "type")
        layout.separator()
        layout.operator_menu_enum("object.constraint_add", "type")
        layout.separator()
        layout.menu("VIEW3D_MT_transform")
        layout.separator()
        layout.operator("object.delete_part", text="Delete Part")
        
        
bpy.utils.register_class(CustomMenu)

km = bpy.context.window_manager.keyconfigs.default.keymaps['3D View']

for kmi in km.keymap_items:
    if kmi.idname == "wm.call_menu" and kmi.properties.name == "OBJECT_MT_CustomMenu":
        #km.keymap_items.remove(kmi)
        print("lol it found something that doesn't even exist yet")

kmi = km.keymap_items.new('wm.call_menu', 'K', 'PRESS')
kmi.properties.name = "OBJECT_MT_CustomMenu"