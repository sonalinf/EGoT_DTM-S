import csv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, metavar='', help = 'name of the file that will be generated')
ap.add_argument('-t', '--time', required=True, metavar='', type=int, help = 'x axis (time in minutes)')
ap.add_argument('-i', '--index', required=False, metavar='', type=int, help = 'specific x axis. could be used to limit data (i.e 3 hours of data only)')
args = ap.parse_args()

actorList = {}
appendFlag = True
lastMessage = {}
activeActors = {}
MVoT_param = []

#set the last value for each of the actors
def setVal(row):
    for actor in actorList:
        if actor in activeActors:
           actorList[actor].append(lastMessage[actor]) 
        else:
            actorList[actor].append(0)
    
#get the most recent message for this time increment 
def getLastMessageInfo(row,value):
    actor = row[1]
    lastMessage[actor] = value
    if actor not in activeActors.values():
        activeActors.update({f'{actor}' : []})

#update time increment and toggle the append flag to false 
def inc_check(row, userTime):
    global appendFlag
    current_time = float(row)
    print('current_time = ', current_time)
    print('userTime = ', userTime)
    next_inc = float(current_time + (userTime))
    print('next_inc = ', next_inc)
    appendFlag = False
    return next_inc

#add an actor to the actor list 
def addActor(actor):
    actorList.update({f'{actor}' : []})

#reset list of actors 
def resetActiveActors():
    activeActors.clear

#create the MVoT parameter vs T csv file
def exportPlot(mvot):
    filename = MVoT_param[mvot]
    filename = filename + "_PerT"
    with open(f'{filename}.csv', 'w',newline='') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in actorList.items():
            print(f'value = {value}')
            if value:
                writer.writerow([key]+ value)
    print(f'{filename} has been created')

#provide the user with the MVoT options
def printMVoTOptions():
    print("Supported MVoT parameters:\n")
    #print(type(MVoT_param))
    idx = 0
    #print(len(MVoT_param))
    for x in MVoT_param:
        print(idx,"  ",x)
        idx+=1 

#open reader file
with open(args.file, 'r') as file:

    reader = csv.reader(file)
    index = 0
    MVoT_param = next(reader)

    #get actors
    for row in reader:
        index += 1
        actor = row[1]
        #check if actor is in actor list, if not add it
        if actor not in actorList.values():
            addActor(actor)

    row = 0
    index = 0

    #reset CSV file pointer
    file.seek(0)

    #skip header row
    next(reader)    
    printMVoTOptions()
    print("enter the number associated with the MVoT parameter")
    mvot = input()
    mvot = int(mvot)

    #traverse through the CSV file    
    for row in reader:
        if appendFlag == True:
            inc = inc_check(float(row[13]), args.time)
            print(f'non updating inc = {inc}')
            index += 1

        #get a new message only if the time inc hasnt been met
        if inc >= float(row[13]):
            getLastMessageInfo(row,row[mvot])

        #update output CSV file value
        if inc < float(row[13]):
            print('float(row[13] = ',float(row[13]))
            resetActiveActors()
            setVal(row)
            appendFlag = True
            print(f"next inc. inc = {inc}")

            #exit if index limit is reached
            if (args.index):
                if (args.index == index):
                    break 
        
    print(actorList)
    exportPlot(mvot)
