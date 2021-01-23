""" 
This is a basic demo on how logs help with tracking issues.
Important URL for logging attributes and formatting.
https://docs.python.org/3/library/logging.html

A best practice is to configure specific loggers for large scale applications.
By default we use the root logger. This can be an issue if we have multiple process trying to use the root logger at once.
"""
# In python there are 5 logging levels which allow us to specify the nature of the problem we have enountered.


# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the 
#          near future (e.g 'disk' space low'). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform somee function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running. 

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s') # The DEBUG is an INT in inc of 10 for each logging level. 


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y 

num1 = 40 
num2 = 20

add_result = add(num1, num2)
# print('Add: {} + {} = {}'.format(num1, num2, add_result))
logging.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = subtract(num1, num2)
# print('Subtract: {} + {} = {}'.format(num1, num2, add_result))
logging.debug('Subtract: {} - {} = {}'.format(num1, num2, add_result))
 
mult_result = multiply(num1, num2)
# print('Multiply: {} + {} = {}'.format(num1, num2, add_result))
logging.debug('Multiply: {} * {} = {}'.format(num1, num2, add_result))

div_result= divide(num1, num2)
# print('Divide: {} + {} = {}'.format(num1, num2, add_result))
logging.debug('Divide: {} / {} = {}'.format(num1, num2, add_result))