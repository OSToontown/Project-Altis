from toontown.safezone import SafeZoneLoader
from toontown.safezone import TTOPlayground
from panda3d.core import DecalEffect

class TTOSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = TTOPlayground.TTOPlayground
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg'
        self.battleMusic = loader.loadMusic('phase_4/audio/bgm/TC_nbrhood.ogg')
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.dnaFile = 'phase_4/dna/toontown_central_old_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_4/dna/storage_TT_sz.pdna'

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

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.birdSound

