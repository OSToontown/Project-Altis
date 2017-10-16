import __builtin__

__builtin__.process = 'ai'

__builtin__.__dict__.update(__import__('panda3d.core', fromlist = ['*']).__dict__)

from direct.extensions_native import HTTPChannel_extensions


from toontown.toonbase import ToonPythonUtil as PythonUtil

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--base-channel', help='The base channel that the server may use.')
parser.add_argument('--max-channels', help='The number of channels the server may use.')
parser.add_argument('--stateserver', help="The control channel of this AI's designated State Server.")
parser.add_argument('--district-name', help="What this AI Server's district will be named.")
parser.add_argument('--astron-ip', help="The IP address of the Astron Message Director to connect to.")
parser.add_argument('--eventlogger-ip', help="The IP address of the Astron Event Logger to log to.")
parser.add_argument('--start-time', help="The time of day to start at")
parser.add_argument('config', nargs='*', default=['config/general.prc', 'config/release/dev.prc', 'config/server.prc'], help="PRC file(s) to load.")
args = parser.parse_args()

for prc in args.config:
    loadPrcFile(prc)

localconfig = ''
if args.base_channel: localconfig += 'air-base-channel %s\n' % args.base_channel
if args.max_channels: localconfig += 'air-channel-allocation %s\n' % args.max_channels
if args.stateserver: localconfig += 'air-stateserver %s\n' % args.stateserver
if args.district_name: localconfig += 'district-name %s\n' % args.district_name
if args.astron_ip: localconfig += 'air-connect %s\n' % args.astron_ip
if args.eventlogger_ip: localconfig += 'eventlog-host %s\n' % args.eventlogger_ip
if args.start_time: localconfig += 'start-time %s\n' % args.start_time
loadPrcFileData('Command-line', localconfig)


from otp.ai.AIBaseGlobal import *

from toontown.ai.ToontownAIRepository import ToontownAIRepository
simbase.air = ToontownAIRepository(config.GetInt('air-base-channel', 401000000),
                                   config.GetInt('air-stateserver', 4002),
                                   config.GetString('district-name', 'Devhaven'),
                                   config.GetInt('start-time', 6))
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
    simbase.air.writeServerEvent('ai-exception', simbase.air.getAvatarIdFromSender(), simbase.air.getAccountIdFromSender(), info)
    import os
    if os.getenv('DISTRICT_NAME', 'Test Canvas') == "Test Canvas":
        raise
    from raven import Client
    from os.path import expanduser
    import traceback
    errorReporter = Client('https://bd12b482b0d04047b97a99be5d8a59f8:cadf8d958a194867b89fd77b61fdad45@sentry.io/189240')
    errorReporter.tags_context({
        'district_name': os.getenv('DISTRICT_NAME', 'UNDEFINED'),
        'AVID_SENDER': simbase.air.getAvatarIdFromSender(),
        'ACID_SENDER': simbase.air.getAccountIdFromSender(),
        'homedir': expanduser('~'),
        'CRITICAL': 'True'
    })
    errorReporter.captureException()
    raise
