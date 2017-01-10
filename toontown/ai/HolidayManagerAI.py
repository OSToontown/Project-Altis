from toontown.toonbase import ToontownGlobals

class HolidayManagerAI:

    def __init__(self, air):
        self.air = air
        self.currentHolidays = []
        self.xpMultiplier = 1
        self.setup()

    def setup(self):
        holidays = config.GetString('active-holidays','')
        if holidays != '':
            for holiday in holidays.split(","):
                holiday = int(holiday)
                self.currentHolidays.append(holiday)
            simbase.air.newsManager.setHolidayIdList(self.currentHolidays)

    def isHolidayRunning(self, holidayId):
        if holidayId in self.currentHolidays:
            return True

    def isMoreXpHolidayRunning(self):
        if ToontownGlobals.MORE_XP_HOLIDAY in self.currentHolidays:
            self.xpMultiplier = 2
            return True
        return False
        
    def isSillyMeterHolidayRunning(self):
        if ToontownGlobals.SILLYMETER_HOLIDAY in self.currentHolidays:
            if ToontownGlobals.SILLY_CHATTER_ONE in self.currentHolidays:
                 self.setSillyMeterPhase(0)
            elif ToontownGlobals.SILLY_CHATTER_TWO in self.currentHolidays:
                 self.setSillyMeterPhase(1)
            elif ToontownGlobals.SILLY_CHATTER_THREE in self.currentHolidays:
                 self.setSillyMeterPhase(2)
            elif ToontownGlobals.SILLY_CHATTER_FOUR in self.currentHolidays:
                 self.setSillyMeterPhase(3)
            elif ToontownGlobals.SILLY_CHATTER_FIVE in self.currentHolidays:
                 self.setSillyMeterPhase(4)
            else:
                 self.setSillyMeterPhase(-1)
                 return False
            return True
        return False
        
    def setSillyMeterPhase(self, phase):
        if not simbase.air.sillyMeterMgr:
            return
        
        simbase.air.sillyMeterMgr.setCheckedPhase(phase)

    def getXpMultiplier(self):
        return self.xpMultiplier
