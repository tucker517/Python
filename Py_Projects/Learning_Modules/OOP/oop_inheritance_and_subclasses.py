""" 
Say we want to subdivide manager and developers at this company into seperate classes.
All the workers are still employees but we will need 2 classes to cater to each groups needs.  
"""

class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
class Developer(Employee): # We can specify which class we want to inherit from, in this case the Employee class
        
        raise_amt = 1.10   # If we pas Employee to the Developer class as an arg, developer inherits all of Employees methods and attributes.
        
        def __init__(self, first, last, pay, prog_lang):
            super().__init__(first, last, pay) # Here we use super().__init__ to point to the Employee constructor for the first, last, and pay attributes.
#             Employee.__init__(self, first, last, pay) # This still works the same as the above line, but this can cause problems with multiple inheritence. Best to use super().__init__
            self.prog_lang = prog_lang 
            
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None): # Never pass mutable objects as default arguments to methods!
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
                  
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
                                 
emp_1 = Employee('Bill', 'Bass', 60000)
emp_2 = Employee('Derrick', 'Fischer', 30000)
""""
Here we create 2 devs using the class Developer.
Python looks for the __init__ method to construct the class objects but does not find it in the Developer Class.
Instead python follows the chain of inheritence until it finds the init method to build the objects. The chain of inheritence that
python follows is referred to as Method Resolution Order !
"""
dev_1 = Developer('Tucker', 'Celestine', 50000, 'Python')
dev_2 = Developer('Quinton', 'Zillowini', 60000, 'Java')

# print(help(Developer)) # Printing the help for the Developer class shows us the Method Resolution Order.
# print(dev_1.email)
# print(dev_2.email)
    
    
# Now we check method resolution order for applying 
# a raise to a the developer subclass of objects
# print(dev_1.pay) 
# dev_1.apply_raise()
# print(dev_1.pay)
# Check that employee raise amount is applied and the employee rate is being used.
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# Now we test that we get a new attribute for developers which is being 
# built in the developer subclass. The email attribute is made in the Employee parent constructor.
# So printing the dev_1.email should check that we are getting both attributes on our dev objects.
# print(dev_1.prog_lang)
# print(dev_1.email)

dev_3 = Developer('James', 'Smith', 50000, 'Python')
# Now check that the manager class works 
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)

# Check managers list of employees.
# print(mgr_1.print_emps())

# Check removal method
mgr_1.remove_emp(dev_3)
# print(mgr_1.print_emps())
# print(help(Manager))
# Python has the built in isinstance. 
# This allows us to check if an instance belongs to a class.
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# Python has the built in issublclass.
# This allows us to check if a subclass belongs to a class
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))