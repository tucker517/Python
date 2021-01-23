""" 
Regular Method - Takes the instance, self as the first argument of the method. To do this don't add any decorators.
Class Method - Takes the class, class obj , as the first argument of the method. To do this add the decorator @classmethod
Static Method  - Don't pass anything automatically, neither instance or class. To do this add the decorator @ staticmethod

"""

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + ' ' + last + '@email.com'
        
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod 
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod # Alternative Constructor Example
    def from_string(cls, emp_str): # Accepts cls as the first arg, and the emp_str as the second
        first, last, pay = emp_str.split('-') # Parses the string, splitting on '-' 
        return cls(first, last, pay) # Returns the class object with attr first, last, pay
    
    @staticmethod # No arg is passed automatically
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
emp_1 = Employee('Tucker', 'Celestine', 60000)
emp_2 = Employee('Test', 'User', 50000)

# Lines 450 through 44 pertain to the example of resetting the raise_amount using the classmethod
# This means that all raise_amounts will hereforth be reset to the value below. Using the classmethod set_raise_amt
Employee.set_raise_amt(1.05)
 
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

""" 
How to use a @classmethod as an alternative constructor...
What does this mean? This means that instead of passing the class args to the init
constructor to build the instance we are instead passing the cls args to a classmethod to construct the new object, allocates memory and takes args. 
"""

# A common problem to demonstrate when using class methods comes in handy
# the below problem is that a coworker comes to you and says I like the 
# functionality of the class you have built but I continually find myself needing to parse
# out my data so that it works with your class. My data comes in a string format ex 'John-Doe-70000' can you create a method so that I can just pass the string in to create an employee? Thanks!

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'April-Smith-50000'
# emp_str_2 = 'Jessica-Winters-60000'
# 
# # This is the general idea to parse the strings, splitting based on '-'
# first, last, pay = emp_str_1.split('-')
# # Then we create a new instance using the class args from the parse op above.
# new_emp_1 = Employee(first, last, pay)

# # This works to create new objects from strings.
# print(new_emp_1.email)
# print(new_emp_1.pay)
"""
The below section demonstrates using a static method. We introduce another method
to determine if the weekday for input date is a weekday or weekend day. This information
could be applicable to objects of the Employee class, say for instance if we need to check if paydates occur on a week or weekend.
So no arg is automatically passed to staticmethod, the method is static and functions independently of class and instance and is said to be static.
An easy way to tell if a method may be a good fit for static is if your not using cls or self, the class var or instance var in the method.
"""
import datetime
my_date = datetime.date(2021, 1, 24)
print(Employee.is_workday(my_date))