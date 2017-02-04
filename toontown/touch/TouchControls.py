from panda3d.core import *
from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals
from direct.showbase.DirectObject import DirectObject

class TouchControls(DirectFrame, DirectObject):

    def __init__(self):
        DirectFrame.__init__(self, relief = None, sortOrder = 5000)
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam')
        shuffleUp = gui.find('**/tt_t_gui_mat_shuffleUp')
        shuffleDown = gui.find('**/tt_t_gui_mat_shuffleDown')
        self.upButton = DirectButton(parent = self, relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (.5, 0.7, 0.9), image1_scale = (0.5, 0.7, 0.9), image2_scale = (0.5, 0.7, 0.9), text_fg = (1, 1, 1, 1), text = "^", text_pos = (0, -0.02), text_scale = .07, scale = 1.2)
        self.downButton = DirectButton(parent = self, relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (.5, 0.7, 0.9), image1_scale = (0.5, 0.7, 0.9), image2_scale = (0.5, 0.7, 0.9), text_fg = (1, 1, 1, 1), text = "\/", text_pos = (0, -0.02), text_scale = .07, scale = 1.2)
        self.leftButton = DirectButton(parent = self, relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (.5, 0.7, 0.9), image1_scale = (0.5, 0.7, 0.9), image2_scale = (0.5, 0.7, 0.9), text_fg = (1, 1, 1, 1), text = "<", text_pos = (0, -0.02), text_scale = .07, scale = 1.2)
        self.rightButton = DirectButton(parent = self, relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (.5, 0.7, 0.9), image1_scale = (0.5, 0.7, 0.9), image2_scale = (0.5, 0.7, 0.9), text_fg = (1, 1, 1, 1), text = ">", text_pos = (0, -0.02), text_scale = .07, scale = 1.2)
        self.jumpButton = DirectButton(parent = self, relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (.5, 0.7, 0.9), image1_scale = (0.5, 0.7, 0.9), image2_scale = (0.5, 0.7, 0.9), text_fg = (1, 1, 1, 1), text = "o", text_pos = (0, -0.02), text_scale = .07, scale = 1.2)
            
        self.upButton.setPos(0, 0, .3)
        self.downButton.setPos(0, 0, -.3)
        self.leftButton.setPos(-.3, 0, 0)
        self.rightButton.setPos(.3, 0, 0)
        self.jumpButton.setPos(0, 0, 0)
            
        self.upButton.bind(DirectGuiGlobals.B1PRESS, self.upClicked)
        self.upButton.bind(DirectGuiGlobals.B1RELEASE, self.upReleased)            
        self.upButton.bind(DirectGuiGlobals.B3PRESS, self.upClicked)
        self.upButton.bind(DirectGuiGlobals.B3RELEASE, self.upReleased)
        
        self.downButton.bind(DirectGuiGlobals.B1PRESS, self.downClicked)
        self.downButton.bind(DirectGuiGlobals.B1RELEASE, self.downReleased)        
        self.downButton.bind(DirectGuiGlobals.B3PRESS, self.downClicked)
        self.downButton.bind(DirectGuiGlobals.B3RELEASE, self.downReleased)
        
        self.leftButton.bind(DirectGuiGlobals.B1PRESS, self.leftClicked)
        self.leftButton.bind(DirectGuiGlobals.B1RELEASE, self.leftReleased)        
        self.leftButton.bind(DirectGuiGlobals.B3PRESS, self.leftClicked)
        self.leftButton.bind(DirectGuiGlobals.B3RELEASE, self.leftReleased)
        
        self.rightButton.bind(DirectGuiGlobals.B1PRESS, self.rightClicked)
        self.rightButton.bind(DirectGuiGlobals.B1RELEASE, self.rightReleased)               
        self.rightButton.bind(DirectGuiGlobals.B3PRESS, self.rightClicked)
        self.rightButton.bind(DirectGuiGlobals.B3RELEASE, self.rightReleased)        
        
        self.jumpButton.bind(DirectGuiGlobals.B1PRESS, self.jumpClicked)
        self.jumpButton.bind(DirectGuiGlobals.B1RELEASE, self.jumpReleased)        
        self.jumpButton.bind(DirectGuiGlobals.B3PRESS, self.jumpClicked)
        self.jumpButton.bind(DirectGuiGlobals.B3RELEASE, self.jumpReleased)

    def start(self):
        self.upButton.show()
        self.downButton.show()
        self.leftButton.show()
        self.rightButton.show()
        self.jumpButton.show()
            
    def stop(self):
        self.upButton.hide()
        self.downButton.hide()
        self.leftButton.hide()
        self.rightButton.hide()
        self.jumpButton.hide()
            
    def destroy(self):
        self.upButton.destroy()
        self.downButton.destroy()
        self.leftButton.destroy()
        self.rightButton.destroy()
        self.jumpButton.destroy()
        DirectFrame.destroy(self)
            
    def upClicked(self, mouseEvent):
        messenger.send(base.MOVE_UP)
        
    def upReleased(self, mouseEvent):
        messenger.send(base.MOVE_UP + "-up")
                    
                    
    def downClicked(self, mouseEvent):
        messenger.send(base.MOVE_DOWN)
        
    def downReleased(self, mouseEvent):
        messenger.send(base.MOVE_DOWN + "-up")
                    
                    
    def leftClicked(self, mouseEvent):
        messenger.send(base.MOVE_LEFT)
        
    def leftReleased(self, mouseEvent):
        messenger.send(base.MOVE_LEFT + "-up")
                    
                    
    def rightClicked(self, mouseEvent):
        messenger.send(base.MOVE_RIGHT)
        
    def rightReleased(self, mouseEvent):
        messenger.send(base.MOVE_RIGHT + "-up")                    
                    
                    
    def jumpClicked(self, mouseEvent):
        messenger.send(base.JUMP)
        
    def jumpReleased(self, mouseEvent):
        messenger.send(base.JUMP + "-up")
        
        