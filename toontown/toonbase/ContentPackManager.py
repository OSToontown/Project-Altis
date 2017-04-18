'''
Created on Feb 19, 2017

@author: Drew
'''
# this is like the 6th time im doing this pls
from direct.directnotify.DirectNotifyGlobal import directNotify
from panda3d.core import Multifile, Filename, VirtualFileSystem
import fnmatch, os
from toontown.pandautils import yaml

SupportedExtensions = ('.jpg', '.png', '.rgb', '.rgba', '.ogg', '.ttf')
DefaultPhases = (3, 3.5, 4, 5, 5.5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

class ContentPackManager:
    notify = directNotify.newCategory('ContentPackManager')

    def __init__(self):
        self.packPath = 'resources/contentpacks/'
        if not os.path.exists(self.packPath):
            os.makedirs(self.packPath)
        self.sortFile = os.path.join(self.packPath, "pack-load-order.yaml") # Use this to change the order in which packs are loaded
        if not os.path.exists(self.sortFile):
            open(self.sortFile, 'a').close()

        self.mountPoint = '/'

        self.vfSys = VirtualFileSystem.getGlobalPtr()

        self.sort = []

    def loadAll(self):
        with open(self.sortFile, 'r') as f:
            self.sort = yaml.load(f) or []
        for filename in self.sort[:]:
            if self.isValid(filename):
                self.applyFile(filename)
            else:
                self.notify.warning('Removing %s...' % filename)
                self.sort.remove(filename)
        for root, _, filenames in os.walk(self.packPath):
            root = root[len(self.packPath):]
            for filename in filenames:
                filename = os.path.join(root, filename).replace('\\', '/')
                if filename in self.sort:
                    continue
                if not self.isValid(filename):
                    continue
                self.applyFile(filename)
                self.sort.append(filename)

        with open(self.sortFile, 'w') as f:
            for filename in self.sort:
                f.write('- %s\n' % filename)

    def isValid(self, filename):
        if not os.path.exists(os.path.join(self.packPath, filename)):
            return False
        basename = os.path.basename(filename)
        if fnmatch.fnmatch(basename, '*.mf'):
            return True

        return False

    def applyFile(self, filename):
        mf = Multifile()
        mf.openReadWrite(Filename(os.path.join(self.packPath, filename)))

        # Remvoe anything thats not allowed
        for subfilename in mf.getSubfileNames():
            if os.path.splitext(subfilename)[1] not in SupportedExtensions:
                mf.removeSubfile(subfilename)
                print("Removing a file that is not allowed: %s" % str(subfilename))

        self.vfSys.mount(mf, self.mountPoint, 0)
        print('Successfully Mounted: ' + str(filename))

