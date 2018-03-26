import glob
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
#Stores all file names that follow the pattern "DATA-##.CSV" in the 
#current directory
filenames = sorted(glob.glob('DATA-0*.CSV'))

#Grabbing the line before start time because the loop I have
#set up reads the next line
search_string = ";Version"
#Declaring the arrays for time and pressure
pressure_data = []
time_data = []

#Defining a function for the median absolute deviation in order to throw out 
#values that are more than 10 stdev away
def mad(a):
    med = np.median(a)
    mad = np.median(np.absolute(a - med))
    return mad 

for a in filenames:
    #scanning the file for the right line, then grabbing the numbers that are
    #on the next line
    with open(a, mode='r', encoding='iso-8859-1') as x:
        reader = csv.reader(y.replace('\0', ' ') for y in x) #replace empty values
        next(reader, None)
        for row in reader:
            if search_string in row: #Searches for start date/time so that it can be grabbed and used
                line = x.readline()
                tokens = str.split(line, ',')
                start_time = tokens[2]
                start_date = tokens[1]
                
                start_date_split = start_date.split('-') #splits the date into its components
                year = int(start_date_split[0])
                month = int(start_date_split[1])
                day = int(start_date_split[2])
                
                start_time_split = start_time.split(':') #splits the the time into its components
                hour = int(start_time_split[0])
                minute = int(start_time_split[1])
                second = float(start_time_split[2])
                
                if year == 2017 and month in range(7,9): #only uses the data for graphing if it is in range
                    print(a)
                    df = pd.read_csv(a, encoding="ISO-8859-1", header=None, usecols=[0,1]) #Grabbing the col needed
                    time_data = df.iloc[8:,:1] #From row 8 to the EOF for time data
                    pressure_data = df.iloc[8:,1:2] #From row 8 to EOF for pressure data
                    
                    #Turning the strings from the dataframes into numbers
                    #TODO: Build a try/catch to toss out corrupted data that can happen deep in file
                    pressure_data = pressure_data.apply(pd.to_numeric) 
                    time_data = time_data.apply(pd.to_numeric)
                    
                    #Gets rid of data that's more than 10 stdev away from MAD
                    stdev = 1.4826 * mad(pressure_data)
                    ind = (abs(pressure_data) > (10*stdev))
                    
                    masked_pressure = pressure_data[ind]
                    
                    #Create plots for each set of data
                    plt.plot(time_data, masked_pressure, '.', ls='')
                    plt.title("Pressure vs Time from " + str(a))
                    plt.xlabel("Time (sec from " + str(start_time) + "on " + str(start_date) + ")")
                    plt.ylabel("Pressure (Pa)")
                    plt.show()
                           
            
        
   
    
    
    
    
    
                    