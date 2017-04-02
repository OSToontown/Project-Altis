'''
Created on Mar 21, 2017

@author: Drew
'''

from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify.DirectNotifyGlobal import directNotify
from datetime import datetime

class TTCodeRedemptionMgr(DistributedObject):
    neverDisable = 1
    notify = directNotify.newCategory('TTCodeRedemptionMgr')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        base.cr.codeRedemptionMgr = self
        self._contextGen = SerialMaskedGen(4294967295L)
        self._context2callback = {}

    def delete(self):
        if hasattr(base.cr, 'codeRedemptionMgr'):
            if base.cr.codeRedemptionMgr is self:
                del base.cr.codeRedemptionMgr

        self._context2callback = None
        self._contextGen = None
        DistributedObject.delete(self)

    def redeemCode(self, code, callback):
        context = self._contextGen.next()
        print(datetime.now())
        self._context2callback[context] = callback
        self.notify.debug('redeemCode(%s, %s)' % (context, code))
        self.sendUpdate('redeemCode', [context, code])

    def redeemCodeResult(self, context, result, awardMgrResult):
        self.notify.debug('redeemCodeResult(%s, %s, %s)' % (context, result, awardMgrResult))
        callback = self._context2callback.pop(context)
        callback(result, awardMgrResult)
