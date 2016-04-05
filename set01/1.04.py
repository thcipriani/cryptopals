#!/usr/bin/env python2

from utils import score_strings

with open('files/4.txt') as f:
    strings = f.read()

_, out = score_strings(strings.splitlines())

print out.strip()
