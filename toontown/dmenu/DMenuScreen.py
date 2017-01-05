# DMENU VERSION 0.7

DMENU_GAME = 'Toontown'

from direct.gui.DirectGui import OnscreenImage, DirectButton
from panda3d.core import TransparencyAttrib, Point3, VBase3, Vec4
from direct.interval.IntervalGlobal import Wait, Func, Sequence, LerpColorScaleInterval, Parallel, LerpFunctionInterval, ActorInterval
from direct.showbase.DirectObject import DirectObject
from toontown.pickatoon import PickAToonOptions, PickAToon
from DMenuGlobals import *
from DMenuLocalizer import *
from DMenuResources import *
from direct.actor import Actor
from direct.showbase import Audio3DManager
import random

if DMENU_GAME == 'Toontown':
# TT
    from toontown.toontowngui.TTGui import btnDn, btnRlvr, btnUp
    from toontown.toonbase import TTLocalizer
    from toontown.hood import SkyUtil
    from toontown.toon import Toon, ToonDNA
    from otp.nametag.NametagConstants import *
    from otp.nametag.NametagGroup import *
    from otp.nametag.NametagGlobals import *

# The camera's initial position when first entering main menu
INIT_POS = (-62, 0, 11)
INIT_HPR = (-90, -2, 0)

# The main position
MAIN_POS = (-60, 0, 11)
MAIN_HPR = (-90, -2, 0)

# To be used when entering PAT
TOON_HALL_POS = (110, 0, 8)
TOON_HALL_HPR = (-90, 0, 0)

# To be used when going to menu
HQ_POS = (14, 16, 8)
HQ_HPR = (-48, 0, 0)

