from panda3d.core import LVector4f
from toontown.dna import DNANode
from toontown.dna import DNAUtil
from toontown.dna import DNAError

class DNALandmarkBuilding(DNANode.DNANode):
    __slots__ = (
        'code', 'wallColor')
    
    COMPONENT_CODE = 13

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.wallColor = LVector4f(1)

    def __del__(self):
        DNANode.DNANode.__del__(self)
        del self.code
        del self.wallColor
        
    def setCode(self, code):
        self.code = str(code)
        
    def getCode(self):
        return self.code
        
    def setWallColor(self, color):
        self.wallColor = LVector4f(int(color))
        
    def getWallColor(self):
        return self.wallColor

    def setupSuitBuildingOrigin(self, nodePathA, nodePathB):
        if (self.name[:2] == 'tb') and (self.name[2].isdigit()) and (self.name.find(':') != -1):
            name = self.name
            name = 's' + name[1:]
            node = nodePathB.find('**/*suit_building_origin')
            if node.isEmpty():
                print 'DNALandmarkBuilding ' + name + ' did not find **/*suit_building_origin'
                node = nodePathA.attachNewNode(name)
                node.setPosHprScale(self.pos, self.hpr, self.scale)
            else:
                node.wrtReparentTo(nodePathA)
                node.setName(name)

    def makeFromDGI(self, dgi, store):
        DNANode.DNANode.makeFromDGI(self, dgi, store)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.wallColor = DNAUtil.dgiExtractColor(dgi)

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNALandmarkBuilding code ' + self.code + ' not found in DNAStorage')
        
        npA = nodePath
        nodePath = node.copyTo(nodePath)
        nodePath.setName(self.name)
        nodePath.setPosHprScale(self.pos, self.hpr, self.scale)
        if dnaStorage.allowSuitOrigin(nodePath):
            self.setupSuitBuildingOrigin(npA, nodePath)
        
        self.traverseChildren(nodePath, dnaStorage)
        if "gag_shop" not in self.name:
            nodePath.flattenStrong()
            
        if 'toon_landmark_DG_pet_shop' in self.name: #The DG Petshop is only here to hide the doodle holes.
            petshop = nodePath
            doodlehole1 = petshop.find('**/*doodle1')
            doodlehole2 = petshop.find('**/*doodle2')
            
            if not doodlehole1.isEmpty() and not base.config('want-dg-petshop-doodle-holes', False):
                doodlehole1.hide()
            if not doodlehole2.isEmpty() and not base.config('want-dg-petshop-doodle-holes', False):
                doodlehole2.hide()

        elif 'toon_landmark_TT_library' in self.name:
            library = nodePath
            
            shadow = library.find('**/square_drop_shadow')
            if not shadow.isEmpty():
                shadow.setDepthOffset(2)
