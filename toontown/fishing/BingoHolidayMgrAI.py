from direct.directnotify.DirectNotifyGlobal import *
from toontown.ai import HolidayBaseAI

class BingoHolidayMgrAI(HolidayBaseAI.HolidayBaseAI):
    notify = directNotify.newCategory('BingoHolidayMgrAI')

    PostName = 'BingoHoliday'
    StartStopMsg = 'BingoHolidayStartStop'

    def start(self):
        HolidayBaseAI.HolidayBaseAI.start(self)

        bboard.post(BingoHolidayMgrAI.PostName, True)
        simbase.air.newsManager.setBingoStart()
        messenger.send(BingoHolidayMgrAI.StartStopMsg)

    def stop(self):
        HolidayBaseAI.HolidayBaseAI.stop(self)

        bboard.remove(BingoHolidayMgrAI.PostName)
        simbase.air.newsManager.setBingoEnd()
        messenger.send(BingoHolidayMgrAI.StartStopMsg)
