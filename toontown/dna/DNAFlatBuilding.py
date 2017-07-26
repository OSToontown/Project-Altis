from panda3d.core import NodePath, DecalEffect, LPoint3f
from toontown.dna import DNANode
from toontown.dna import DNAWall
import random

class DNAFlatBuilding(DNANode.DNANode):
    __slots__ = (
        'width', 'hasDoor')
    
    COMPONENT_CODE = 9
    currentWallHeight = 0

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.width = 0
        self.hasDoor = False

    def __del__(self):
        DNANode.DNANode.__del__(self)
        del self.width
        del self.hasDoor

    def getWidth(self):
        return self.width
        
    def setWidth(self, width):
        self.width = int(width)

    def makeFromDGI(self, dgi, store):
        DNANode.DNANode.makeFromDGI(self, dgi, store)
        self.width = dgi.getUint16() / 10.0
        self.hasDoor = dgi.getBool()

    def setupFlat(self, np, store, chr, wallCode):
        if self.name[:2] != 'tb':
            return

        ss = chr + 'b' + self.name[2:]

        node = np.attachNewNode(ss)

        scale = LPoint3f(self.scale)
        scale.setX(self.width)
        scale.setZ(DNAFlatBuilding.currentWallHeight)

        node.setZ(DNAFlatBuilding.currentWallHeight)
        node.setPosHprScale(self.pos, self.hpr, scale)

        numCodes = store.getNumCatalogCodes(wallCode)
        if not numCodes:
            return

        wallNode = store.findNode(store.getCatalogCode(wallCode, random.randint(0, numCodes - 1)))
        if wallNode.isEmpty():
            return

        wallNode.copyTo(node)
        if self.hasDoor:
            wallNp = node.find("wall_*")
            doorNp = store.findNode("suit_door").copyTo(wallNp)
            doorNp.setPosHprScale(0.5, 0, 0, 0, 0, 0, 1.0 / self.width, 0, 1.0 / DNAFlatBuilding.currentWallHeight)
            wallNp.setEffect(DecalEffect.make())

        node.flattenMedium()
        node.stash()

    def setupSuitFlatBuilding(self, np, store):
        self.setupFlat(np, store, 's', 'suit_wall')

    def setupCogdoFlatBuilding(self, np, store):
        self.setupFlat(np, store, 'c', 'cogdo_wall')

    def traverse(self, np, store):
        DNAFlatBuilding.currentWallHeight = 0
        node = np.attachNewNode(self.name)
        internalNode = node.attachNewNode(self.getName() + '-internal')
        scale = LPoint3f(self.scale)
        scale.setX(self.width)
        internalNode.setScale(scale)
        node.setPosHpr(self.pos, self.hpr)

        for child in self.children:
            if isinstance(child, DNAWall.DNAWall):
                child.traverse(internalNode, store)
            else:
                child.traverse(node, store)

        if DNAFlatBuilding.currentWallHeight != 0:
            result = store.findNode("wall_camera_barrier")
            if result.isEmpty():
                raise DNAError.DNAError('DNAFlatBuilding requires that there is a wall_camera_barrier in storage')

            cameraBarrier = result.copyTo(internalNode)
            cameraBarrier.setScale(1, 1, DNAFlatBuilding.currentWallHeight)
            self.setupSuitFlatBuilding(np, store)
            self.setupCogdoFlatBuilding(np, store)
            internalNode.flattenStrong()

            collNp = node.find("**/door_*/+CollisionNode")
            if not collNp.isEmpty():
                collNp.setName("KnockKnockDoorSphere_" + store.getBlock(self.name))

            cameraBarrier.wrtReparentTo(np)
            wallCollection = internalNode.findAllMatches("wall*")
            doorCollection = internalNode.findAllMatches("**/door*")
            corniceCollection = internalNode.findAllMatches("**/cornice*_d")
            windowCollection = internalNode.findAllMatches("**/window*")
            wallHolder = node.attachNewNode("wall_holder")
            wallDecal = node.attachNewNode("wall_decal")
            wallCollection.reparentTo(wallHolder)
            doorCollection.reparentTo(wallDecal)
            corniceCollection.reparentTo(wallDecal)
            windowCollection.reparentTo(wallDecal)

            for i in range(wallHolder.getNumChildren()):
                child = wallHolder.getChild(i)
                child.clearTag("DNARoot")
                child.clearTag("DNACode")

            wallHolder.flattenStrong()
            wallDecal.flattenStrong()
            holderChild0 = wallHolder.getChild(0)
            wallDecal.getChildren().reparentTo(holderChild0)
            holderChild0.reparentTo(internalNode)
            holderChild0.setEffect(DecalEffect.make())
            wallHolder.removeNode()
            wallDecal.removeNode()
