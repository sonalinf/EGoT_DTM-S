import sys
import csv
import time
import argparse
import random
from random import randrange

#take in user arguments
ap = argparse.ArgumentParser()

ap.add_argument('-f', '--file', required=True, metavar='', help = 'name of the file that will be generated')
ap.add_argument('-p', '--profile', required=True, metavar='', help = 'the profile deciding the type data is generated')
ap.add_argument('-n', '--number', required=True, metavar='', type=int, help = 'the number of data sets generated')
ap.add_argument('-i', '--increment', required=True, metavar='', type =float, help = 'time increment')
#optional args
ap.add_argument('-pa', '--profile_addon', required=False, metavar='', type=int, help = 'allows for random time steps for each data point')
ap.add_argument('-ma', '--mixed_args', nargs='+', required=False, metavar='', help= 'the profiles to be used in the mixed profile')

args = ap.parse_args()

profiles = ['ideal', 'random', 'flawed', 'almost_good', 'almost_bad', 'mixed']
mixedFlag = False

#fileWriter = csv.writer(csvFile)
if args.profile not in profiles:
    print(f"please specify a valid profile. '{args.profile}' is not a valid option")
    print("here are the options: ")
    print(profiles)
    quit()

#this ideal profile only generates expected data
def ideal_profile(fileWriter,num_datapoints, mixedCounter):
    num_datapoints = int(num_datapoints) * 4
    actorList = ['DER','DCM','DERAS','DTM']
    randomIndexA = randrange(len(actorList))
    actor = actorList[randomIndexA]
    num_datapoints_rand = int(num_datapoints) * 4
    inc = 0
    if(args.profile_addon == 1):
        for x in range(num_datapoints_rand+1):
            randVar = random.randint(0, 10)
            randomIndexA = randrange(len(actorList))
            actor = actorList[randomIndexA]
            fileWriter.writerow([actor, 'Ex', '%f' % (time.time() + randVar), random.randint(15, 45)/100, 'No Attack'])
    
    elif(args.profile_addon == 2):
        print("here")
        print(args.increment)
        for x in range(num_datapoints_rand+1):
            randomIndexA = randrange(len(actorList))
            actor = actorList[randomIndexA]
            inc += args.increment 
            fileWriter.writerow([actor, 'Ex', '%f' % (time.time() + rand_timestep[x] + inc), random.randint(15, 45)/100, 'No Attack'])
    else:
        global mixedFlag
        print("num_datapoints IDEAL:", num_datapoints)
        if (mixedFlag):
            for idx in range(num_datapoints+1):
                fileWriter.writerow([actorList[idx%(len(actorList))] , 'Ex', '%f' % (time.time() + args.increment * mixedCounter), random.randint(15, 45)/100, 'No Attack'])
                print("mixedCounter IDEAL", mixedCounter)
                mixedCounter += 1
            return mixedCounter
        else:
            for x in range(num_datapoints+1):
                fileWriter.writerow([actorList[x%(len(actorList))] , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])

                '''
                fileWriter.writerow(['DCM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
                fileWriter.writerow(['DERAS' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DTM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            '''
            
    return

#this radom profile generates ex, Ux, ind, or n data
def random_profile(fileWriter,num_datapoints, mixedCounter):
    messageList = ['Ex','Ux','Ind','N', 'Dis', 'Err']
    actorList = ['DER','DCM','DERAS','DTM']
    num_datapoints = int(num_datapoints) * 4
    rand_timestep = random.sample(range(1, 86400), num_datapoints)
    rand_timestep.sort()
    print("num_datapoints RANDOM:", num_datapoints)
    global mixedFlag
    if (mixedFlag):
        for idx in (range(num_datapoints+1)):
            randomIndexM = randrange(len(messageList))
            message = messageList[randomIndexM]

            randomIndexA = randrange(len(actorList))
            actor = actorList[randomIndexA]
            fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * mixedCounter) , random.randint(15, 45)/100, 'No Attack'])
            mixedCounter += 1
            print("mixedCounter RANDOM", mixedCounter)
        return mixedCounter
    else:
        for x in (range(num_datapoints+1)):
            randomIndexM = randrange(len(messageList))
            message = messageList[randomIndexM]

            randomIndexA = randrange(len(actorList))
            actor = actorList[randomIndexA]
            if(args.profile_addon == 1):
                fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + rand_timestep[x]) , random.randint(15, 45)/100, 'No Attack'])  
            else:
                fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * x) , random.randint(15, 45)/100, 'No Attack'])
    return 

