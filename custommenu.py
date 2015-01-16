import bpy, time, groupdelete

class DeletePartOperator(bpy.types.Operator):
    bl_idname = "object.delete_part"
    bl_label = "Delete Part"

    def execute(self,context):
        groupdelete.main()
        return {'FINISHED'}

class LoadFlagPartOperator(bpy.types.Operator):
    bl_idname = "object.load_flag"
    bl_label = "Load Flag"
    
    filename = StringProperty(name="Flag Image", subtype="FILE_PATH"
    
    
    def execute(self,context):
        loadflag.main()
        return {'FINISHED'}
    
# EnableEditingOperator
# DisableEditingOperator
# ChangeSymmetryOperator
# SelectShipOperator
# JoinAllMeshesOperator
# SetMaterialAllOperator


bpy.utils.register_class(DeletePartOperator)
bpy.utils.register_class(LoadFlagOperator)

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
        layout.operator("object.load_flag", text="Load Flag")
        
        
bpy.utils.register_class(CustomMenu)

km = bpy.context.window_manager.keyconfigs.default.keymaps['3D View']

for kmi in km.keymap_items:
    if kmi.idname == "wm.call_menu" and kmi.properties.name == "OBJECT_MT_CustomMenu":
        km.keymap_items.remove(kmi)
        #print("lol it found something that doesn't even exist yet")

kmi = km.keymap_items.new('wm.call_menu', 'K', 'PRESS')
kmi.properties.name = "OBJECT_MT_CustomMenu"