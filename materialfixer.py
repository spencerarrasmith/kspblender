import bpy

def main(obj,partpart):
    
    #kill preexisting at some point
    
    
    
    scn = bpy.context.scene
    scn.objects.active = obj
    mat = obj.data.materials[0]
    
    if "Material Output" in mat.node_tree.nodes:
        return
    
    mat.name = partpart+"_"+obj.name
    
    tx0 = mat.node_tree.nodes.new('ShaderNodeTexCoord')
    im0 = mat.node_tree.nodes.new('ShaderNodeTexImage')
    ma0 = mat.node_tree.nodes.new('ShaderNodeMath')
    gl0 = mat.node_tree.nodes.new('ShaderNodeBsdfGlossy')
    om0 = mat.node_tree.nodes.new('ShaderNodeOutputMaterial')
    
    location = [(550,250),(800,450),(1050,350),(1300,300),(1550,300)]
    
    tx0.location = location[0]
    mat.node_tree.links.new(tx0.outputs['UV'],im0.inputs['Vector'])
    
    
    im0.location = location[1]
    mat.node_tree.links.new(im0.outputs['Color'],gl0.inputs['Color'])
    mat.node_tree.links.new(im0.outputs['Color'],ma0.inputs[1])
    for node in mat.node_tree.nodes.keys():
        if "mainTex" in node:
            imA = mat.node_tree.nodes[node]
            im0.image = bpy.data.images[imA.texture.name]
            newname = partpart+"_"+obj.name+"_tex"
            print(bpy.data.images[imA.texture.name].name)
            bpy.data.images[imA.texture.name].name = newname
    
    
    ma0.location = location[2]
    mat.node_tree.links.new(ma0.outputs['Value'],gl0.inputs['Roughness'])
    ma0.operation = "DIVIDE"
    ma0.inputs[0].default_value = 1
    
    
    gl0.location = location[3]
    mat.node_tree.links.new(gl0.outputs['BSDF'],om0.inputs['Surface'])
    
    om0.location = location[4]
    
#main(bpy.context.active_object)