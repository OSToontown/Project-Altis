from toontown.pgui.DirectGui import *
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.task import Task
from toontown.toontowngui import TTDialog
from toontown.fishing import FishGlobals
from direct.actor import Actor
from direct.interval.IntervalGlobal import *

class RodBuyGUI(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('FishGui')

    def __init__(self, doneEvent):
        DirectFrame.__init__(self, relief=None, state='normal', geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor, geom_scale=(2.0, 1, 1.5), frameSize=(-1, 1, -1, 1), pos=(0, 0, 0), text='', text_wordwrap=26, text_scale=0.06, text_pos=(0, 0.65))
        self.initialiseoptions(RodBuyGUI)
        self.doneEvent = doneEvent
        self.geom = None
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        okImageList = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        cancelImageList = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
        self.currRod = 0
        for rod in base.localAvatar.getFishingRods():
            if rod > self.currRod:
                self.currRod = rod
        self.cancelButton = DirectButton(parent=self, relief=None, image=cancelImageList, pos=(0, 0, -0.58), text=TTLocalizer.FishGuiCancel, text_scale=TTLocalizer.FSGUIcancelButton, text_pos=(0, -0.1), command=self.__cancel)
        if not self.currRod >= 4:
            self.rodButton = DirectButton(parent=self, relief=None, geom=DGG.getDefaultDialogGeom(), geom_scale=(0.5, 0.5, 0.75), pos=(-0.5, 0, 0), text=TTLocalizer.FishingJellybeanItem % ToontownGlobals.FishingRodCosts[self.currRod + 1], text_scale=TTLocalizer.FSGUIokButton, text_pos=(0, -0.3), command=self.promptBuyRod)
            rodPath = FishGlobals.RodFileDict.get(self.currRod + 1)
            if self.geom:
                self.geom.cleanup()
                self.geom.removeNode()
                self.geom = None
                if self.geomRotate:
                    self.geomRotate.finish()
            self.geom = Actor.Actor(rodPath, {'cast': 'phase_4/models/props/fishing-pole-chan'})
            self.geom.setHpr(90, 55, -90)
            self.geom.setPos(0, 0, 0)
            self.geom.setScale(.075)
            self.geomRotate = self.geom.hprInterval(4, Vec3(450, 55, -90)).loop()
            self.geom.reparentTo(self.rodButton)
            self.geom.pose('cast', 130)
        if not base.localAvatar.getMaxFishTank() == 100:
            gui = loader.loadModel('phase_4/models/gui/fishingGui')
            bucket = gui.find('**/bucket')
            bucket.setBin("gui-popup", 50)
            self.bucketButton = DirectButton(parent=self, relief=None, geom=DGG.getDefaultDialogGeom(), geom_scale=(0.5, 0.5, 0.75), pos=(0.5, 0, 0), image=bucket, image_scale=0.8, image_pos=(-0.9, 0, 1), text=TTLocalizer.FishingJellybeanItem % ToontownGlobals.BucketCosts.get(base.localAvatar.getMaxFishTank() + 10), text_scale=TTLocalizer.FSGUIokButton, text_pos=(0, -0.3), command=self.promptBuyBucket)
        buttons.removeNode()

    def destroy(self):
        DirectFrame.destroy(self)

    def __cancel(self):
        messenger.send(self.doneEvent, [0])
		
    def promptBuyRod(self):
        self.dialog = TTDialog.TTGlobalDialog(
            style=TTDialog.TwoChoice,
            text=TTLocalizer.FishRodBuy % {'type': TTLocalizer.FishingRodNameDict.get(self.currRod + 1), 'beans': ToontownGlobals.FishingRodCosts[self.currRod + 1]},
            text_wordwrap=18.5,
            text_scale=TTLocalizer.APBdialog,
            okButtonText=TTLocalizer.lOK,
            cancelButtonText=TTLocalizer.lCancel,
            doneEvent='IgnoreConfirm',
            command=self.__buyRod)
        DirectLabel(
            parent=self.dialog,
            relief=None,
            pos=(0, 0, 0.125),
            text=TTLocalizer.FishPurchase,
            textMayChange=0,
            text_scale=0.08)
        self.dialog.show()
		
    def promptBuyBucket(self):
        self.dialog = TTDialog.TTGlobalDialog(
            style=TTDialog.TwoChoice,
            text=TTLocalizer.FishBucketBuy % ToontownGlobals.BucketCosts.get(base.localAvatar.getMaxFishTank() + 10),
            text_wordwrap=18.5,
            text_scale=TTLocalizer.APBdialog,
            okButtonText=TTLocalizer.lOK,
            cancelButtonText=TTLocalizer.lCancel,
            doneEvent='IgnoreConfirm',
            command=self.__buyBucket)
        DirectLabel(
            parent=self.dialog,
            relief=None,
            pos=(0, 0, 0.125),
            text=TTLocalizer.FishPurchase,
            textMayChange=0,
            text_scale=0.08)
        self.dialog.show()

    def __buyRod(self, option):
        if option == -1:
            self.dialog.hide()
            return
        self.dialog.hide()
        messenger.send(self.doneEvent, [1])
		
    def __buyBucket(self, option):
        if option == -1:
            self.dialog.hide()
            return
        self.dialog.hide()
        messenger.send(self.doneEvent, [2])