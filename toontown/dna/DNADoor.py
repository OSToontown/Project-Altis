from panda3d.core import LVector4f, LVecBase3f, LVecBase4f, DecalEffect, NodePath
from toontown.dna import DNAGroup
from toontown.dna import DNAError
from toontown.dna import DNAUtil

class DNADoor(DNAGroup.DNAGroup):
    __slots__ = (
        'code', 'color')
    
    COMPONENT_CODE = 17

    def __init__(self, name):
        DNAGroup.DNAGroup.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1)

    def __del__(self):
        DNAGroup.DNAGroup.__del__(self)
        del self.code
        del self.color

    @staticmethod
    def setupDoor(doorNodePath, parentNode, doorOrigin, dnaStore, block, color):
        doorNodePath.setPosHprScale(doorOrigin, LVecBase3f(0), LVecBase3f(0), LVecBase3f(1))
        doorNodePath.setColor(color)
        leftHole = doorNodePath.find("door_*_hole_left")
        leftHole.setName("doorFrameHoleLeft")
        leftHoleGeom = leftHole.find("**/+GeomNode")
        leftHoleGeom.setName("doorFrameHoleLeftGeom")
        rightHole = doorNodePath.find("door_*_hole_right")
        rightHole.setName("doorFrameHoleRight")
        rightHoleGeom = rightHole.find("**/+GeomNode")
        rightHoleGeom.setName("doorFrameHoleRightGeom")
        leftDoor = doorNodePath.find("door_*_left")
        leftDoor.setName("leftDoor")
        rightDoor = doorNodePath.find("door_*_right")
        rightDoor.setName("rightDoor")
        doorFlat = doorNodePath.find("door_*_flat")
        doorFlat.setEffect(DecalEffect.make())
        leftHole.wrtReparentTo(doorFlat, 0)
        rightHole.wrtReparentTo(doorFlat, 0)
        
        if not leftHoleGeom.getNode(0).isGeomNode():
            leftHoleGeom = leftHoleGeom.find("**/+GeomNode")
    
        if not rightHoleGeom.getNode(0).isGeomNode():
            rightHoleGeom = rightHoleGeom.find("**/+GeomNode")
            
        leftHoleGeom.setEffect(DecalEffect.make())
        rightHoleGeom.setEffect(DecalEffect.make())
        rightDoor.wrtReparentTo(parentNode, 0)
        leftDoor.wrtReparentTo(parentNode, 0)
        rightDoor.setColor(color, 0)
        leftDoor.setColor(color, 0)
        rightDoor.hide()
        leftDoor.hide()
        rightHole.hide()
        leftHole.hide()
        leftHole.setColor(LVecBase4f(0, 0, 0, 1), 0)
        rightHole.setColor(LVecBase4f(0, 0, 0, 1), 0)
        
        doorTrigger = doorNodePath.find("door_*_trigger")
        doorTrigger.setScale(2, 2, 2)
        doorTrigger.wrtReparentTo(parentNode, 0)
        doorTrigger.setName("door_trigger_" + str(block))
        
        storeNp = NodePath("door_trigger_" + str(block))
        storeNp.setPosHprScale(doorTrigger, LVecBase3f(0), LVecBase3f(0), LVecBase3f(1))
        dnaStore.storeBlockDoor(block, storeNp)

    def makeFromDGI(self, dgi, store):
        DNAGroup.DNAGroup.makeFromDGI(self, dgi, store)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.color = DNAUtil.dgiExtractColor(dgi)

    def traverse(self, nodePath, dnaStorage):
        frontNode = nodePath.find('**/*_front')
        if not frontNode.getNode(0).isGeomNode():
            frontNode = frontNode.find('**/+GeomNode')
        
        frontNode.setEffect(DecalEffect.make())
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNADoor code ' + self.code + ' not found in DNAStorage')
        
        doorNode = node.copyTo(frontNode)
        block = dnaStorage.getBlock(nodePath.getName())
        DNADoor.setupDoor(doorNode, nodePath, nodePath.find('**/*door_origin'), dnaStorage, block, self.color)
        node.removeNode()
        
setupDoor = DNADoor.setupDoor