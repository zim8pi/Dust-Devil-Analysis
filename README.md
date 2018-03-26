# Dust-Devil-Analysis

## Pressure-Time-Processing.py 

###Overview:

This program runs from whatever directory it is in, and grabs all the .csv files with the format "DATA-###.csv" where "###" is some number. It takes the time and pressure data and plots it with titles for every .csv file it is given. 

###Running:

In order to run this code, simply download it, ensure that the desired files to be processed are in the same directory, and run it. It will automatically grab the .csv files from the current directory and do its analysis on them. 

###Known Bugs/Issues:

Currently, this code does not handle corrupted files if the corruption happens farther than the first few rows. If it hits a corrupted cell, it will immediately exit the code and return an error without completing the other .csv files. 


	
	

