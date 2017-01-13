import base64
import pyaes
import os
import sys

aesKey = 'J8AdT6l8kx1uoG6a3W2ygzb3HGaIrlN1'
iv = 'mz5kvZC51A4VT95X'
aes = pyaes.AESModeOfOperationCTR(key)

def encrypt_file(filename, output):
    if not os.path.exists(filename):
        raise IOError('Cannot find file with filename %s' % (filename))

    with open(filename, 'r') as file:
        data = file.read()
        file.close()

    with open(output, 'w') as file:
        file.write(aes.encrypt(data))
        file.close()

    print >> sys.stderr, "Successfully created new AES encrypted file %s!\r" % (
        output)

if len(sys.argv) < 3:
    raise Exception('Please specify all arguments! [filename, output]')

encrypt_file(sys.argv[1], sys.argv[2])