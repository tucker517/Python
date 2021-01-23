"""
What is a closure:

A inner function that remembers and has access to variables in the 
local scope in which it was created, even after the outer function has
finished executing.
"""

def outer_func(msg):
    message = msg
    
    def inner_func(add_msg):
        print(message, add_msg)
        
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func('How ya doing?!')
# hello_func()




        
