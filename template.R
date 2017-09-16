#Here no need to import libraries in R as we do in python. 
#R will automatically includes all the necessary packages that are previously in-built with the application.
#select working directory.
#On the right hand select files and select the folder in which .csv file is present. and go to more and select set as working directory.
#include .csv file
dataset = read.csv('Data.csv') #Run this line 
#press View(dataset) in the console to confirm the .csv file in the program
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN= function(x) mean(x, na.rm= TRUE)),
                     dataset$Age)
dataset$Salary= ifelse(is.na(dataset$Salary),
                       ave(dataset$Salary,FUN= function(y) mean(y,na.rm=TRUE)),
                       dataset$Salary)
#Its time to encode the dependent elements into numbers as we have to apply mathematical equations on numbers.
dataset$Country= factor(dataset$Country,
                       levels=c('France', 'Spain', 'Germany')
                       labels=c(1,2,3))
#factor is used to encode the given set of elements(i.e., listed in levels) into numbers(i.e., listed in labels)
dataset$Purchased= factor(dataset$Purchased,
                         levels=c('No','Yes'),
                         labels=c(0,1))                       
#we need to split the whole set into training and testing sets. For this we need to install another library.
install.packages('caTools')
#Next we have to include it in the program.
library(caTools)
set.seed(123)
split=sample.split(dataset$Purchased, SplitRatio= 0.8)
training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)                       
#feature scaling
#we have to scale the elements since if we compare two elements those two should be in some less distance if u take sqrt(1324131^2-2^2)
                       #it would be very dominating.
training_set[,2:3]=scale(training_set[,2:3])
testing_set[,2:3]=scale(testing_set[,2:3])
