from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal

class AltisAudio:
    notify = DirectNotifyGlobal.directNotify.newCategory('AltisAudio')

    def fadeInMusic(self, musicFile, looping = 1):
        #fade in music
        base.playMusic(musicFile, looping = looping, volume = 0)
        LerpFunctionInterval(musicFile.setVolume, fromData = 0, toData = 1, duration = 1).start()

    def fadeOutMusic(self, musicFile):
        #same as above but fading out
        Sequence(LerpFunctionInterval(musicFile.setVolume, fromData = 1, toData = 0, duration = 1),
        Func(musicFile.stop)).start()
