from panda3d.core import *
from toontown.pgui.DirectGui import *
from toontown.pgui import DirectGuiGlobals
from direct.showbase.DirectObject import DirectObject

class ChatLog(DirectFrame, DirectObject):
    def __init__(self):
        DirectFrame.__init__(self, relief = None, sortOrder = 500)
        DirectObject.__init__(self)
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        arrowGui = loader.loadModel('phase_9/models/gui/tt_m_gui_brd_arrow')
        hideImageList = (arrowGui.find('**/tt_t_gui_brd_arrow_up'), arrowGui.find('**/tt_t_gui_brd_arrow_down'), arrowGui.find('**/tt_t_gui_brd_arrow_hover'))

        self.toggleBtn = DirectButton(parent=base.a2dLeftCenter, relief=None, text_pos=(0, 0.15), text_scale=0.06, text_align=TextNode.ALeft, text_fg=Vec4(0, 0, 0, 1), text_shadow=Vec4(1, 1, 1, 1), image=hideImageList, image_scale=(0.35, 1, 0.5), pos=(0.02, 0, 0.45), scale=1.05, command=self.toggle)

        self.log = DirectScrolledList(parent = self,
            decButton_pos= (0.35, 0, 0.53),
            decButton_image = (gui.find('**/FndsLst_ScrollUp'),
            gui.find('**/FndsLst_ScrollDN'),
            gui.find('**/FndsLst_ScrollUp_Rllvr'),
            gui.find('**/FndsLst_ScrollUp')),
            decButton_relief = None,
            
            incButton_pos= (0.35, 0, -0.025),
            incButton_image = (gui.find('**/FndsLst_ScrollUp'),
            gui.find('**/FndsLst_ScrollDN'),
            gui.find('**/FndsLst_ScrollUp_Rllvr'),
            gui.find('**/FndsLst_ScrollUp')),
            incButton_relief = None,
            incButton_scale = (1.0, 1.0, -1.0),
            
            itemFrame_geom = (loader.loadModel("phase_3.5/models/gui/frame")),
            itemFrame_geom_scale = .12,
            itemFrame_geom_pos = (0, 0, -.15),
            itemFrame_relief = None,
            
            items = [],
            numItemsVisible = 6,
            forceHeight = .062,
            itemFrame_frameSize = (-0.4, 0.4, -0.37, 0.11),
            itemFrame_pos = (0.35, 0, 0.4),
            )
        self.isHidden = True
        
        base.cr.chatLog = self
        
    def stop(self):
        self.log.destroy()
        self.toggleBtn.destroy()
        base.cr.chatLog = None
        
    def addToLog(self, msg):
        msg = DirectLabel(relief = None, text = msg, text_scale = 0.032, text_pos = (-.35, 0), text_style = 3, text_align = TextNode.ALeft, text_wordwrap = 20)
        self.log.addItem(msg)
        self.log.scrollTo(len(self.log['items']) - 1)
        
    def toggle(self):
        if self.isHidden:
            self.toggleBtn.scaleInterval(0.5, Vec3(-1, 1, 1), blendType = 'easeInOut').start()
            self.posInterval(0.5, Point3(0.12, 0, 0.2), blendType = 'easeInOut').start()
            self.isHidden = False
            base.setCellsActive([base.leftCells[0]], 0)
        else:
            self.toggleBtn.scaleInterval(0.5, Vec3(1, 1, 1), blendType = 'easeInOut').start()
            self.posInterval(0.5, Point3(-1, 0, 0.2), blendType = 'easeInOut').start()
            self.isHidden = True
            base.setCellsActive([base.leftCells[0]], 1)