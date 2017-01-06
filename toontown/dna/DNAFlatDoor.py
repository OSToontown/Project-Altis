from panda3d.core import NodePath, DecalEffect
from toontown.dna import DNADoor

class DNAFlatDoor(DNADoor.DNADoor):
    COMPONENT_CODE = 18

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        node = node.copyTo(nodePath)
        node.setScale(NodePath(), (1, 1, 1))
        node.setPosHpr((0.5, 0, 0), (0, 0, 0))
        node.setColor(self.color)
        
        if base.config.GetBool('want-dna-depth-offsets', False):
            node.setDepthOffset(0)
        else:
            node.getNode(0).setEffect(DecalEffect.make())