#this flawed profile  
def flawed_profile(fileWriter,num_datapoints, mixedCounter):
    messageList = ['Ux','Ind','N', 'Dis', 'Err']
    actorList = ['DER','DCM','DERAS','DTM']
    num_datapoints = int(num_datapoints) * 4
    rand_timestep = random.sample(range(1, 86400), num_datapoints)
    rand_timestep.sort()
    print("num_datapoints FLAWED:", num_datapoints)
    global mixedFlag
    if (mixedFlag):
        
        for idx in (range(num_datapoints+1)):
            randomIndex = randrange(len(messageList))
            message = messageList[randomIndex]

            randomIndexA = randrange(len(actorList))
            actor = actorList[randomIndexA]
            fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * mixedCounter), random.randint(15, 45)/100, 'No Attack'])
            mixedCounter += 1
            print("mixedCounter FLAWED", mixedCounter)
        return mixedCounter
    else:
        for x in range(num_datapoints+1):
            randomIndex = randrange(len(messageList))
            message = messageList[randomIndex]

            randomIndexA = randrange(len(actorList))
            actor = actorList[randomIndexA]

            if(args.profile_addon == 1):
                fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + rand_timestep[x]) , random.randint(15, 45)/100, 'No Attack'])
            else:
                fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    return 

def almost_ideal(fileWriter,num_datapoints):
    num_datapoints_rand = int(num_datapoints) * 4
    rand_timestep = random.sample(range(1, 86400), num_datapoints_rand)
    rand_timestep.sort()
    actorList = ['DER','DCM','DERAS','DTM']
    randomIndexA = randrange(len(actorList))
    
    
    for x in range(num_datapoints_rand - (int(num_datapoints_rand / 10))):
        actor = actorList[randomIndexA]
        num_datapoints_rand = int(num_datapoints) * 4
        fileWriter.writerow([actor, 'Ux', '%f' % (time.time() + rand_timestep[x]), random.randint(15, 45)/100, 'No Attack'])

    for x in range(int(num_datapoints_rand / 10)):
        actor = actorList[randomIndexA]
        num_datapoints_rand = int(num_datapoints) * 4
        fileWriter.writerow([actor, 'Ex', '%f' % (time.time() + rand_timestep[x]), random.randint(15, 45)/100, 'No Attack'])


    return

def almost_flawed(fileWriter,num_datapoints):
    num_datapoints_rand = int(num_datapoints) * 4
    rand_timestep = random.sample(range(1, 86400), num_datapoints_rand)
    rand_timestep.sort()
    actorList = ['DER','DCM','DERAS','DTM']
    num_datapoints_rand = int(num_datapoints) * 4
   
    for x in range(num_datapoints_rand - (int(num_datapoints_rand / 10))):
        randomIndexA = randrange(len(actorList))
        actor = actorList[randomIndexA]
        fileWriter.writerow([actor, 'Ux', '%f' % (time.time() + rand_timestep[x]), random.randint(15, 45)/100, 'No Attack'])
           
    for x in range(int(num_datapoints_rand / 10)):
        randomIndexA = randrange(len(actorList))
        actor = actorList[randomIndexA]
        fileWriter.writerow([actor, 'Ex', '%f' % (time.time() + rand_timestep[x]), random.randint(15, 45)/100, 'No Attack'])
          
    return 

def mixed(fileWriter,num_datapoints):
    x = len(args.mixed_args)
    num_datapoints_per_profile = int(num_datapoints / x)
    print("num_datapoints_per_profile", num_datapoints_per_profile)
    # check args to be valid
    global mixedFlag
    mixedFlag = True 
    print("mix counter reset")
    counter = 0
    for idx in args.mixed_args:
        if idx not in profiles:
            print(f"please specify a valid profile. '{idx}' is not a valid option")
            print("here are the options: ")
            print(profiles)
            quit()
        if (idx == "ideal"):
             counter += ideal_profile(fileWriter,num_datapoints_per_profile, counter)
        elif (idx== "random"):
             counter +=  random_profile(fileWriter,num_datapoints_per_profile, counter)
        elif(idx == "flawed"):
             counter +=  flawed_profile(fileWriter,num_datapoints_per_profile, counter)
        elif(idx == "almost_good"):
             counter =  almost_ideal(fileWriter,num_datapoints_per_profile)
        elif(idx == "almost_bad"):
             counter = almost_flawed(fileWriter,num_datapoints_per_profile)
       
        print(counter)
    print(x)
    print(args.mixed_args)
    return

#create and write to csv file
#TODO: check if the file name aleady exists to avoid overwrite 
with open(args.file, 'w',newline='') as csvFile:
    fileWriter = csv.writer(csvFile)
    num_datapoints = args.number
    fileWriter.writerow(['Actor', 'Message Eval Catagory', 'Current Time', 'Transit Time', 'Attack Status'])
    #get information from data generator 
    if (args.profile == "ideal"):
        ideal_profile(fileWriter,num_datapoints, 0)
    elif (args.profile == "random"):
        random_profile(fileWriter,num_datapoints, 0)
    elif(args.profile == "flawed"):
        flawed_profile(fileWriter,num_datapoints, 0)
    elif(args.profile == "almost_good"):
        almost_ideal(fileWriter,num_datapoints)
    elif(args.profile == "almost_bad"):
        almost_flawed(fileWriter,num_datapoints)
    elif(args.profile == "mixed"):
        mixed(fileWriter,num_datapoints)

#TODO: use xml file comparison against the xsd to determine EX, Ux, Ind, N instead of these 
# values being hardcoded in 

#TODO: look at python library xmlschema 

#TODO: create a profile where everything goes right until the end