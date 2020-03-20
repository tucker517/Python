'''
Created on Mar 19, 2020

@author: Tucker Celestine

Memo: This is a script that performs decision making using the ml library
scikit-learn. We will be importing the IRIS flower data set in this example.
This code will stand as a framework to build upon
'''

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np


# Define seed value for random values
np.random.seed(0)

# Now load the IRIS dataset
iris = load_iris()

#print(iris)

# Create the dataframe with pandas
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add a column for the species name using the python dictionary using target
# to specify the data we want to add to the df, in this case names
df['species'] = pd.Categorical.from_codes(iris.target,
iris.target_names)

# Add a column for random number [0,1] for in
# in the length of the df. If <= .75 TRUE, else >.75 FALSE.
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

# Check the data by printig to terminal
print(df.head())

# Create two new dataframes with test rows and training rows
# from the original data frame. So based on the numpy function above
# we will have 0.25 percent of the data in Train and 75% in test
train, test = df[df['is_train']==True], df[df['is_train']==False]

# Show the number of observations for the test and training data frames
print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:', len(test))

# Create a list of feature column's names
features = df.columns[:4]
print(features)

# Now we need to convert the species into a digits
# so the computer understands
y = pd.factorize(train['species'])[0]

# View the target
print(y)

# Create a random forest classifier
# n_jobs prioritize the tasks to perform need to specify own machine
# if larger network cluster, use multiple machines and specify which
# to run jobs on. random_state is the seed value basically, so for species
# the computer will recognize the species as 0,1,2
clf = RandomForestClassifier(n_jobs=2, random_state=0)

# Train the classifier. The fit method is how we basically train the script
# based on a model that we fit to a dataset in this case features. We fit and 
# train our features and our target y
clf.fit(train[features], y)

# Now we apply the trained classifier to the test data set, 25% of df
print(clf.predict(test[features]))

# Viewing the predicted probabilities of the 1st 10 observations
# This array tells us the likely hood of each prediction based on percentage for 
# for that species. So if [1, 0, 0] we predict it will be a setosa, if [0,1,0.5] we predict a virginica.
# Important Note!... If [0,0.5,0.5] we will predict the first in the if the two probabilities are equal.
print(clf.predict_proba(test[features])[0:10])

# We will now map names for the plants for each predicted plant name
preds = iris.target_names[clf.predict(test[features])]

# View the predicted specises for the first five observations
preds[0:25]

# Viewing the actual species for the first 5 observations
test['species'].head()

# Creating a confusion matrix, this is a matrix that
# combines the predicted species name with the observed 
# species name, "Actual Name from the original df" to understand
# how good our model is. Crosstab takes to sets of data and creates
# a chart.
pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species'])

# Now apply those predictions to 2 new flowers inserted as an array of arrays
preds = iris.target_names[clf.predict( [[5.0, 3.6, 1.4, 2.0],[5.0, 3.6, 1.4, 2.0]] )]
print('Test_Data', preds)
