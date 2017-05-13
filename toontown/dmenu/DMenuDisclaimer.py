from direct.gui.DirectGui import OnscreenText, DirectButton
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from toontown.toonbase import ToontownGlobals

class DMenuDisclaimer(DirectObject):
    notify = directNotify.newCategory('DisclaimerScreen')
    
    def __init__(self):
        DirectObject.__init__(self)
        base.setBackgroundColor(0, 0, 0)
        disclaimerText = "Project Altis is a not-for-profit fanmade parody made under Fair Use. Project Altis is not affiliated with The Walt Disney Company and/or the Disney Interactive Media Group (collectively referred to as \"Disney\") by clicking I agree you hereby agree that you acknowledge this fact."
        self.disclaimer = OnscreenText(text = disclaimerText, font = ToontownGlobals.getMinnieFont(), style = 3, wordwrap = 30, scale = .08, pos = (0, .3, 0))
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam')
        yesUp = gui.find('**/tt_t_gui_mat_okUp')
        yesDown = gui.find('**/tt_t_gui_mat_okDown')
        noUp = gui.find('**/tt_t_gui_mat_closeUp')
        noDown = gui.find('**/tt_t_gui_mat_closeDown')
        
        self.accept = DirectButton(parent = aspect2d, relief = None, image = (yesUp, yesDown, yesUp), image_scale = (0.6, 0.6, 0.6), image1_scale = (0.7, 0.7, 0.7), image2_scale = (0.7, 0.7, 0.7), text = ('', 'I Agree', 'I Agree'), text_pos=(0, -0.175), text_style = 3, text_scale=0.08, pos = (.4, 0, -.5), command = self.accept)
        
        self.deny = DirectButton(parent = aspect2d, relief = None, image = (noUp, noDown, noUp), image_scale = (0.6, 0.6, 0.6), image1_scale = (0.7, 0.7, 0.7), image2_scale = (0.7, 0.7, 0.7), text = ('', 'I Disagree', 'I Disagree'), text_pos=(0, -0.175), text_style = 3, text_scale=0.08, pos = (-.4, 0, -.5), command = self.deny)
        
    def accept(self):
        self.disclaimer['text'] = 'Loading...'
        self.accept.destroy()
        self.deny.destroy()
        base.graphicsEngine.renderFrame()
        messenger.send("AgreeToGame")
        base.cr.hasAccepted = True
        self.disclaimer.removeNode()
        
    def deny(self):
        base.exitFunc()