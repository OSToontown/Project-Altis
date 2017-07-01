'''
Created on Nov 16, 2016

@author: Drew
'''
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.task.Task import Task
from otp.ai.MagicWordGlobal import *
from panda3d.core import *
from toontown.distributed import ToontownDistrictStats
from toontown.hood import ZoneUtil
from toontown.shtiker import ShtikerPage
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toontowngui import TTDialog
import random
POP_COLORS = (Vec4(0.4, 0.4, 1.0, 1.0), Vec4(0.4, 1.0, 0.4, 1.0), Vec4(1.0, 0.4, 0.4, 1.0))
def setupInvasionMarker(node, invasionStatus):
    if node.find('**/*invasion-marker'):
        return

    markerNode = node.attachNewNode('invasion-marker')

    icons = loader.loadModel('phase_3/models/gui/cog_icons')

    if invasionStatus == 1:
        icon = icons.find('**/CorpIcon').copyTo(markerNode)
    elif invasionStatus == 2:
        icon = icons.find('**/LegalIcon').copyTo(markerNode)
    elif invasionStatus == 3:
        icon = icons.find('**/MoneyIcon').copyTo(markerNode)
    elif invasionStatus == 4:
        icon = icons.find('**/SalesIcon').copyTo(markerNode)
    else:
        icon = icons.find('**/BoardIcon').copyTo(markerNode)

    icons.removeNode()

    icon.setPos(0.44, 0, 0.015)
    icon.setScale(0.053)

def removeInvasionMarker(node):
    markerNode = node.find('**/*invasion-marker')

    if not markerNode.isEmpty():
        markerNode.removeNode()

