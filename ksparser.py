import os, string
import bpy, mathutils, math
os.chdir("C:\\Users\\Spencer.Satan-PC\\Art\\Projects\\ksp\\kspblender")

def zup_tuple(line):
    zup = [float(i) for i in line.split(" ")[-1].split(",")]
    zup[1], zup[2] = zup[2], zup[1]
    return tuple(zup)

def zup_quat(line):
    zup = [float(i) for i in line.split(" ")[-1].split(",")]
    zup = mathutils.Quaternion([zup[3], zup[0], zup[2], zup[1]])
    return (mathutils.Quaternion.to_euler(zup).x, mathutils.Quaternion.to_euler(zup).y, mathutils.Quaternion.to_euler(zup).z)

class kspcraft:
    """A Kerbal Space Program craft lol"""
    def __init__(self,filename):
        self.filename = filename
        self.lines = None
        self.ship = None
        self.version = None
        self.description = None
        self.type = None
        self.size = None
        self.partslist = []

        self.parse_file()
        self.set_data(self.lines[0:5])
        self.set_partslist(self.lines)

    def num_parts(self):
        try:
            return len(self.partslist)
        except TypeError:
            return 0
    
    def parse_file(self):
        fileobj = open(self.filename)
        text = fileobj.read()
        fileobj.close()
        self.lines = text.splitlines()

    def set_data(self,lines):
        self.ship = " ".join(lines[0].split(" ")[2:])
        self.version = lines[1].split(" ")[2]
        self.description = " ".join(lines[2].split(" ")[2:])
        self.type = lines[3].split(" ")[2]
        self.size = zup_tuple(lines[4])

    def set_partslist(self,lines):
        startindices = []
        endindices = []
        for i in range(len(self.lines)):
            if self.lines[i]=="{":
                startindices.append(i)
            if self.lines[i]=="\tEVENTS":
                endindices.append(i)

        for i in range(len(startindices)):
            self.partslist.append(part(self.lines[startindices[i]:endindices[i]]))



class part:
    """A part for a ship lol"""
    def __init__(self,lines):
        self.lines = lines
        self.part = None
        self.partNumber = None
        self.partName = None
        self.pos = None
        self.attPos = None
        self.attPos0 = None
        self.rot = None
        self.attRot = None
        self.attRot0 = None
        self.mir = None
        self.symMethod = None
        self.istg = None
        self.dstg = None
        self.sidx = None
        self.sqor = None
        self.attm = None
        self.modCost = None
        self.modMass = None
        self.modSize = None
        self.linklist = []
        self.attNlist = []
        self.symlist = []
        self.srfNlist = []

        self.set_data(self.lines)

    def set_data(self,lines):
        for line in lines:
            if line.split()[0] == "part":
                self.part = line.split(" ")[2]
                self.partNumber = int(line.split("_")[1])
                self.partName = "".join(line.split("_")[0:-1]).split()[-1]
            #if line.split()[0] == "partName":
                #self.partName = " ".join(line.split()[2:])
            if line.split()[0] == "pos":
                self.pos = zup_tuple(line)
            if line.split()[0] == "attPos":
                self.attPos = zup_tuple(line)
            if line.split()[0] == "attPos0":
                self.attPos0 = zup_tuple(line)
            if line.split()[0] == "rot":
                self.rot = zup_quat(line)
            if line.split()[0] == "attRot":
                self.attRot = zup_quat(line)
            if line.split()[0] == "attRot0":
                self.attRot0 = zup_quat(line)
            if line.split()[0] == "mir":
                self.mir = zup_tuple(line)
            if line.split()[0] == "symMethod":
                self.symMethod = line.split(" ")[2]
            if line.split()[0] == "istg":
                self.istg = int(line.split()[2])
            if line.split()[0] == "dstg":
                self.dstg = int(line.split()[2])
            if line.split()[0] == "sidx":
                self.sidx = int(line.split()[2])
            if line.split()[0] == "sqor":
                self.sqor = int(line.split()[2])
            if line.split()[0] == "attm":
                self.attm = int(line.split()[2])
            if line.split()[0] == "modCost":
                self.modCost = float(line.split()[2])
            if line.split()[0] == "modMass":
                self.modMass = float(line.split()[2])
            if line.split()[0] == "modSize":
                self.modSize = tuple([float(" ".join(line.split()[2:]).split(", ")[0][1:]), float(" ".join(line.split()[2:]).split(", ")[2][0:-1]), float(" ".join(line.split()[2:]).split(", ")[1])])
            if line.split()[0] == "link":
                self.linklist.append(link(line))
            if line.split()[0] == "attN":
                self.attNlist.append(attN(line))
            if line.split()[0] == "sym":
                self.symlist.append(sym(line))
            if line.split()[0] == "srfN":
                self.srfNlist.append(srfN(line))


class link:
    """A link for a part for a ship lol"""
    def __init__(self,line):
        self.line = line
        self.part = None
        self.partNumber = None

        self.set_data(self.line)

    def set_data(self,line):
        self.part = line.split(" ")[2]
        self.partNumber = int(line.split("_")[1])


class attN:
    """An attN for a part for a ship lol"""
    def __init__(self,line):
        self.line = line
        self.loc = None
        self.part = None
        self.partNumber = None

        self.set_data(self.line)

    def set_data(self,line):
        self.loc = line.split(" ")[2].split(",")[0]
        self.part = line.split(" ")[2].split(",")[1]
        self.partNumber = int(line.split("_")[1])


class sym:
    """An attN for a part for a ship lol"""
    def __init__(self,line):
        self.line = line
        self.part = None
        self.partNumber = None

        self.set_data(self.line)

    def set_data(self,line):
        self.part = line.split(" ")[2]
        self.partNumber = int(line.split("_")[1])
        

class srfN:
    """An attN for a part for a ship lol"""
    def __init__(self,line):
        self.line = line
        self.type = None
        self.part = None
        self.partNumber = None

        self.set_data(self.line)

    def set_data(self,line):
        self.type = line.split(" ")[2].split(",")[0]
        self.part = line.split(" ")[2].split(",")[1]
        self.partNumber = int(line.split("_")[1])



def addcubes_dumb(partslist):
    for part in partslist:
        bpy.ops.mesh.primitive_cube_add(radius = 1, location = part.pos, rotation = (mathutils.Quaternion.to_euler(part.rot).x, mathutils.Quaternion.to_euler(part.rot).y, mathutils.Quaternion.to_euler(part.rot).z))

def addcubes(partslist):
    for part in partslist:
        me = bpy.data.meshes.get('Cube')
        ob = bpy.data.objects.new(part.part, me)
        ob.location = part.pos
        ob.rotation_euler = part.rot
        
        scn = bpy.context.scene
        scn.objects.link(ob)
        scn.objects.active = ob
        ob.select = True
        
        tex = bpy.ops.object.text_add()
        tex = bpy.context.object
        tex.data.body = "".join(["    -",part.part])
        tex.scale = (.001,.001,.001)
        tex.rotation_euler = (math.pi/2,0,0)
        tex.location = part.pos
#        scn.objects.link(tex)
#        scn.objects.active = tex

def add_parts(partslist):
    for part in partslist:
        me = bpy.data.meshes.get(part.partName)
        ob = bpy.data.objects.new(part.part, me)
        ob.location = part.pos
        ob.rotation_euler = part.rot
        
        scn = bpy.context.scene
        scn.objects.link(ob)
        scn.objects.active = ob
        ob.select = True

def run():
    mycraft = kspcraft('Kerbal 2.craft')
    add_parts(mycraft.partslist)
    return mycraft

mycraft = run()
print([part.part for part in mycraft.partslist])