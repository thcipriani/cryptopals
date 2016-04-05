#!/usr/bin/env python

from utils import test, hex_to_base64

h2b64 = hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b'
                      '65206120706f69736f6e6f7573206d757368726f6f6d')

test(h2b64, 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
