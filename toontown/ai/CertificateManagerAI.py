import random
import httplib

class CertificateManagerAI():
    def __init__(self, air):
        self.air = air
        self.accountId = 0
        self.certs = []


    def addCode(self, av, code):
        file = open('data/certificate_fishing_codes.txt', 'a')
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
        request = httplib.HTTPSConnection('wwsw.projectaltis.com')
        request.request('GET', '/api/addbetacert/JBPAWDT3JM6CTMLUH3476RBVVGDPN2XHHSA45KVMMF69K94RAVQBMPQLKTS5WDDN/%s' % (code))
