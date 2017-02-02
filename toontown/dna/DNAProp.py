from panda3d.core import LVector4f, ModelNode
from toontown.dna import DNANode
from toontown.dna import DNAUtil

class DNAProp(DNANode.DNANode):
    __slots__ = (
        'code', 'color')
    
    COMPONENT_CODE = 4

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1)

    def __del__(self):
        DNANode.DNANode.__del__(self)
        del self.code
        del self.color
        
    def getCode(self):
        return self.code
        
    def setCode(self, code):
        self.code = code
        
    def getColor(self):
        return self.color

    def makeFromDGI(self, dgi, store):
        DNANode.DNANode.makeFromDGI(self, dgi, store)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.color = DNAUtil.dgiExtractColor(dgi)
        
    def smartFlatten(self, node):
        if 'trolley' in self.name:
            return
        elif self.children:
            node.flattenMedium()
        elif 'HQTelescopeAnimatedProp' in self.name:
            node.flattenMedium()
        elif node.find('**/water1*').isEmpty():
            node.flattenStrong()
        elif not node.find('**/water').isEmpty():
            print 'Found some water!'
            water = node.find('**/water')
            water.setTransparency(1)
            water.setColor(1, 1, 1, 0.8)
            node.flattenStrong()
        elif not node.find('**/water1*').isEmpty():
            water = node.find('**/water1*')
            water.setTransparency(1)
            water.setColorScale(1.0, 1.0, 1.0, 1.0)
            water.setBin('water', 51, 1)
            node.flattenStrong()

    def traverse(self, nodePath, dnaStorage):
        if self.code == 'DCS':
            node = ModelNode(self.name)
            node.setPreserveTransform(ModelNode.PTNet)
            node = nodePath.attachNewNode(node)
        else:
            node = dnaStorage.findNode(self.code)
            if node.isEmpty():
                return
            
            node = node.copyTo(nodePath)
        
        node.setPosHprScale(self.pos, self.hpr, self.scale)
        node.setName(self.name)
        node.setColorScale(self.color)
        self.smartFlatten(node)
        self.traverseChildren(node, dnaStorage)