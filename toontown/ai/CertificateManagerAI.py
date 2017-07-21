import random

class CertificateManagerAI():
    def __init__(self, air):
        self.air = air

    def addCode(self, av, code):
        file = open('data/certificate_fishing_codes.txt', 'a')
        file.write(code + "\n")
        file.close()
        certs = av.getCerts()
        certs.append(code)
        av.b_setCerts(certs)
		
    def generateCode(self):
        code = ''
        for i in xrange(12):
            number = random.randint(0, 9)
            code += str(number)
            if (i - 3) % 4 == 0 and i != 12:
                code += '-'
        return code