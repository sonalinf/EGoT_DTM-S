# Examples used:
# https://stackoverflow.com/questions/27241804/sending-a-file-over-tcp-sockets-in-python
# https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
#CDTA as Server
import os
import socket 
import threading

HEADER = 64
PORT = 5050
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
SERVER = socket.gethostbyname(socket.gethostname())
#Method 2
#SERVER = socket.gethostbyname("localhost")
#Method 3
#SERVER = socket.gethostbyname('')
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
dir_path = os.path.dirname(os.path.realpath(__file__))
    
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')    
    received = conn.recv(BUFFER_SIZE).decode()
    #filesize = received.getsize(filename)
    filename = os.path.basename(filename)
    filesize = os.path.getsize(filename)    
    #filesize = int(filesize)
    
    filetodown = open(filename, 'rb')
    while True:
        print('Receiving ...')
        data_read = client_socket.recv(BUFFER_SIZE)
        if not data_read:
            print('Done Receiving.')
            break
        filetodown.write(data_read)
    SERVER.send('File received.  Thank you!')       
    conn.close()
        

def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #print(f"[NEW CONNECTION] {addr} connected.") 
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')
print("[STARTING] server is starting...")
start()