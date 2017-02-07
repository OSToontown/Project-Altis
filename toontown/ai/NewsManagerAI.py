from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toonbase import ToontownGlobals
from otp.ai.MagicWordGlobal import *
from HolidayGlobals import *

class NewsManagerAI(DistributedObjectAI):
    notify = directNotify.newCategory('NewsManagerAI')
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.holidayList = []
        self.weeklyHolidays = WEEKLY_HOLIDAYS
        self.yearlyHolidays = YEARLY_HOLIDAYS
        self.oncelyHolidays = ONCELY_HOLIDAYS

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        self.accept('avatarEntered', self.__handleAvatarEntered)

    def __handleAvatarEntered(self, avatar):
        if self.air.suitInvasionManager.getInvading():
            self.air.suitInvasionManager.notifyInvasionBulletin(avatar.getDoId())
        if self.air.holidayManager.isHolidayRunning(MORE_XP_HOLIDAY):
            self.sendUpdateToAvatarId(avatar.getDoId(), 'setMoreXpHolidayOngoing', [])
        if self.air.holidayManager.isHolidayRunning(TROLLEY_HOLIDAY):
            self.sendUpdateToAvatarId(avatar.getDoId(), 'holidayNotify', [])
        if self.air.holidayManager.isHolidayRunning(CIRCUIT_RACING_EVENT):
            self.sendUpdateToAvatarId(avatar.getDoId(), 'startHoliday', [CIRCUIT_RACING_EVENT])
        if self.air.holidayManager.isHolidayRunning(HYDRANT_ZERO_HOLIDAY):
            self.sendUpdateToAvatarId(avatar.getDoId(), 'startHoliday', [HYDRANT_ZERO_HOLIDAY])

    def setPopulation(self, todo0):
        pass

    def setBingoWin(self, avatar, zoneId):
        self.sendUpdateToAvatarId(avatar.getDoId(), 'setBingoWin', [zoneId])

    def setBingoStart(self):
        self.sendUpdate('setBingoStart', [])
    
    def setBingoOngoing(self):
        self.sendUpdate('setBingoOngoing', [])

    def setBingoEnd(self):
        self.sendUpdate('setBingoEnd', [])

    def setCircuitRaceStart(self):
        self.sendUpdate('setCircuitRaceStart', [])
        
    def setCircuitRaceOngoing(self):
        self.sendUpdate('setCircuitRaceOngoing', [])

    def setCircuitRaceEnd(self):
        self.sendUpdate('setCircuitRaceEnd', [])

    def setTrolleyHolidayStart(self):
        self.sendUpdate('setTrolleyHolidayStart', [])
        
    def setTrolleyHolidayOngoing(self):
        self.sendUpdate('setTrolleyHolidayOngoing', [])

    def setTrolleyHolidayEnd(self):
        self.sendUpdate('setTrolleyHolidayEnd', [])

    def setTrolleyWeekendStart(self):
        self.sendUpdate('setTrolleyWeekendStart', [])
        
    def setTrolleyWeekendOngoing(self):
        self.sendUpdate('setTrolleyWeekendOngoing', [])

    def setTrolleyWeekendEnd(self):
        self.sendUpdate('setTrolleyWeekendEnd', [])

    def setRoamingTrialerWeekendStart(self):
        self.sendUpdate('setRoamingTrialerWeekendStart', [])
    
    def setRoamingTrialerWeekendOngoing(self):
        self.sendUpdate('setRoamingTrialerWeekendOngoing', [])

    def setRoamingTrialerWeekendEnd(self):
        self.sendUpdate('setRoamingTrialerWeekendEnd', [])
    
    def setSellbotNerfHolidayStart(self):
        self.sendUpdate('setSellbotNerfHolidayStart', [])
        
    def setSellbotNerfHolidayEnd(self):
        self.sendUpdate('setSellbotNerfHolidayEnd', [])
    
    def setMoreXpHolidayStart(self):
        self.sendUpdate('setMoreXpHolidayStart', [])
        
    def setMoreXpHolidayOngoing(self):
        self.sendUpdate('setMoreXpHolidayOngoing', [])
        
    def setMoreXpHolidayEnd(self):
        self.sendUpdate('setMoreXpHolidayEnd', [])

    def setInvasionStatus(self, msgType, cogType, numRemaining, skeleton):
        self.sendUpdate('setInvasionStatus', args=[msgType, cogType, numRemaining, skeleton])

    def d_setHolidayIdList(self, holidays):
        self.sendUpdate('setHolidayIdList', holidays)

    def holidayNotify(self):
        self.sendUpdate('holidayNotify', [])

    def d_setWeeklyCalendarHolidays(self, weeklyHolidays):
        self.sendUpdate('setWeeklyCalendarHolidays', [weeklyHolidays])

    def getWeeklyCalendarHolidays(self):
        return self.weeklyHolidays

    def d_setYearlyCalendarHolidays(self, yearlyHolidays):
        self.sendUpdate('setYearlyCalendarHolidays', [yearlyHolidays])

    def getYearlyCalendarHolidays(self):
        return self.yearlyHolidays

    def setOncelyCalendarHolidays(self, oncelyHolidays):
        self.sendUpdate('setOncelyCalendarHolidays', [oncelyHolidays])

    def getOncelyCalendarHolidays(self):
        return self.oncelyHolidays

    def setRelativelyCalendarHolidays(self, relatHolidays):
        self.sendUpdate('setRelativelyCalendarHolidays', [relatHolidays])

    def getRelativelyCalendarHolidays(self):
        return []

    def setMultipleStartHolidays(self, multiHolidays):
        self.sendUpdate('setMultipleStartHolidays', [multiHolidays])

    def getMultipleStartHolidays(self):
        return []

    def sendSystemMessage(self, message, style):
        self.sendUpdate('sendSystemMessage', [message, style])
        
    def sendSystemMessageToAvatar(self, avatar, message, style):
        self.sendUpdateToAvatarId(avatar.getDoId(), 'sendSystemMessage', [message, style])

@magicWord(category=CATEGORY_PROGRAMMER, types=[int])
def startHoliday(holidayId):
    simbase.air.newsManager.setHolidayIdList([holidayId])
    return 'Successfully set holiday to %d.' % (holidayId)
    
@magicWord(category=CATEGORY_PROGRAMMER, types=[int])
def addHoliday(holidayId):
    simbase.air.newsManager.addHolidayId(holidayId)
    return 'Successfully added holiday %d to ongoing holidays!' % (holidayId)
    
@magicWord(category=CATEGORY_PROGRAMMER, types=[int])
def removeHoliday(holidayId):
    simbase.air.newsManager.removeHolidayId(holidayId)
    return 'Successfully removed holiday %d from ongoing holidays!' % (holidayId)
