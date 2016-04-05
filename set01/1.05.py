#!/usr/bin/env python2

from utils import rep_key_xor, test

phrase = 'Burning \'em, if you ain\'t quick and nimble\n' \
         'I go crazy when I hear a cymbal'

test(rep_key_xor(phrase).encode('hex'),
     '0b3637272a2b2e63622c2e69692a23693a2a3c6'
     '324202d623d63343c2a26226324272765272a28'
     '2b2f20430a652e2c652a3124333a653e2b20276'
     '30c692b20283165286326302e27282f')
