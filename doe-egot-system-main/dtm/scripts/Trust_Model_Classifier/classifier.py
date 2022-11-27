import xml.etree.ElementTree as ET
import ast
from bs4 import BeautifulSoup
import csv
import time
import random
import os
import sys
import subprocess
from simple_server import a
#from test1 import a
#import argparse

path = os.getcwd()
#ap = argparse.ArgumentParser()
#ap.add_argument('-f', '--file', required=True, metavar='', help = 'input XML file')
#ap.add_argument('-o', '--output', required=True, metavar='', help = 'output CSV file')

#args = ap.parse_args()

GSP_DCM = {
            #GSP  :   [DCM]
            '/dcap': [
                  'DeviceCapability',
                  'TimeLink',
                  'EndDeviceListLink',
                  'SelfDeviceLink'],
            '/tm': [
                  'Time',
                  'CurrentTime',
                  'dstEndTime',
                  'dstOffset',
                  'dstStartTime',
                  'localTime',
                  'quality',
                  'tzOffset'],
            '/edev': [
                  'EndDevice',
                  'lFDI',
                  'sFD',
                  'changedTime',
                  'enabled',
                  'FlowReservationRequestListLink',
                  'FlowReservationResponseListLink',
                  'postRate'],
            '/fres': [
                  'FlowReservationRespons',
                  'mRID',
                  'description',
                  'version',
                  'creationTime',
                  'EventStatus',
                  'currentStatus',
                  'dateTime',
                  'potentiallySuperseded',
                  'potentiallySupersededTime',
                  'reason',
                  'EventStatus',
                  'interval',
                  'duration',
                  'start',
                  'interval',
                  'energyAvailable',
                  'multiplier',
                  'value',
                  'energyAvailable',
                  'powerAvailable',
                  'multiplier',
                  'value',
                  'powerAvailable',
                  'subject'],
            '/freq':[],
            '/sdev':[
                  'SelfDevice',
                  'ConfigurationLink',
                  'DERListLink',
                  'deviceCategory',
                  'DeviceInformationLink',
                  'DeviceStatusLink',
                  'FileStatusLink',
                  'IPInterfaceListLink',
                  'lFDI',
                  'LoadShedAvailabilityListLink',
                  'LogEventListLink',
                  'PowerStatusLink',
                  'sFDI']
            }

Ack_Nak =['Ack', 'Nak']
DCM_msg = {
            'ExportEnergyCommand': Ack_Nak.copy(),
            'IdelCommand': Ack_Nak.copy(),
            'ImportEnergyCommand': Ack_Nak.copy(),
            'CriticalPeakEventCommand': Ack_Nak.copy(),
            'GridEmergencyEventCommand': Ack_Nak.copy(),
            'OutsideCommConnectionStatusCommand': Ack_Nak.copy(),
            'GetEnergy': Ack_Nak.copy(),
            'GetNameplate': Ack_Nak.copy(),
            'MaxPayloadCommand': Ack_Nak.copy()
            }
DER_msg = {
            'QueryOperationalState': Ack_Nak.copy(),
            'App Ack': Ack_Nak.copy(),
            'App Nak': Ack_Nak.copy(),
            'Commodity Read Response': Ack_Nak.copy(),
            'MaxPayloadCommand': Ack_Nak.copy(),
            'MaxPayloadCommandResponse': Ack_Nak.copy(),
            'GetNameplateResponse': Ack_Nak.copy()
            }

#POST_MSG = {}
#soup = BeautifulSoup((sys.argv, 'r'), "html.parser")

#soup =  (BeautifulSoup.prettify(a.s, "xml"))
soup = a.message_content
#soup = BeautifulSoup(open(args.file, 'r'), "html.parser")
""" i = 1
while os.path.isfile(f'{i}_ExpectedOperation.xml'):
    i += 1
i -= 1
soup = BeautifulSoup(POST_MSG, 'r'), "html.parser") """

#soup = BeautifulSoup(open(f"{i}_ExpectedOperation.xml", 'r'), "html.parser")
print("start")

request_count = {}
#TODO: make this an argument that you take in 
HIST = 3
history = {}
TIMESTAMP_MIN = 0
TIMESTAMP_Err = []
TYPE_Err = []

