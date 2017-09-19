# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 08:54:25 2017

@author: dhanu
"""
#import required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importing the dataset
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:2].values
Y=dataset.iloc[:,2].values
"""#training and testing the dataset
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X, Y, test_size=0.2, random_state=0)"""

#Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X,Y)
#Fitting Polyniómial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)
lin_reg2=LinearRegression()
lin_reg2.fit(X_poly,Y)
#Visualizing the Linear Regression model
plt.scatter(X,Y, color='red')
plt.plot(X,lin_reg.predict(X), color='green')
plt.title('Truth or Bluff(Linear Regression)')
plt.xlabel('position level')
plt.ylabel('Salary')
plt.show()
#Visualize the polynomial regression model
X_grid = np.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,Y, color='red')
plt.plot(X_grid,lin_reg2.predict(poly_reg.fit_transform(X_grid)), color='green')
plt.title('Truth or Bluff(Polynomial Regression)')
plt.xlabel('position level')
plt.ylabel('Salary')
plt.show()
#Increase the degree by 1 to get the exact curve and the exact results.
#predict a new result with linear regression model
lin_reg.predict(6.5)
#predict a new value with polynomial regression model
lin_reg2.predict(poly_reg.fit_transform(6.5))