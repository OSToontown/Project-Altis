from panda3d.core import LVector4f

# Byte orders...
LITTLE_ENDIAN = '<'
BIG_ENDIAN = '>'

# Data types...

# Signed integers...
INT8 = 'b'
INT16 = 'h'
INT32 = 'i'
INT64 = 'q'

# Unsigned integers...
UINT8 = 'B'
UINT16 = 'H'
UINT32 = 'I'
UINT64 = 'Q'

# Strings...
STRING = 'S'

# Booleans...
BOOLEAN = '?'

# Floats... (signed)
FLOAT32 = 'f'
FLOAT64 = 'd'  # double


def dgiExtractString8(dgi):
    return dgi.extractBytes(dgi.getUint8())

def dgiExtractColor(dgi):
    a, b, c, d = (dgi.getUint8() / 255.0 for _ in xrange(4))
    return LVector4f(a, b, c, d)