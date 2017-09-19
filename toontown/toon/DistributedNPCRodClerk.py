from direct.gui.DirectGui import *
from direct.interval.LerpInterval import LerpPosHprInterval
from direct.task.Task import Task
from pandac.PandaModules import *
import time
from toontown.toon.DistributedNPCToonBase import *
from toontown.toon import NPCToons
from toontown.chat.ChatGlobals import *
from toontown.fishing import RodBuyGUI
from toontown.nametag.NametagGlobals import *
from toontown.toonbase import TTLocalizer


class DistributedNPCRodClerk(DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.isLocalToon = 0
        self.av = None
        self.button = None
        self.popupInfo = None
        self.buyGui = None
        self.nextCollision = 0
        self.npcType = 'Rod Salesman'
        return

    def disable(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupFishGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        if self.buyGui:
            self.buyGui.destroy()
            self.buyGui = None
        self.av = None
        if self.isLocalToon:
            base.localAvatar.posCamera(0, 0)
        DistributedNPCToonBase.disable(self)
        return

    def generate(self):
        DistributedNPCToonBase.generate(self)
        self.buyGuiDoneEvent = 'buyGuiDone'

    def announceGenerate(self):
        DistributedNPCToonBase.announceGenerate(self)
        self.setHat(18, 0, 0)

    def handleCollisionSphereEnter(self, collEntry):
        self.currentTime = time.time()
        if self.nextCollision > self.currentTime:
            self.nextCollision = self.currentTime + 2
        else:
            base.cr.playGame.getPlace().fsm.request('purchase')
            self.sendUpdate('avatarEnter', [])
            self.nextCollision = self.currentTime + 2

    def __handleUnexpectedExit(self):
        self.notify.warning('unexpected exit')
        self.av = None
        return

    def setupAvatars(self, av):
        self.ignoreAvatars()
        av.stopLookAround()
        av.lerpLookAt(Point3(-0.5, 4, 0), time=0.5)
        self.stopLookAround()
        self.lerpLookAt(Point3(av.getPos(self)), time=0.5)

    def resetFisherman(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupFishGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.buyGui:
            self.buyGui.destroy()
            self.buyGui = None
        self.show()
        self.startLookAround()
        self.detectAvatars()
        self.clearMat()
        if self.isLocalToon:
            self.freeAvatar()
        return Task.done

    def setMovie(self, mode, npcId, avId, extraArgs, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.remain = NPCToons.CLERK_COUNTDOWN_TIME - timeStamp
        self.npcId = npcId
        self.isLocalToon = avId == base.localAvatar.doId
        if mode == NPCToons.SELL_MOVIE_CLEAR:
            return
        if mode == NPCToons.SELL_MOVIE_TIMEOUT:
            taskMgr.remove(self.uniqueName('lerpCamera'))
            if self.isLocalToon:
                self.ignore(self.buyGuiDoneEvent)
                if self.popupInfo:
                    self.popupInfo.reparentTo(hidden)
                if self.buyGui:
                    self.buyGui.destroy()
                    self.buyGui = None
            self.setChatAbsolute(TTLocalizer.STOREOWNER_TOOKTOOLONG, CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_START:
            self.av = base.cr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return
            else:
                self.accept(self.av.uniqueName('disable'), self.__handleUnexpectedExit)
            self.setupAvatars(self.av)
            if self.isLocalToon:
                camera.wrtReparentTo(render)
                quat = Quat()
                quat.setHpr((-150, -2, 0))
                camera.posQuatInterval(1, Point3(-5, 9, base.localAvatar.getHeight() - 0.5), quat, other=self, blendType='easeOut').start()
            if self.isLocalToon:
                taskMgr.doMethodLater(1.0, self.popupFishGUI, self.uniqueName('popupFishGUI'))
        elif mode == NPCToons.SELL_MOVIE_COMPLETE:
            chatStr = TTLocalizer.STOREOWNER_GOODBYE
            self.setChatAbsolute(chatStr, CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_NOROD:
            chatStr = TTLocalizer.STOREOWNER_NEEDJELLYBEANS
            self.setChatAbsolute(chatStr, CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_ROD:
            self.av = base.cr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return
            else:
                self.setChatAbsolute(TTLocalizer.STOREOWNER_ROD_BUY, CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_BUCKET:
            self.av = base.cr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return
            else:
                self.setChatAbsolute(TTLocalizer.STOREOWNER_BUCKET_BUY, CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_NO_MONEY:
            self.notify.warning('SELL_MOVIE_NO_MONEY should not be called')
            self.resetFisherman()
        return

    def __handleSaleDone(self, type):
        self.ignore(self.buyGuiDoneEvent)
        self.sendUpdate('completeSale', [type])
        self.buyGui.destroy()
        self.buyGui = None
        return

    def popupFishGUI(self, task):
        self.setChatAbsolute('', CFSpeech)
        self.acceptOnce(self.buyGuiDoneEvent, self.__handleSaleDone)
        self.buyGui = RodBuyGUI.RodBuyGUI(self.buyGuiDoneEvent)
