import ssl
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from bs4 import BeautifulSoup
from urllib.parse import parse_qs
from socketserver import ThreadingMixIn
import threading

threding_count = 0
HOST_NAME = "localhost"
PORT = 8000
message_content = {}

httpd = HTTPServer((HOST_NAME, PORT), BaseHTTPRequestHandler)

# addition of SSL
#httpd.socket = ssl.wrap_socket (httpd.socket, keyfile="./server.key", certfile='./client.crt', server_side=True)
#httpd.socket=ssl.wrap_socket(httpd.socket, server_side=True, certfile="ssl/server.crt",keyfile="ssl/server.key", ca_certs="ssl/client.crt")
httpd.socket=ssl.wrap_socket(httpd.socket, server_side=True, certfile="./server.crt",keyfile="./server.key", ca_certs="./client.crt")

#class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
class handler(ThreadingMixIn, HTTPServer):
    #GET for viewing messages
    def do_GET(self):
        print("get_start")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Message Received!')
        print("get_end")
    #POST for submitting messages
    def do_POST(self):
        print("post_start")

        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length).decode()
        print("data")
        message = parse_qs(data)["message"][0]

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())
        #self.wfile.write(self.path[1:])
        a.message_content = data
        print("POST_end")
class a():
   message_content = BeautifulSoup((message_content, 'r'), "html.parser")
   threding_count
   import classifier

if __name__ == "__main__":
    #server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    while True:
        conn, addr = httpd.accept()
        try:
            thread = threading.Thread(target=handler, args=(conn, addr))
            thread.start()
            threding_count = {threading.activeCount() - 1}
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            print = threding_count
        except KeyboardInterrupt:
            httpd.server_close()
        print("Server stopped successfully")
        sys.exit(0)