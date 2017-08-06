from toontown.safezone import DLPlayground
from toontown.safezone import SafeZoneLoader
from toontown.toon import NPCToons
from toontown.chat.ChatGlobals import *
from toontown.toonbase import TTLocalizer
import random
from direct.task.Task import Task

class DLSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
	
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DLPlayground.DLPlayground
        self.musicFile = 'phase_8/audio/bgm/DL_nbrhood.ogg'
        self.activityMusicFile = 'phase_8/audio/bgm/DL_SZ_activity.ogg'
        self.dnaFile = 'phase_8/dna/donalds_dreamland_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_DL_sz.pdna'
        self.bat = NPCToons.createLocalNPC(7013)
		
    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.bat.reparentTo(render)
        self.bat.setPos(-17.417, -2.848, -14.975)
        self.bat.setH(210)
        self.bat.setName('Bat')
        self.bat.initializeBodyCollisions('toon')
        taskMgr.doMethodLater(1, self.__batDialog, 'bat-dial')
		
    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        taskMgr.remove('bat-dial')
        self.bat.stash()
        self.bat = None
		
    def __batDialog(self, task):
        if self.bat:
            self.bat.setChatAbsolute(random.choice(TTLocalizer.BatChatter), CFSpeech | CFTimeout)
            time = random.random() * 20.0 + 2
            taskMgr.doMethodLater(time, self.__batDialog, 'bat-dial')
        return Task.done
