from toontown.safezone import DGPlayground
from toontown.safezone import SafeZoneLoader
from toontown.toon import NPCToons
from toontown.chat.ChatGlobals import *
from toontown.toonbase import TTLocalizer
import random
from direct.task.Task import Task

class DGSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DGPlayground.DGPlayground
        self.musicFile = 'phase_8/audio/bgm/DG_nbrhood.ogg'
        self.activityMusicFile = 'phase_8/audio/bgm/DG_SZ_activity.ogg'
        self.dnaFile = 'phase_8/dna/daisys_garden_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_DG_sz.pdna'
        self.fox = NPCToons.createLocalNPC(7012)

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.birdSound = map(base.loader.loadSfx, ['phase_8/audio/sfx/SZ_DG_bird_01.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_02.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_03.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_04.ogg'])
        self.fox.reparentTo(render)
        self.fox.setPos(14.113, 110.719, 0.025)
        self.fox.setH(20)
        self.fox.setName('Fox')
        self.fox.initializeBodyCollisions('toon')
        taskMgr.doMethodLater(1, self.__foxDialog, 'fox-dial')
		
    def __foxDialog(self, task):
        if self.fox:
            self.fox.setChatAbsolute(random.choice(TTLocalizer.FoxChatter), CFSpeech | CFTimeout)
            time = random.random() * 20.0 + 2
            taskMgr.doMethodLater(time, self.__foxDialog, 'fox-dial')
        return Task.done

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.birdSound
        taskMgr.remove('fox-dial')
        self.fox.stash()
        self.fox = None