class ShardPicker(ShtikerPage.ShtikerPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('ShardPicker')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.shardButtonMap = {}
        self.shardButtons = []
        self.scrollList = None
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)
        self.ShardInfoUpdateInterval = 5.0
        self.lowPop, self.midPop, self.highPop = base.getShardPopLimits()
        self.showPop = True # config.GetBool('show-total-population', 1)
        self.adminForceReload = 0
        self.load()

    def showPicker(self):
        self.enter()

    def hidePicker(self):
        self.exit()

    def load(self):
        main_text_scale = 0.06
        title_text_scale = 0.12
        helpText_ycoord = 0.403
        shardPop_ycoord = helpText_ycoord - 0.523
        totalPop_ycoord = shardPop_ycoord - 0.26
        self.gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.totalPopulationText = DirectLabel(parent=self, relief=None, text=TTLocalizer.ShardPagePopulationTotal % 1, text_scale=main_text_scale, text_wordwrap=8, textMayChange=1, text_align=TextNode.ACenter, pos=(0.65, 0, totalPop_ycoord), text_style = 3, text_fg = (1, 1, 1, 1))
        self.totalPopulationText.show()
        self.listXorigin = -0.02
        self.listFrameSizeX = 0.67
        self.listZorigin = -0.96
        self.listFrameSizeZ = 1.04
        self.arrowButtonScale = 1.3
        self.itemFrameXorigin = -0.237
        self.itemFrameZorigin = 0.365
        self.buttonXstart = self.itemFrameXorigin + 0.293
        self.regenerateScrollList()
        self.reparentTo(base.a2dBottomLeft)
        self.setPos(0.5, 0, 1.1)

    def unload(self):
        self.gui.removeNode()
        self.scrollList.destroy()
        self.totalPopulationText.destroy()
        del self.scrollList
        del self.shardButtons
        del self.totalPopulationText
        taskMgr.remove('ShardPageUpdateTask-doLater')
        ShtikerPage.ShtikerPage.unload(self)

    def regenerateScrollList(self):
        selectedIndex = 0
        if self.scrollList:
            selectedIndex = self.scrollList.getSelectedIndex()
            for button in self.shardButtons:
                button.detachNode()

            self.scrollList.destroy()
            self.scrollList = None
        self.scrollList = DirectScrolledList(parent = self, relief = None, pos = (0, 0, 0), incButton_image = (self.gui.find('**/FndsLst_ScrollUp'),
         self.gui.find('**/FndsLst_ScrollDN'),
         self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
         self.gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (self.arrowButtonScale, self.arrowButtonScale, -self.arrowButtonScale), incButton_pos = (self.buttonXstart, 0, self.itemFrameZorigin - 0.999), incButton_image3_color = Vec4(1, 1, 1, 0.2), decButton_image = (self.gui.find('**/FndsLst_ScrollUp'),
         self.gui.find('**/FndsLst_ScrollDN'),
         self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
         self.gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (self.arrowButtonScale, self.arrowButtonScale, self.arrowButtonScale), decButton_pos = (self.buttonXstart, 0, self.itemFrameZorigin + 0.125), decButton_image3_color = Vec4(1, 1, 1, 0.2), itemFrame_pos = (self.itemFrameXorigin, 0, self.itemFrameZorigin), itemFrame_scale = 1.0, itemFrame_relief = DGG.SUNKEN, itemFrame_frameSize = (self.listXorigin,
         self.listXorigin + self.listFrameSizeX,
         self.listZorigin,
         self.listZorigin + self.listFrameSizeZ), itemFrame_frameColor = (0.4, 0.4, 1, 0.5), itemFrame_borderWidth = (0.01, 0.01), numItemsVisible = 15, forceHeight = 0.065, items = self.shardButtons)
        self.scrollList.scrollTo(selectedIndex)
        
    def askForShardInfoUpdate(self, task = None):
        ToontownDistrictStats.refresh('shardInfoUpdated')
        taskMgr.doMethodLater(self.ShardInfoUpdateInterval, self.askForShardInfoUpdate, 'ShardPageUpdateTask-doLater')
        return Task.done

    def makeShardButton(self, shardId, shardName, shardPop):
        shardButtonParent = DirectFrame()
        shardButtonL = DirectButton(parent = shardButtonParent, relief = None, text = shardName, text_scale = 0.06, text_align = TextNode.ALeft, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, textMayChange = 0, text_style = 3, command = self.getPopChoiceHandler(shardPop), extraArgs = [shardId])
        if self.showPop:
            popText = str(shardPop)
            if shardPop == None:
                popText = ''
            shardButtonR = DirectButton(parent = shardButtonParent, relief = None, text = popText, text_scale = 0.06, text_align = TextNode.ALeft, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, textMayChange = 1, pos = (0.5, 0, 0), text_style = 3, command = self.choseShard, extraArgs = [shardId])
        else:
            model = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
            button = model.find('**/minnieCircle')
            shardButtonR = DirectButton(parent = shardButtonParent, relief = None, image = button, image_scale = (0.3, 1, 0.3), image2_scale = (0.35, 1, 0.35), image_color = self.getPopColor(shardPop), pos = (0.6, 0, 0.0125), text = self.getPopText(shardPop), text_scale = 0.06, text_align = TextNode.ACenter, text_pos = (-0.0125, -0.0125), text_fg = Vec4(0, 0, 0, 0), text1_fg = Vec4(0, 0, 0, 0), text2_fg = Vec4(0, 0, 0, 1), text3_fg = Vec4(0, 0, 0, 0), command = self.getPopChoiceHandler(shardPop), extraArgs = [shardId])

            del model
            del button

        invasionMarker = NodePath('InvasionMarker-%s' % shardId)
        invasionMarker.reparentTo(shardButtonParent)
        return (shardButtonParent, shardButtonR, shardButtonL, invasionMarker)

    def getPopColor(self, pop):
        if config.GetBool('want-lerping-pop-colors', True):
            if pop < self.midPop:
                color1 = POP_COLORS[0]
                color2 = POP_COLORS[1]
                popRange = self.midPop - self.lowPop
                pop = pop - self.lowPop
            else:
                color1 = POP_COLORS[1]
                color2 = POP_COLORS[2]
                popRange = self.highPop - self.midPop
                pop = pop - self.midPop
            popPercent = pop / float(popRange)
            if popPercent > 1:
                popPercent = 1
            newColor = color2 * popPercent + color1 * (1 - popPercent)
        elif pop <= self.lowPop:
            newColor = POP_COLORS[0]
        elif pop <= self.midPop:
            newColor = POP_COLORS[1]
        else:
            newColor = POP_COLORS[2]
        return newColor

    def getPopText(self, pop):
        if pop <= self.lowPop:
            popText = TTLocalizer.ShardPageLow
        elif pop <= self.midPop:
            popText = TTLocalizer.ShardPageMed
        else:
            popText = TTLocalizer.ShardPageHigh

        return popText

    def getPopChoiceHandler(self, pop):
        if base.cr.productName == 'JP':
            handler = self.choseShard
        elif pop <= self.midPop:
            handler = self.choseShard
        elif self.showPop:
            handler = self.choseShard
        else:
            handler = self.shardChoiceReject

        return handler

    def getCurrentZoneId(self):
        return None

    def getCurrentShardId(self):
        zoneId = self.getCurrentZoneId()
        if zoneId != None and ZoneUtil.isWelcomeValley(zoneId):
            return ToontownGlobals.WelcomeValleyToken
        else:
            if not base.cr.defaultShard:
                base.cr.defaultShard = random.choice(base.cr.listActiveShards())

            return base.cr.defaultShard

    def updateScrollList(self):
        curShardTuples = base.cr.listActiveShards()

        def compareShardTuples(a, b):
            if a[1] < b[1]:
                return -1
            elif b[1] < a[1]:
                return 1
            else:
                return 0

        curShardTuples.sort(compareShardTuples)
        if base.cr.welcomeValleyManager:
            curShardTuples.append((ToontownGlobals.WelcomeValleyToken,
             TTLocalizer.WelcomeValley[-1],
             0,
             0))
        currentShardId = self.getCurrentShardId()
        shardName = None
        anyChanges = 0
        totalPop = 0
        totalWVPop = 0
        currentMap = {}
        self.shardButtons = []
        for i in range(len(curShardTuples)):
            shardId, name, pop, WVPop, invasionStatus = curShardTuples[i]
            if shardId == currentShardId:
                shardName = name

            totalPop += pop
            totalWVPop += WVPop
            currentMap[shardId] = 1
            buttonTuple = self.shardButtonMap.get(shardId)
            if buttonTuple == None or self.adminForceReload:
                buttonTuple = self.makeShardButton(shardId, name, pop)
                self.shardButtonMap[shardId] = buttonTuple
                anyChanges = 1
            elif self.showPop:
                buttonTuple[1]['text'] = str(pop)
            else:
                buttonTuple[1]['image_color'] = self.getPopColor(pop)
                if not base.cr.productName == 'JP':
                    buttonTuple[1]['text'] = self.getPopText(pop)
                    buttonTuple[1]['command'] = self.getPopChoiceHandler(pop)
                    buttonTuple[2]['command'] = self.getPopChoiceHandler(pop)
            self.shardButtons.append(buttonTuple[0])
            if shardId == currentShardId:
                buttonTuple[1]['state'] = DGG.DISABLED
                buttonTuple[2]['state'] = DGG.DISABLED
            else:
                buttonTuple[1]['state'] = DGG.NORMAL
                buttonTuple[2]['state'] = DGG.NORMAL

            if invasionStatus:
                setupInvasionMarker(buttonTuple[3], invasionStatus)
            else:
                removeInvasionMarker(buttonTuple[3])

        for shardId, buttonTuple in self.shardButtonMap.items():
            if shardId not in currentMap:
                buttonTuple[0].destroy()
                del self.shardButtonMap[shardId]
                anyChanges = 1

        buttonTuple = self.shardButtonMap.get(ToontownGlobals.WelcomeValleyToken)
        if buttonTuple:
            if self.showPop:
                buttonTuple[1]['text'] = str(totalWVPop)
            else:
                buttonTuple[1]['image_color'] = self.getPopColor(totalWVPop)
                if not base.cr.productName == 'JP':
                    buttonTuple[1]['text'] = self.getPopText(totalWVPop)
                    buttonTuple[1]['command'] = self.getPopChoiceHandler(totalWVPop)
                    buttonTuple[2]['command'] = self.getPopChoiceHandler(totalWVPop)
                    buttonTuple[3]['command'] = self.getPopChoiceHandler(totalWVPop)

        if anyChanges or self.adminForceReload:
            self.regenerateScrollList()
            
        self.totalPopulationText['text'] = TTLocalizer.ShardPagePopulationTotal % totalPop
            
        helpText = TTLocalizer.ShardPageHelpIntro
        if shardName:
            if currentShardId == ToontownGlobals.WelcomeValleyToken:
                helpText += TTLocalizer.ShardPageHelpWelcomeValley % shardName
            else:
                helpText += TTLocalizer.ShardPageHelpWhere % shardName

        if self.adminForceReload:
            self.adminForceReload = 0

    def enter(self):
        self.askForShardInfoUpdate()
        self.updateScrollList()
        buttonTuple = self.shardButtonMap.get(self.getCurrentShardId())
        if buttonTuple:
            i = self.shardButtons.index(buttonTuple[0])
            self.scrollList.scrollTo(i, centered = 1)

        ShtikerPage.ShtikerPage.enter(self)
        self.accept('shardInfoUpdated', self.updateScrollList)

    def exit(self):
        self.ignore('shardInfoUpdated')
        self.ignore('confirmDone')
        taskMgr.remove('ShardPageUpdateTask-doLater')
        ShtikerPage.ShtikerPage.exit(self)

    def shardChoiceReject(self, shardId):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent = 'confirmDone', message = TTLocalizer.ShardPageChoiceReject, style = TTDialog.Acknowledge)
        self.confirm.show()
        self.accept('confirmDone', self.__handleConfirm)

    def __handleConfirm(self):
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm

    def choseShard(self, shardId):
        base.cr.defaultShard = shardId
        self.updateScrollList()
