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