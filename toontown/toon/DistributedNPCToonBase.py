from direct.directnotify import DirectNotifyGlobal
from direct.distributed import ClockDelta
from direct.distributed import DistributedObject
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
import random
from toontown.toon import DistributedToon
from toontown.toon import NPCToons
from toontown.nametag import NametagGlobals
from toontown.quest import QuestChoiceGui
from toontown.quest import QuestParser
from toontown.quest import Quests
from toontown.toonbase import ToontownGlobals
from direct.gui.DirectGui import *

class DistributedNPCToonBase(DistributedToon.DistributedToon):
    
    def __init__(self, cr):
        try:
            self.DistributedNPCToon_initialized
            return
        except:
            self.DistributedNPCToon_initialized = 1
        
        DistributedToon.DistributedToon.__init__(self, cr)
        self.__initCollisions()
        self.setPickable(0)
        self.setPlayerType(NametagGlobals.CCNonPlayer)

    def disable(self):
        self.ignore('enter' + self.cSphereNode.getName())
        DistributedToon.DistributedToon.disable(self)

    def delete(self):
        try:
            self.DistributedNPCToon_deleted
            return
        except:
            self.DistributedNPCToon_deleted = 1
        
        self.__deleteCollisions()
        DistributedToon.DistributedToon.delete(self)

    def generate(self):
        DistributedToon.DistributedToon.generate(self)
        self.cSphereNode.setName(self.uniqueName('NPCToon'))
        self.detectAvatars()
        self.setParent(ToontownGlobals.SPRender)
        self.startLookAround()

    def generateToon(self):
        self.setLODs()
        self.generateToonLegs()
        self.generateToonHead()
        self.generateToonTorso()
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.rightHands = []
        self.leftHands = []
        self.headParts = []
        self.hipsParts = []
        self.torsoParts = []
        self.legsParts = []
        self.__bookActors = []
        self.__holeActors = []

    def announceGenerate(self):
        self.initToonState()
        DistributedToon.DistributedToon.announceGenerate(self)

    def initToonState(self):
        self.setAnimState('neutral', 0.9, None, None)
        npcOrigin = render.find('**/npc_origin_' + str(self.posIndex))
        if not npcOrigin.isEmpty():
            self.reparentTo(npcOrigin)
            self.initPos()

    def initPos(self):
        self.clearMat()

    def wantsSmoothing(self):
        return 0

    def detectAvatars(self):
        self.accept('enter' + self.cSphereNode.getName(), self.prompt)

    def prompt(self, collEntry):
        if base.wantInteractKey:
            self.accept('exit' + self.cSphereNode.getName(), self.handleCollisionSphereExit)
            self.accept(base.INTERACT, self.activate, [collEntry])
            if hasattr(self, "name"):
                text = ("Press " + str(base.INTERACT).upper() + " to interact with %s" %self.name)
            else:
                text = "Press " + str(base.INTERACT).upper() + " to interact"
                
            if base.wantMobile:
                self.enterText = DirectButton(relief = None, parent = base.a2dBottomCenter, image = (base.shuffleUp, base.shuffleUp, base.shuffleDown), image_scale = (1, 0.7, 0.7), image1_scale = (1.02, 0.7, 0.7), image2_scale = (1.02, 0.7, 0.7), text = ("Tap to interact"), text_style = 3, text_scale = .07, text_pos = (0, -0.02), text_fg = (1, 0.9, 0.1, 1), scale = 1.5, pos = (0.0, 0.0, 0.5), command = self.activate, extraArgs = [collEntry])
            else:                
                self.enterText = OnscreenText(text = text, style = 3, scale = .09, parent = base.a2dBottomCenter, fg = (1, 0.9, 0.1, 1), pos = (0.0, 0.5))

            self.colorSeq = Sequence(
            LerpColorScaleInterval(self.enterText, .8, VBase4(.5, .6, 1, .9)),
            LerpColorScaleInterval(self.enterText, .8, VBase4(1, 1, 1, 1))).loop()
        else:
            self.handleCollisionSphereEnter(collEntry)

    def activate(self, collEntry):
        self.ignore("shift")
        if hasattr(self, "colorSeq"):
            if self.colorSeq:
                self.colorSeq.finish()
        if hasattr(self, "enterText"):
            self.enterText.removeNode()
            del self.enterText
        
        self.handleCollisionSphereEnter(collEntry)
            
    def handleCollisionSphereExit(self, collEntry):
        self.ignore("shift")
        if hasattr(self, "colorSeq"):
            if self.colorSeq:
                self.colorSeq.finish()
        if hasattr(self, "enterText"):
            self.enterText.removeNode()
            del self.enterText
            
    def ignoreAvatars(self):
        self.ignore('enter' + self.cSphereNode.getName())

    def getCollSphereRadius(self):
        return 3.25

    def __initCollisions(self):
        self.cSphere = CollisionTube(0.0, 1.0, 0.0, 0.0, 1.0, 5.0, self.getCollSphereRadius())
        self.cSphere.setTangible(0)
        self.cSphereNode = CollisionNode('cSphereNode')
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)

    def __deleteCollisions(self):
        self.ignore("shift")
        if hasattr(self, "colorSeq"):
            if self.colorSeq:
                self.colorSeq.finish()
        if hasattr(self, "enterText"):
            self.enterText.removeNode()
            del self.enterText
        del self.cSphere
        del self.cSphereNode
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath

    def handleCollisionSphereEnter(self, collEntry):
        pass

    def setupAvatars(self, av):
        self.ignoreAvatars()
        av.headsUp(self, 0, 0, 0)
        self.headsUp(av, 0, 0, 0)
        av.stopLookAround()
        av.lerpLookAt(Point3(-0.5, 4, 0), time=0.5)
        self.stopLookAround()
        self.lerpLookAt(Point3(av.getPos(self)), time=0.5)

    def b_setPageNumber(self, paragraph, pageNumber):
        self.setPageNumber(paragraph, pageNumber)
        self.d_setPageNumber(paragraph, pageNumber)

    def d_setPageNumber(self, paragraph, pageNumber):
        timestamp = ClockDelta.globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('setPageNumber', [paragraph, pageNumber, timestamp])

    def freeAvatar(self):
        base.localAvatar.posCamera(0, 0)
        base.cr.playGame.getPlace().setState('walk')

    def setPositionIndex(self, posIndex):
        self.posIndex = posIndex
