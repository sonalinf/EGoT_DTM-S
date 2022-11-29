# Trust Model Simulator and Data Generator 
Trust model simulator and data generator to test the latest MVoT calculations.

## System
Both the trust model simulator and data generator have been tested on Linux and macOS.<br />
This how-to guide mimics the process on a Linux machine running Ubuntu 20.04.1 LTS.<br />
This is a Python-based program tested on Python 3.8.5. Other versions of Python3 should 
work but haven't been tested.

## Dependencies 
To run the simulator, the Pandas library must be installed. <br />
To install Pandas, start by installing pip3
````
sudo apt install python3-pip
````

Once pip3 is installed, install Pandas

````
pip3 install pandas
````

## Running the Trust Mode Data Generator
````
python3 TMsimDataGenerator.py -f [FILENAME] -p [PROFILE] -n [NUMBER OF DATA POITNS] -i [TIMESTEP] -pa {optional} [PROFILE ADDONS] -ma {optional} [MIXED ARGS] -db {optional} [DER BIAS]
````
FILENAME - The name of the file you are generating. This must be a csv file (.csv) <br />

PROFILE - The profile you want the generated data to be. Pick one of the profiles available below. <br />
    ideal - This profile only generates expected data<br />
    random - This randomly assigns a message evaluation to a random actor <br />
    flawed - This profile generates no expected messages<br />
    almost_good - This profile generates expected messages until the last set <br />
    almost_bad - This profile generates Ux, Ind, Dis, N messages until the last set<br />

N DATA POINTS - The number of messages to be generated per actor <br />

TIMESTEP - The increment between each message <br /> 

PROFILE ADDONS - Allows for special funcitonality in some profiles <br />
    Random profile - if PROFILE ADDONS is 1, each data point will have a random timestamp <br />
    almost_good - if PROFILE ADDONS is not zero, PROFILE ADDONS value will be where a UX message is added <br />
    almost_bad - if PROFILE ADDONS is not zero, PROFILE ADDONS value will be where a EX message is added <br />

MIXED ARGS - Allows the user to specify the profiles to be used in the mixed profile <br />

DER BIAS - Alows the user to specify how many more DERs should be generated 
### Example 
````
python3 TMsimDataGenerator.py -f test.csv -p ideal -n 100 -i 1
````
This example generates a file called test.csv, the message evaluation for all the actors will be expected. <br />
There will be 100 messages per actor (400 messages total) and there is 1-sec step in the time

````
python3 TMSimDataGenerator.py -f testMixed.csv -p mixed -n 100 -i 1 -ma ideal mixed flawed
````
This example generates a file called testMixed.csv, the message evaluation will be mixed between ideal, mixed, and flawed. <br />

