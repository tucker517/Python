"""
Python has treats functions as first class objects! 

Properties of First-Class Functions:
You can store the function in a variable.
You can pass a function as a parameter to another function.
You can return a function from a function.
You can store a function in data structures such as hash tables, lists, dicts, ...
"""

def square(x):
    return x * x
 
def cube(x):
    return x * x * x
 
# This shows us that we can save a function as a variable
f = square
 
# This checks the variable f is set to the function square
print(square)
print(f)
print(f(25))
# Passing
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
# This shows how you can pass a function to a function
squares = my_map(square, [1, 2, 3, 4, 5]) # function square is passed to the my_map func
cubes = my_map(cube, [1, 2, 3, 4, 5])     # and then saved as 
 
print(squares)
print(cubes)


# This shows us how we can return a function from a function. 
def logger(msg):
     
    def log_message():
        print('Log:', msg)
         
    return log_message # here we didn't give () so the function didn't execute when it was entered

log_hi = logger('Hi!') # So here we see that the variable log_hi is converted into the function log_message. 
# Now we can treat this log_hi as a function and execute with ().
log_hi()               

# This shows us how you can store a function in a data structure.
def html_tag(tag):
    
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg)) # the 0 and 1 correspond to tag and msg!
    
    return wrap_text

print_h1 = html_tag('h1')
# print(print_h1) # Shows us the variable is equal to wrap text func waiting to be executed.
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph')

