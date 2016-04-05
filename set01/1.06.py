#!/usr/bin/env python

import utils

utils.test(utils.hamming_distance(utils.str_to_bin('this is a test'),
                                  utils.str_to_bin('wokka wokka!!!')), 37)

with open('files/6.txt') as f:
    text = f.read().decode('base64')

bin_text = utils.str_to_bin(text)
bin_text_arr = bin_text.split()
min_distance = 0
sizes = []

keysizes = []
for keysize in range(2, 41):
    # first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes
    info = [bin_text_arr[i:i+keysize]
            for i in range(0, len(bin_text_arr), keysize)]

    total_normalized_distance = 0

    # average the hamming distance between sets of bytes
    for a, b in zip(info[::2], info[1::2]):
        edit_distance = utils.hamming_distance(''.join(a), ''.join(b))
        # Normalize this result by dividing by KEYSIZE.
        total_normalized_distance += float(edit_distance) / float(keysize)

    avg_distance = float(total_normalized_distance) / float(len(info))

    keysizes.append((keysize, avg_distance))

keysize, _ = min(keysizes, key=lambda key: key[1])

print '[...] Keysize is {}'.format(keysize)

# Convert ciphertext into _keysize_-length blocks
chunks = [text[i:i+keysize] for i in range(0, len(text), keysize)
          if len(text[i:i+keysize]) == 29]

# Now transpose the blocks
blocks = zip(*[list(x) for x in chunks])

the_magic_key = ''
for block in blocks:
    # print block
    letter, _, _ = utils.score_raw_string(''.join(block))
    the_magic_key += letter

print '[...] The Magic Key is: "{}"'.format(the_magic_key)

print '[...] The Magic Message is\n--------------\n{}'.format(
    utils.rep_key_xor(text, the_magic_key))
