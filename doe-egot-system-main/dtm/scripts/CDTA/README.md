# Trust Model Simulator and Data Generator 
Trust model simulator and data generator to test the latest MVoT calculations.

## System
Both the trust model simulator and data generator have been tested on Linux and macOS.<br />
This how-to guide mimics the process on a Linux machine running Ubuntu 20.04.1 LTS.<br />
This is a Python-based program tested on Python 3.8.5. Other versions of Python3 should 
work but haven't been tested.


## Running CDTA Alert Script
````
python3 CDTA_alert.py -f [FILENAME] -ta [GROUP THRESHOLD]
````
FILENAME - The name of the file you are generating. This must be a csv file (.csv) <br />

GROUP THRESHOLD - A limit for actors exceeding their threshold. Exceeding this will generate a 
group specific alert<br />

### Example 
````
python3 CDTA_alert.py -f TestTSLC.csv -ta 20
````
This example would read in TestTSLC.csv as an input and provide the user with the avaialble parameters (MVoTs).<br />
The user will select the MVoT parameter they are interested in and the program will generate a local alert with the 
number of actors exceeding the 20 actor threshold.
### Options
````
1 	 Actor
2 	 Message Eval Catagory
3 	 Current Time
4 	 Transit Time
5 	 trust score
6 	 reputation
7 	 distrust score
8 	 certainty
9 	 relative factor of certainty
10 	 expected message count
11 	 unexpected message count
12 	 total message count
13 	 time stamp
14 	 registration date
15 	 communication frequency
16 	 message transit time
17 	 average transit time
18 	 time since last communication
19 	 timeout count
20 	 alert count
21 	 other action count
22 	 SD transit time
23 	 Max CommFreq
24 	 Min TSLC
25 	 DTM response
Enter the number associated with the MVoT parameter: 18
````

### Output
````
['time since last communication'] threshold err row 1926 actor DERAS_1
['time since last communication'] threshold err row 1927 actor DTM_1
['time since last communication'] threshold err row 3848 actor DER_2
['time since last communication'] threshold err row 3849 actor DCM_2
['time since last communication'] threshold err row 3850 actor DERAS_2
['time since last communication'] threshold err row 3851 actor DTM_2
['time since last communication'] threshold err row 4 actor DER_0
['time since last communication'] threshold err row 5 actor DCM_0
['time since last communication'] threshold err row 6 actor DERAS_0
['time since last communication'] threshold err row 7 actor DTM_0
['time since last communication'] threshold err row 1928 actor DER_1
['time since last communication'] threshold err row 1929 actor DCM_1
['time since last communication'] threshold err row 1930 actor DERAS_1
['time since last communication'] threshold err row 1931 actor DTM_1
['time since last communication'] threshold err row 3852 actor DER_2
['time since last communication'] threshold err row 3853 actor DCM_2
['time since last communication'] threshold err row 3854 actor DERAS_2
['time since last communication'] threshold err row 3855 actor DTM_2
['time since last communication'] threshold err row 8 actor DER_0
['time since last communication'] threshold err row 9 actor DCM_0
['time since last communication'] threshold err row 10 actor DERAS_0
['time since last communication'] threshold err row 11 actor DTM_0
['time since last communication'] threshold err row 1932 actor DER_1
23 Violations found
3 actors have exceeded the time since last communication threshold you set (20)
````