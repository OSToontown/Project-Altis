from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from toontown.safezone import Playground
from toontown.launcher import DownloadForceAcknowledge
from toontown.building import Elevator
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer
from toontown.racing import RaceGlobals
from direct.fsm import State
from toontown.safezone import GolfKart
from direct.task.Task import Task

class OZPlayground(Playground.Playground):
    waterLevel = 3

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.parentFSM = parentFSM
        self.cameraSubmerged = -1
        self.toonSubmerged = -1

    def load(self):
        Playground.Playground.load(self)

    def unload(self):
        Playground.Playground.unload(self)

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)

    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('oz-check-toon-underwater')
        taskMgr.remove('oz-check-cam-underwater')
        self.loader.hood.setNoFog()

    def doRequestLeave(self, requestStatus):
        self.fsm.request('trialerFA', [requestStatus])

    def enterDFA(self, requestStatus):
        doneEvent = 'dfaDoneEvent'
        self.accept(doneEvent, self.enterDFACallback, [requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(doneEvent)
        if requestStatus['hoodId'] == ToontownGlobals.MyEstate:
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(ToontownGlobals.MyEstate))
        else:
            self.dfa.enter(5)

    def enterStart(self):
        self.cameraSubmerged = 0
        self.toonSubmerged = 0
        taskMgr.add(self.__checkToonUnderwater, 'oz-check-toon-underwater')
        taskMgr.add(self.__checkCameraUnderwater, 'oz-check-cam-underwater')

    def __checkCameraUnderwater(self, task):
        if camera.getZ(render) < self.waterLevel and not base.localAvatar.isFishing:
            self.__submergeCamera()
        else:
            self.__emergeCamera()
        return Task.cont

    def __checkToonUnderwater(self, task):
        if base.localAvatar.getZ() < 0 and not base.localAvatar.isFishing:
            self.__submergeToon()
        else:
            self.__emergeToon()
        return Task.cont

    def __submergeCamera(self):
        if self.cameraSubmerged == 1:
            return
        self.loader.hood.setUnderwaterFog()
        base.playSfx(self.loader.underwaterSound, looping=1, volume=0.8)
        self.cameraSubmerged = 1
        self.walkStateData.setSwimSoundAudible(1)

    def __emergeCamera(self):
        if self.cameraSubmerged == 0:
            return
        self.loader.hood.setNoFog()
        self.loader.underwaterSound.stop()
        self.cameraSubmerged = 0
        self.walkStateData.setSwimSoundAudible(0)

    def __submergeToon(self):
        if self.toonSubmerged == 1:
            return
        base.playSfx(self.loader.submergeSound)
        if base.config.GetBool('disable-flying-glitch') == 0:
            self.fsm.request('walk')
        self.walkStateData.fsm.request('swimming', [self.loader.swimSound])
        pos = base.localAvatar.getPos(render)
        base.localAvatar.d_playSplashEffect(pos[0], pos[1], self.waterLevel)
        self.toonSubmerged = 1

    def __emergeToon(self):
        if self.toonSubmerged == 0:
            return
        self.walkStateData.fsm.request('walking')
        self.toonSubmerged = 0

    def enterTeleportIn(self, requestStatus):
        reason = requestStatus.get('reason')
        if reason == RaceGlobals.Exit_Barrier:
            requestStatus['nextState'] = 'popup'
            self.dialog = TTDialog.TTDialog(text=TTLocalizer.KartRace_RaceTimeout, command=self.__cleanupDialog, style=TTDialog.Acknowledge)
        elif reason == RaceGlobals.Exit_Slow:
            requestStatus['nextState'] = 'popup'
            self.dialog = TTDialog.TTDialog(text=TTLocalizer.KartRace_RacerTooSlow, command=self.__cleanupDialog, style=TTDialog.Acknowledge)
        elif reason == RaceGlobals.Exit_BarrierNoRefund:
            requestStatus['nextState'] = 'popup'
            self.dialog = TTDialog.TTDialog(text=TTLocalizer.KartRace_RaceTimeoutNoRefund, command=self.__cleanupDialog, style=TTDialog.Acknowledge)
        self.toonSubmerged = -1
        taskMgr.remove('oz-check-toon-underwater')
        Playground.Playground.enterTeleportIn(self, requestStatus)

    def teleportInDone(self):
        self.toonSubmerged = -1
        taskMgr.add(self.__checkToonUnderwater, 'oz-check-toon-underwater')
        Playground.Playground.teleportInDone(self)

    def __cleanupDialog(self, value):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        if hasattr(self, 'fsm'):
            self.fsm.request('walk', [1])
        return

    def showPaths(self):
        from toontown.classicchars import CCharPaths
        from toontown.toonbase import TTLocalizer
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Chip))
