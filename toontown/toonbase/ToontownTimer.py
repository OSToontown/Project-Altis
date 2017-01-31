from otp.otpbase.OTPTimer import OTPTimer
from pandac.PandaModules import *

class ToontownTimer(OTPTimer):

    def __init__(self, useImage = True, highlightNearEnd = True):
        OTPTimer.__init__(self, useImage, highlightNearEnd)
        self.initialiseoptions(ToontownTimer)

    def getImage(self):
        if ToontownTimer.ClockImage == None:
            model = loader.loadModel('phase_3.5/models/gui/clock_gui')
            ToontownTimer.ClockImage = model.find('**/alarm_clock')
            model.removeNode()
        
        return ToontownTimer.ClockImage
		
    def posAboveMapButton(self):
        self.reparentTo(base.a2dBottomRight)
        self.setPos(-0.173, 0, 0.65)