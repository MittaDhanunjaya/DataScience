#import dataset
# dataset = dataset[, 2:3]
#training and testing sets
#install.packages('caTools')
library(caTools)
set.seed(123)
split=sample.split(dataset$Salary,SplitRatio = 2/3)
training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)
#feature scaling
# training_set[,2:3]=scale(training_set[,2:3])
# testing_set[,2:3]=scale(testing_set[,2:3])
regressor=lm(formula = Salary ~ YearsExperience,
             data=training_set)
#predict the test results
Y_pred= predict(regressor,testing_set)
#visualizing the training results
#install.packages('ggplot2')
ggplot()+
  geom_point(aes(x=training_set$YearsExperience,y=training_set$Salary),
             colour='red')+
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata = training_set)),
            colour='blue')+
  ggtitle('Salary vs YearsExperience(Training set)')+
  xlab('Experience')+
  ylab('Salary')
ggplot()+
  geom_point(aes(x=testing_set$YearsExperience,y=testing_set$Salary),
               colour='red')+
  geom_line(aes(x=testing_set$YearsExperience,y=Y_pred),
            colour='green')+
  ggtitle('Salary vs Experience(Testing set)')+
            xlab('Experince')+
            ylab('Salary')
