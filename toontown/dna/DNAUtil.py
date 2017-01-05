from panda3d.core import LVector4f

def dgiExtractString8(dgi):
    return dgi.getString()

def dgiExtractColor(dgi):
    a, b, c, d = (dgi.getUint8() / 255.0 for _ in xrange(4))
    return LVector4f(a, b, c, d)