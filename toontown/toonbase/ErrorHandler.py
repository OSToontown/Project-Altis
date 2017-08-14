import os
import httplib
import urllib
import getpass
import re
import ssl

class ErrorHandler(object):

    def __init__(self):
        self.tags = {}

        self.sysinfo = self.preloadSysInfo()

        self.addtags({
            'USERNAME': os.getenv('TT_USERNAME', 'UNDEFINED'),
            'CPU_USERNAME': getpass.getuser(),
            'CPU_HOSTNAME': self.sysinfo.get('Host Name', 'UNDEFINED'),
            'OSNAME': self.sysinfo.get('OS Name', 'UNDEFINED'),
            'OSVERSION': self.sysinfo.get('OS Version', 'UNDEFINED'),
            'SYSTEMTYPE': self.sysinfo.get('System Type', 'UNDEFINED'),
            'TOTALMEMORY': self.sysinfo.get('Total Physical Memory', 'UNDEFINED'),
            'AVAILABLEMEMORY': self.sysinfo.get('Available Physical Memory', 'UNDEFINED'),
            'LOCALE': self.sysinfo.get('System Locale', 'UNDEFINED')
        })

    def addtags(self, tags):
        self.tags.update(tags)


    def reporterror(self, error):
        if type(error) is not str:
            return self.message('Tried reporting error that wasn\'t a string')

        self.addtags({
            'USER_KEY': 'Jb03JXqzPvF53fFwzgq2HB88IDCs1pdpYAjcqTuBnSjHqvfzYHYBPo5KX0T2gWfd2S1ZZWGFUFkRyxBJg9t6HOFHlZPO38qJZnID',
            'CONTENT': error
        })
        params = urllib.urlencode(self.tags)
        conn = httplib.HTTPSConnection('www.projectaltis.com', context=ssl._create_unverified_context())
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        conn.request('POST', '/api/crash', params, headers)
        response = conn.getresponse()
        print self.responseMessage(response.status)


    @staticmethod
    def responseMessage(responsecode):
        return {
            200: 'Success',
            201: 'Success',
            202: 'Success',
            400: 'We tried sending something that was not a string.',
            403: 'Invalid secret key passed to server.',
            404: 'API has been removed.',
            413: 'Exception too long to be sent to server.',
            418: 'I\'m a Teapot! https://google.com/teapot',
            429: 'We\'ve crashed too many times and the server has rate limited us.',
            500: 'Server errored when handling request.',
            502: 'Server errored when handling request.',
            503: 'Server is under load or down for maintenance.'


        }.get(responsecode, 'Unknown response code.')

    def message(self, message):
        m = 'ErrorHandler: ' + message
        print m
        return m

    def preloadSysInfo(self):
        try:
            values = {}
            cache = os.popen2("SYSTEMINFO")
            source = cache[1].read()
            sysOpts = ["Host Name", "OS Name", "OS Version", "System type", "Total Physical Memory",
                       "Available Physical Memory", "System Locale"]

            for opt in sysOpts:
                values[opt] = [item.strip() for item in re.findall("%s:\w*(.*?)\n" % (opt), source, re.IGNORECASE)][0]
            return values
        except:
            self.message('Unable to load system information for advanced reporting.')
            pass
