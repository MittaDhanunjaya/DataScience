#import necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
#include dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

#Splitting the dataset into training and test sets
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
Sc_X = StandardScaler()
Sc_Y = StandardScaler()
X_train = Sc_X.fit_transform(X_train)
X_test = Sc_X.transform(Y_test)
Y_train = Sc_Y.fit_transform(Y_train)
Y_test = Sc_Y.transform(Y_test)

# Fitting the Regression Model(SVR) to the dataset
# Create your regressor here
from sklearn.svm import SVR 
regressor=SVR(kernel='rbf')
regressor.fit(X,Y)
# Predicting a new result
y_pred = regressor.predict(6.5)

# Visualising the SVR results
plt.scatter(X, Y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()