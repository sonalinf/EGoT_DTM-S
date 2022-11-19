import csv
import argparse
import ast

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, metavar='', help = 'name of the input file')
#ap.add_argument('-t', '--thresh', required=True, metavar='', help = 'threshold file')
ap.add_argument('-ta', '--threshalert', required=True, type=int, help = 'number of actors exceeding a threshold before sending a message')
args = ap.parse_args()

#load in threshold information into dictionaries
threshDict_over = {
    "distrust score" : 50,
    "timeout count": 2,
    "alert count" : 2,
    "time since last communication": 700
}

threshDict_under = {
    "trust score" : .1,
    "certainty" : .1,
    "relative factor of certainty": .5,
    "communication frequency": 1,
}

MVoT_param = []

def printMVoTOptions():
    print("MVoT parameters:\n")
    #print(type(MVoT_param))
    idx = 0
    #print(len(MVoT_param))
    for x in MVoT_param:
        if idx > 0:
            print(idx,"\t",x)
        idx+=1 

with open(args.file, 'r') as file:

    reader = csv.reader(file)
    MVoT_param = next(reader)

    print(MVoT_param)
    
    #skip header row
    next(reader)    
    printMVoTOptions()
    print("Enter the number associated with the MVoT parameter")
    mvot = input()
    mvot = int(mvot)
    cnt = 0

    for row in reader:
        if MVoT_param[mvot] in threshDict_over:
            if float(row[mvot]) > threshDict_over[MVoT_param[mvot]]:
                print(f'{[MVoT_param[mvot]]} threshold err row {row[0]} actor {row[1]}')
                cnt += 1
        elif MVoT_param[mvot] in threshDict_under:
            if float(row[mvot]) < threshDict_under[MVoT_param[mvot]]:
                 print(f'{[MVoT_param[mvot]]} threshold err row {row[0]} actor {row[1]}')
                 cnt += 1

        else:
            print(f'Parameter has no threshold!')
            break
    
    print(f'{cnt} Violations found')
    
    if cnt >= args.threshalert:
        print(f'{cnt-args.threshalert} actors have exceeded the {MVoT_param[mvot]} threshold you set ({args.threshalert})')
        


