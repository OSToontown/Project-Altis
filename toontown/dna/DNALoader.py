from toontown.dna import DNASuitPoint
from toontown.dna import DNAError
from toontown.dna import DNAGroup
from toontown.dna import DNAVisGroup
from toontown.dna import DNANode
from toontown.dna import DNAProp
from toontown.dna import DNASign
from toontown.dna import DNASignBaseline
from toontown.dna import DNASignText
from toontown.dna import DNASignGraphic
from toontown.dna import DNAFlatBuilding
from toontown.dna import DNAWall
from toontown.dna import DNAWindows
from toontown.dna import DNACornice
from toontown.dna import DNALandmarkBuilding
from toontown.dna import DNAAnimProp
from toontown.dna import DNAInteractiveProp
from toontown.dna import DNAAnimBuilding
from toontown.dna import DNADoor
from toontown.dna import DNAFlatDoor
from toontown.dna import DNAStreet

import zlib
from panda3d.core import *
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from direct.distributed.PyDatagram import PyDatagram

COMPCODE_RETURN = 255

compClassTable = {
    1: DNAGroup.DNAGroup,
    2: DNAVisGroup.DNAVisGroup,
    3: DNANode.DNANode,
    4: DNAProp.DNAProp,
    5: DNASign.DNASign,
    6: DNASignBaseline.DNASignBaseline,
    7: DNASignText.DNASignText,
    8: DNASignGraphic.DNASignGraphic,
    9: DNAFlatBuilding.DNAFlatBuilding,
    10: DNAWall.DNAWall,
    11: DNAWindows.DNAWindows,
    12: DNACornice.DNACornice,
    13: DNALandmarkBuilding.DNALandmarkBuilding,
    14: DNAAnimProp.DNAAnimProp,
    15: DNAInteractiveProp.DNAInteractiveProp,
    16: DNAAnimBuilding.DNAAnimBuilding,
    17: DNADoor.DNADoor,
    18: DNAFlatDoor.DNAFlatDoor,
    19: DNAStreet.DNAStreet
}

childlessComps = (
    11, # DNAWindows
    12, # DNACornice
    17, # DNADoor
    18, # DNAFlatDoor
    19 # DNAStreet
)

