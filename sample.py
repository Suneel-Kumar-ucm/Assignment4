import pandas as pd
import matplotlib.pyplot as plt

#Reading the provided CSV file ‘data.csv’.
data = pd.read_csv('D://data.csv')

# Showing the basic statistical description about the data.
description = data.describe()

# Check if the data has null values.
# And then Replace the null values with the mean

check_null = data.isnull().sum()

replace_value = data['Calories'].mean()


data['Calories'].fillna(data['Calories'].mean(), inplace=True)

sele_col = data[['Duration','Calories']]

# Select at least two columns and aggregate the data using: min, max, count, mean.
total = sele_col.aggregate(['min','max','count','mean'])

# Filter the dataframe to select the rows with calories values between 500 and 1000.
betw_cal = data[(data['Calories'] >= 500) & (data['Calories'] <= 1000)]

# Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
in_cal = (data[(data['Calories'] < 100)]).append(data[(data['Calories'] > 500)])

#Create a new “df_modified” dataframe that contains all the columns from df except for
#“Maxpulse”.
df_modified = data.drop('Maxpulse', axis=1)

#. Delete the “Maxpulse” column from the main df dataframe
data.drop('Maxpulse', axis=1, inplace=True)

#Convert the datatype of Calories column to int datatype.
data['Calories'] = data['Calories'].astype(int)

#Using pandas create a scatter plot for the two columns (Duration and Calories)
plt.scatter(data['Duration'], data['Calories'])
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()