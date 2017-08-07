from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toontowngui import TTDialog
from direct.gui.DirectGui import *

class DistributedPublicPetMgr(DistributedObject.DistributedObject):
    neverDisable = 1
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetMgr')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        cr.publicPetMgr = self
        self.buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.frame = None
        self.panel = None

    def clearResponsePanel(self, value = 0):
        if self.frame:
            self.frame.destroy()

        self.enableCallButton()

    def showResponsePanel(self, txt):
        self.frame = TTDialog.TTDialog(style=TTDialog.Acknowledge, text=txt, command=self.clearResponsePanel)
        self.frame.setPos(-1.01, 0.1, -0.27)
        self.frame.reparentTo(base.a2dTopRight)

    def enableCallButton(self):
        if self.panel:
            self.panel.callButton['state'] = DGG.ENABLED

    def disableCallButton(self):
        if self.panel:
            self.panel.callButton['state'] = DGG.DISABLED

    def requestAppearanceResp(self, resp):
        if resp == 1:
            self.showResponsePanel(TTLocalizer.PetRequestBadLocation)
        elif resp == 2:
            self.showResponsePanel(TTLocalizer.PetRequestAlreadyPresent)
        elif self.panel:
            self.panel.doClose()

    def requestAppearance(self, panel):
        if self.frame:
            self.frame.destroy()

        self.disableCallButton()
        self.sendUpdate('requestAppearance', [])

    def disable(self):
        self.clearResponsePanel()
        self.buttons.removeNode()
        DistributedObject.DistributedObject.disable(self)