class DNALoader(object):
    __slots__ = (
        'curComp', 'curStore')

    def __init__(self):
        self.curComp = None
        self.curStore = None

    def loadDNAFile(self, store, _file):
        #if base.wantHighPerformance:
        #    _file = _file [:-5] + "_m.pdna"
        self.loadDNAFileBase(store, _file)

        if not self.curComp:
            print "DNA has no component, returning empty nodepath"
            return NodePath()

        np = NodePath("dna")
        self.curComp.traverse(np, self.curStore)

        self.curStore = None
        self.curComp = None

        return np

    def loadDNAFileAI(self, store, _file):
        self.loadDNAFileBase(store, _file)
        self.curStore = None
        return self.curComp

    def handleStorageData(self, dgi):
        # Catalog codes
        num_roots = dgi.getUint16()
        for i in range(num_roots):
            root = dgi.getString()
            num_codes = dgi.getUint8()
            for x in range(num_codes):
                self.curStore.storeCatalogCode(root, dgi.getString())

        # Textures
        num_textures = dgi.getUint16()
        for i in range(num_textures):
            code = dgi.getString()
            filename = dgi.getString()
            self.curStore.storeTexture(code, loader.loadTexture(filename))

        # Fonts
        num_fonts = dgi.getUint16()
        for i in range(num_fonts):
            code = dgi.getString()
            filename = dgi.getString()
            self.curStore.storeFont(code, loader.loadFont(filename), filename)

        # Nodes
        num_nodes = dgi.getUint16()
        for i in range(num_nodes):
            code = dgi.getString()
            filename = dgi.getString()
            search = dgi.getString()
            self.curStore.storeNode(filename, search, code)

        num_nodes = dgi.getUint16()
        for i in range(num_nodes):
            code = dgi.getString()
            filename = dgi.getString()
            search = dgi.getString()
            self.curStore.storeHoodNode(filename, search, code)

        num_nodes = dgi.getUint16()
        for i in range(num_nodes):
            code = dgi.getString()
            filename = dgi.getString()
            search = dgi.getString()
            self.curStore.storePlaceNode(filename, search, code)

        # Blocks
        num_blocks = dgi.getUint16()
        for i in range(num_blocks):
            number = dgi.getUint8()
            zone = dgi.getUint16()
            title = dgi.getString()
            article = dgi.getString()
            bldg_type = dgi.getString()
            self.curStore.storeBlock(number, title, article, bldg_type, zone)

        # Suit Points
        num_points = dgi.getUint16()
        for i in range(num_points):
            index = dgi.getUint16()
            point_type = dgi.getUint8()
            x, y, z = (dgi.getInt32() / 100.0 for _ in range(3))
            pos = LPoint3f(x, y, z)
            landmark_building_index = dgi.getInt16()
            self.curStore.storeSuitPoint(DNASuitPoint.DNASuitPoint(index, point_type, pos, landmark_building_index))

        # Suit Edges
        num_edges = dgi.getUint16()
        for i in range(num_edges):
            index = dgi.getUint16()
            num_points = dgi.getUint16()
            for p in range(num_points):
                end_point = dgi.getUint16()
                zone_id = dgi.getUint16()
                self.curStore.storeSuitEdge(index, end_point, zone_id)

    def handleCompData(self, dgi):
        while dgi.getRemainingSize():
            comp_code = dgi.getUint8()

            if comp_code == COMPCODE_RETURN:
                self.verify(self.curComp != None)
                p = self.curComp.getParent()
                if p != None:
                    self.curComp = p
                else:
                    self.verify(self.curComp.name == "root")
            else:
                if comp_code == DNAVisGroup.DNAVisGroup.COMPONENT_CODE:
                    new_comp = DNAVisGroup.DNAVisGroup("unnamed_comp")
                    self.curStore.storeDNAVisGroup(new_comp)
                else:
                    if comp_code in compClassTable.keys():
                        new_comp = compClassTable[comp_code]("unnamed_comp")
                    else:
                        raise DNAError.DNAError("Invalid comp code %s" % comp_code)

                new_comp.makeFromDGI(dgi, self.curStore)

                if self.curComp:
                    new_comp.setParent(self.curComp)
                    self.curComp.add(new_comp)

                if comp_code not in childlessComps:
                    self.curComp = new_comp

    def loadDNAFileBase(self, store, _file):
        if type(_file) == str and _file.endswith(".dna"):
            _file = _file.replace(".dna", ".pdna")
            #_file = _file.replace("../resources/", "")
        if __debug__:
            _file = Filename("resources/" + _file)
        else:
            _file = Filename("/" + _file)

        vfs = VirtualFileSystem.getGlobalPtr()
        vfs.resolveFilename(_file, "")
        if not vfs.exists(_file):
            raise DNAError.DNAError("Unable to open DNA file '%s'" % (str(_file)))
        dnaData = vfs.readFile(_file, True)

        self.curStore = store
        dg = PyDatagram(dnaData)
        dgi = PyDatagramIterator(dg)
        header = dgi.extractBytes(5)
        if header != 'PDNA\n':
            raise DNAError.DNAError('Invalid header: %s' % (header))

        compressed = dgi.getBool()
        dgi.skipBytes(1)

        if compressed:
            data = dgi.getRemainingBytes()
            data = zlib.decompress(data)
            dg = PyDatagram(data)
            dgi = PyDatagramIterator(dg)

        self.curComp = None
        self.handleStorageData(dgi)
        self.handleCompData(dgi)

    def verify(self, condition):
        if not condition:
            raise DNAError.DNAError("Condition failed")

    def destroy(self):
        del self.curStore
        del self.curComp