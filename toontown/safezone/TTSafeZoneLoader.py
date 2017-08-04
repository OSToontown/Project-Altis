from toontown.safezone import SafeZoneLoader
from toontown.safezone import TTPlayground
from panda3d.core import DecalEffect
from toontown.toon import NPCToons
from toontown.chat.ChatGlobals import *
from toontown.toonbase import TTLocalizer
import random
from direct.task.Task import Task

class TTSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = TTPlayground.TTPlayground
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg'
        self.raccoontleMusic = loader.loadMusic('phase_4/audio/bgm/TC_nbrhood.ogg')
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.dnaFile = 'phase_4/dna/toontown_central_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_4/dna/storage_TT_sz.pdna'
        self.raccoon = NPCToons.createLocalNPC(7014)

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.birdSound = map(base.loader.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird2.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird3.ogg'])
        
        library = self.geom.find('**/*toon_landmark_TT_library_DNARoot')
        if not library.isEmpty():
            libraryDoor = library.find('**/door_double_round_ur')
            if not libraryDoor.isEmpty():
                libraryDoorGeom = libraryDoor.find('**/+GeomNode')
                libraryDoorGeom.setEffect(DecalEffect.make())
                libraryDoor.setY(0.0930333)
        bank = self.geom.find('**/*toon_landmark_TT_bank_DNARoot')
        if not bank.isEmpty():
            bankDoorOrigin = bank.find('**/*door_origin')
            doorTrigger = bank.find('**/door_trigger*')
            bankDoor = bank.find('**/door_double_round_ur')
            doorTrigger.setY(doorTrigger.getY() - 1.5)
            offsetFix = 0.51
            doorTrigger.setZ(doorTrigger.getZ() + offsetFix)
            bankDoorOrigin.setZ(bankDoorOrigin.getZ() + offsetFix)
            bankDoor.setZ(bankDoor.getZ() + offsetFix)
        self.raccoon.reparentTo(render)
        self.raccoon.setPos(79.405, 16.677, 4.025)
        self.raccoon.setH(65)
        self.raccoon.setName('Raccoon')
        self.raccoon.initializeBodyCollisions('toon')
        taskMgr.doMethodLater(1, self.__raccoonDialog, 'raccoon-dial')

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.birdSound
        taskMgr.remove('raccoon-dial')
        self.raccoon.stash()
        self.raccoon = None
		
    def __raccoonDialog(self, task):
        if self.raccoon:
            self.raccoon.setChatAbsolute(random.choice(TTLocalizer.RaccoonChatter), CFSpeech | CFTimeout)
            time = random.random() * 20.0 + 2
            taskMgr.doMethodLater(time, self.__raccoonDialog, 'raccoon-dial')
        return Task.done

