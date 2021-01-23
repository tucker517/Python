""" 
What is a Context Manager: 
A context manager handles cases within a context scope for the setup and teardown of resources. 
We can create context managers in 2 ways: class methods or decorator functions.
In this tutorial we will explore how we can use class methods to setup and teardown resources
so as to avoid exceptions during functional operations for a number of test cases.

An example of a Context Manager:
Take for instance the file context manager with in python. with allows us to 
open a file and not worry about having to close it once we are done performing operations.
Also with accounts for exceptions to program run time for file operations. In total with
handles setup and teardown for for file resources in python.
"""

# # The below class shows how the context manager with is used
# # to open a file using the example class Open_File, which behaves the same as the built in open.
# class Open_File():
#     
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#     
#     def __enter__(self): # Setup method, opens the file
#         self.file = open(self.filename, self.mode)
#         return self.file
#     
#     def __exit__(self, exc_type, exc_vale, traceback): # Teardown method, closes the file.
#         self.file.close()
#         
# with Open_File('sample.txt', 'w') as f:
#     f.write('Testing') # Here we are within the context manager and have run the special method __enter__
# # Once we step out of the block we run the teardown special method __exit__     
# print(f.closed) # Print closed attribute of the file which evaluates to True


# Here is the functional equivalent of the above class code. We use the @context built in context manager
# decorator instead of writing our own decorator. It is called with @contextmanager.

# from contextlib import contextmanager
# 
# @contextmanager
# def Open_File(filename, mode):
#     f = open(filename, mode)
#     yield f # Equivalent to the __enter__ method above. The setup of the context manager. 
#     f.close()# Equivalent to the __exit__ method above. The setup
# 
# with Open_File('sample2.txt', 'w') as f: # Here f is the yielded f from the above code.
#     f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.') # Here we have stepped into the context manager.
# # Here we step out of the context manager and the teardown method is run.
# 
# print(f.closed)

# Another example using context managers. Here we need to change our working dir and checking the 
# contents with many directories. We want to have a script to do this. This is the below.

import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield # Here we setup the resource with context manager.
    finally:
        os.chdir(cwd) # Here we teardown the resource with context manager.

with change_dir('Sample_Dir_One'):
    print(os.listdir())
    
with change_dir('Sample_Dir_Two'):
    print(os.listdir())

# Basic schema of what we are doing in the above code.
# cwd = os.getcwd()
# os.chdir('Sample-Dir-One')
# print(os.listdir())
#  
# cwd = os.getcwd()
# os.chdir('Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)





