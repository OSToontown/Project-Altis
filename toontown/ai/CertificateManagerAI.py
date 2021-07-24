import random
import httplib

class CertificateManagerAI():
    def __init__(self, air):
        self.air = air


    def addCode(self, av, code):
        file = open('dependencies/data/certificate_fishing_codes.txt', 'a')
        file.write(code + "\n")
        file.close()
        certs = av.getCerts()
        certs.append(code)
        av.b_setCerts(certs)
        self.sendCode(code)

    def generateCode(self):
        code = ''
        for i in xrange(12):
            number = random.randint(0, 9)
            code += str(number)
            if (i - 3) % 4 == 0 and i != 11:
                code += '-'
        return code

    def sendCode(self, code):
        domain = str(ConfigVariableString('ws-domain', 'localhost'))
        key = str(ConfigVariableString('ws-key', 'secretkey'))
        request = httplib.HTTPSConnection(domain)
        request.request('GET', '/api/addbetacert/%s/%s' % (key, code))
        print request.getresponse().read()