def my_int(b):
    '''
        casts a hex string to a int 
        b: is the base of the int
    '''
    def func(x):
        return int(x,base=b)
    return func

types = {
    'int': int,
    'string': str,
    'float':float,
    'hex': my_int(16)
}


print(TYPE_Err)

#get and store from
required0 = soup.find_all("from")
from_list = []
for i in required0:
    from_list.append(i.get_text())

#get and store to
required0 = soup.find_all("to")
to_list = []
for i in required0:
    to_list.append(i.get_text())

#get and store request
required0 = soup.find_all("target")
target = []
for i in required0:
    target.append(i.get_text())

#get and store DER request
required0 = soup.find_all("body")
body = []
for i in required0:
    target.append(i.get_text())


#get DCM_timestamp 
required0 = soup.find_all("dcm_timestamp")
timestamp = []
#121
idx = 0
for i in required0:
    print(type(i))
    timestamp.append(i.get_text())
    if int(i.get_text()) >= TIMESTAMP_MIN:
        TIMESTAMP_MIN = int(i.get_text())
        print("TIMESTAMP_MIN = ", TIMESTAMP_MIN)
    else:
        TIMESTAMP_Err.append(idx)
    idx += 1

#request response pair check for
req = "request"
res = "response"
count = 1
idx = 0
required0 = soup.find_all("http_method")
http_type = []
http_err = []
for i in required0:
    curr_http = i.get_text()
    http_type.append(curr_http)
    print("curr_http: ", curr_http)
    if (count % 2) == 0:
        if res in curr_http:
            print("Ex")
        else:
            print("UX wrong HTTP request/response")
            http_err.append(idx)
    else:
        if req in curr_http:
            print("Ex")
        else:
            print("UX wrong HTTP request/response")
            http_err.append(idx)
    count += 1
    idx += 1

#print(from_list[0])
print(TIMESTAMP_Err)
    

numUniqueActors = len(set(from_list))
print(numUniqueActors)


valid_actors = ['DCM', 'GSP', 'DER', 'DTM']

eval = ""
body_count = 0
j = 0
m = 0
while os.path.isfile(f'{j}_ExpectedOperation.xml'):
    j += 1
j -=1
basePath = os.path.dirname('.')

while os.path.isfile(f'{m}_ExpectedOperation.csv'):
    m += 1
m -=1

if j < m:
        sys.exit("Error: Extra csv files exist")
elif j == m:
        print ("csv's match xml") 

