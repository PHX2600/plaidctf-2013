#!/usr/bin/python

import socket
import time

for i in range(0, 1000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("174.129.103.33", 9001))

	s.recv(1024)
	s.recv(95)

	inString = s.recv(92)

	inString = inString[12:25]

	print inString

	inString += "\n"

	with open("hashes", "a") as myfile:
		myfile.write(inString)

	time.sleep(2)