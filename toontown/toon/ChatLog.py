from panda3d.core import *
from toontown.pgui.DirectGui import *
from toontown.pgui import DirectGuiGlobals
from direct.showbase.DirectObject import DirectObject
from otp.avatar import Avatar

class ChatLog(DirectFrame, DirectObject):
    def __init__(self):
        DirectFrame.__init__(self, relief = None, sortOrder = 500)
        DirectObject.__init__(self)
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        arrowGui = loader.loadModel('phase_9/models/gui/tt_m_gui_brd_arrow')
        hideImageList = (arrowGui.find('**/tt_t_gui_brd_arrow_up'), arrowGui.find('**/tt_t_gui_brd_arrow_down'), arrowGui.find('**/tt_t_gui_brd_arrow_hover'))

        self.toggleBtn = DirectButton(parent=base.a2dLeftCenter, relief=None, text = ('', 'Toggle Chat Log', 'Toggle Chat Log'), text_pos=(.2, 0), text_scale=0.06, text_align=TextNode.ALeft, text_fg=Vec4(0, 0, 0, 1), text_shadow=Vec4(1, 1, 1, 1), image=hideImageList, image_scale=(0.35, 1, 0.5), pos=(0.025, 0, 0.45), scale=1.05, command=self.toggle)

        self.log = DirectScrolledList(parent = self,
            decButton_pos= (0.45, 0, 0.65),
            decButton_image = (gui.find('**/FndsLst_ScrollUp'),
            gui.find('**/FndsLst_ScrollDN'),
            gui.find('**/FndsLst_ScrollUp_Rllvr'),
            gui.find('**/FndsLst_ScrollUp')),
            decButton_relief = None,
            
            incButton_pos= (0.45, 0, -0.1475),
            incButton_image = (gui.find('**/FndsLst_ScrollUp'),
            gui.find('**/FndsLst_ScrollDN'),
            gui.find('**/FndsLst_ScrollUp_Rllvr'),
            gui.find('**/FndsLst_ScrollUp')),
            incButton_relief = None,
            incButton_scale = (1.0, 1.0, -1.0),
            
            itemFrame_geom = (loader.loadModel("phase_3.5/models/gui/frame")),
            itemFrame_geom_scale = (.14, 1, .17),
            itemFrame_geom_pos = (0, 0, -.25),
            itemFrame_geom_color = (1,1,1,0.6),
            itemFrame_relief = None,
            
            items = [],
            numItemsVisible = 6,
            forceHeight = .1,
            itemFrame_frameSize = (-0.4, 0.5, -0.4, 0.16),
            itemFrame_pos = (0.45, 0, 0.5),
            )
        self.isHidden = True
        
        base.cr.chatLog = self
        
    def stop(self):
        self.log.destroy()
        self.toggleBtn.destroy()
        base.cr.chatLog = None
        
    def addToLog(self, msg, avId = 0):
        msg = msg.replace('\n', ' ')
        msgd = DirectButton(relief = None, text = msg, text_scale = 0.035, text_pos = (-.44, 0), text_style = 3, text_align = TextNode.ALeft, text_wordwrap = 25, text_shadow=(0, 0, 0, 1), command = self.buttonizeIt, extraArgs = [avId])
        self.log.addItem(msgd)
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
			
    def updateTransparency(self, transparency):
        self.log.itemFrame_geom_color[3] = transparency

    def buttonizeIt(self, avId):
        av = base.cr.doId2do.get(avId)
        if not av:
            return
        if str(avId)[:2] != "10":
            return
        av.clickedNametag()