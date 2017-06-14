from toontown.town import TTStreet

class TutorialStreet(TTStreet.TTStreet):

    def enter(self, requestStatus):
        TTStreet.TTStreet.enter(self, requestStatus, visibilityFlag=0, arrowsOn=0)
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setScale(0.8)
        self.sky.reparentTo(render)
        self.sky.setDepthTest(0)
        self.sky.setDepthWrite(0)
        self.sky.setBin('background', 100)
        self.sky.find('**/Sky').reparentTo(self.sky, -1)

    def exit(self):
        TTStreet.TTStreet.exit(self, visibilityFlag=0)
        self.sky.removeNode()
        del self.sky

    def enterTeleportIn(self, requestStatus):
        TTStreet.TTStreet.enterTeleportIn(self, requestStatus)

    def enterTownBattle(self, event):
        self.loader.townBattle.enter(event, self.fsm.getStateNamed('battle'), tutorialFlag=1)

    def handleEnterTunnel(self, requestStatus, collEntry):
        messenger.send('stopTutorial')
        TTStreet.TTStreet.handleEnterTunnel(self, requestStatus, collEntry)

    def exitDoorIn(self):
        base.localAvatar.obscureMoveFurnitureButton(-1)
