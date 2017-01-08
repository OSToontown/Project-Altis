from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toonbase import ToontownGlobals
from otp.ai.MagicWordGlobal import *

class NewsManagerAI(DistributedObjectAI):
    notify = directNotify.newCategory('NewsManagerAI')
    
    def __init__(self, air):
        self.air = air
        self.holidayList = []

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        self.accept('avatarEntered', self.__handleAvatarEntered)

    def __handleAvatarEntered(self, avatar):
        if self.air.suitInvasionManager.getInvading():
            self.air.suitInvasionManager.notifyInvasionBulletin(avatar.getDoId())

    def setPopulation(self, todo0):
        pass

    def setBingoWin(self, todo0):
        pass

    def setBingoStart(self):
        pass

    def setBingoEnd(self):
        pass

    def setCircuitRaceStart(self):
        pass

    def setCircuitRaceEnd(self):
        pass

    def setTrolleyHolidayStart(self):
        pass

    def setTrolleyHolidayEnd(self):
        pass

    def setTrolleyWeekendStart(self):
        pass

    def setTrolleyWeekendEnd(self):
        pass

    def setRoamingTrialerWeekendStart(self):
        pass

    def setRoamingTrialerWeekendEnd(self):
        pass

    def setInvasionStatus(self, msgType, cogType, numRemaining, skeleton):
        self.sendUpdate('setInvasionStatus', args=[msgType, cogType, numRemaining, skeleton])
        
    def setHolidayIdList(self, holidays):
        self.holidayList = holidays

    def d_setHolidayIdList(self, holidays):
        self.sendUpdate('setHolidayIdList', [holidays])
        self.checkForNotify()
 
    def b_setHolidayIdList(self, holidays):
        self.setHolidayIdList(holidays)
        self.d_setHolidayIdList(holidays)
        
    def resendHolidayList(self):
        self.b_setHolidayIdList(self.holidayList)
        
    def checkForNotify(self):
        if len(self.holidayList) > 0:
            self.holidayNotify()

    def holidayNotify(self):
        self.sendUpdate('holidayNotify', [])
        
    def addHolidayId(self, holidayId):
        if int(holidayId) != holidayId:
            return
            
        if holidayId not in self.holidayList:
            self.holidayList.append(holidayId)
            self.resendHolidayList()
        else:
            return
        
    def removeHolidayId(self, holidayId):
        if int(holidayId) != holidayId:
            return
            
        if holidayId in self.holidayList:
            del self.holidayList[holidayId]
            self.resendHolidayList()
        else:
            return

    def setWeeklyCalendarHolidays(self, todo0):
        pass

    def getWeeklyCalendarHolidays(self):
        return []

    def setYearlyCalendarHolidays(self, todo0):
        pass

    def getYearlyCalendarHolidays(self):
        return []

    def setOncelyCalendarHolidays(self, todo0):
        pass

    def getOncelyCalendarHolidays(self):
        return []

    def setRelativelyCalendarHolidays(self, todo0):
        pass

    def getRelativelyCalendarHolidays(self):
        return []

    def setMultipleStartHolidays(self, todo0):
        pass

    def getMultipleStartHolidays(self):
        return []

    def sendSystemMessage(self, message, style):
        self.sendUpdate('sendSystemMessage', [message, style])

@magicWord(category=CATEGORY_PROGRAMMER, types=[int])
def startHoliday(holidayId):
    simbase.air.newsManager.b_setHolidayIdList([holidayId])
    return 'Successfully set holiday to %d.' % (holidayId)
    
@magicWord(category=CATEGORY_PROGRAMMER, types=[int])
def addHoliday(holidayId):
    simbase.air.newsManager.addHolidayId(holidayId)
    return 'Successfully added holiday %d to ongoing holidays!' % (holidayId)
    
@magicWord(category=CATEGORY_PROGRAMMER, types=[int])
def removeHoliday(holidayId):
    simbase.air.newsManager.removeHolidayId(holidayId)
    return 'Successfully removed holiday %d from ongoing holidays!' % (holidayId)