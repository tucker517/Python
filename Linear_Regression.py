'''
Created on Feb 24, 2020

@author: JTC
'''

# Basic linear regression Script#
# This script uses pandas to read a csv file and plot data.#
# This script does Linear Regression and prints the R^2 Coefficient to the terminal#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = (10.0, 10.0)

# Read a test data set, must be csv format! #
data = pd.read_csv('XXXXX')
print(data.shape)
data.head()

# Specify X and Y Values to Use based on Column Title #
X = data['XXXX']                
Y = data['XXXX']

# Calculate the mean of X and Y values#
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Find the total number of X values.
# This equals the number of rows or xy pairs in the data set#

m = len(X)

# Use a formula to calculate  b1 and b0 to find equation y=b0 + b1x #
numer = 0
denom = 0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

# We could specify a limit buffer around the #
# max x value and an increment between plotted points if we wanted. #
max_x = np.max(X)
min_x = np.min(X)

x = np.linspace(min_x, max_x)
y = b0 + b1 * x

# Plot the regression line #
plt.plot(x, y, color='red', label='Regression Line')
# Plot the Data Set on scatter plot #
plt.scatter(X, Y, color='blue', label='Data-Points')

# Format Graph #

plt.xlabel('Event #')
plt.ylabel('Magnitude (Mw)')
plt.legend()
plt.show()

# Calculate R^2 value using equation R^2=1 - ss_r/ss_t #
# where ss_r is the sum of squared residual and ss_t is the sum #
# of squared total #
ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
R2 = 1 - (ss_r/ss_t)
print('You just calculated R^2!!')
print(R2)


