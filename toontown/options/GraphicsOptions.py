from panda3d.core import *

from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals

resolution_table = [
    (800, 600),
    (1024, 768),
    (1280, 1024),
    (1600, 1200),
    (1280, 720),
    (1920, 1080)]

AspectRatios = [
             0, # Adaptive
             (1.33333), # 4:3
             (1.25), # 5:4
             (1.77777), # 16:9
             (2.33333) ] # 21:9

AspectRatioLabels = [
             "Adaptive",
             "4:3",
             "5:3",
             "16:9",
             "21:9"]
class GraphicsOptions:
        
    def setTextureScale(self):
        pass # TODO
        
