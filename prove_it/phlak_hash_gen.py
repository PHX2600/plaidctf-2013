#!/usr/bin/python

import hashlib

for i in xrange(0, 1000000):

    print hashlib.md5('i').hexdigest()