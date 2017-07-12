from toontown.classicchars import DistributedDaisyAI
from toontown.hood import HoodAI
from toontown.safezone import ButterflyGlobals
from toontown.safezone import DistributedButterflyAI
from toontown.safezone import DistributedDGFlowerAI
from toontown.safezone import DistributedTrolleyAI
from toontown.toonbase import ToontownGlobals
from toontown.ai import DistributedGreenToonEffectMgrAI
from toontown.ai import DistributedSofieListenerMgrAI
from toontown.ai import DistributedTrickOrTreatTargetAI
from toontown.ai import DistributedWinterCarolingTargetAI
from direct.showbase.DirectObject import DirectObject

class DGHoodAI(HoodAI.HoodAI, DirectObject):
    def __init__(self, air):
        DirectObject.__init__(self)
        HoodAI.HoodAI.__init__(self, air,
                               ToontownGlobals.DaisyGardens,
                               ToontownGlobals.DaisyGardens)

        self.trolley = None
        self.flower = None
        self.classicChar = None

        self.startup()

    def startup(self):
        HoodAI.HoodAI.startup(self)

        if simbase.config.GetBool('want-minigames', True):
            self.createTrolley()
        self.createFlower()
        if simbase.config.GetBool('want-classic-chars', True):
            if simbase.config.GetBool('want-daisy', True):
                self.createClassicChar()
        if simbase.config.GetBool('want-butterflies', True):
            self.createButterflies()
            
        if simbase.air.holidayManager.isHolidayRunning(ToontownGlobals.IDES_OF_MARCH):
            self.GreenToonEffectManager = DistributedGreenToonEffectMgrAI.DistributedGreenToonEffectMgrAI(self.air)
            self.GreenToonEffectManager.generateWithRequired(5819)
			
        self.SofieSquirtMgr = DistributedSofieListenerMgrAI.DistributedSofieListenerMgrAI(self.air)
        self.SofieSquirtMgr.generateWithRequired(5717)
            
        self.accept('startIdes', self.startIdes)
        self.accept('endIdes', self.endIdes)
        
        if simbase.air.wantHalloween:
            self.TrickOrTreatTargetManager = DistributedTrickOrTreatTargetAI.DistributedTrickOrTreatTargetAI(self.air)
            self.TrickOrTreatTargetManager.generateWithRequired(5620)
        
        if simbase.air.wantChristmas:
            self.WinterCarolingTargetManager = DistributedWinterCarolingTargetAI.DistributedWinterCarolingTargetAI(self.air)
            self.WinterCarolingTargetManager.generateWithRequired(5626)

    def startIdes(self):
        if simbase.air.holidayManager.isHolidayRunning(ToontownGlobals.IDES_OF_MARCH):
            self.GreenToonEffectManager = DistributedGreenToonEffectMgrAI.DistributedGreenToonEffectMgrAI(self.air)
            self.GreenToonEffectManager.generateWithRequired(5819)
            
    def endIdes(self):
        self.GreenToonEffectManager.requestDelete()
            
    def shutdown(self):
        HoodAI.HoodAI.shutdown(self)

        ButterflyGlobals.clearIndexes(self.zoneId)

    def createTrolley(self):
        self.trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        self.trolley.generateWithRequired(self.zoneId)
        self.trolley.start()

    def createFlower(self):
        self.flower = DistributedDGFlowerAI.DistributedDGFlowerAI(self.air)
        self.flower.generateWithRequired(self.zoneId)
        self.flower.start()

    def createClassicChar(self):
        self.classicChar = DistributedDaisyAI.DistributedDaisyAI(self.air)
        self.classicChar.generateWithRequired(self.zoneId)
        self.classicChar.start()

    def createButterflies(self, playground):
        ButterflyGlobals.generateIndexes(self.zoneId, ButterflyGlobals.DG)
        for i in xrange(0, ButterflyGlobals.NUM_BUTTERFLY_AREAS[ButterflyGlobals.DG]):
            for _ in xrange(0, ButterflyGlobals.NUM_BUTTERFLIES[ButterflyGlobals.DG]):
                butterfly = DistributedButterflyAI(self.air, playground, i, self.zoneId)
                butterfly.generateWithRequired(self.zoneId)
                butterfly.start()
