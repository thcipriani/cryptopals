#!/usr/bin/env python2

from utils import score_string

encoded_str = '1b37373331363f78151b7f2b783431333d' \
              '78397828372d363c78373e783a393b3736'

_, output_str = score_string(encoded_str)

print output_str
