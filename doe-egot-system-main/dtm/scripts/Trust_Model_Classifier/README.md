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

## Running the Trust Mode Classifier
````
python3 classifier.py -f [FILENAME.xml] -o [OUTPUTFILE.csv]
````
FILENAME - The name of the file you are classifying. This must be a XML file (.xml) <br />

OUTPUTFILE - The name of the output file. This must be a CSV file. 
### Example 
````
python3 classifier.py -f ExpectedOperation.xml -o ExpectedOperation.csv
````
This example will classfying the messages found in ExpectedOperation.xml. <br />
The classification results are written to ExpectedOperation.csv
