#!/usr/bin/env python2

with open('files/8.txt') as f:
    data = f.read()

data = [datum.strip().decode('hex') for datum in data.splitlines()]

for datum in data:
    sixteens = [''.join(datum[i:i+16]) for i in range(0, len(datum), 16)]

    if len(set(sixteens)) != len(sixteens):
        print datum.encode('hex')
