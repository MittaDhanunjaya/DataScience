#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#set working directory... In windows go for the fileExplorer tab in the right side
#and select the .csv file and try to write this code in the same folder in which .csv file exists.
#import .csv file
dataset = pd.read_csv('Data.csv')
#Here we need to take two matrices one for non-dependent variables and one for dependent variables.
X = dataset.ilog[: , :-1].values #This will select all rows and columns except that last column
Y = dataset.ilog[: , 3].values #This will select all rows and the last column.
# Take care of missing elements
from sklearn.preprocessing import Imputer 
imputer =Imputer(missing_values='NaN', strategy='mean', axis=0, verbose=0, copy=True)
#axis=0 for column wise mean and 1 for row wise mean
imputer=imputer.fit(X[:, 1:3])
X[:, 1:3]= imputer.transform(X[:,1:3])
