from toontown.classicchars import CCharPaths
from toontown.safezone import Playground
from toontown.toonbase import TTLocalizer

class DLPlayground(Playground.Playground):

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        render.setColorScale(Vec4(.55, .55, .65, 1))
        self.loader.hood.setDreamlandFog()

    def exit(self):
        Playground.Playground.exit(self)
        render.setColorScale(Vec4(1, 1, 1, 1))
        self.loader.hood.setNoFog()

    def showPaths(self):
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Donald))
