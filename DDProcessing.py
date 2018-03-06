import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #pandas package to be used for reading the csv

df = pd.read_csv('Time_Pressure.csv')

pressure_data = np.array
time_data = np.array

pressure_data = df.V2
time_data = df.V1

#Saving the start time variable (it's a string) so it can be converted and used
start_time = pressure_data[0]

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

#Declaring "trash" arrays to throw out values that are > 10*stdev
#pTrash = []
#tTrash = []

#Iterates through pressure_data, and "throws away" values that are too far off

#np.where (??) -- not a good option as the array created only gives the indices
#of the values where the condition is met, meaning there would still need to be 
#a loop in place to append those values to the pTrash and tTrash arrays in 
#order to be deleted from the value arrays


ind = (abs(pressure_data) > (10*stdev))

masked_time = time_data[ind]
masked_pressure = pressure_data[ind]


#for x in range(0,pd_size):
#    if abs(pressure_data[x]) > (10*stdev):
#        pTrash.append(pressure_data[x])
#        tTrash.append(time_data[x])
#        
#pressure_data[~np.in1d(pressure_data,pTrash).reshape(pressure_data.shape)]
#time_data[~np.in1d(time_data,tTrash).reshape(time_data.shape)]   

plt.plot(masked_time, masked_pressure, '.', ls='')
plt.title("Pressure vs Time")
plt.xlabel("Time (Julian Day)")
plt.ylabel("Pressure (Pa)")
plt.show()


    

    