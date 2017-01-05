from panda3d.core import LVector4f, ModelNode
import DNANode
import DNAUtil

class DNAProp(DNANode.DNANode):
    COMPONENT_CODE = 4
    __slots__ = ('code', 'color')

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1)
        
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