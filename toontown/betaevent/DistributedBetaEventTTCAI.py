from DistributedEventAI import DistributedEventAI
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownGlobals


class DistributedBetaEventTTCAI(DistributedEventAI):
    notify = directNotify.newCategory('DistributedBetaEventTTCAI')

    def __init__(self, air):
        DistributedEventAI.__init__(self, air)
        self.air = air

    def start(self):
        DistributedEventAI.start(self)
        
    def systemMessageAll(self, text):
        # Whisper to everyone if we need to
        for doId in simbase.air.doId2do:
            if str(doId)[:2] == '10':
                player = simbase.air.doId2do.get(doId)
                player.d_setSystemMessage(0, text)

    def enterPreEvent(self): 
        pass
    
    def exitPreEvent(self):
        pass
    
    def enterGotoHq(self):
        self.systemMessageAll("Toon HQ: All toons are being teleported to Loony Labs!")
        # magic teleport everyone to Boardbot HQ
        for doId in simbase.air.doId2do:
            if str(doId)[:2] == '10':
                player = simbase.air.doId2do.get(doId)
                player.magicTeleportInitiate(doId, 19000, 19000)
    
    def exitGotoHq(self):
        pass

    def enterCogTv(self):
        pass
    
    def exitCogTv(self):
        pass
    
    