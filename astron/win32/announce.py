#!/usr/bin/python

from jsonrpclib import Server
import time
import random
import json
import math
import os
from Crypto.Cipher import AES
import base64
import sys


RPC_SERVER_SECRET = sys.argv[1]

client = Server(sys.argv[2])

def generate_token(accessLevel):
    """
    Generate an RPC server token with the given access level.
    """
    token = {'timestamp': int(time.mktime(time.gmtime())), 'accesslevel': accessLevel}
    data = json.dumps(token)
    iv = os.urandom(AES.block_size)
    cipher = AES.new(RPC_SERVER_SECRET, mode=AES.MODE_CBC, IV=iv)
    data += '\x00' * (16 - (len(data)%AES.block_size))
    token = cipher.encrypt(data)
    return base64.b64encode(iv + token)

random.seed()
while True:
  try:
    res = client.ping(generate_token(700), 12345)
    if res != 12345:
      print "Is the server accessable?\n"
      exit
    
    msg = raw_input('Message: ')
    while True:
      shards = client.messageAll(generate_token(700), msg)
      print('sent msg')
      time.sleep(300)
  except Exception, e:
    print e
  time.sleep(300)