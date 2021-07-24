from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from otp.launcher.LauncherBase import LauncherBase
import os
import sys
import time

class LogAndOutput:
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()

    def flush(self):
        self.log.flush()
        self.orig.flush()

class TTALauncher(LauncherBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('AltisLauncher')

    def __init__(self):
        self.http = HTTPClient()
        self.logPrefix = 'project-altis-'

        ltime = 1 and time.localtime()
        logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2],
                                                   ltime[3], ltime[4], ltime[5])

        if not os.path.exists('user/'):
            os.mkdir('user/')
        if not os.path.exists('user/logs/'):
            os.mkdir('user/logs/')
            self.notify.info('Made new directory to save logs.')

        logfile = os.path.join('user/logs', self.logPrefix + logSuffix + '.log')

        log = open(logfile, 'a')
        logOut = LogAndOutput(sys.stdout, log)
        logErr = LogAndOutput(sys.stderr, log)
        sys.stdout = logOut
        sys.stderr = logErr
        self.notify.info('Starting Project Altis...')

    def getPlayToken(self):
        return self.getValue('TT_PLAYCOOKIE')

    def getGameServer(self):
        return self.getValue('TT_GAMESERVER')

    def getUsername(self):
        return self.getValue('TT_USERNAME')

    def getPassword(self):
        return self.getValue('TT_PASSWORD')

    def setPandaErrorCode(self, code):
        pass

    def getGame2Done(self):
        return True

    def getLogFileName(self):
        return 'toontown'

    def getValue(self, key, default = None):
        return os.environ.get(key, default)

    def setValue(self, key, value):
        os.environ[key] = str(value)

    def getVerifyFiles(self):
        return config.GetInt('launcher-verify', 0)

    def getTestServerFlag(self):
        return self.getValue('IS_TEST_SERVER', 0)

    def isDownloadComplete(self):
        return 1

    def isTestServer(self):
        return 0

    def getPhaseComplete(self, phase):
        return 1

    def startGame(self):
        self.newTaskManager()
        eventMgr.restart()
        from toontown.toonbase import ToontownStart
