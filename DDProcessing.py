import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #pandas package to be used for reading the csv

df = pd.read_csv('Time_Pressure.CSV')

pressure_data = np.array
time_data = np.array

pressure_data = df.V2
time_data = df.V1

#Saving the start time variable (it's a string) so it can be converted and used
start_time = pressure_data[0]
print(start_time)
start_time_split = start_time.split(':')

hour = start_time_split[0]
minute = start_time_split[1]
second = start_time_split[2]

#Putting the columns into numpy arrays
pressure_data = np.array(pressure_data)
time_data = np.array(time_data)

#Deleting the start_time string that is at the beginning of both arrays
pressure_data = np.delete(pressure_data, [0])
time_data = np.delete(time_data, [0])

#Changing the variable types to floats intstead of strings
pressure_data = pressure_data.astype(np.float)
time_data = time_data.astype(np.float)
 
#defining a function for the Median Absolute Deviation, which is 
def mad(a):
    med = np.median(a)
    mad = np.median(np.absolute(a - med))
    
    return mad    

#Saving the value for Standard Deviation, so that data points that are more 
#than 10 standard deviations away may be discarded    
stdev = 1.4826 * mad(pressure_data)

pd_size = pressure_data.size

ind = (abs(pressure_data) > (10*stdev))

#Keeping only values that are within 10 standard deviations
masked_time = time_data[ind]
masked_pressure = pressure_data[ind]
 

plt.plot(masked_time, masked_pressure, '.', ls='')
plt.title("Pressure vs Time")
plt.xlabel("Time (Julian Day)")
plt.ylabel("Pressure (Pa)")
plt.show()


    

    