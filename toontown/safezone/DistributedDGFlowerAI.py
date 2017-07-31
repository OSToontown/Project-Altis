from direct.distributed import DistributedObjectAI
from direct.distributed.ClockDelta import *
from otp.ai.AIBase import *
from toontown.toonbase.ToontownGlobals import *
import random

HEIGHT_DELTA = 0.5
MAX_HEIGHT = 10.0
MIN_HEIGHT = 2.0
EGG_TOONS = 20

class DistributedDGFlowerAI(DistributedObjectAI.DistributedObjectAI):
    
    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)

        self.height = MIN_HEIGHT
        self.avList = []
        self.canSlam = True

    def delete(self):
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def start(self):
        pass

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.avList:
            self.avList.append(avId)
            if self.height + HEIGHT_DELTA <= MAX_HEIGHT:
                self.height += HEIGHT_DELTA
                self.sendHeight(self.height)
            if len(self.avList) >= EGG_TOONS:
                if self.canSlam:
                    self.slamHeight()
					
    def slamHeight(self):
        self.sendHeight(20)
        taskMgr.doMethodLater(1, self.slam, 'flowerSlam')
		
    def slam(self, task):
        self.canSlam = False
        self.sendHeight(0.5)
        taskMgr.doMethodLater(0.5, self.healEm, 'fateTask')
        taskMgr.doMethodLater(60, self.resetTimer, 'slamTimer')
		
    def resetTimer(self, task):
        self.canSlam = True
		
    def healEm(self, task):
        for avId in self.avList:
            av = simbase.air.doId2do.get(avId)
            if av:
                av.toonUp(av.getMaxHp())
		
    def sendHeight(self, height):
        self.sendUpdate('setHeight', [height])

    def avatarExit(self):
        avId = self.air.getAvatarIdFromSender()
        if avId in self.avList:
            self.avList.remove(avId)
            if self.height - HEIGHT_DELTA >= MIN_HEIGHT:
                self.height -= HEIGHT_DELTA
                self.sendHeight(self.height)
