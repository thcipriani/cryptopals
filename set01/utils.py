#!/usr/bin/env python2

import inspect
import itertools
import string
import sys


def test(a, b):
    try:
        assert(a == b)
    except AssertionError:
        print '{} is not equal {}\n' \
              '{} is fucked up'.format(a, b, inspect.stack()[1][1])
        sys.exit(1)

    print '{} is cool'.format(inspect.stack()[1][1])


def hex_to_base64(thing):
    """Convert a hex-encoded string to base64"""
    return thing.decode('hex').encode('base64').strip()


def xor(c1, c2):
    """xor two chars"""
    return chr(ord(c1) ^ ord(c2))


def sxor(s1, s2):
    """Single byte xor"""
    c = ''
    for a, b in zip(s1, s2):
        c += xor(a, b)
    return c


def score_raw_string(thing):
    return score_string_key(thing, False)


def score_string_key(encoded_str, encoded=True):
    common = 'etaoin shrdlu'
    max_score = 0
    output_str = ''

    for char in string.printable:
        c = ''
        thing = encoded_str
        if encoded:
            thing = encoded_str.decode('hex')
        for a, b in zip(itertools.repeat(char), thing):
            c += chr(ord(a) ^ ord(b))

        score = 0
        for mark in list(common):
            score += c.lower().count(mark)

        if score > max_score:
            max_score = score
            output_str = c
            key = char

    return key, max_score, output_str


def score_string(encoded_str):
    char, max_score, output_str = score_string_key(encoded_str)
    return max_score, output_str


def score_strings(encoded_strings):
    """Does score_string for an array of strings

    :param: encoded_strings list
    """
    max_score = 0
    final_str = ''
    for enc in encoded_strings:
        score, output = score_string(enc.strip())

        if score > max_score:
            max_score = score
            final_str = output

    return max_score, final_str


def rep_key_xor(unenc_str, key='ICE'):
    """In repeating-key XOR, you'll sequentially apply each byte of the
    key; the first byte of plaintext will be XOR'd against I, the next
    C, the next E, then I again for the 4th byte, and so on.

    :param unenc_str - str to be encoded
    :param key - str key to use for XOR
    """
    ret = ''
    for a, b in zip(itertools.cycle(list(key)), unenc_str):
        ret += xor(a, b)

    return ret


def str_to_bin(thing):
    return ' '.join('{0:08b}'.format(ord(x)) for x in thing)


def hamming_distance(a, b):
    """The Hamming distance is just the number of differing bits"""
    distance = 0
    for b1, b2 in zip(a, b):
        if ord(b1) ^ ord(b2):
            distance += 1

    return distance
