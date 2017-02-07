from direct.directnotify.DirectNotifyGlobal import *
from toontown.ai import HolidayBaseAI

class BingoWeekendMgrAI(HolidayBaseAI.HolidayBaseAI):
    notify = directNotify.newCategory('BingoWeekendMgrAI')

    PostName = 'BingoWeekend'
    StartStopMsg = 'BingoWeekendStartStop'

    def start(self):
        HolidayBaseAI.HolidayBaseAI.start(self)

        bboard.post(BingoWeekendMgrAI.PostName, True)
        simbase.air.newsManager.setBingoStart()
        messenger.send(BingoWeekendMgrAI.StartStopMsg)

    def stop(self):
        HolidayBaseAI.HolidayBaseAI.stop(self)

        bboard.remove(BingoWeekendMgrAI.PostName)
        simbase.air.newsManager.setBingoEnd()
        messenger.send(BingoWeekendMgrAI.StartStopMsg)
