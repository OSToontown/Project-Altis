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
from toontown.toon import Toon, ToonDNA

class OZSafeZoneLoader(SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.musicFile = 'phase_6/audio/bgm/OZ_SZ.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/GS_KartShop.ogg'
        self.dnaFile = 'phase_6/dna/outdoor_zone_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_OZ_sz.pdna'
        self.__toonTracks = {}
        del self.fsm
        self.fsm = ClassicFSM.ClassicFSM('SafeZoneLoader', [State.State('start', self.enterStart, self.exitStart, ['quietZone', 'playground', 'toonInterior']),
         State.State('playground', self.enterPlayground, self.exitPlayground, ['quietZone', 'golfcourse']),
         State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, ['quietZone']),
         State.State('quietZone', self.enterQuietZone, self.exitQuietZone, ['playground', 'toonInterior', 'golfcourse']),
         State.State('golfcourse', self.enterGolfCourse, self.exitGolfCourse, ['quietZone', 'playground']),
         State.State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')

    def load(self):
        self.done = 0
        SafeZoneLoader.load(self)
        self.birdSound = map(base.loader.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg', 'phase_4/audio/sfx/SZ_TC_bird2.ogg', 'phase_4/audio/sfx/SZ_TC_bird3.ogg'])
        self.underwaterSound = base.loader.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loader.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loader.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        self.accept('clientLogout', self._handleLogout)

    def exit(self):
        self.clearToonTracks()
        SafeZoneLoader.exit(self)
        self.ignore('clientLogout')

    def restoreLocal(self, task = None):
        place = base.cr.playGame.getPlace()
        if place:
            place.fsm.request('walk')
        
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.collisionsOn()
        base.localAvatar.dropShadow.show()

    def restoreRemote(self, remoteAv, task = None):
        if remoteAv in Avatar.Avatar.ActiveAvatars:
            remoteAv.startSmooth()
            remoteAv.dropShadow.show()

    def changeCamera(self, newParent, newPos, newHpr):
        camera.reparentTo(newParent)
        camera.setPosHpr(newPos, newHpr)

    def doPrint(self, thing):
        return 0
        print thing

    def unload(self):
        del self.birdSound
        SafeZoneLoader.unload(self)
        self.done = 1

    def enterPlayground(self, requestStatus):
        self.playgroundClass = OZPlayground
        SafeZoneLoader.enterPlayground(self, requestStatus)

    def exitPlayground(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        SafeZoneLoader.exitPlayground(self)
        self.playgroundClass = None
        return

    def handlePlaygroundDone(self):
        status = self.place.doneStatus
        self.doneStatus = status
        messenger.send(self.doneEvent)

    def enteringARace(self, status):
        if not status['where'] == 'golfcourse':
            return 0
        if ZoneUtil.isDynamicZone(status['zoneId']):
            return status['hoodId'] == self.hood.hoodId
        else:
            return ZoneUtil.getHoodId(status['zoneId']) == self.hood.hoodId

    def enteringAGolfCourse(self, status):
        if not status['where'] == 'golfcourse':
            return 0
        if ZoneUtil.isDynamicZone(status['zoneId']):
            return status['hoodId'] == self.hood.hoodId
        else:
            return ZoneUtil.getHoodId(status['zoneId']) == self.hood.hoodId

    def enterGolfCourse(self, requestStatus):
        if 'curseId' in requestStatus:
            self.golfCourseId = requestStatus['courseId']
        else:
            self.golfCourseId = 0
        self.accept('raceOver', self.handleRaceOver)
        self.accept('leavingGolf', self.handleLeftGolf)
        base.transitions.irisOut(t=0.2)

    def exitGolfCourse(self):
        del self.golfCourseId

    def handleRaceOver(self):
        print 'you done!!'

    def handleLeftGolf(self):
        req = {'loader': 'safeZoneLoader',
         'where': 'playground',
         'how': 'teleportIn',
         'zoneId': 6000,
         'hoodId': 6000,
         'shardId': None}
        self.fsm.request('quietZone', [req])
        return

    def _handleLogout(self):
        self.clearToonTracks()

    def storeToonTrack(self, avId, track):
        self.clearToonTrack(avId)
        self.__toonTracks[avId] = track

    def clearToonTrack(self, avId):
        oldTrack = self.__toonTracks.get(avId)
        if oldTrack:
            oldTrack.pause()
            DelayDelete.cleanupDelayDeletes(oldTrack)
            del self.__toonTracks[avId]

    def clearToonTracks(self):
        keyList = []
        for key in self.__toonTracks:
            keyList.append(key)

        for key in keyList:
            if key in self.__toonTracks:
                self.clearToonTrack(key)
