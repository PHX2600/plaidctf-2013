#!/usr/bin/python

import socket
import time

file = open("all_hashes.list", "r")

lineArray = []
for LINE in file:
   lineArray.append(LINE)


def BruteForce():
    done = False
    while not done:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("174.129.103.33", 9001))

        print s.recv(1024)
        for i in range(0, 21):
            if i >= 21:
                done = True
            data = s.recv(1024)
            
            print data
            splitData = data.split()
            md5Index = -1
            for i in range(0,len(splitData)):
              if (splitData[i] == 'Prefix:'):
                 md5Index = i+1
            md5Prefix = splitData[md5Index]
            print md5Prefix 
            
            found = False

            for LINE in lineArray:
                line = LINE.split()
                if line[1][:13] == md5Prefix:
                    s.send(line[0] + "\n")
                    #print "Out: " + lineArray[0]
                    print "Found"
                    found = True
                    break

            if not found:
                print "Not found"
                s.close()
                time.sleep(1)
                break

            time.sleep(1)
        
BruteForce()
