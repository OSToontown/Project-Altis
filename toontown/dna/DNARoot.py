from toontown.dna.DNAGroup import DNAGroup
from toontown.dna.parser import *
from toontown.dna.tokens import *
from toontown.dna.ply import yacc

class DNARoot(DNAGroup):
    __slots__ = (
        'dnaStores')

    def __init__(self, name='root', dnaStore=None):
        DNAGroup.__init__(self, name)

        self.dnaStore = dnaStore

    def read(self, stream):
        parser = yacc.yacc(debug=0, optimize=0)
        parser.dnaStore = self.dnaStore
        parser.root = self
        parser.parentGroup = self
        parser.modelName = None
        parser.modelType = None
        parser.parse(stream.read())