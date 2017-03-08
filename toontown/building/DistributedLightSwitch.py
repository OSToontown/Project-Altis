from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from panda3d.core import *

class DistributedLightSwitch(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLightSwitch')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

        self.interiorDoId = 0
        self.lightSwitch = None

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)

        toonInterior = base.cr.doId2do[self.getInteriorDoId()]
        self.lightSwitch = toonInterior.interior.find('**/light_switch')
        if self.lightSwitch.isEmpty():
            return
        self.lightSwitch.find('**/button').setColor(LVector4f(0, 1, 0, 1))
        self.lightSwitch.find('**/button').setPos(0, -.1, 0)
        self.picker = CollisionTraverser()
        self.pq = CollisionHandlerQueue()
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.lightSwitch.setCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP, self.pq)
        self.accept('mouse1', self.toggleLight)

    def delete(self):
        self.lightSwitch = None
        self.picker = None
        self.pq = None
        self.pickerNode = None
        self.pickerNP = None
        self.pickerRay = None
        self.ignore('mouse1')

        # reset render color scale
        render.setColorScale(LVector4f(1, 1, 1, 1))

        DistributedObject.delete(self)

    def setInteriorDoId(self, interiorDoId):
        self.interiorDoId = interiorDoId

    def getInteriorDoId(self):
        return self.interiorDoId

    def toggleLight(self):
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
            self.picker.traverse(render)
            
            if self.pq.getNumEntries():
                self.pq.sortEntries()
                pickedObj = self.pq.getEntry(0).getIntoNodePath()
                if pickedObj in ([self.lightSwitch.find('**/button'), self.lightSwitch.find('**/collision_floor')]):
                    self.sendUpdate('toggleLight', [])
                    
    def setLightState(self, lightState):
        if not lightState:
            self.lightSwitch.find('**/button').setColor(LVector4f(1, 0, 0, 1))
            render.setColorScale(LVector4f(0.2, 0.2, 0.2, 1))
            self.lightSwitch.find('**/button').setPos(0, 0, 0)
        else:
            self.lightSwitch.find('**/button').setColor(LVector4f(0, 1, 0, 1))
            render.setColorScale(LVector4f(1, 1, 1, 1))
            self.lightSwitch.find('**/button').setPos(0, -.1, 0)