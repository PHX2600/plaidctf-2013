#!/usr/bin/python

import sys,hashlib

file = open('words.list', 'r')

for line in file:
    word = line.rstrip()
    print word + "\t" + hashlib.md5(word).hexdigest()