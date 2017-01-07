from direct.stdpy import threading
from toontown.dna import DNALoader
from toontown.dna.DNAStorage import *
from toontown.dna.DNASuitPoint import *
from toontown.dna.DNAGroup import *
from toontown.dna.DNAVisGroup import *
from toontown.dna.DNADoor import *
from toontown.dna.DNAAnimBuilding import *
from toontown.dna.DNAAnimProp import *
from toontown.dna.DNABattleCell import *
from toontown.dna.DNACornice import *
from toontown.dna.DNAFlatBuilding import *
from toontown.dna.DNAFlatDoor import *
from toontown.dna.DNAInteractiveProp import *
from toontown.dna.DNALandmarkBuilding import *
from toontown.dna.DNAWall import *
from toontown.dna.DNAWindows import *
from toontown.suit.SuitLegList import *

class DNABulkLoader:
    __slots__ = (
        'dnaStorage', 'dnaFiles')

    def __init__(self, storage, files):
        self.dnaStorage = storage
        self.dnaFiles = files

    def loadDNAFiles(self):
        for file in self.dnaFiles:
            print 'Reading DNA file...', file
            loadDNABulk(self.dnaStorage, file)
        
        del self.dnaStorage
        del self.dnaFiles

def loadDNABulk(dnaStorage, file):
    dnaLoader = DNALoader.DNALoader()
    dnaLoader.loadDNAFile(dnaStorage, file)
    dnaLoader.destroy()

def loadDNAFile(dnaStorage, file):
    print 'Reading DNA file...', file
    dnaLoader = DNALoader.DNALoader()
    node = dnaLoader.loadDNAFile(dnaStorage, file)
    dnaLoader.destroy()
    if node.node().getNumChildren() > 0:
        return node.node()

def loadDNAFileAI(dnaStorage, file):
    dnaLoader = DNALoader.DNALoader()
    data = dnaLoader.loadDNAFileAI(dnaStorage, file)
    dnaLoader.destroy()
    return data