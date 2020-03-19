'''
Created March 16, 2020
Author: Tucker Celestine

Memo: This script is an exercise using the ML libraries of Scikit-Learn
to perform Logistic Regression on a data set. The next version of this 
will be random forest regression.

Compatability: This script connects to a specific MS SQL server and grabs
a specified tables data using pyodbc and takes a sql query. 

Using the Sigmoidal Logit Function to create a model curve
of form Y=(1/(1+e^-(m*x+b))). Note:The power in the principal exponential
is the m*x+b from the slope/intercept eq. y=m*x+b.
'''

# import all modules necessary to run the script

import pandas as pd
import pandas.io.sql
import pyodbc
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics._classification import classification_report

# Declare server name and database
server_name = 'NITROHPC\SQLEXPRESS'
db_name = 'test_database'

# Create the database connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server_name + ';DATABASE=' + db_name + ';Trusted_Connection=yes')

# Query the database for the table data
sql = """

SELECT *
FROM Insurance

"""
# Create datafile variable using pd.read_sql and print to check
# that data is being read.
df = pd.read_sql(sql,conn)
# print(df)
 
# Setup test_train split test using the scikit learn module
X_train, X_test, y_train, y_test = train_test_split(df[['Age']],df.Insurance_Info,test_size=0.1)

# Look at the test.
# print(X_test)
 
# Look at the training data set.
# print(X_train)

# Create the model that we will be using.
model = LogisticRegression()
model.fit(X_train,y_train)

# Plot the data for intial inspection
plt.scatter(df.Age, df.Insurance_Info, marker='X', color="red")
plt.show()
 
# Create predictions 
predictions = model.predict(X_test)

# Create classification report
print(classification_report(y_test,predictions))
 
