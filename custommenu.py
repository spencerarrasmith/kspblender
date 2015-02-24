import bpy, time, ksparser

class SelectShipOperator(bpy.types.Operator):
    bl_idname = "object.select_ship"
    bl_label = "Select Ship"
    
    def execute(self,context):
        scn = bpy.context.scene
        selected = bpy.context.selected_objects
        shippart = selected.pop(0)
        bpy.ops.object.select_all(action = 'DESELECT')
        shippart.select = True
        
        for obj in bpy.data.objects:
            if not obj.parent:
                if obj["ship"] == shippart["ship"]:
                    obj.select = True
                    
        return {'FINISHED'}
        

class DeletePartOperator(bpy.types.Operator):
    bl_idname = "object.delete_part"
    bl_label = "Delete Part"

    def execute(self,context):
        scn = bpy.context.scene
        kill = bpy.context.selected_objects

        for obj in kill:
            if obj.parent == None:
                queue = [obj]

                while queue:
                    current = queue.pop(0)
                    current.hide_select = False
                    current.hide = False
                    current.select = True
                    scn.objects.active = current
                    for child in current.children:
                        queue.append(child)
                        
                bpy.ops.object.delete(use_global = False)
        return {'FINISHED'}
    
class ToggleDeployOperator(bpy.types.Operator):
    bl_idname = "object.toggle_deploy"
    bl_label = "Toggle Deploy"

    def execute(self,context):
        scn = bpy.context.scene
        toggle = bpy.context.selected_objects
        selection = toggle
        
        while toggle:
            curobj = toggle.pop(0)
            for child in curobj.children:
                toggle.append(child)
                
            scn.objects.active = curobj
            curobj.select = True
            if curobj.animation_data:
                for track in curobj.animation_data.nla_tracks:
                    for strip in track.strips:
                        strip.use_reverse = not(strip.use_reverse)
                        
            curobj.select = False
        bpy.ops.object.select_all(action = 'DESELECT')
        bpy.context.scene.frame_current=1
        bpy.context.scene.frame_current=0
        for object in selection:
            object.select = True
        return {'FINISHED'}
    
class ToggleEditableOperator(bpy.types.Operator):
    bl_idname = "object.toggle_editable"
    bl_label = "Toggle Editable"

    def execute(self,context):
        scn = bpy.context.scene
        editable = bpy.context.selected_objects
        
        while editable:
            curobj = editable.pop(0)
            for child in curobj.children:
                editable.append(child)
                
            if curobj.type == "MESH" and curobj.hide == False:
                scn.objects.active = curobj
                curobj.select = True
                curobj.hide_select = not(curobj.hide_select)
                
        return {'FINISHED'}

class ImportCraftOperator(bpy.types.Operator):
    bl_idname = "object.import_craft"
    bl_label = "Import Craft"
   
    def execute(self,context):
        ksparser.main("Kerbal 2.craft")
        return {'FINISHED'}

#class LoadFlagPartOperator(bpy.types.Operator):
#    bl_idname = "object.load_flag"
#    bl_label = "Load Flag"
    
    #filename = StringProperty(name="Flag Image", subtype="FILE_PATH")
    
    
#    def execute(self,context):
#        loadflag.main()
#        return {'FINISHED'}
    
# EnableEditingOperator
# DisableEditingOperator
# ChangeSymmetryOperator
# SelectShipOperator
# JoinAllMeshesOperator
# SetMaterialAllOperator


bpy.utils.register_class(SelectShipOperator)
bpy.utils.register_class(DeletePartOperator)
bpy.utils.register_class(ToggleDeployOperator)
bpy.utils.register_class(ToggleEditableOperator)
#bpy.utils.register_class(ImportCraftOperator)
#bpy.utils.register_class(LoadFlagOperator)

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
        layout.operator("object.select_ship", text="Select Ship")
        layout.operator("object.delete_part", text="Delete Part")
        layout.operator("object.toggle_deploy", text="Toggle Deploy")
        layout.operator("object.toggle_editable", text="Toggle Editable")
        #layout.operator("object.import_craft", text="Import Craft")
        
        
bpy.utils.register_class(CustomMenu)

km = bpy.context.window_manager.keyconfigs.default.keymaps['3D View']

#for kmi in km.keymap_items:
    #if kmi.idname == "wm.call_menu" and kmi.properties.name == "OBJECT_MT_CustomMenu":
        #km.keymap_items.remove(kmi)
        #print("lol it found something that doesn't even exist yet")

kmi = km.keymap_items.new('wm.call_menu', 'K', 'PRESS')
kmi.properties.name = "OBJECT_MT_CustomMenu"