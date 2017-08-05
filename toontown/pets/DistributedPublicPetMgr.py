from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from direct.gui.DirectGui import *

class DistributedPublicPetMgrAI(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetMgrAI')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.cr.publicPetMgr = self
        self.buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.frame = None

    def showResponsePanel(self, txt):
        def handleOk():
            self.frame.destroy()

        self.frame = DirectFrame(pos=(-1.01, 0.1, -0.35), parent=base.a2dTopRight,
                            image_color=ToontownGlobals.GlobalDialogColor, image_scale=(1.0, 1.0, 0.6), text=txt,
                            text_wordwrap=13.5, text_scale=0.06, text_pos=(0.0, 0.18))

        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.bOk = DirectButton(self.frame, image=(
            buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')),
                                relief=None, text=TTLocalizer.TeleportPanelOK, text_scale=0.05,
                                text_pos=(0.0, -0.1), pos=(0.0, 0.0, -0.1), command=handleOk)

        buttons.removeNode()

    def requestAppearanceResp(self, resp):
        if resp == 1:
            self.showResponsePanel(TTLocalizer.PetRequestBadLocation)
        elif resp == 2:
            self.showResponsePanel(TTLocalizer.PetRequestAlreadyPresent)

    def requestAppearance(self):
        if self.frame:
            self.frame.destroy()

        self.sendUpdate('requestAppearance', [])

    def disable(self):
        self.buttons.removeNode()
        DistributedObject.DistributedObject.disable(self)


