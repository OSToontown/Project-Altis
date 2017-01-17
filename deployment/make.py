from direct.distributed.PyDatagram import PyDatagram
import argparse
import sys
import os

if not os.path.exists('built'):
    os.mkdir('built')

sys.path.append('nirai/src')

from niraitools import *

parser = argparse.ArgumentParser()
parser.add_argument('--compile-cxx', '-c', action='store_true',
                    help='Compile the CXX codes and generate AltisEngine.exe into built.')
parser.add_argument('--make-nri', '-n', action='store_true',
                    help='Generate gamedata.bin.')
parser.add_argument('--models', '-m', action='store_true',
                    help='Pack models.mf.')

args = parser.parse_args()

def niraicall_obfuscate(code):
    # We'll obfuscate if len(code) % 4 == 0
    # This way we make sure both obfuscated and non-obfuscated code work.
    if len(code) % 4:
        return False, None

    # There are several ways to obfuscate it
    # For this example, we'll invert the string
    return True, code[::-1]

niraimarshal.niraicall_obfuscate = niraicall_obfuscate

class SourcePackager(NiraiPackager):
    HEADER = '\x84\x80\x65'
    BASEDIR = '..' + os.sep

    def __init__(self, outfile):
        NiraiPackager.__init__(self, outfile)
        self.__manglebase = self.get_mangle_base(self.BASEDIR)

        self.add_panda3d_dirs()
        self.add_default_lib()
        self.add_directory(self.BASEDIR, mangler=self.__mangler)

    def add_source_dir(self, dir):
        self.add_directory(self.BASEDIR + dir, mangler=self.__mangler)

    def __mangler(self, name):
        # N.B. Mangler can be used to strip certain files from the build.
        # The file is not included if it returns an empty string.
        # TODO: Do not build the AI or UD module code!

        return name[self.__manglebase:].strip('.')

    def generate_niraidata(self):
        print 'Generating niraidata'

        config = self.get_file_contents(self.BASEDIR + 'config/general.prc', True)
        configRelease = self.get_file_contents(self.BASEDIR + 'config/release/release.prc', True)
        niraidata = 'CONFIG = %r %r' % (config, configRelease)
        self.add_module('niraidata', niraidata, compile=True)

    def process_modules(self):
        dg = PyDatagram()
        dg.addUint32(len(self.modules))

        for moduleName in self.modules:
            (data, size) = self.modules[moduleName]

            dg.addString(moduleName)
            dg.addInt32(size)
            dg.appendData(data)

        data = dg.getMessage()

        iv = '\0' * 16
        key = 'g89a1hU0acBrlcru'
        return aes.encrypt(data, key, iv)

if args.compile_cxx:
    if sys.platform == 'win32':
        output = 'ProjectAltis.exe'

    elif sys.platform == 'darwin':
        output = 'ProjectAltis'

    else:
        raise Exception('The platform "%s" in use is not supported.' % sys.platform)

    compiler = NiraiCompiler(output)
    compiler.add_nirai_files()
    compiler.add_source('src/altis.cxx')
    compiler.run()

if args.make_nri:
    pkg = SourcePackager('built/gamedata.bin')
    pkg.add_source_dir('otp')
    pkg.add_source_dir('toontown')
    pkg.add_file('NiraiStart.py')
    pkg.generate_niraidata()
    pkg.write_out()

#if args.models:
#    os.chdir('..')
#    cmd = 'multify -cf build/built/models.mf models'
#    p = subprocess.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr, shell=True)
#    v = p.wait()
#
#    if v != 0:
#        print 'The following command returned non-zero value (%d): %s' % (v, cmd[:100] + '...')
#        sys.exit(1)
