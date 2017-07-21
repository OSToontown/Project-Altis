from panda3d.core import *
from panda3d.direct import *
import ShtikerPage
import ShtikerBook
from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from panda3d.core import *
from panda3d.direct import *
from toontown.toonbase import TTLocalizer
import os
import string
from toontown.toonbase import ToontownGlobals
from sys import platform

class CertPage(ShtikerPage.ShtikerPage):

    notify = DirectNotifyGlobal.directNotify.newCategory('CertPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)
        self.certs = []
        self.selectedFileName = None
        self.selectedFilePath = None
        self.installPath = os.getcwd()
        self.certPath = TTLocalizer.ScreenshotPath
        self.certIndex = 0
        return

    def load(self):
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.CertPageTitle, text_scale=0.1, pos=(0, 0, 0.6))
        self.pictureImage = loader.loadModel('phase_3.5/models/gui/photo_frame')
        self.pictureImage.setScale(0.2)
        self.pictureImage.setPos(0.44, 0, 0.25)
        self.pictureImage.reparentTo(self)
        self.pictureFg = self.pictureImage.find('**/fg')
        self.pictureFg.setColor(1, 1, 1, 0.1)
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.scrollList = DirectScrolledList(parent=self, relief=None, forceHeight=0.07, pos=(-0.5, 0, 0), incButton_image=(gui.find('**/FndsLst_ScrollUp'),
         gui.find('**/FndsLst_ScrollDN'),
         gui.find('**/FndsLst_ScrollUp_Rllvr'),
         gui.find('**/FndsLst_ScrollUp')), incButton_relief=None, incButton_scale=(1.3, 1.3, -1.3), incButton_pos=(0.08, 0, -0.60), incButton_image3_color=Vec4(1, 1, 1, 0.2), decButton_image=(gui.find('**/FndsLst_ScrollUp'),
         gui.find('**/FndsLst_ScrollDN'),
         gui.find('**/FndsLst_ScrollUp_Rllvr'),
         gui.find('**/FndsLst_ScrollUp')), decButton_relief=None, decButton_scale=(1.3, 1.3, 1.3), decButton_pos=(0.08, 0, 0.52), decButton_image3_color=Vec4(1, 1, 1, 0.2), itemFrame_pos=(-0.237, 0, 0.41), itemFrame_scale=1.0, itemFrame_relief=DGG.SUNKEN, itemFrame_frameSize=(-0.05,
         0.66,
         -0.98,
         0.07), itemFrame_frameColor=(0.85, 0.95, 1, 1), itemFrame_borderWidth=(0.01, 0.01), numItemsVisible=13, items=[])
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.scroll = loader.loadModel('phase_3/models/gui/toon_council').find('**/scroll')
        self.scroll.reparentTo(self)
        self.scroll.setPos(0.0, 1.0, 0.2)
        self.scroll.setScale(0.6, 0.6, 0.6)
        self.tip = DirectLabel(parent=self.scroll, relief=None, text=TTLocalizer.CertPageInfo, text_scale=0.13, pos=(0.0, 0.0, 0.1), text_fg=(0.4, 0.3, 0.2, 1), text_wordwrap=18, text_align=TextNode.ACenter)
        gui.removeNode()
        buttons.removeNode()
        return

    def unload(self):
        del self.title
        del self.scrollList
        del self.pictureImage
        del self.pictureFg
        del self.scroll
        del self.tip
        ShtikerPage.ShtikerPage.unload(self)

    def makeCertButton(self, cert, index):
        return DirectButton(relief=None, text=cert, text_scale=0.06, text_align=TextNode.ALeft, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, command=self.choseCert, extraArgs=[index])

    def choseCert(self, cert):
        self.selectedFileName = None
        self.pictureFg.clearTexture()
        self.pictureFg.setColor(1, 1, 1, 0.1)

    def newScreenshot(self, filename):
        self.updateScrollList()

    def updateScrollList(self):
        newCerts = base.localAvatar.getCerts()
        self.scrollList.removeAllItems()
        self.certs = []
		
        i = 0		
        for cert in newCerts:
            if cert not in self.certs:
                certButton = self.makeCertButton(cert, i)
                self.scrollList.addItem(certButton)
                self.certs.append(certButton)
            i += 1

        if self.certs:
            self.choseCert(self.certs[0])
            self.scroll.hide()
            self.scrollList.show()
            self.pictureImage.show()
            self.scrollList.show()
        else:
            self.choseCert(None)
            self.scroll.show()
            self.scrollList.hide()
            self.pictureImage.hide()

    def enter(self):
        self.updateScrollList()
        chatEntry = base.localAvatar.chatMgr.chatInputNormal.chatEntry
        self.oldFocus = chatEntry['backgroundFocus']
        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        self.ignore('screenshot')
        ShtikerPage.ShtikerPage.exit(self)

    def updateArrows(self):
        self.certIndex = 0
        self.choseCert(self.getCerts()[self.certIndex])

    def prevCert(self):
        try:
            self.choseCert(self.getCerts()[self.certIndex])
            self.certIndex -= 1
        except:
            self.certIndex = 0

    def nextCert(self):
        try:
            self.choseCert(self.getCerts()[self.certIndex])
            self.certIndex += 1
        except:
            self.certIndex = 0
