from direct.fsm import ClassicFSM, State
from toontown.toonbase.ToontownGlobals import OptionsPageHotkey
from toontown.toontowngui import TTDialog

class FeatureComingSoonDialog:

    def __init__(self, text = "Woah! That feature will be enabled in \n\1textShadow\1beta\2! Sorry about that!"):
        self.dialog = TTDialog.TTGlobalDialog(
            dialogName='ControlRemap', doneEvent='exitDialog', style=TTDialog.Acknowledge,
            text=text, text_wordwrap=24,
            text_pos=(0, 0, -0.8), suppressKeys = True, suppressMouse = True
        )
        self.dialog.accept('exitDialog', self.exitDialog)
        base.transitions.fadeScreen(.5)
        
    def exitDialog(self):
        base.transitions.noFade()
        self.dialog.cleanup()
        del self.dialog