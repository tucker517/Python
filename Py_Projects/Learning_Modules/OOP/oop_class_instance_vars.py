
class Employee:
    
    num_of_emps = 0 # Here we initialize the class variable num_of_emps, a counter for the total number of employees
    raise_amount = 1.04 # Here we initialize the class variable raise_amount 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + ' ' + last + '@email.com'
        
        Employee.num_of_emps += 1 # We need this within the init method because this will count 1 everytime the init method is run, or each time a employee is added. 
#                                  # We access the class variable so we are getting the value that the class namespace sees. Its better not to have this value change if we re-assign things further downline in code for 
#                                  # for particular instances.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
#         self.pay = int(self.pay * 1.04) # This works but since this variable applies to all objects of the class it makes sense to store it as a class
        self.pay = int(self.pay * self.raise_amount) # variable instead of hardcoding in this line. We do this by going to the top of the class and initializing the class variable as raise_amount
#                                                    # In the above line we can access either the class variable or instance variable raise_amount depending on how we want our code to function. Here it is better to access the instance so that any particular instance differences in raise_amount recorded in the namespace after alterations downline in code are accurately used.
#                                                    # For Example Employee.raise_amount or self.raise_amount .
emp_1 = Employee('Tucker', 'Celestine', 50000)
emp_2 = Employee('Test', 'User', 20000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount # just showing how we should be able to access
# Employee.raise_amount

print(Employee.raise_amount) # We can access the class var from the class itself because the attribute exists for the class
print(emp_1.raise_amount)# When we access the class var here using the instance, the instance doesn't actually have the attribute itself, the instance must use the class's raise_amount attribute
print(emp_2.raise_amount)

print(emp_1.__dict__) # Here we print the namespace of the instance and see that raise_amount DNE!
print(Employee.__dict__)# Here we print the namesace of the class and see that raise_amount Does Exist!


print(Employee.num_of_emps)
print(emp_1.num_of_emps)
# Important Take-Aways :
"""
    In the line where we apply the class variable raise amount to the pay attribute  for each
    instance for objects of the class employee. Notice that it makes a big difference if we 
    access the class variable using the class or the instance, i.e. Employee.raise_amount vs self.raise_amount
    If we use Employee.raise_amount we are always going to access the value 1.04 because this is inherited from the
    class variable initialized on line 4. If we use self.raise_amount, we actually access the most recent namespace for
    the instance which can be updated downline in the code. This means that we can reassign the value for raise_amount on
    a instance by instance basis and inherit that assigned value downline in the code.
"""