#csv_File = open(f"{j}_ExpectedOperation.csv", "w", newline='')
#with open(args.output, 'w',newline='') as csvFile:
#with csv_File.write() as csvFile:
with open(f"{j}_ExpectedOperation.csv", "w", newline='') as csvFile:
    fileWriter = csv.writer(csvFile)
    fileWriter.writerow(['Actor', 'Message Eval Catagory', 'Current Time', 'Transit Time', 'Attack Status'])
    #print(range(len(required0)))
    
    for x in range(len(required0)):
        print(int(timestamp[x]))
        if int(timestamp[x]) > (time.time() + 3):
            print("Time in future check")
            print("ERR: Time in future")
        print(from_list[x])
        

        #print(from_list[x],to_list[x])
        print(type(from_list[x]))
        #print(type("gsp"))
        if from_list[x] not in valid_actors:
            print("ERROR! invalid From actor")
            eval = "ERR: Invalid FROM actor"
        elif to_list[x] not in valid_actors:
            print("ERROR! invalid To actor")
            eval = "ERR: Invalid TO actor"

        # check for element match with TIMESTAMP_Err list
        elif x in TIMESTAMP_Err:
            print("ERROR! old message stamp")
            eval = "ERR: Old message stamp"
            
        # check for same from and to actors
        elif to_list[x] == from_list[x]:
            print("ERROR! Same FROM and TO actor")
            eval = "ERR: Same FROM and TO actor"
        
        elif x in http_err:
            print("ERROR! non expected pair")
            eval = "ERR: Invalid HTTP method"

        elif from_list[x] or to_list[x] == 'GSP':
            print(target[x])
            if target[x] in request_count:
                request_count[target[x]] += 1
            else:
                request_count[target[x]] = 1

            #TODO: allow user to set timeframe and pass it in as an arg (int(timestamp[0]) + (args.timeframe * 3600)
            if request_count[target[x]] > 4 and int(timestamp[x]) < (int(timestamp[0]) + 86400):
                eval = "Ind"
                print("IND with count ",  request_count[target[x]])
            elif from_list[x] or to_list[x] == 'GSP':
                if target[x] in GSP_DCM:
                    print("EX")
                    eval = "Ex"
                else:
                    print("UX GSP")
                    eval = "Ux"
        
        elif from_list[x] or to_list[x] == 'DER':
            if from_list[x] == 'DER':
                if body[body_count] in DER_msg:
                    print("EX")
                    eval = "Ex"
                else:
                    print("UX DER")
                    eval = "Ux"
            body_count += 1
            if from_list[x] == 'DCM':
                if target[x] in DCM_msg:
                    print("EX")
                    eval = "Ex"
                else:
                    print("UX DCM")
                    eval = "Ux"
        

        required0 = soup.find_all(attrs={"type":True})
        # print(required0)
        body = []
        idx = 0
        for i in required0:
            #obtain the proposed type of the element you are currently indexing 
            t = i.attrs['type']
            text = i.get_text()
            try:
                #try to cast using the proposed type
                # if text.isalpha() and t == 'int': # check if we should try to cast a hex
                    # print(i.name,types[t](text,base=16))
                # else:
                print(i.name,types[t](text))
            except Exception as e:
                # attempt to cast 
                TYPE_Err.append(idx)
                print(e)
                print(f"\tERunable to cast {i.name} -- unexpected value")
                print("ERROR! Unexpected value")
                eval = "ERR: Unexpected Type"



        fileWriter.writerow([from_list[x], eval, timestamp[x], random.randint(15, 45)/100, 'No Attack'])
        print("file write")
        
        if from_list[-x-1] in history:
            if len(history[from_list[-x-1]]) < HIST:
                #add the most recent target
                history[from_list[-x-1]].append(target[-x-1])
                print(from_list[-x-1],"in list", x, history[from_list[-x-1]])
        #add the actor and thier target 
        elif from_list[-x-1] not in history:
            
            history[from_list[-x-1]] = [target[-x-1]]
            print(from_list[-x-1],"ADDED", x, history[from_list[-x-1]])
        
  
print(from_list)
print(to_list)


file = open("classifierDict.txt", "r")
contents = file.read()
dict = ast.literal_eval(contents)

#xml = ET.parse(args.file)
k = 0
while os.path.isfile(f'{k}_ExpectedOperation.xml'):
    k += 1
k -= 1
xml = ET.parse(f'{k}_ExpectedOperation.xml')

root = xml.getroot()

def getDataRecursive(element):
    data = list()

    # get attributes of element, necessary for all elements
    for key in element.attrib.keys():
        data.append(element.tag + '.' + key + ' ' + element.attrib.get(key))

    # only end-of-line elements have important text, at least in this example
    if len(element) == 0:
        if element.text is not None:
            data.append(element.tag + ' ' + element.text)

    # otherwise, go deeper and add to the current tag
    else:
        for el in element:
            within = getDataRecursive(el)

            for data_point in within:
                data.append(element.tag + '.' + data_point)

    return data
counter = 0
# print results
for x in getDataRecursive(root):
    #print("-- --")
    #print(x)
    if "TrustLog.dtm_log_entry.message.content.body." in x:
        if "type" not in x:
            new_x = x.replace("TrustLog.dtm_log_entry.message.content.body.{urn:ieee:std:2030.5:ns}", "")
            print("new_x", new_x)
            new_x = new_x.replace("{urn:ieee:std:2030.5:ns}","")
            print("new_x", new_x)
           
            new_x = new_x.split(" ")
            
            if new_x[0] in dict:
                valRange = dict[new_x[0]]
                #print(valRange)
                if len(valRange) > 1:
                    if int(new_x[1]) >= valRange[0] and int(new_x[1]) <= valRange[0]:
                        print(new_x[1])
                        print("Range is good")
                    else:
                        print(f'ERR! Out of range. Range is {valRange} but value used is {new_x[1]}')
                print("target is good")
            else:
                print("something is up")
            print(new_x[0])
            counter+=1

