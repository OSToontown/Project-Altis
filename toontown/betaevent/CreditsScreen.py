'''
Created on Dec 30, 2016

@author: Drew
'''
from panda3d.core import Vec4, TransparencyAttrib, Point3, VBase3, VBase4, TextNode
from direct.interval.IntervalGlobal import * 
from toontown.toon import Toon, ToonDNA
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from toontown.betaevent.CreditsLines import *
from toontown.toonbase import ToontownGlobals

class CreditsScreen:
    '''
    The ending of the event, the all original credits sequence that no other server has ever put at the end of an event!
    '''


    def __init__(self):
        '''
        Setup the screen
        '''
        self.creditsSequence = None
        self.text = None
        self.roleText = None
        self.logo = OnscreenImage(image='phase_3/maps/toontown-logo.png',
                                  scale=(0.8 * (4.0/3.0), 0.8, 0.8 / (4.0/3.0)),
                                  pos=(0, 0, 0))
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        self.logo.reparentTo(aspect2d)
        self.logo.hide()
        self.logo.setColorScale(1, 1, 1, 0)
        
        def startScreen(*args):
            self.screenObject = args[0]
            self.screenObject.reparentTo(render)
            self.screenObject.setPos(0, -100, -5)
            self.screenObject.setHpr(180, -90, 0)

        asyncloader.loadModel("phase_3.5/models/events/charity/flying_screen.bam", callback = startScreen)

    def startCredits(self):
        base.musicManager.stopAllSounds()
        self.music = loader.loadMusic('phase_3/audio/bgm/downloader.ogg')
        base.playMusic(self.music, looping = 1)

        self.creditsSequence = Sequence(
            Wait(2),
            Func(base.localAvatar.stopUpdateSmartCamera),
            Func(base.camera.wrtReparentTo, render),
            Func(base.transitions.letterboxOn, 1),
            base.camera.posHprInterval(3, Point3(0, -50, 10), VBase3(180, 90, 0)),
            Func(self.logo.show),
            LerpColorScaleInterval(self.logo, 2, Vec4(1, 1, 1, 1)),
            Wait(2),
            LerpColorScaleInterval(self.logo, 2, Vec4(1, 1, 1, 0)),
            Func(self.logo.hide),
            base.camera.posHprInterval(2, Point3(0, -100, 10), VBase3(180, -90, 0)),
            Wait(1),
            Func(self.displayText, dubito),
            Wait(6),
            Func(self.hideText),
            Wait(1),
            Func(self.displayText, judge),
            Wait(6),
            Func(self.hideText),
            Wait(1),
            Func(self.displayText, drew),
            Wait(6),
            Func(self.hideText),
            Wait(1),
            Func(self.displayText, skipps),
            Wait(6),
            Func(self.hideText),
            ).start()
            
    def displayText(self, person):
        # Person is imported from CreditLines, which has a dict
        # Each DICT has the name and their role on the team
        
        # Open and split it out for use
        name, role = person
        
        self.showText(name, role)
        
    def showText(self, name, role):
        if not self.text:
            self.text = DirectLabel(text = name, text_style=3, relief = None, text_fg=(1, 1, 1, 1), text_align = TextNode.ACenter, text_scale = .8, text_wordwrap = 30, text_font = ToontownGlobals.getMinnieFont())
        else:
            self.text['text'] = name
        self.text.setColorScale(VBase4(1, 1, 1, 0))
        
        if not self.roleText:
            self.roleText = DirectLabel(text = role, text_style=3, relief = None, text_fg=(1, 1, 1, 1), text_align = TextNode.ACenter,  text_scale = .8, text_wordwrap = 30, text_font = ToontownGlobals.getMinnieFont())
        else:
            self.roleText['text'] = role
            
        self.roleText.setColorScale(VBase4(1, 1, 1, 0))
        self.text.reparentTo(self.screenObject)
        self.text.setPos(self.screenObject.find("**/front_screen").getPos() + Point3(0.0, -1.5, 0.4))
        self.roleText.reparentTo(self.screenObject)
        self.roleText.setPos(self.screenObject.find("**/front_screen").getPos() + Point3(0.0, -1.5, -0.4))
        self.text.show()
        self.roleText.show()
        
        Sequence(LerpColorScaleInterval(self.text, 1, VBase4(1, 1, 1, 1), blendType = 'easeInOut'), LerpColorScaleInterval(self.roleText, 1, VBase4(1, 1, 1, 1))).start()
        

    def hideText(self):
        if self.text:
            Sequence(LerpColorScaleInterval(self.text, .5, VBase4(1, 1, 1, 0), blendType = 'easeInOut'), LerpColorScaleInterval(self.roleText, .5, VBase4(1, 1, 1, 0))).start()