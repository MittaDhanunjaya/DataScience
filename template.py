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
#we have successfully filled up the missing elements and now we have to encode the country and dependent variables
#Since, age and salary doesn't effect the whole 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X= LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0]) #Now we have encoded the entire country column into numbers but this is not we need.
#we are not going to convey that the higher number indicates the larger country. So, we need to encode this into a matrix. 
onehotencoder= OneHotEncoder(categorical_features=[0])
X= onehotencoder.fit_transform(X).toarray()
labelencoder_Y= LabelEncoder()
Y= labelencoder_Y.fit_transform(Y)
#Now we have to split the table into training sets and testing sets.
# Since we are doing it in a machine learning we have to train the machine and test it to the results.
from sklearn.cross_validation import train_test_split
X_training,X_testing,Y_training,Y_testing = train_test_split(X,Y,test_size=0.2,random_state=0)
#Now we have to scale the elements to make comparitive.
#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)
#Generally we don't have to use take care of missing elements, scaling and encoding.
