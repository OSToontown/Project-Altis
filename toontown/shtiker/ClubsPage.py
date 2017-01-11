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
from direct.gui.OnscreenText import OnscreenText
from toontown.toontowngui import TTDialog

class ClubsPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.ClubsPageTitle, text_scale=0.1, pos=(0, 0, 0.65))
        self.buttonModel = 'phase_3/models/gui/quit_button.bam'

        self.noClubFound = OnscreenText(parent=self, text=TTLocalizer.ClubsNotFound, pos=(0, 0, 0), 
            scale=0.1, fg=(1, 0, 0, 1))
        
        self.joinWithCodeButton = DirectButton(parent = self, relief = None, text=TTLocalizer.ClubsJoinWithCode,
                                               image_scale=(0.7, 1, 1), text_scale=0.052, text_pos=(0, -0.02),
                                               image=(self.buttonModel.find('**/QuitBtn_UP'), self.buttonModel.find('**/QuitBtn_DN'), self.buttonModel.find('**/QuitBtn_RLVR')),
                                               command = CodeInputUI())

    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)

    def enter(self):
        base.cr.toonClubManager.requestStatus(self._toonClubStatusResp)

        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        
    def setAvatar(self, av):
        self.avatar = av

    def getAvatar(self):
        return self.avatar

    def _toonClubStatusResp(self, clubFound, clubDoId):
        if clubFound:
            # todo
            return

        self.noClubFound.show()
        
class CodeInputUI:

    def __init__(self):
        self.dialog = TTDialog.TTGlobalDialog(
            dialogName='ControlRemap', doneEvent='joinWithCode', style=TTDialog.TwoChoice,
            text=TTLocalizer.ClubsJoinWithCode, text_wordwrap=24,
            text_pos=(0, 0, -0.8), suppressKeys = True, suppressMouse = True
        )
        scale = self.dialog.component('image0').getScale()
        scale.setX(((scale[0] * 2.5) / base.getAspectRatio()) * 1.2)
        scale.setZ(scale[2] * 2.5)

        self.dialog.component('image0').setScale(scale)
        self.codeInput = DirectEntry(parent = self.dialog, initialText = TTLocalizer.ClubsCode, numLines = 1, focus = 1, width = 30)
        self.buttonModel = 'phase_3/models/gui/quit_button.bam'
        self.submitButton = DirectButton(parent = self.dialog, relief = None, text=TTLocalizer.ClubsSubmitCode,
                                               image_scale=(0.7, 1, 1), text_scale=0.052, text_pos=(0, -0.02),
                                               image=(self.buttonModel.find('**/QuitBtn_UP'), self.buttonModel.find('**/QuitBtn_DN'), self.buttonModel.find('**/QuitBtn_RLVR')),
                                               command = self.unload()) # TODO: Replace with function to submit the code and attempt to join club

    def unload(self):
        if self.dialog:
            self.dialog.cleanup()
            del self.dialog