class DMenuScreen(DirectObject):
    notify = directNotify.newCategory('DMenuScreen')

    def __init__(self):
        DirectObject.__init__(self)
        base.cr.DMENU_SCREEN = self
        self.seq = None
        self.isSeqPlaying = False # .isPlaying() doesnt want to work
        if DMENU_GAME == 'Toontown':
            base.cr.avChoice = None
        fadeSequence = Sequence(
            Func(base.transitions.fadeOut, .001),
            Wait(.5),
            Func(base.transitions.fadeIn, .5),
            base.camera.posHprInterval(1, Point3(MAIN_POS), VBase3(MAIN_HPR), blendType = 'easeInOut')).start()
        if DMENU_GAME == 'Toontown':
            self.background = loader.loadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall')
            self.background.reparentTo(render)
            self.background.setPosHpr(-25, 0, 8.1, -95, 0, 0)
            ropes = loader.loadModel('phase_4/models/modules/tt_m_ara_int_ropes')
            ropes.reparentTo(self.background)
            self.sillyMeter = Actor.Actor('phase_4/models/props/tt_a_ara_ttc_sillyMeter_default', {'arrowTube': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_arrowFluid',
             'phaseOne': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseOne',
             'phaseTwo': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseTwo',
             'phaseThree': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseThree',
             'phaseFour': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFour',
             'phaseFourToFive': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFourToFive',
             'phaseFive': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFive'})
            self.sillyMeter.reparentTo(self.background)
            self.sillyMeter.makeSubpart('arrow', ['uvj_progressBar*', 'def_springA'])
            self.sillyMeter.makeSubpart('meter', ['def_pivot'], ['uvj_progressBar*', 'def_springA'])
            self.audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)

            self.phase3Sfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseThree.ogg')
            self.phase3Sfx.setLoop(True)
            self.arrowSfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterArrow.ogg')
            self.arrowSfx.setLoop(False)
            self.phase3Sfx.setVolume(0.2)
            self.arrowSfx.setVolume(0.2)
            
            self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=236, endFrame=247), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=247, endFrame=276), Sequence(Func(self.phase3Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase3Sfx, self.sillyMeter))))
            self.animSeq.start()
            self.smPhase2 = self.sillyMeter.find('**/stage2')
            self.smPhase2.show()
            self.sillyMeter.loop('phaseOne', partName='meter')
            self.sillyMeter.setBlend(frameBlend = True)
            
            self.surlee = Toon.Toon()
            self.surlee.setName('Doctor Surlee')
            self.surlee.setPickable(0)
            self.surlee.setPlayerType(CCNonPlayer)
            dna = ToonDNA.ToonDNA()
            dna.newToonFromProperties('pls', 'ls', 'l', 'm', 9, 0, 9, 9, 98, 27, 86, 27, 38, 27)
            self.surlee.setDNA(dna)
            self.surlee.loop('scientistGame')
            self.surlee.reparentTo(self.background)
            self.surlee.setPosHpr(13, 24, 0.025, -180, 0, 0)
            
            self.dimm = Toon.Toon()
            self.dimm.setName('Doctor Dimm')
            self.dimm.setPickable(0)
            self.dimm.setPlayerType(CCNonPlayer)
            dna = ToonDNA.ToonDNA()
            dna.newToonFromProperties('fll', 'ss', 's', 'm', 15, 0, 15, 15, 99, 27, 86, 27, 39, 27)
            self.dimm.setDNA(dna)
            self.dimm.loop('scientistGame')
            self.dimm.reparentTo(self.background)
            self.dimm.setPosHpr(16, 24, 0.025, -180, 0, 0)
            
            surleeHand = self.surlee.find('**/def_joint_right_hold')
            clipBoard = loader.loadModel('phase_4/models/props/tt_m_prp_acs_clipboard')
            surleeHandNode = surleeHand.attachNewNode('ClipBoard')
            clipBoard.instanceTo(surleeHandNode)
            surleeHandNode.setH(180)
            surleeHandNode.setScale(render, 1.0)
            surleeHandNode.setPos(0, 0, 0.1)
            
            dimmHand = self.dimm.find('**/def_joint_right_hold')
            sillyReader = loader.loadModel('phase_4/models/props/tt_m_prp_acs_sillyReader')
            dimHandNode = dimmHand.attachNewNode('SillyReader')
            sillyReader.instanceTo(dimHandNode)
            dimHandNode.setH(180)
            dimHandNode.setScale(render, 1.0)
            dimHandNode.setPos(0, 0, 0.1)
            
            self.banana = self.background.find('**/gagBanana')
            
            self.bananaClicker = CollisionTraverser()
            #self.bananaClicker.showCollisions(render)
            self.collHandlerQueue = CollisionHandlerQueue()
            
            self.bananaRayNode = CollisionNode('bananaMouseRay')
            self.bananaRayNP = base.camera.attachNewNode(self.bananaRayNode)
            self.bananaRayNode.setIntoCollideMask(BitMask32.bit(0))
            self.bananaRayNode.setFromCollideMask(BitMask32.bit(1))
            self.banana.setCollideMask(BitMask32.bit(1))
            self.ray = CollisionRay()
            self.bananaRayNode.addSolid(self.ray)
            self.bananaClicker.addCollider(self.bananaRayNP, self.collHandlerQueue)
            self.accept("mouse1", self.slipAndSlideOnThisBananaPeelHaHaHa)
           
            
            for frame in render.findAllMatches('*/doorFrame*'):
                frame.removeNode()
            self.sky = loader.loadModel('phase_3.5/models/props/TT_sky')
            SkyUtil.startCloudSky(self)
            base.camera.setPosHpr(MAIN_POS, MAIN_HPR)


        self.logo = OnscreenImage(image = GameLogo, scale = (.5, .5, .25))
        self.logo.reparentTo(aspect2d)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        self.logo.setPos(0, 0, .5)
        self.logo.setColorScale(Vec4(0, 0, 0, 0))
        fadeInLogo = (LerpColorScaleInterval(self.logo, 1, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0))).start()

        self.createButtons()

        self.fadeOut = None
        self.optionsMgr = PickAToonOptions.NewPickAToonOptions()
        #self.quitConfirmation = DMenuQuit()
        self.patNode = None
        
        if DMENU_GAME == 'Toontown':
            # TT: We need these to run the Pick A Toon screen
            self.patAvList = base.cr.PAT_AVLIST
            self.patFSM = base.cr.PAT_LOGINFSM
            self.patDoneEvent = base.cr.PAT_DONEEVENT
            
    def slipAndSlideOnThisBananaPeelHaHaHa(self):
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()

            def setPlayingStatus(status):
                self.isSeqPlaying = status
            
            self.ray.setFromLens(base.camNode, mpos.getX(), mpos.getY())
            self.bananaClicker.traverse(render)

            if self.collHandlerQueue.getNumEntries() > 0:
                self.collHandlerQueue.sortEntries()
                pickedObj = self.collHandlerQueue.getEntry(0).getIntoNodePath()
                surleeAnim = random.choice(['slip-backward', 'slip-forward'])
                dimmAnim = random.choice(['slip-backward', 'slip-forward'])
                if pickedObj == self.banana:
                    self.seq = Sequence(
                        Func(setPlayingStatus, True),
                        Func(self.surlee.play, surleeAnim),
                        Func(self.dimm.play, dimmAnim),
                        Wait(3),
                        Func(self.surlee.loop, 'scientistGame'),
                        Func(self.dimm.loop, 'scientistGame'),
                        Func(setPlayingStatus, False)
                    )
                    if not self.isSeqPlaying:
                        self.seq.start()

    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    def createButtons(self):
        buttonImage = GuiModel.find('**/QuitBtn_RLVR')

        self.PlayButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = PlayGame, text_scale = .1, scale = 0.95, command = self.playGame)
        self.PlayButton.reparentTo(aspect2d)
        self.PlayButton.setPos(PlayBtnHidePos)
        self.PlayButton.show()

        self.OptionsButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = Options, text_scale = .1, scale = 0.95, command = self.openOptions)
        self.OptionsButton.reparentTo(aspect2d)
        self.OptionsButton.setPos(OptionsBtnHidePos)
        self.OptionsButton.show()

        self.QuitButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = Quit, text_scale = .1, scale = 0.95, command = self.quitGame)
        self.QuitButton.reparentTo(aspect2d)
        self.QuitButton.setPos(QuitBtnHidePos)
        self.QuitButton.show()


        # self.BRButton = DirectButton(text = 'REPORT BUG', text_scale = .1, scale=0.95)
        # self.BRButton.reparentTo(aspect2d)
        # self.BRButton.setPos(-.9, 0, -.9)
        # self.BRButton.show()
        
        self.buttonInAnimation()

    def murder(self):
        if self.logo is not None:
            self.logo.destroy()
            self.logo = None

        if self.background is not None:
            self.background.hide()
            self.background.reparentTo(hidden)
            self.background.removeNode()
            self.background = None

        if self.PlayButton is not None:
            self.PlayButton.destroy()
            self.PlayButton = None

        if self.OptionsButton is not None:
            self.OptionsButton.destroy()
            self.OptionsButton = None

        if self.QuitButton is not None:
            self.QuitButton.destroy()
            self.QuitButton = None
            
        if self.phase3Sfx:
            self.phase3Sfx.stop()
            del self.phase3Sfx
            
        if self.surlee:
            self.surlee.delete()
        if self.dimm:
            self.dimm.delete()
            
            
        del self.bananaRayNode
        del self.bananaRayNP
        del self.bananaClicker
        del self.collHandlerQueue
        del self.ray
        
        self.ignoreAll()
        
        taskMgr.remove('skyTrack')
        self.sky.reparentTo(hidden)

    def openOptions(self):
        self.optionsMgr.showOptions()
        self.closeOptionsButton = DirectButton(relief = None, image = (btnUp, btnDn, btnRlvr), text = "Back", text_fg = (0, 0, 0, 1), text_scale = TTLocalizer.AClogoutButton, text_pos = (0, -0.035), image_scale = 1, image1_scale = 1.05, image2_scale = 1.05, scale = 0.7, command = self.hideOptions)
        self.closeOptionsButton.reparentTo(base.a2dTopLeft)
        self.closeOptionsButton.setPos(0.5, 0, -0.07)
        Parallel(
            self.PlayButton.posInterval(.5, Point3(PlayBtnHidePos), blendType = 'easeInOut'),
            self.OptionsButton.posInterval(.5, Point3(OptionsBtnHidePos), blendType = 'easeInOut'),
            self.QuitButton.posInterval(.5, Point3(QuitBtnHidePos), blendType = 'easeInOut'),
            self.logo.posInterval(0.5, Point3(0, 0, 2.5), blendType = 'easeInOut')).start()

    def hideOptions(self):
        self.optionsMgr.hideOptions()
        self.closeOptionsButton.hide()
        self.buttonInAnimation()

    def playGame(self):
        if self.fadeOut is not None:
            self.fadeOut.finish()
            self.fadeOut = None
        self.fadeOut = base.transitions.getFadeOutIval(t = 1)
        #base.camera.posHprInterval(1, Point3(TOON_HALL_POS), VBase3(TOON_HALL_HPR), blendType = 'easeInOut').start()
        Sequence(
            Func(self.doPlayButton),
            Wait(1),
            #Func(self.murder),
            Func(self.enterGame)).start()
            #Func(base.transitions.fadeIn, 1)).start()

    def enterOptions(self):
        pass

    def enterGame(self):
        base.cr.avChoice = PickAToon.PickAToon(self.patAvList, self.patFSM, self.patDoneEvent)
        base.cr.avChoice.load()
        base.cr.avChoice.enter()

    def doPlayButton(self):
        Parallel(
            self.PlayButton.posInterval(1, Point3(PlayBtnHidePos), blendType = 'easeInOut'),
            self.OptionsButton.posInterval(1, Point3(OptionsBtnHidePos), blendType = 'easeInOut'),
            self.QuitButton.posInterval(1, Point3(QuitBtnHidePos), blendType = 'easeInOut'),
            self.logo.posInterval(0.5, Point3(0, 0, 2.5), blendType = 'easeInOut')).start()

    def quitGame(self):
        self.showQuitConfirmation()

    def showQuitConfirmation(self):
        #self.quitConfirmation.showConfirmation()
        base.exitFunc()

    def buttonInAnimation(self):
        logo = self.logo.posInterval(.5, Point3(0, 0, .5), blendType = 'easeInOut')
        play = self.PlayButton.posInterval(.5, Point3(PlayBtnPos), blendType = 'easeInOut')
        opt = self.OptionsButton.posInterval(.5, Point3(OptionsBtnPos), blendType = 'easeInOut')
        quit = self.QuitButton.posInterval(.5, Point3(QuitBtnPos), blendType = 'easeInOut')
        
        Sequence(
                 Func(logo.start),
                 Wait(0.1),
                 Func(play.start),
                 Wait(0.2),
                 Func(opt.start),
                 Wait(0.2),
                 Func(quit.start)).start()
                 
    def showHamburgerMenu(self):
        self.hbButton.hide()
        self.hbHideButton.show()
        
        self.patNode2d = aspect2d.find("**/patNode2d")
        self.patNode2d.posInterval(.5, Point3(.5, 0, 0), blendType = 'easeInOut').start()
        
        self.patNode = render.find("**/patNode")
        self.patNode.posInterval(.5, Point3(0, -3, 0), blendType = 'easeInOut').start()
        
    def hideHamburgerMenu(self):
        self.hbButton.show()
        self.hbHideButton.hide()

        self.patNode2d.posInterval(.5, Point3(0, 0, 0), blendType = 'easeInOut').start()

        self.patNode.posInterval(.5, Point3(0, 0, 0), blendType = 'easeInOut').start()

    def reportBug(self):
        BugReportGUI.BugReportGUI()
        
        
    def createTabs(self):
        self.PlayButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = PlayGame, text_scale = .1, scale = 0.95, command = self.playGame)
        self.PlayButton.reparentTo(aspect2d)
        self.PlayButton.setPos(PlayBtnHidePos)
        self.PlayButton.show()

        self.OptionsButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = Options, text_scale = .1, scale = 0.95, command = self.openOptions)
        self.OptionsButton.reparentTo(aspect2d)
        self.OptionsButton.setPos(OptionsBtnHidePos)
        self.OptionsButton.show()

        self.QuitButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = Quit, text_scale = .1, scale = 0.95, command = self.quitGame)
        self.QuitButton.reparentTo(aspect2d)
        self.QuitButton.setPos(QuitBtnHidePos)
        self.QuitButton.show()