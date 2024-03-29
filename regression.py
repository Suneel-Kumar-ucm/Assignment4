# Simple Linear Regression
# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the datasets
 
datasets = pd.read_csv("C:/Salary_Data.csv") #getting the csv file

X = datasets.iloc[:, :-1].values #splitting the dataset values
Y = datasets.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=1/3, random_state = 0)

# Fitting Simple Linear Regression to the training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)

# Predicting the Test set result  

Y_Pred = regressor.predict(X_Test)

#calculating mean squared error

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(Y_Test, Y_Pred)
print("Mean Squared Error:", mse)



# Visualising the Training set results


plt.scatter(X_Train, Y_Train, color='red')
plt.plot(X_Train, regressor.predict(X_Train), color='blue')
plt.title("Salary vs Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# Visualising the Test set results
plt.scatter(X_Test, Y_Test, color='red')
plt.plot(X_Train, regressor.predict(X_Train), color='blue')
plt.title("Salary vs Experience (Test Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()