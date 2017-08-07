from otp.level import DistributedLevelAI, LevelSpec
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from otp.level import LevelSpec
from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals
from toontown.coghq import FactoryEntityCreatorAI, LevelSuitPlannerAI
from toontown.coghq.boardbothq import BoardOfficeRoomBase
from toontown.coghq.boardbothq import DistributedBoardOfficeBattleAI, BoardOfficeRoomSpecs
from toontown.suit import DistributedBoardOfficeSuitAI

class DistributedBoardOfficeRoomAI(DistributedLevelAI.DistributedLevelAI, BoardOfficeRoomBase.BoardOfficeRoomBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardOfficeRoomAI')

    def __init__(self, air, boardofficeId, boardofficeDoId, zoneId, roomId, roomNum, avIds, battleExpAggreg):
        DistributedLevelAI.DistributedLevelAI.__init__(self, air, zoneId, 0, avIds)
        BoardOfficeRoomBase.BoardOfficeRoomBase.__init__(self)
        self.setBoardOfficeId(boardofficeId)
        self.setRoomId(roomId)
        self.roomNum = roomNum
        self.boardofficeDoId = boardofficeDoId
        self.battleExpAggreg = battleExpAggreg

    def createEntityCreator(self):
        return FactoryEntityCreatorAI.FactoryEntityCreatorAI(level=self)

    def getBattleCreditMultiplier(self):
        return ToontownBattleGlobals.getBoardOfficeCreditMultiplier(self.boardofficeId)

    def generate(self):
        self.notify.debug('generate %s: room=%s' % (self.doId, self.roomId))
        self.notify.debug('loading spec')
        specModule = BoardOfficeRoomSpecs.getBoardOfficeRoomSpecModule(self.roomId)
        roomSpec = LevelSpec.LevelSpec(specModule)
        if __dev__:
            self.notify.debug('creating entity type registry')
            typeReg = self.getBoardOfficeEntityTypeReg()
            roomSpec.setEntityTypeReg(typeReg)
        self.notify.debug('creating entities')
        DistributedLevelAI.DistributedLevelAI.generate(self, roomSpec)
        self.notify.debug('creating cogs')
        cogSpecModule = BoardOfficeRoomSpecs.getCogSpecModule(self.roomId)
        self.planner = LevelSuitPlannerAI.LevelSuitPlannerAI(self.air, self, DistributedBoardOfficeSuitAI.DistributedBoardOfficeSuitAI, DistributedBoardOfficeBattleAI.DistributedBoardOfficeBattleAI, cogSpecModule.CogData, cogSpecModule.ReserveCogData, cogSpecModule.BattleCells, battleExpAggreg=self.battleExpAggreg)
        suitHandles = self.planner.genSuits()
        messenger.send('plannerCreated-' + str(self.doId))
        self.suits = suitHandles['activeSuits']
        self.reserveSuits = suitHandles['reserveSuits']
        self.d_setSuits()
        self.notify.debug('finish boardoffice room %s %s creation' % (self.roomId, self.doId))

    def delete(self):
        self.notify.debug('delete: %s' % self.doId)
        suits = self.suits
        for reserve in self.reserveSuits:
            suits.append(reserve[0])

        self.planner.destroy()
        del self.planner
        for suit in suits:
            if not suit.isDeleted():
                suit.factoryIsGoingDown()
                suit.requestDelete()

        del self.battleExpAggreg
        DistributedLevelAI.DistributedLevelAI.delete(self, deAllocZone=False)

    def getBoardOfficeId(self):
        return self.boardofficeId

    def getRoomId(self):
        return self.roomId

    def getRoomNum(self):
        return self.roomNum

    def getCogLevel(self):
        return self.cogLevel

    def d_setSuits(self):
        self.sendUpdate('setSuits', [self.getSuits(), self.getReserveSuits()])

    def getSuits(self):
        suitIds = []
        for suit in self.suits:
            suitIds.append(suit.doId)

        return suitIds

    def getReserveSuits(self):
        suitIds = []
        for suit in self.reserveSuits:
            suitIds.append(suit[0].doId)

        return suitIds

    def d_setBossConfronted(self, toonId):
        if toonId not in self.avIdList:
            self.notify.warning('d_setBossConfronted: %s not in list of participants' % toonId)
            return
        self.sendUpdate('setBossConfronted', [toonId])

    def setVictors(self, victorIds):
        activeVictors = []
        activeVictorIds = []
        for victorId in victorIds:
            toon = self.air.doId2do.get(victorId)
            if toon is not None:
                activeVictors.append(toon)
                activeVictorIds.append(victorId)

        description = '%s|%s' % (self.boardofficeId, activeVictorIds)
        for avId in activeVictorIds:
            self.air.writeServerEvent('boardofficeDefeated', avId, description)

        for toon in activeVictors:
            simbase.air.questManager.toonDefeatedBoardOffice(toon, self.boardofficeId, activeVictors)
            toon.addStat(ToontownGlobals.STATS_BOARD_OFFICES)
            simbase.air.achievementsManager.bdo(toon.doId)

    def b_setDefeated(self):
        self.d_setDefeated()
        self.setDefeated()

    def d_setDefeated(self):
        self.sendUpdate('setDefeated')

    def setDefeated(self):
        pass

    def allToonsGone(self, toonsThatCleared):
        DistributedLevelAI.DistributedLevelAI.allToonsGone(self, toonsThatCleared)
        if self.roomNum == 0:
            boardoffice = simbase.air.doId2do.get(self.boardofficeDoId)
            if boardoffice is not None:
                boardoffice.allToonsGone()
            else:
                self.notify.warning('no boardoffice %s in allToonsGone' % self.boardofficeDoId)
        return