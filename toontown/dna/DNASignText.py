<<<<<<< HEAD
from toontown.dna import DNANode
=======
import DNANode
from DNAUtil import *
>>>>>>> origin/master

class DNASignText(DNANode.DNANode):
    __slots__ = (
        'letters')

    COMPONENT_CODE = 7

    def __init__(self):
        DNANode.DNANode.__init__(self, '')
        self.letters = ''

    def setLetters(self, letters):
        self.letters = letters
        
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNANode.DNANode.packerTraverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNASignText'  # Override the name for debugging.
        packer.pack('letters', self.letters, STRING)
        return packer