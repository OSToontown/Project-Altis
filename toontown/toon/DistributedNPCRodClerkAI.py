from otp.ai.AIBaseGlobal import *
from pandac.PandaModules import *
from toontown.toon.DistributedNPCToonBaseAI import *
from toontown.fishing import FishGlobals
from toontown.hood import ZoneUtil
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.fishing import FishGlobals
from direct.task import Task

class DistributedNPCRodClerkAI(DistributedNPCToonBaseAI):

    def __init__(self, air, npcId):
        DistributedNPCToonBaseAI.__init__(self, air, npcId)
        self.givesQuests = 0
        self.busy = 0

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.ignoreAll()
        DistributedNPCToonBaseAI.delete(self)

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.air.doId2do:
            self.notify.warning('Avatar: %s not found' % avId)
            return
        if self.isBusy():
            self.freeAvatar(avId)
            return
        for spot in self.air.hoodId2Hood[ZoneUtil.getCanonicalBranchZone(self.zoneId)].fishingSpots: 
            if spot.avId == avId:
                return

        av = self.air.doId2do[avId]
        self.busy = avId
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])
        flag = NPCToons.SELL_MOVIE_START
        self.d_setMovie(avId, flag)
        taskMgr.doMethodLater(30.0, self.sendTimeoutMovie, self.uniqueName('clearMovie'))
        DistributedNPCToonBaseAI.avatarEnter(self)
        return

    def rejectAvatar(self, avId):
        self.notify.warning('rejectAvatar: should not be called by a fisherman!')

    def d_setMovie(self, avId, flag, extraArgs = []):
        self.sendUpdate('setMovie', [flag,
         self.npcId,
         avId,
         extraArgs,
         ClockDelta.globalClockDelta.getRealNetworkTime()])

    def sendTimeoutMovie(self, task):
        self.d_setMovie(self.busy, NPCToons.SELL_MOVIE_TIMEOUT)
        self.sendClearMovie(None)
        return Task.done

    def sendClearMovie(self, task):
        self.ignore(self.air.getAvatarExitEvent(self.busy))
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.busy = 0
        self.d_setMovie(0, NPCToons.SELL_MOVIE_CLEAR)
        return Task.done

    def completeSale(self, type):
        avId = self.air.getAvatarIdFromSender()
        if self.busy != avId:
            self.air.writeServerEvent('suspicious', avId, 'DistributedNPCFishermanAI.completeSale busy with %s' % self.busy)
            self.notify.warning('somebody called setMovieDone that I was not busy with! avId: %s' % avId)
            return

        for spot in self.air.hoodId2Hood[ZoneUtil.getCanonicalBranchZone(self.zoneId)].fishingSpots:
            if spot.avId == avId:
                self.sendClearMovie(None)
                return

        if type == 1: # Rods
            av = simbase.air.doId2do.get(avId)
            if av:
                newIndex = 0
                for rod in av.getFishingRods():
                    if rod > newIndex:
                        newIndex = rod
                newIndex += 1
                extraArgs = []
                try:
                    if av.getTotalMoney() >= ToontownGlobals.FishingRodCosts[newIndex]:
                        av.takeMoney(ToontownGlobals.FishingRodCosts[newIndex], bUseBank=True)
                        rods = av.getFishingRods()
                        rods.append(newIndex)
                        av.b_setFishingRods(rods)
                        av.b_setFishingRod(newIndex)
                        movieType = NPCToons.SELL_MOVIE_ROD
                    else:
                        movieType = NPCToons.SELL_MOVIE_NOROD
                        extraArgs = []
                except:
                    movieType = NPCToons.SELL_MOVIE_COMPLETE
                    extraArgs = []
                self.d_setMovie(avId, movieType, extraArgs)
        elif type == 2: # Buckets
            av = simbase.air.doId2do.get(avId)
            if av:
                currMaxTank = av.getMaxFishTank()
                newTank = currMaxTank + 10
                extraArgs = []
                try:
                    if av.getTotalMoney() >= ToontownGlobals.BucketCosts.get(newTank):
                        av.takeMoney(ToontownGlobals.BucketCosts.get(newTank), bUseBank=True)
                        av.b_setMaxFishTank(newTank)
                        movieType = NPCToons.SELL_MOVIE_BUCKET
                    else:
                        movieType = NPCToons.SELL_MOVIE_NOROD
                except:
                    movieType = NPCToons.SELL_MOVIE_COMPLETE
                    extraArgs = []
                self.d_setMovie(avId, movieType, extraArgs)
        else:
            av = simbase.air.doId2do.get(avId)
            if av:
                self.d_setMovie(avId, NPCToons.SELL_MOVIE_COMPLETE)
        self.sendClearMovie(None)
        return

    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')
        self.notify.warning('not busy with avId: %s, busy: %s ' % (avId, self.busy))
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.sendClearMovie(None)
        return
