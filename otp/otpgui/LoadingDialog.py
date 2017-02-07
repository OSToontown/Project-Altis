from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
import string
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from panda3d.core import TransparencyAttrib, VBase3, TextNode
from direct.interval.IntervalGlobal import Wait, Func, Sequence, LerpColorScaleInterval, Parallel, LerpFunctionInterval

class LoadingDialog:

    def __init__(self):
        self.loadingGui = aspect2d.attachNewNode('loadingUI')
        self.loadingGui.reparentTo(aspect2d, 3000)
        self.loadingText = OnscreenText(text='Connecting...', align=TextNode.ACenter, scale=0.1, pos=(0, 0, 0))
        self.loadingCircle = OnscreenImage(image = 'phase_3/maps/dmenu/loading_circle.png')
        self.loadingCircle.setScale(0.1)
        self.loadingCircle.setTransparency(TransparencyAttrib.MAlpha)
        self.loadingCircle.reparentTo(base.a2dBottomRight)
        self.loadingCircle.setPos(-0.1, 0, 0.1)
        self.background = OnscreenImage(image = 'phase_3.5/maps/loading/toon.jpg', parent = aspect2d)
        self.background.setScale(2, 1, 1)
        
    def start(self, text='Connecting...'):
        self.loadingGui.reparentTo(aspect2d, 3000)
        self.background.reparentTo(aspect2d, 2999)
        self.loadingText['text'] = text
        self.loadingCircle.show()
        self.background.show()
        
        self.background.wrtReparentTo(self.loadingGui)
        self.loadingText.wrtReparentTo(self.loadingGui)
        self.loadingCircle.wrtReparentTo(self.loadingGui)
        
        self.Seq = Sequence(
            Func(self.loadingCircle.setHpr, VBase3(0, 0, 0)),
            self.loadingCircle.hprInterval(1, VBase3(0, 0, 360)))
        self.Seq.loop()
            
    def stop(self):
        if self.loadingGui:
            self.loadingGui.removeNode()
            self.loadingGui = None
            
        if self.Seq:
            self.Seq.finish()
            
        if self.loadingText:
            self.loadingText.destroy()
            self.loadingText = None
            
        if self.loadingCircle:
            self.loadingCircle.destroy()
            self.loadingCircle = None
            
        if self.background:
            self.background.destroy()
            self.background = None