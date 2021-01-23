"""
What is a decorator:

A decorator is an outer function which returns an inner function
that is kept from execution and args are remembered until the function is called.

Decorators allow us to dynamically alter the functionality of our code by storing
unexecuted inner/wrapper functions which are passed a seperate function through an
outer decorator function. The unexcuted inner wrapper function can also act as secondary place to alter
the decorated function's functionality. This can be done by editing the code within the wrapper function. 
We can accept both functions that require positional args and those that do not by using the *args and **kwargs
variables. These are special variables and make it so that we can decorate functions that require positional args and kwargs.
"""
# Here an unexcuted function object , original_function is passed to the decorator function


# def decorator_function(original_function):
#      
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function
#  
# def display_func():
#     print('display function ran')
#      
# display = decorator_function(display_func)
#  
# display()



# Or we can use a different syntax that does the same thing.
# the below code is the same as above but note the decorator 
# and change from calling the wrapper func using the decorated_display object.

# def decorator_func(original_func):
#      
#     def wrapper_func():
#         print('Wrapper executed before {}'.format(original_func.__name__))
#         return original_func() 
#      
#     return wrapper_func
#  
# @decorator_func # This line and the line below are the same as saying display = decorator_func !
# def display():
#     print('Display Message!')
# 
# display()


# Now we try and add another function and apply the decorator to it
# Same as above example but note the new func has 2 positional args!

# def decorator_func(original_func):
#     
#     def wrapper_func(*args, **kwargs): # Here we add *args and **kwargs so that we don't get the positional arg error from introducing a decorated function with both positional args and without!
#         print('Wrapper executed before'.format(original_func.__name__))
#         return original_func(*args, **kwargs)
#     return wrapper_func
# 
# @decorator_func
# def display():
#     print('Display String!')
# 
# @decorator_func
# def display_info(name, age):
#     return 'Display info ran with positional args ({}, {})'.format(name, age)
# 
# display_info('John', 25)
# display()


# Now we introduce a decorator_class to do the same operation but for decorator class objects only.
 
# class decorator_class(object):
#      
#     def __init__(self, original_function):
#         self.original_function = original_function
#          
#     def __call__(self, *args, **kwargs):
#         print('__call__ executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#      
# @decorator_class
# def display():
#     print('Display String!')
#  
# @decorator_class
# def display_info(name, age):
#     return 'Display info ran with positional args ({}, {})'.format(name, age)
#  
# display_info('John', 25)
# display()


# Practical examples

# Here we see how to use a logger function

# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
#     
#     def wrapper(*args, **kwargs):
#         logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)
#     
#     return wrapper
# 
# @my_logger # here we see that we are able to apply the functionality of the logger function to any other function by making it a decorator.
# def display_info(name, age): # this helps modulate our code and keep from rewriting error prone code again and again.
#     print('display_info ran with arguments ({}, {})'.format(name,age))
#     
# display_info('John', 25)

# Timer function that times how long it takes for a function to run.

def my_timer(orig_func):
    import time
      
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
#         time.sleep(2) # Tests we are executing the wrapper
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

@my_timer
def display_info(name, age):
    print('display_info has ran with 2 args ({},{})'.format(name, age))
    
@my_timer
def display():
    print('Display function ran!') 
       
display_info('John', 28)
display()
