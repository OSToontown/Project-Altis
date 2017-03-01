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
        
    def setColor(self, color):
        self.color = LVector4f(int(color))

    def makeFromDGI(self, dgi, store):
        DNANode.DNANode.makeFromDGI(self, dgi, store)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.color = DNAUtil.dgiExtractColor(dgi)
        
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
        self.traverseChildren(node, dnaStorage)