""" 
This is a basic demo on how logs help with tracking issues.
Important URL for logging attributes and formatting.
https://docs.python.org/3/library/logging.html

A best practice is to configure specific loggers for large scale applications.
By default we use the root logger. This can be an issue if we have multiple process trying to use the root logger at once.
Handlers allow us to specify which logger we want to handle logging for certain processes. The below show how we can break apart our
previous basic config file.
"""
# In python there are 5 logging levels which allow us to specify the nature of the problem we have enountered.


# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the 
#          near future (e.g 'disk' space low'). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform somee function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running. 

import logging
import employee_logging_advanced_demo

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample_test.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero') # using exception method here gives us traceback information.
    else:
        return result
    return x / y 

num1 = 40 
num2 = 10

add_result = add(num1, num2)
# print('Add: {} + {} = {}'.format(num1, num2, add_result))
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result)) # Note we changed to logger our new logger instance

sub_result = subtract(num1, num2)
# print('Subtract: {} + {} = {}'.format(num1, num2, add_result))
logger.debug('Subtract: {} - {} = {}'.format(num1, num2, add_result))
 
mult_result = multiply(num1, num2)
# print('Multiply: {} + {} = {}'.format(num1, num2, add_result))
logger.debug('Multiply: {} * {} = {}'.format(num1, num2, add_result))

div_result= divide(num1, num2)
# print('Divide: {} + {} = {}'.format(num1, num2, add_result))
logger.debug('Divide: {} / {} = {}'.format(num1, num2, add_result))