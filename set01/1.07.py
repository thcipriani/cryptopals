#!/usr/bin/env python2

from Crypto.Cipher import AES

obj = AES.new(b'YELLOW SUBMARINE')

with open('files/7.txt') as f:
    message = f.read().decode('base64')

print obj.decrypt(message)
