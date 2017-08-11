import copy
import random
from direct.actor import Actor
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
from otp.avatar import Avatar
from toontown.chat.ChatGlobals import *
from toontown.nametag.NametagGroup import *
from otp.otpbase import OTPGlobals
from toontown.distributed import DelayDelete
from toontown.effects import Bubbles
from toontown.hood import ZoneUtil
from toontown.safezone.OZPlayground import OZPlayground
from toontown.safezone.SafeZoneLoader import SafeZoneLoader
from toontown.toon import Toon, ToonDNA, NPCToons
from toontown.toonbase import TTLocalizer
from direct.task.Task import Task

class OZSafeZoneLoader(SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = OZPlayground
        self.musicFile = 'phase_6/audio/bgm/AA_nbrhood.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/AA_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/outdoor_zone_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_OZ_sz.pdna'
        self.beaver = NPCToons.createLocalNPC(7011)

    def load(self):
        self.done = 0
        SafeZoneLoader.load(self)
        self.birdSound = map(base.loader.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg', 'phase_4/audio/sfx/SZ_TC_bird2.ogg', 'phase_4/audio/sfx/SZ_TC_bird3.ogg'])
        self.underwaterSound = base.loader.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loader.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loader.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        
        binMgr = CullBinManager.getGlobalPtr()
        binMgr.addBin('water', CullBinManager.BTFixed, 29)
        binMgr = CullBinManager.getGlobalPtr()
        water = self.geom.find('**/Water*')
        water.setTransparency(1)
        water.setBin('water', 51, 1)

    def exit(self):
        SafeZoneLoader.exit(self)

    def unload(self):
        del self.birdSound
        SafeZoneLoader.unload(self)
        self.done = 1

