#!/usr/bin/python

import socket
import time

file = open("HashRice", "r")

lineArray = []
for LINE in file:
   lineArray.append(LINE.rstrip())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("174.129.103.33", 9001))

print s.recv(1024)
for i in range(0, 21):
    print s.recv(95)
    
    inString = s.recv(92)

    inString = inString[12:25]

    print "Received: " + inString
    
    found = False

    for LINE in lineArray:
        line = LINE.split()
        if line[1][:13] == inString:
            s.send(line[0])
            #print "Out: " + lineArray[0]
            print "Found"
            found = True
            break

    print str(i)

    if not found:
        print "Not found"
        break
        
    time.sleep(5)
