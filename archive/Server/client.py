import socket
import os

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

s = socket.socket()
s.connect(('10.200.147.231',9991))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    s.send(send_length)
    s.send(message)
    print(s.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
input()

send(DISCONNECT_MESSAGE)