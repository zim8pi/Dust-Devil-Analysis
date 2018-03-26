import glob
import math
import numpy as np
import matplotlib.pyplot as plt
import csv


filenames = sorted(glob.glob('DATA-0*.CSV'))

search_string = ";Version"


for f in filenames:
    print(f)
    
    with open(f, mode='r', encoding='iso-8859-1') as x:
        reader = csv.reader(y.replace('\0', '') for y in x)
        for row in reader:
            if search_string in row:
                print("I did it!")
                break
    
                
            
                    