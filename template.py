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
