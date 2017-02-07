
class SimpleMailBase:

    def __init__(self, msgId, senderId, year, month, day, body):
        self.msgId = msgId
        self.senderId = senderId
        self.year = year
        self.month = month
        self.day = day
        self.body = body
        
    def setTime(self, day, year, month):
        self.day = day
        self.year = year
        self.month = month
        
    def setBody(self, body):
        self.body = body
        
    def setSenderId(self, senderId):
        self.senderId = senderId
        
    def setMsgId(self, msgId):
        self.msgId = msgId

    def __str__(self):
        string = 'msgId=%d ' % self.msgId
        string += 'senderId=%d ' % self.senderId
        string += 'sent=%s-%s-%s ' % (self.year, self.month, self.day)
        string += 'body=%s' % self.body
        return string
