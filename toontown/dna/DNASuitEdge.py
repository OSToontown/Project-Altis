
class DNASuitEdge(object):
    __slots__ = (
        'startpt', 'endpt', 'zoneId')

    def __init__(self, startpt, endpt, zoneId):
        self.startpt = startpt
        self.endpt = endpt
        self.zoneId = zoneId

    def __del__(self):
        del self.startpt
        del self.endpt
        del self.zoneId

    def getEndPoint(self):
        return self.endpt
        
    def setEndPoint(self, endpt):
        self.endpt = endpt

    def getStartPoint(self):
        return self.startpt
        
    def setStartPoint(self, startpt):
        self.startpt = startpt

    def getZoneId(self):
        return self.zoneId

    def setZoneId(self, zoneId):
        self.zoneId = zoneId