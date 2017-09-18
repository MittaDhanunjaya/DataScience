# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:15:35 2017

@author: dhanu
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import dataset
dataset= pd.read_csv('50_Startups.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:, 4].values

#Since we have categorical variable in the list. we need to encode this to integer by using 
#LabelEncoder
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:,3])
onehotencoder= OneHotEncoder(categorical_features=[3])
X=onehotencoder.fit_transform(X).toarray()
#to avoid dummy trap
X=X[:,1:]
#training and testing sets
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
#feature scaling
#fitting multiple linear regression to training set
from sklearn.linear_model import LinearRegression
regression= LinearRegression()
regression.fit(X_train, Y_train)
#predict the test results
Y_pred=regression.predict(X_test)
#Building optimal model using Backward Elimination
import statsmodels.formula.api as sm
X=np.append(arr=np.ones((50,1)).astype(int), values=X, axis=1)
X_opt=X[:,[0,1,2,3,4,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,1,3,4,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3,4,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()