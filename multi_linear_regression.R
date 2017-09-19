#import dataset
dataset = read.csv('50_Startups.csv')
# dataset = dataset[, 2:3]
#encoding categorical data
dataset$State=factor(dataset$State,
                     levels=c('New York','California','Florida'),
                     labels=c(1,2,3))
#training and testing sets
#install.packages('caTools')
library(caTools)
set.seed(123)
split=sample.split(dataset$Profit,SplitRatio = 0.8)
training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)
#feature scaling
# training_set[,2:3]=scale(training_set[,2:3])
# testing_set[,2:3]=scale(testing_set[,2:3])
#Fitting Multiple Linear Regression to the training set
#The simple way to write the forula is linear diff. bt dependent variable and .i.e., it includes all the independent variables
regressor=lm(formula = Profit ~ .,
             data=training_set)
#check summary(regressor) in the console to know the significance of the independent variables
#predicting the test set results
Y_pred= predict(regressor,newdata = testing_set)
#Building the optimal model by using backward elimination
regressor=lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
             data=dataset)
summary(regressor)
regressor=lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend ,
             data=dataset)
summary(regressor)
regressor=lm(formula = Profit ~ R.D.Spend  + Marketing.Spend ,
             data=dataset)
summary(regressor)
regressor=lm(formula = Profit ~ R.D.Spend ,
             data=dataset)
summary(regressor)