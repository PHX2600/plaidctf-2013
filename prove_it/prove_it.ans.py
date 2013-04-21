import socket

host = '174.129.103.33'
port = 9001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
data = sock.recv(1024)
print data
f = open('prove_it.word', 'r')
lines = f.readlines()
while True:
   data = sock.recv(1024)
   print data
   splitData = data.split()
   md5Index = -1
   for i in range(0,len(splitData)):
      if (splitData[i] == 'Prefix:'):
         md5Index = i+1
   md5Prefix = splitData[md5Index]
   print md5Prefix 
   found = False
   for line in lines:
      splitLine = line.split()
      if (len(splitLine) > 1):
         hashee = splitLine[1]
      else:
         continue
      if (hashee[:len(md5Prefix)] == md5Prefix):
         string = line.split()[0]
         sock.send(string + "\n")
         print string
         response = sock.recv(26)
         print response
         found = True
         break
   if (not found):
      string = raw_input('Not Found:')
      sock.send(string + "\n")
