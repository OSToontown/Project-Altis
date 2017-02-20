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

        base.musicManager.stopAllSounds()
        self.toonMusic = loader.loadMusic('phase_14/audio/bgm/tt2_ambient_1.mp3') # Placeholder
        base.playMusic(self.toonMusic, looping = 1)

    def announceGenerate(self):
        DistributedEvent.announceGenerate(self)
        
    def start(self):
        pass

    def delete(self):
        DistributedEvent.delete(self)
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
    
    
    def enterGotoHq(self, timestamp):
        self.prepostera.animFSM.request('TeleportOut')
    
    def exitGotoHq(self):
        pass
    
    def toonTalk(self, phrase, toon):
        toon.setChatAbsolute(phrase, CFSpeech|CFTimeout)
