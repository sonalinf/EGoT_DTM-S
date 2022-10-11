#DTMC as Client
# Examples used:
# https://stackoverflow.com/questions/27241804/sending-a-file-over-tcp-sockets-in-python
# https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
import socket
import os

#SERVER = socket.gethostbyname(socket.gethostname())
# replace with webaddres such as:
#    remote_host = 'www.python.org'
#get the ipaddress of this computer by name
#SERVER = socket.gethostbyname(socket.gethostname())

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname('192.168.88.169')
#SERVER = socket.gethostbyname('0.0.0.0')
ADDR = (SERVER, PORT)
filetosend = 'Text.txt'
filesize = os.path.getsize(filetosend)
BUFFER_SIZE = 4096 # send 4096 bytes each time step

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(file):
    file = open(filetosend, 'rb')
    while True:
        bytes_read = file.read(BUFFER_SIZE)
        if not bytes_read:
            break
        print('Sending ...')
        client.send(bytes_read)
    client.shutdown(2)
    client.close()


#filetosend = open('Text.txt', 'rb')

send(filetosend)
input()
send(DISCONNECT_MESSAGE)