import numpy as np
from os import listdir
import math 
#Returns the info from the CSV as an array, pulled from the given path. This one
# is for a single file, while read_dir is for multiple
def read_dd_csv(path):
    data = np.genfromtxt(path, comments = ';', delimiter = ',', filling_values = math.nan)
    
    f = open(path, 'r')
    for i in range(3):#3 reads the third line and is OS dependent 
        line = f.readline()
    tokens = str.split(line, ',') #splits up the CSV by commas
    f.close()
    
    data = data[:,:4]
    #**Change path to only file name at some point**
    return path, tokens[1], tokens[2], data
        
def read_dir(path):
    files = listdir(path)
    csvs = [f for f in files if f[-4:].lower()=='.csv'] #checks the last four characters 
    
    return [read_dd_csv(f) for f in csvs]

