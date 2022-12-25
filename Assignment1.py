#Q9) Calculate Skewness, Kurtosis & draw inferences on the following data Cars speed and distance
#Use Q9_a.csv

import pandas as pd
import numpy as np
import scipy as sp

#reading CSV file
data = pd.read_csv('file/Q9_a.csv')

#Finding Speed data
speed = data['speed'].values

#Printing Skewness and Kurtosis
print("Skewness of Speed:",round(sp.stats.skew(speed,axis=0,bias=True),4))
print("Kurtosis of Speed:",round(sp.stats.kurtosis(speed,axis=0,bias=True),4))

#Finding distance data
distance = data['dist'].values

#Printing skewness and kurtosis of distance
print("Skewness of Distance:", round(sp.stats.skew(distance,axis=0, bias=True),4))
print("Kurtosis of Distance:", round(sp.stats.kurtosis(distance, axis=0, bias=True),4))









