#!/usr/bin/python
#########################################
# Author: GTKlondike	  		#
# This script is designed to connect to #
# any of the cheap servers. Data is 	#
# then sent via TCP stream and assembly #
# is returned.				#
#########################################

# This script can also be ran in the python interpreter

from socket import *

s = socket() # Open TCP Stream socket

# Connect to one of the Cheap servers
# 50.17.171.79:9998
# 54.224.183.192:9998
# 184.73.107.54:9998
# 54.234.231.14:9998
# 54.224.176.148:9998

s.connect(("54.224.176.148", 9998))

s.send("\x90" * 500) # Send 500 bytes of data
data = s.recv(20000) # Recieve 2k bytes from incoming stream buffer


s.close() # Close socket





