'''
Created on Jan 10, 2017

@author: Drew
'''
from panda3d.core import *
from toontown.shtiker import ShtikerPage
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from toontown.toontowngui import TTDialog
from toontown.shtiker.OptionsPageGUI import *
from toontown.quest.QuestBookPoster import TEXT_WORDWRAP

class ClubsPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.inputUi = CodeInputUI()

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = OptionLabel(parent=self, relief=None, text_align = TextNode.ACenter, text=TTLocalizer.ClubsPageTitle, text_scale=0.1, pos=(0, 0, 0.65))
        self.buttonModel = 'phase_3/models/gui/quit_button.bam'

        self.noClubFound = OnscreenText(parent=self, text=TTLocalizer.ClubsNotFound, pos=(0, 0, 0), 
            scale=0.06, fg=(1, 0, 0, 1))
        
        self.joinWithCodeButton = OptionButton(parent = self, relief = None, text=TTLocalizer.ClubsJoinWithCode, text_wordwrap = 6, text_scale = 0.048, text_pos = (0, 0.01), command = self.showCodeInput)

    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)
        if self.title:
            self.title.removeNode()
            self.noClubFound.removeNode()
            self.joinWithCodeButton.removeNode()
            self.inputUi.unload()

    def enter(self):
        base.cr.toonClubManager.requestStatus(self._toonClubStatusResp)

        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        
    def setAvatar(self, av):
        self.avatar = av

    def getAvatar(self):
        return self.avatar
    
    def showCodeInput(self):
        self.inputUi.load()

    def _toonClubStatusResp(self, clubFound, clubDoId):
        if clubFound:
            # todo
            return

        self.noClubFound.show()
        
class CodeInputUI:

    def __init__(self):
        self.dialog = None
        self.codeInput = None
        
    def load(self):
        self.dialog = TTDialog.TTGlobalDialog(
            dialogName='ControlRemap', doneEvent='joinWithCode', style=TTDialog.TwoChoice,
                text=TTLocalizer.ClubsJoinWithCode, text_wordwrap=24, okButtonText = TTLocalizer.ClubsSubmitCode,
                text_pos=(0, 0, 0.5), suppressKeys = True, suppressMouse = True
            )
        scale = self.dialog.component('image0').getScale()
        scale.setX(((scale[0] * 2.5) / base.getAspectRatio()) * 1.2)
        scale.setZ(scale[2] * 2)
        nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        self.dialog.component('image0').setScale(scale)
        self.codeInputLabel = OptionLabel(parent = self.dialog, text=TTLocalizer.ClubsCode, text_align = TextNode.ACenter, pos=(0.0, 0.0, 0.2))
        self.codeInput = DirectEntry(parent = self.dialog, relief=None, image = nameBalloon, image1_color = (0.8, 0.8, 0.8, 1.0), scale = 0.064, pos = (-.3, 0, 0), numLines = 1, focus = 1, cursorKeys = 1, width = 9.1)
        self.codeInput.setScale(0.07)
        
        self.dialog.accept('joinWithCode', self.submitCode)
        
    def submitCode(self):
        code = self.codeInput.get()
        if self.dialog.doneStatus == "ok":
            print("Submitting code: " + code)
        self.unload()    
    
    def unload(self):
        if self.dialog:
            self.dialog.cleanup()
            del self.dialog