from panda3d.core import ModelNode
import DNAAnimProp

class DNAInteractiveProp(DNAAnimProp.DNAAnimProp):
    COMPONENT_CODE = 15

    def __init__(self, name):
        DNAAnimProp.DNAAnimProp.__init__(self, name)
        self.cellId = -1

    def makeFromDGI(self, dgi, store):
        DNAAnimProp.DNAAnimProp.makeFromDGI(self, dgi, store)
        self.cellId = dgi.getInt16()
        
    def getCellId(self):
        return self.cellId

    def traverse(self, nodePath, dnaStorage):
        node = None
        if self.code == 'DCS':
            node = ModelNode(self.name)
            node.setPreserveTransform(ModelNode.PTNet)
            node = nodePath.attachNewNode(node)
        else:
            node = dnaStorage.findNode(self.code)
            node = node.copyTo(nodePath)
            node.setName(self.name)
        node.setTag('DNAAnim', self.animName)
        node.setTag('DNACellIndex', str(self.cellId))
        node.setPosHprScale(self.pos, self.hpr, self.scale)
        node.setColorScale(self.color, 0)
        self.traverseChildren(node, dnaStorage)