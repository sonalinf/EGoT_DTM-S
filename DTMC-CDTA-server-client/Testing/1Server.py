import socket
import os
import sys
s=socket.socket()
#host=socket.gethostname()
host=’192.168.0.2′
port=12000 #ports after 6000 are free
s.bind((host,port))
s.listen(10)
while True:
c,addr=s.accept()
print “Client connected”,addr
print (‘Got Connection from’ ,addr)
content=c.recv(100).decode()
if not content:
break
print content 