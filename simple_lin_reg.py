# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:03:37 2017

@author: dhanu
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[: , :-1].values #independent values
Y= dataset.iloc[: , 1].values #dependent values
#training and testing set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y, test_size=1/3, random_state=0)
#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)"""
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(X_train,Y_train)
#predecting the test results
Y_pred=regressor.predict(X_test)
#visualizing the training set results
plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(Training set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()
#visualizing the testing set results
plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(Test set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()