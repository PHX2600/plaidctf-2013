#!/usr/bin/python

import hashlib

for i in xrange(0, 1000000000):

    print str(i) + "\t" + hashlib.md5(str(i)).hexdigest()
