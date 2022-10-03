#DTMC as Client
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#Method 2
#SERVER = socket.gethostbyname("localhost")
#Method 3
SERVER = socket.gethostbyname('127.0.0.1')
#SERVER = socket.gethostbyname(socket.gethostname())
# replace with webaddres such as:
#    remote_host = 'www.python.org'
#get the ipaddress of this computer by name
#SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

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