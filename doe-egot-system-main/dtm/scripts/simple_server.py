#!/usr/bin/python3
# https://flaviocopes.com/python-http-server/
# https://pythonsansar.com/creating-simple-http-server-python/
from pathlib import Path
import sys
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from bs4 import BeautifulSoup
import ssl
from datetime import datetime



#<<<<<<< Updated upstream
#adding a small change
#=======
# tried three methods of  imports.
# following also gives an error when the classifier is in the scripts folder
#import classifier
# error caused by line 11 - 14
#try:
#    from trust import classifier
#except ImportError:
#    from trust_model_classifier import classifier
    
#>>>>>>> Stashed changes
HOST_NAME = "0.0.0.0"
PORT = 8090
ROOT = sys.argv[0]
print("***********")
print(ROOT)
LOG = ROOT

message_content = {}
def logPost (data):
    with open(LOG,'a') as file:
        file.write(data)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if (self.path != '/na'):
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(201)
            self.end_headers()

            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length).decode("utf-8")
            logPost(data)
            print("The type is : ", type(data))
            #a.message_content = data
            
            message = data
            #message = BeautifulSoup((data, 'r'), "html.parser") 
            print ("Current working dir : %s" % os.getcwd())
            path = os.getcwd() + '/dtm/scripts/trust_model_classifier'
            sys.path.append(path)
            print("*************classifier")
            import classifier
#***********************************************************************************************
# https://stackoverflow.com/questions/63647694/how-to-make-classes-not-run-without-being-called 
#***********************************************************************************************           
            #from . import classifier
            #from mypackage.mymodule import as_int

    # def a(self, message):
    #     self.message = BeautifulSoup((message, 'r'), "html.parser")
    #     return(self.message)
    #     print("printing in class a the message")
    #     #message_content = BeautifulSoup((message_content, 'r'), "html.parser")
    # p1 = a(message)    
    # import classifier
        #a.message_content = data
        print("POST_end")

# class a():
#       print("printing in class a the message")
#       message_content = BeautifulSoup((message_content, 'r'), "html.parser")
#       import classifier

if __name__ == "__main__":
    LOG = ROOT + datetime.now().strftime('/log_%H_%M_%d_%m_%Y.log')

    server = HTTPServer((HOST_NAME, PORT), handler)
    server.socket = ssl.wrap_socket(
        server.socket,
        server_side=True,
        certfile=ROOT + '/root-ca/server.crt', 
        keyfile=ROOT + '/root-ca/private/server.key',
        ca_certs=ROOT + '/root-ca/cert_chain.crt')

    print(f"DTMC started on https://{HOST_NAME}:{PORT}")
    print(f"message log found at {LOG}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped successfully")
        sys.exit(0)
        
