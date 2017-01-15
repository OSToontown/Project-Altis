from direct.directbase.DirectStart import *
from panda3d.core import loadPrcFile

loadPrcFile('config/general.prc')
loadPrcFile('config/release/dev.prc')

import LevelEditor
l = LevelEditor.LevelEditor()
