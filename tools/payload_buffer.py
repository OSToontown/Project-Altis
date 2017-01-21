import struct
import os
import sys
import StringIO
import pyaes

class Buffer(object):

    def __init__(self, data=None):
        self._data = data if data is not None else bytes()
        self._offset = 0

    def add(self, data):
        self._data += data

    def read(self, length, offset=0):
        if offset:
            self._offset += offset

        data = self._data[self._offset:length]
        self._offset += length
        return data

    def pack(self, fmt, *args):
        return struct.pack('!%s' % (fmt), *args)

    def unpack(self, fmt):
        data = struct.unpack_from('!%s' % (fmt), self._data, self._offset)
        self._offset += struct.calcsize('!%s' % (fmt))
        return data

    def pack_string(self, string):
        return self.pack('I', len(string)) + string

    def unpack_string(self):
        return self.read(self.unpack('I')[0])

class PayloadWriter(object):

    def __init__(self, filenames, output='payload.dll'):
        self._filenames = filenames
        self._output = output

        self._key = os.urandom(16)
        self._aes = pyaes.AESModeOfOperationCTR(self._key)

    def write(self):
        payload_data = b''

        with open(self._output, 'wb') as file:
            for filename in self._filenames:
                if not os.path.exists(filename):
                    raise IOError('Failed to find file with filename %s' % (
                        filename))

                with open(filename, 'rb') as _file:
                    payload_data += Buffer().pack_string(_file.read())
                    
                    _file.close()

            # write out the encrypted data.
            file.write(self._aes.encrypt(
                payload_data))
            
            file.close()

        print "Successfully generated dll, aes_key=%r" % (
            self._key)

if __name__ == '__main__':
    writer = PayloadWriter(sys.argv[1:])
    writer.write()