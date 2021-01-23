""" 
This is a training on special methods and operator overloading.
Special methods help when checking for class object information.
Two important special methods are __repr__ and __str__
__repr__ - Stands for represent and changes the way the print function works on classes with this special method.
__str__  - Stands for string and changes the way the print function works on classes with this special method.
"""

# What is operator overloading
# Here the + operator treats strings and integers differently
# We see the strings concatenated and the ints added together
# # Addition
# print(1 + 2)
# # Concatenation
# print('a' + 'b')

# Overloading is the act of changing the behavior of the operator.
# In the above example this is demonstrated by the + operator, i.e. str concatenation vs int addition.


class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay): # Dunder, double-under, init method is a special method that is implicitly run first and constructs objects for the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
           
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
         
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
     
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
        
emp_1 = Employee('Tucker', 'Celestine', 60000)
emp_2 = Employee('Test', 'User', 50000)

# We see that once we implement the __repr__ method that when we print
# the emp_1 object that we get the class attributes in the string format that we 
# setup within the __repr__ method within the Employee class.
print(emp_1)
print(repr(emp_1))
print(str(emp_1))   


# So what is print(1+2) doing in the below line.
print(1+2)
# Here we are actually using the special method dunder add or __add__
# This special method is implicitly called when the + operator is used between two integers.
print(int.__add__(1,2))
print(str.__add__('a','b')) # Here the str version of __add__ concatenates. Ahaha I see!


# Here we use the __add__ that we created above in the Employee class
# to overload the + operator for emp_1 and emp_2 objects.
print(emp_1 + emp_2)

# Here we see that len is a special method. We can run it on the 'test' string.
print(len('test'))
print('test'.__len__())