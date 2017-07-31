from toontown.safezone import SafeZoneLoader
from toontown.safezone import DDPlayground
from toontown.toon import NPCToons
from toontown.chat.ChatGlobals import *
from toontown.toonbase import TTLocalizer
import random
from direct.task.Task import Task

class DDSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DDPlayground.DDPlayground
        self.musicFile = 'phase_6/audio/bgm/DD_nbrhood.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/DD_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/donalds_dock_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_DD_sz.pdna'
        self.gator = NPCToons.createLocalNPC(7010)

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.seagullSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_Seagull.ogg')
        self.underwaterSound = base.loader.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loader.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loader.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        water = self.geom.find('**/water')
        water.setTransparency(1)
        water.setColor(1, 1, 1, 0.8)
        self.boat = self.geom.find('**/donalds_boat')
        if self.boat.isEmpty():
            self.notify.error('Boat not found')
        else:
            wheel = self.boat.find('**/wheel')
            if wheel.isEmpty():
                self.notify.warning('Wheel not found')
            else:
                wheel.hide()
            self.boat.stash()
        self.dockSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.ogg')
        self.foghornSound = base.loader.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.ogg')
        self.bellSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.ogg')
        self.waterSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.ogg')
        self.gator.reparentTo(render)
        self.gator.setPos(42.798, 63.956, -1.884)
        self.gator.setH(-230)
        self.gator.setName('Gator')
        self.gator.initializeBodyCollisions('toon')
        taskMgr.doMethodLater(1, self.__gatorDialog, 'gator-dial')
		
    def __gatorDialog(self, task):
        if self.gator:
            self.gator.setChatAbsolute(random.choice(TTLocalizer.GatorChatter), CFSpeech | CFTimeout)
            time = random.random() * 20.0 + 2
            taskMgr.doMethodLater(time, self.__gatorDialog, 'gator-dial')
        return Task.done

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.seagullSound
        del self.underwaterSound
        del self.swimSound
        del self.dockSound
        del self.foghornSound
        del self.bellSound
        del self.waterSound
        del self.submergeSound
        del self.boat
        taskMgr.remove('gator-dial')
        self.gator.stash()
        self.gator = None
