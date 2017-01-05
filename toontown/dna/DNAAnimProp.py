import DNAProp
from DNAUtil import *
from panda3d.core import ModelNode

class DNAAnimProp(DNAProp.DNAProp):
    COMPONENT_CODE = 14

    def __init__(self, name):
        DNAProp.DNAProp.__init__(self, name)
        self.animName = ''
        
    def getAnimName(self):
        return self.animName

    def makeFromDGI(self, dgi, store):
        DNAProp.DNAProp.makeFromDGI(self, dgi, store)
        self.animName = dgiExtractString8(dgi)

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
        node.setPosHprScale(self.pos, self.hpr, self.scale)
        node.setColorScale(self.color)
        self.traverseChildren(node, dnaStorage)