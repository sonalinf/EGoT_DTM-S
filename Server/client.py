import socket
import os
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

s = socket.socket()
s.connect(('172.30.29.122',9991))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
input()

send(DISCONNECT_MESSAGE)