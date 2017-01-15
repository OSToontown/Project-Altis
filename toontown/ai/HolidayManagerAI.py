from direct.directnotify import DirectNotifyGlobal 
from toontown.toonbase import ToontownGlobals

class HolidayManagerAI():
    notify = DirectNotifyGlobal.directNotify.newCategory('HolidayManagerAI')

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
            simbase.air.newsManager.b_setHolidayIdList(self.currentHolidays)
            
        self.notify.debug(str(self.currentHolidays))
        if self.isSillyMeterHolidayRunning():
            self.notify.info("Silly Meter is now running!")


    def isHolidayRunning(self, holidayId):
        if holidayId in self.currentHolidays:
            return True

    def isMoreXpHolidayRunning(self):
        if ToontownGlobals.MORE_XP_HOLIDAY in self.currentHolidays:
            self.xpMultiplier = 2
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
