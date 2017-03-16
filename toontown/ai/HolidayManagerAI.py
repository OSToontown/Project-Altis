from direct.directnotify import DirectNotifyGlobal 
from toontown.toonbase import ToontownGlobals
from datetime import datetime
from HolidayGlobals import *
from direct.showbase.DirectObject import DirectObject

class HolidayManagerAI(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('HolidayManagerAI')

    def __init__(self, air):
        DirectObject.__init__(self)
        self.air = air
        self.currentHolidays = []
        self.xpMultiplier = 3 # for the rest of alpha if 5x isnt enabled
        self.setup()
        self.checkForHoliday('checkForHoliday')

    def setup(self):
        holidays = config.GetString('active-holidays', '')
        if holidays != '':
            for holiday in holidays.split(","):
                holiday = int(holiday)
                self.currentHolidays.append(holiday)
            simbase.air.newsManager.d_setHolidayIdList([self.currentHolidays])
            
        self.notify.debug(str(self.currentHolidays))
        if self.isSillyMeterHolidayRunning():
            self.notify.info("Silly Meter is now running!")


    def isHolidayRunning(self, holidayId):
        if holidayId in self.currentHolidays:
            return True

    def isMoreXpHolidayRunning(self):
        if ToontownGlobals.MORE_XP_HOLIDAY in self.currentHolidays:
            self.xpMultiplier = 5
            return True
        return False
        
    def isSillyMeterHolidayRunning(self):
        if ToontownGlobals.SILLYMETER_HOLIDAY in self.currentHolidays or ToontownGlobals.SILLYMETER_EXT_HOLIDAY in self.currentHolidays:
            if ToontownGlobals.SILLY_METER_GENERAL_PHASE_ZERO in self.currentHolidays:
                 self.setSillyMeterPhase(0)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_ONE in self.currentHolidays:
                 self.setSillyMeterPhase(1)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_TWO in self.currentHolidays:
                 self.setSillyMeterPhase(2)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_THREE in self.currentHolidays:
                 self.setSillyMeterPhase(3)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_FOUR in self.currentHolidays:
                 self.setSillyMeterPhase(4)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_FIVE in self.currentHolidays:
                 self.setSillyMeterPhase(5)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_SIX in self.currentHolidays:
                 self.setSillyMeterPhase(6)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_SEVEN in self.currentHolidays:
                 self.setSillyMeterPhase(7)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_EIGHT in self.currentHolidays:
                 self.setSillyMeterPhase(8)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_NINE in self.currentHolidays:
                 self.setSillyMeterPhase(9)  
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_TEN in self.currentHolidays:
                 self.setSillyMeterPhase(10)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_ELEVEN in self.currentHolidays:
                 self.setSillyMeterPhase(11)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_TWELVE in self.currentHolidays:
                 self.setSillyMeterPhase(12)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_THRITEEN in self.currentHolidays: 
                 self.setSillyMeterPhase(13)
            elif ToontownGlobals.SILLY_METER_GENERAL_PHASE_FOURTEEN in self.currentHolidays:
                 self.setSillyMeterPhase(14)
            else:
                 self.setSillyMeterPhase(-1)
                 return False
            return True
        return False
        
    def setSillyMeterPhase(self, phase):
        if not simbase.air.sillyMeterMgr:
            self.notify.warning("No Silly Meter Mgr to set phase with!")
            return
        
        simbase.air.sillyMeterMgr.setCheckedPhase(phase)

    def getXpMultiplier(self):
        return self.xpMultiplier
        
    def addHoliday(self, holidayId):
        if holidayId not in self.currentHolidays:
            self.currentHolidays.append(holidayId)
        simbase.air.newsManager.d_setHolidayIdList([self.currentHolidays])
        
    def startHoliday(self, holidayId):
        if holidayId == ToontownGlobals.MORE_XP_HOLIDAY:
            self.air.newsManager.setMoreXpHolidayStart()
        if holidayId == ToontownGlobals.TROLLEY_HOLIDAY:
            simbase.air.trolleyHolidayMgr.start()
        if holidayId == ToontownGlobals.IDES_OF_MARCH:
            messenger.send('startIdes')
    
    def removeHoliday(self, holidayId):
        if self.holidayId in self.currentHolidays:
            self.currentHolidays.remove(holidayId)
        if holidayId == ToontownGlobals.IDES_OF_MARCH:
            messenger.send('endIdes')
        simbase.air.newsManager.d_setHolidayIdList([self.currentHolidays])
        
    def endHoliday(self, holidayId):
        if holidayId == ToontownGlobals.MORE_XP_HOLIDAY:
            self.xpMultiplier = 3 # for the rest of alpha if 5x isnt enabled
            self.air.newsManager.setMoreXpHolidayEnd()
        if holidayId == ToontownGlobals.TROLLEY_HOLIDAY:
            simbase.air.trolleyHolidayMgr.stop()

    def checkForHoliday(self, task):
        for holiday in WEEKLY_HOLIDAYS:
            holidayId = holiday[0]
            day = holiday[1]
            now = datetime.now()
            if now.weekday == day and holidayId not in self.currentHolidays:
                self.addHoliday(holidayId)
                self.startHoliday(holidayId)
            elif now.weekday != day and holidayId in self.currentHolidays:
                self.removeHoliday(holidayId)
                self.endHoliday(holidayId)
        for holiday in YEARLY_HOLIDAYS:
            holidayId = holiday[0]
            now = datetime.now()
            start = datetime(now.year, *holiday[1])
            end = datetime(now.year, *holiday[2])
            if start < now < end and holidayId not in self.currentHolidays:
                self.addHoliday(holidayId)
                self.startHoliday(holidayId)
            elif end < now and holidayId in self.currentHolidays:
                self.removeHoliday(holidayId)
                self.endHoliday(holidayId)
        for holiday in ONCELY_HOLIDAYS:
            holidayId = holiday[0]
            now = datetime.now()
            start = datetime(*holiday[1])
            end = datetime(*holiday[2])
            if start < now < end and holidayId not in self.currentHolidays:
                self.addHoliday(holidayId)
                self.startHoliday(holidayId)
            elif end < now and holidayId in self.currentHolidays:
                self.removeHoliday(holidayId)
                self.endHoliday(holidayId)
        taskMgr.doMethodLater(4000, self.checkForHoliday, 'holidaycheck')

    def getCurPhase(self, holidayId):
        return 1 #TODO: Get Phase for Actual Holiday.
