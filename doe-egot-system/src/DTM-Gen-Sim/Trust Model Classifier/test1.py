import ssl
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import os 
import subprocess
from bs4 import BeautifulSoup


POST_MSG = {}



class a():
    i = 1
    while os.path.isfile(f'{i}_ExpectedOperation.xml'):
        i += 1
    i -= 1
    message = BeautifulSoup(open(f"{i}_ExpectedOperation.xml", 'r'), "html.parser")

print("POST_end")
import classifier
    #soup = BeautifulSoup(open(f"{i}_ExpectedOperation.xml", 'r'), "html.parser")
    #print('Printing_soup',f)
    #####
    #soup = BeautifulSoup(open(f"{i}_ExpectedOperation.xml", 'r'), "html.parser")
   
    #subprocess.call(["./classifier.py",soup])