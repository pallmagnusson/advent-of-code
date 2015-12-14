#!/usr/bin/python

import hashlib

SECRET = 'iwrupvqb'

count = 1
while True:
    md5hash = hashlib.md5('{}{}'.format(SECRET, count)).hexdigest()
    if md5hash.startswith('00000'):
        print count
        break
    count += 1
