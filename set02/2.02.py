#!/usr/bin/env python2

from Crypto.Cipher import AES

KEY = b'YELLOW SUBMARINE'

obj = AES.new(KEY)

iv = '\x00' * 16

with open('files/10.txt') as f:
    message = f.read()
