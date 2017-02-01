from toontown.toonbase import ToontownGlobals
from toontown.environment import TemperatureGlobals
import random
import math

class TemperatureManagerAI:

    def __init__(self, air):
        self.air = air
        self._temperatures = {}
    
    def calculateRandom(self, low, high):
        return random.randint(low, high) # todo: kinda cheep way of randomly setting starting tempearture
    
    def update(self, task, zoneId):
        # todo, update temperature based on time of day.
        return task.again
    
    def getTemperature(self, zoneId):
        return self._temperatures[zoneId]
    
    def loadHood(self, zoneId):
        if zoneId not in ToontownGlobals.Hoods:
            return
        
        (low, high) = TemperatureGlobals.hood2average[zoneId]
        self._temperatures[zoneId] = self.calculateRandom(
            low, high)
        
        for hood in self.air.hoods:
            if hood.zoneId is not zoneId:
                continue
                
            if self.getTemperature(zoneId) <= TemperatureGlobals.TemperatureFreezingPoint:
                hood.rainMgr.b_setState('Snow')
            elif self.getTemperature(zoneId) > TemperatureGlobals.TemperatureFreezingPoint:
                hood.rainMgr.b_setState('Rain')
    
    def unloadHood(self, zoneId):
        if zoneId not in self._temperatures.keys():
            return
        
        del self._temperatures[zoneId]
    
    def delete(self):
        self._temperatures = None
