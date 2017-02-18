from panda3d.core import *
from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals
from direct.showbase.DirectObject import DirectObject

class StreamerMode(DirectObject):
    def __init__(self):
        DirectObject.__init__(self)
        
    def start(self):
        self.accept("updateDistrictName", self.updateDistrictName)
    
    def stop(self):
        self.ignore("updateDistrictName")
        
    def updateDistrictName(self):
        name = base.cr.getShardName(base.localAvatar.defaultShard)
        districtFile = open("streamerinfo_district.txt", 'w')
        districtFile.write(name)