import glob
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
#Stores all file names that follow the pattern "DATA-##.CSV" in the 
#current directory
filenames = sorted(glob.glob('DATA-0*.CSV'))

#Grabbing the line before start time because the loop I have
#set up reads the next line
search_string = ";Version"
files_in_range = []

for a in filenames:
    #scanning the file for the right line, then grabbing the numbers that are
    #on the next line
    with open(a, mode='r', encoding='iso-8859-1') as x:
        reader = csv.reader(y.replace('\0', '') for y in x)
        for row in reader:
            if search_string in row:
                line = x.readline()
                tokens = str.split(line, ',')
                start_time = tokens[2]
                start_date = tokens[1]
                
                start_date_split = start_date.split('-') #splits the date into its components
                year = int(start_date_split[0])
                month = int(start_date_split[1])
                day = int(start_date_split[2])
                print(year, month, day)
                
                if year == 2017 and month in range(7,9):
                    files_in_range.append(a)
                    print(a)
                    break
                break
        
    
#Using glob to go through this process with every CSV file. It will create a graph
#of pressure v time for each given CSV
for f in files_in_range:
    #Creating the data array that will hold the first four rows
    data = np.genfromtxt(f, comments = ';', delimiter = ',', filling_values = math.nan)
    data = data[:,:4]
                    