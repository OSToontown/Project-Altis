from panda3d.core import ModelNode
from toontown.dna import DNAAnimProp

class DNAInteractiveProp(DNAAnimProp.DNAAnimProp):
    __slots__ = (
        'cellId')

    COMPONENT_CODE = 15

    def __init__(self, name):
        DNAAnimProp.DNAAnimProp.__init__(self, name)
        self.cellId = -1

    def setCellId(self, id):
        self.cellId = id

    def getCellId(self):
        return cellId

    def makeFromDGI(self, dgi):
        DNAAnimProp.DNAAnimProp.makeFromDGI(self, dgi)
        self.cellId = dgi.getInt16()

    def traverse(self, nodePath, dnaStorage):
        node = None
        if self.getCode() == 'DCS':
            node = ModelNode(self.getName())
            node.setPreserveTransform(ModelNode.PTNet)
            node = nodePath.attachNewNode(node, 0)
        else:
            node = dnaStorage.findNode(self.getCode())
            node = node.copyTo(nodePath, 0)
            node.setName(self.getName())
        
        node.setTag('DNAAnim', self.getAnim())
        node.setTag('DNACellIndex', str(self.cellId))
        node.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())
        node.setColorScale(self.getColor(), 0)
        node.flattenStrong()
        for child in self.children:
            child.traverse(node, dnaStorage)
            
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNAAnimProp.DNAAnimProp.packerTraverse(
            self, recursive=False, verbose=verbose)
        packer.name = 'DNAInteractiveProp'  # Override the name for debugging.

        packer.pack('cell ID', self.cellId, INT16)

        if recursive:
            packer += self.packerTraverseChildren(verbose=verbose)
        return packer
