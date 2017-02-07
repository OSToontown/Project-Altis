from panda3d.core import LVector4f, NodePath, DecalEffect, ModelNode
from toontown.dna import DNAProp
from toontown.dna import DNAUtil

class DNASign(DNAProp.DNAProp):
    COMPONENT_CODE = 5

    def __init__(self, name):
        DNAProp.DNAProp.__init__(self, name)

    def traverse(self, nodePath, dnaStorage):
        decalNode = nodePath.find("**/sign_decal")
        if decalNode.isEmpty():
            decalNode = nodePath.find("**/*_front")
        
        if decalNode.isEmpty() or decalNode.getNode(0).isGeomNode():
            decalNode = nodePath.find("**/+GeomNode")
        
        if self.code:
            np = dnaStorage.findNode(self.code).copyTo(decalNode)
            np.setName("sign")
        else:
            np = decalNode.attachNewNode(ModelNode("sign"))
        
        np.setDepthOffset(50)
        origin = nodePath.find("**/*sign_origin")
        np.setPosHprScale(origin, self.pos, self.hpr, self.scale)
        np.setColor(self.color)
        np.wrtReparentTo(origin, 0)
        self.traverseChildren(np, dnaStorage)
        np.flattenStrong()