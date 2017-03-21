from DistributedEventAI import DistributedEventAI
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownGlobals
from direct.task.TaskManagerGlobal import taskMgr
from toontown.suit.DistributedSuitPlannerAI import DistributedSuitPlannerAI

class DistributedBetaEventTTCAI(DistributedEventAI):
    notify = directNotify.newCategory('DistributedBetaEventTTCAI')

    def __init__(self, air):
        DistributedEventAI.__init__(self, air)
        self.air = air
        self.air.betaEventTTC = self

    def start(self):
        DistributedEventAI.start(self)
                
    def setVisGroups(self, visGroups):
        self.sendUpdate('setVisGroups', [visGroups])

    def setupDNA(self, suitPlanner):
        if suitPlanner.dnaStore:
            return None

        suitPlanner.dnaStore = DNAStorage()
        loadDNAFileAI(suitPlanner.dnaStore, 'phase_4/dna/toontown_central_old_sz.pdna')

        visGroups = {}
        for visGroup in suitPlanner.dnaStore.DNAVisGroups:
            zone = int(visGroup.name)
            if zone == 20000:
                visGroups[20000] = self.zoneId
            else:
                visGroups[zone] = self.air.allocateZone()
            visGroup.name = str(visGroups[zone])

        for suitEdges in suitPlanner.dnaStore.suitEdges.values():
            for suitEdge in suitEdges:
                suitEdge.setZoneId(visGroups[suitEdge.zoneId])

        self.setVisGroups(visGroups.values())
        suitPlanner.initDNAInfo()
        
    def systemMessageAll(self, text):
        # Whisper to everyone if we need to
        for doId in simbase.air.doId2do:
            if str(doId)[:2] == '10':
                player = simbase.air.doId2do.get(doId)
                player.d_setSystemMessage(0, text)
                
    def enterPreEvent(self):
        self.systemMessageAll("Toon HQ: All toons are being teleported to Toontown Central for the Special Event!")
        # magic teleport everyone to TTC
        for doId in simbase.air.doId2do:
            if str(doId)[:2] == '10':
                player = simbase.air.doId2do.get(doId)
                player.magicTeleportInitiate(doId, 2900, 2900)
                
    def exitPreEvent(self):
        pass
    
    def enterEvent(self): 
        pass
    
    def exitEvent(self):
        pass
        
    def enterHoncho(self):
        pass
                
    def exitHoncho(self):
        pass
        
    def enterGotoHq(self):
        self.systemMessageAll("Toon HQ: All toons are being teleported to Loony Labs!")
        # magic teleport everyone to Boardbot HQ
        for doId in simbase.air.doId2do:
            if str(doId)[:2] == '10':
                player = simbase.air.doId2do.get(doId)
                player.magicTeleportInitiate(doId, 19000, 19000)
        taskMgr.doMethodLater(6, self.air.betaEventBDHQ.setState('StartBd'))
    
    def exitGotoHq(self):
        pass

    def enterInvasion(self):
        self.suitPlanner = DistributedSuitPlannerAI(self.air, self.zoneId)
        self.suitPlanner.generateWithRequired(self.zoneId)
        self.suitPlanner.d_setZoneId(self.zoneId)
        self.suitPlanner.initTasks()
    
    def exitInvasion(self):
        if self.suitPlanner:  
            self.suitPlanner.cleanup()  
            self.suitPlanner = None
        
    def enterCogTv(self):
        pass
    
    def exitCogTv(self):
        pass
    
    