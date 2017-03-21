from panda3d.core import Point3, VBase3, Vec3, Vec4
from toontown.betaevent.DistributedEvent import DistributedEventfrom toontown.betaevent import CogTV
from toontown.hood import ZoneUtil
from direct.fsm import ClassicFSM, State
from direct.interval.IntervalGlobal import * 
from toontown.toon import Toon, ToonDNA
from direct.actor.Actor import Actor
from otp.avatar import Avatar
from toontown.chat.ChatGlobals import *
from toontown.nametag.NametagGroup import *
from toontown.suit import DistributedSuitBase, SuitDNA
from toontown.toon import NPCToons
from toontown.betaevent import BetaEventGlobals as BEGlobals
from toontown.battle import BattleParticles
from toontown.dna.DNAStorage import DNAStorage
from toontown.dna.DNAParser import loadDNAFileAI

class DistributedBetaEventTTC(DistributedEvent):
    notify = directNotify.newCategory('DistributedBetaEventTTC')
    
    def __init__(self, cr):
        DistributedEvent.__init__(self, cr)
        self.cr = cr
        self.spark = loader.loadSfx('phase_11/audio/sfx/LB_sparks_1.ogg') # i think this could be used somewhere

        # Create prepostera
        self.prepostera = Toon.Toon()
        self.prepostera.setName('Professor Prepostera')
        self.prepostera.setPickable(0)
        self.prepostera.setPlayerType(NametagGlobals.CCNonPlayer)
        dna = ToonDNA.ToonDNA()
        dna.newToonFromProperties('hss', 'ms','m', 'm', 20, 0, 20, 20, 97, 27, 86, 27, 37, 27)
        self.prepostera.setDNA(dna)
        self.prepostera.loop('scientistEmcee')
        self.prepostera.reparentTo(render)
        self.prepostera.setPosHpr(68, -10, 4.024, 75, 0, 0)
        self.prepostera.blinkEyes()
        self.prepostera.head = self.prepostera.find('**/__Actor_head')
        self.prepostera.initializeBodyCollisions('toon')
        
        self.headHoncho1 = DistributedSuitBase.DistributedSuitBase(self.cr)
        headHoncho1suitDNA = SuitDNA.SuitDNA()
        headHoncho1suitDNA.newSuit('hho')
        self.headHoncho1.setDNA(headHoncho1suitDNA)
        self.headHoncho1.setDisplayName('???')
        self.headHoncho1.setPickable(0)
        self.headHoncho1.setPosHpr(0, 0, 0, 0, 0, 0)
        self.headHoncho1.reparentTo(render)
        self.headHoncho1.doId = 0
        self.headHoncho1.hide()
        self.headHoncho1.initializeBodyCollisions('toon')
        
        #base.musicManager.stopAllSounds()
        self.toonMusic = loader.loadMusic('phase_14/audio/bgm/tt2_ambient_1.mp3') # Placeholder
        self.invasion1 = loader.loadMusic('phase_14/audio/bgm/event_temp_1.ogg') # Placeholder
        #base.playMusic(self.toonMusic, looping = 1)

    def announceGenerate(self):
        DistributedEvent.announceGenerate(self)
        dnaStore = DNAStorage()
        dnaFileToLoad = 'phase_4/dna/toontown_central_old_sz.pdna'
        loadDNAFileAI(dnaStore, dnaFileToLoad)

        # Collect all of the vis group zone IDs:
        zoneVisDict = {}
        for i in xrange(dnaStore.getNumDNAVisGroupsAI()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            visGroup = dnaStore.getDNAVisGroupAI(i)
            visZoneId = int(base.cr.hoodMgr.extractGroupName(groupFullName))
            visibles = []
            for i in xrange(visGroup.getNumVisibles()):
                visibles.append(int(visGroup.visibles[i]))
            visibles.append(ZoneUtil.getBranchZone(visZoneId))
            zoneVisDict[visZoneId] = visibles

        # Next, we want interest in all vis groups due to this being a Cog HQ:
        self.cr.sendSetZoneMsg(self.zoneId, zoneVisDict.values()[0])
        
    def start(self):
        self.prepostera.setChatAbsolute("Just sitting here waiting to be coded", CFThought)

    def delete(self):
        DistributedEvent.delete(self)
        base.unlockMusic()
        self.prepostera.delete()
        
    def enterPreEvent(self, timestamp):
        pass
    
    def exitPreEvent(self):
        pass
            
    def enterEvent(self, timestamp):
        Sequence(
                 Func(self.toonTalk, "Helloooooooo Toontown!", self.prepostera),
                 Wait(4),
                 Func(self.toonTalk, "We gathered you all here today...", self.prepostera),
                 Wait(4),
                 Func(self.toonTalk, "To announce the reconstruction and opening of...", self.prepostera),
                 Wait(5),
                 Func(self.toonTalk, "Loony La...", self.prepostera),
                 Wait(3),
                 Func(self.toonTalk, "It seems like Doctor Dimm is trying to reach me...", self.prepostera)).start()
    
    def exitEvent(self):
        pass
        
    def enterHoncho(self, timestamp):
        Sequence(
                self.headHoncho1.beginSupaFlyMove(Vec3(68, -2, 4.024), True, "firstCogInvadeFlyIn", walkAfterLanding=False),
                Func(self.headHoncho1.loop, 'walk'),
                self.headHoncho1.hprInterval(2, VBase3(90, 0, 0)),
                Func(self.headHoncho1.loop, 'neutral')).start()
                
    def exitHoncho(self):
        pass
                
    def enterCogTv(self, timestamp):
        # Todo: Make the models and make the tv code.
        '''
        self.cogTvModel = None
        self.cogTvModel.setPosHpr(0, 0, 0, 0, 0, 0) 
        self.cogTv = CogTV.CogTV
        self.cogTv.setScreen("Introduction")
        '''
        pass
    
    def exitCogTv(self):
        pass
    
    def enterInvasion(self, timestamp):
        base.musicManager.stopAllSounds()
        base.lockMusic()
        base.playMusic(self.invasion1, looping = 1)
        
    def exitInvasion(self):
        pass
    
    def enterGotoHq(self, timestamp):
        self.prepostera.animFSM.request('TeleportOut')
    
    def exitGotoHq(self):
        pass
    
    def toonTalk(self, phrase, toon):
        toon.setChatAbsolute(phrase, CFSpeech|CFTimeout)
