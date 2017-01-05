from panda3d.core import NodePath, DecalEffect
import DNADoor

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
            '''
            The reason we set the parent to decal is because the actual door 
            will flicker without this. Why this is actually needed is unknown 
            but it works.
            '''
            node.getParent().node().setEffect(DecalEffect.make())
            node.node().setEffect(DecalEffect.make())