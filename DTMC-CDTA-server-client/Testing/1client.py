import socket
import os
s=socket.socket()
#host=socket.gethostname() #server hostname
host= '192.168.0.3'
port=12000 #same as server
s.connect((host,port))
fileToSend = open(“ToSend.txt”,”r”)
content = fileToSend.read()
s.send(content.encode())