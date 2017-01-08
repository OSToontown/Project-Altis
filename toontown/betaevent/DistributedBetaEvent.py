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

class DistributedBetaEvent(DistributedEvent):
    notify = directNotify.newCategory('DistributedBetaEvent')
    
    def __init__(self, cr):
        DistributedEvent.__init__(self, cr)
        self.cr = cr
        self.spark = loader.loadSfx('phase_11/audio/sfx/LB_sparks_1.ogg') # i think this could be used somewhere
        
        # The toon version of Looney Labs - Before it gets taken over
        self.toonLabs = None
        
        # The cog version of Looney Labs - After it gets taken over
        self.cogLabs = None

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
        self.prepostera.setPosHpr(4, -3, -68.367, 0, 0, 0)
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
        
        middlemanDNA = SuitDNA.SuitDNA()
        middlemanDNA.newSuit('mdm')
        
        self.middleman1 = DistributedSuitBase.DistributedSuitBase(self.cr)
        self.middleman1.setDNA(middlemanDNA)
        self.middleman1.setDisplayName('Middleman')
        self.middleman1.setPickable(0)
        self.middleman1.setPosHpr(0, 0, 0, 0, 0, 0)
        self.middleman1.reparentTo(render)
        self.middleman1.doId = 1
        self.middleman1.hide()
        self.middleman1.initializeBodyCollisions('toon')
        
        self.middleman2 = DistributedSuitBase.DistributedSuitBase(self.cr)
        self.middleman2.setDNA(middlemanDNA)
        self.middleman2.setDisplayName('Middleman')
        self.middleman2.setPickable(0)
        self.middleman2.setPosHpr(0, 0, 0, 0, 0, 0)
        self.middleman2.reparentTo(render)
        self.middleman2.doId = 2
        self.middleman2.hide()
        self.middleman2.initializeBodyCollisions('toon')
        
        base.musicManager.stopAllSounds()
        self.toonMusic = loader.loadMusic('phase_14/audio/bgm/ttiHalcyon.mp3') # Placeholder
        base.playMusic(self.toonMusic, looping = 1)

    def announceGenerate(self):
        DistributedEvent.announceGenerate(self)
        
    def start(self):
        pass

    def delete(self):
        DistributedEvent.delete(self)
        self.prepostera.delete()
            
    def enterPreEvent(self, timestamp):
        # If for some reason the cog lab is loaded, unload
        if self.cogLabs:
            self.cogLabs.removeNode()
            self.cogLabs = None
        
        # Load the toon lab if its not already loaded incase a new player enters
        if not self.toonLabs:
            self.loadToonLab()
       
        
    def exitPreEvent(self):
        pass
    
    def enterAnnouncement(self, timestamp):
        """
        Announcing looney labs's renovation
        """
        # If for some reason the cog lab is loaded, unload
        if self.cogLabs:
            self.cogLabs.removeNode()
            self.cogLabs = None
        
        # Load the toon lab if its not already loaded incase a new player enters
        if not self.toonLabs:
            self.loadToonLab()
        
        Sequence(
                    Func(self.prepostera.setChatAbsolute, 'Greetings Toons of the world!', CFSpeech|CFTimeout),
                    Wait(3),
                    Func(self.prepostera.setChatAbsolute, 'Today, we are proud to announce...', CFSpeech|CFTimeout),
                    Wait(3),
                    Func(self.prepostera.setChatAbsolute, 'The renovation and public opening of...', CFSpeech|CFTimeout),
                    Wait(4),
                    Func(self.prepostera.setChatAbsolute, 'Looney Labs!', CFSpeech|CFTimeout),
                    Wait(2),
                 ).start()
        
    def exitAnnouncement(self):
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
    
    def enterCogInvade(self, timestamp):
        self.headHoncho1.setPosHpr(0, 0, 0, 0, 0, 0)
        self.headHoncho1.show()
        Sequence(
                    self.headHoncho1.beginSupaFlyMove(Vec3(12, -4, -68.367), True, "firstCogInvadeFlyIn", walkAfterLanding=False),
                    Func(self.headHoncho1.loop, 'walk'),
                    self.headHoncho1.hprInterval(2, VBase3(90, 0, 0)),
                    Func(self.headHoncho1.loop, 'neutral'),
                    Wait(1),
                    Func(self.headHoncho1.setChatAbsolute, 'Hello Toon...', CFSpeech|CFTimeout),
                    Wait(4),
                    Func(self.headHoncho1.setChatAbsolute, "I'd hate to crash the party...", CFSpeech|CFTimeout),
                    Wait(4),
                    Func(self.headHoncho1.setChatAbsolute, "Actually... I'd love to!", CFSpeech|CFTimeout)
                 ).start()
        
    def exitCogInvade(self):
        pass
    
    def enterCogTalk(self, timestamp):
        self.middleman1.show()
        self.middleman2.show()
        Sequence(
                 Func(self.headHoncho1.setChatAbsolute, 'I hear you are opening Looney Labs...', CFSpeech|CFTimeout),
                 Wait(4),
                 Parallel(
                          self.middleman1.beginSupaFlyMove(Vec3(-8, -4, -68.367), True, "firstCogInvadeFlyIn", walkAfterLanding=False),
                          self.middleman2.beginSupaFlyMove(Vec3(4, -12, -68.367), True, "firstCogInvadeFlyIn", walkAfterLanding=False)
                          ),
                 Func(self.middleman2.loop, 'neutral'),
                 Parallel(
                          Sequence(
                                Func(self.middleman1.loop, 'walk'),
                                self.middleman1.hprInterval(2, VBase3(-90, 0, 0)),
                                Func(self.middleman1.loop, 'neutral')),
                          Func(self.headHoncho1.setChatAbsolute, "Well let's see about that", CFSpeech|CFTimeout))
                 ).start()
                 
    def exitCogTalk(self):
        pass
    
    def enterCogTakeover(self, timestamp):
        """
        Cogs take over looney labs
        - Fade screen to black
        - Delete looney labs model and replace it with the Cog version of looney labs
        - AI will create suit planner
        - Screen unfades
        """
        # Unload the toon labs if its loaded
        if self.toonLabs:
            self.toonLabs.removeNode()
            self.toonLabs = None
        
        # Load the cog lab if its not already loaded incase a new player enters
        if not self.cogLabs:
            self.loadCogLab()
    
    def exitCogTakeover(self):
        pass
    
    def enterCredits(self, timestamp):
        import CreditsScreen
        self.credits = CreditsScreen.CreditsScreen()
        self.credits.startCredits()
        
    def exitCredits(self):
        pass
    
    def toonTalk(self, phrase, toon):
        toon.setChatAbsolute(phrase, CFSpeech|CFTimeout)
        
    def loadToonLab(self):
        # After the model is loaded, spawn it in
        def spawnToonLab(*args):
            self.toonLabs = args[0]
            self.toonLabs.reparentTo(render)
            self.toonLabs.setPos(0, -140, -60.3)
        
        # Asynchronously load the model to not lag the game
        asyncloader.loadModel('phase_14/models/looneylabs/temp_observatory', callback = spawnToonLab) # TODO: Models
        pass
        
    def loadCogLab(self):
        # After the model is loaded, spawn it in
        def spawnCogLab(*args):
            self.cogLabs = args[0]
            self.cogLabs.reparentTo(render)
        
        # Asynchronously load the model to not lag the game
        #asyncloader.loadModel('phase_14/models/looneylabs/looney_labs_cog', callback = spawnCogLab) # TODO: Models
        pass
        