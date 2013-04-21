#!/usr/bin/env python

import hashlib

file = open('words.list', 'r')

for line in file:
    word = line.rstrip()
    print word + "\t" + hashlib.md5(word).hexdigest()
