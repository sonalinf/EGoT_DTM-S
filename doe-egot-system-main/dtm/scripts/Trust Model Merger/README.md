### Running CDTA Merger Script 
````
python3 merger.py -f [FILE 1] [FILE 2] ... [FILE N] -o [OUTPUT FILE]
````
All thats needed to run the CDTA merger script is to list all the csv files that you would like to merger 
in the current directory and the name of the output file. 

### Example
````
python3 merger.py -f test1_SimOut.csv test2_SimOut.csv. testN_SimOut.csv [...] -o outputMerger.csv
````
