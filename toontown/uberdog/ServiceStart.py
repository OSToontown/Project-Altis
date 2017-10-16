import __builtin__


__builtin__.process = 'uberdog'


# Temporary hack patch:
__builtin__.__dict__.update(__import__('panda3d.core', fromlist=['*']).__dict__)
def __runfunc(*args, **kw):
   raise SystemExit

from direct.extensions_native import HTTPChannel_extensions


from toontown.toonbase import ToonPythonUtil as PythonUtil

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--base-channel', help='The base channel that the server may use.')
parser.add_argument('--max-channels', help='The number of channels the server may use.')
parser.add_argument('--stateserver', help="The control channel of this UD's designated State Server.")
parser.add_argument('--astron-ip', help="The IP address of the Astron Message Director to connect to.")
parser.add_argument('--eventlogger-ip', help="The IP address of the Astron Event Logger to log to.")
parser.add_argument('config', nargs='*', default=['config/general.prc', 'config/release/dev.prc', 'config/server.prc'], help="PRC file(s) to load.")
args = parser.parse_args()

for prc in args.config:
    loadPrcFile(prc)

localconfig = ''
if args.base_channel: localconfig += 'air-base-channel %s\n' % args.base_channel
if args.max_channels: localconfig += 'air-channel-allocation %s\n' % args.max_channels
if args.stateserver: localconfig += 'air-stateserver %s\n' % args.stateserver
if args.astron_ip: localconfig += 'air-connect %s\n' % args.astron_ip
if args.eventlogger_ip: localconfig += 'eventlog-host %s\n' % args.eventlogger_ip
loadPrcFileData('Command-line', localconfig)


from otp.ai.AIBaseGlobal import *

from toontown.uberdog.ToontownUberRepository import ToontownUberRepository
simbase.air = ToontownUberRepository(config.GetInt('air-base-channel', 400000000),
                                     config.GetInt('air-stateserver', 4002))
__builtin__.eval = __runfunc
__builtin__.compile = __runfunc
__builtin__.execfile = __runfunc
__builtin__.globals = __runfunc
__builtin__.locals = __runfunc
host = config.GetString('air-connect', '127.0.0.1')
port = 7100
if ':' in host:
    host, port = host.split(':', 1)
    port = int(port)
simbase.air.connect(host, port)

try:
    run()
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    info = PythonUtil.describeException()
    simbase.air.writeServerEvent('uberdog-exception', simbase.air.getAvatarIdFromSender(), simbase.air.getAccountIdFromSender(), info)
    from raven import Client
    from os.path import expanduser
    import traceback
    errorReporter = Client('https://45206ecaaba840498741f18ed05e1b8b:39f55ef5dba047abb57cad0aa3a23d47@sentry.io/189241')
    errorReporter.user_context({
        'AVID_SENDER': simbase.air.getAvatarIdFromSender(),
        'ACID_SENDER': simbase.air.getAccountIdFromSender(),
        'homedir': expanduser('~'),
        'critical': 'True'
    })
    errorReporter.captureMessage(traceback.format_exc())
    raise
