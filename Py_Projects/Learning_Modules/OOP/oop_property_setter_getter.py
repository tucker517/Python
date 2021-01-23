
class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
#         self.email = first + '.' + last + '@email.com' # here we setup email as a attribute within the init method
    
    @property # Allows us to call the return val of the method as an attribute not .email() but .email
    def email(self): # Here we use a method to create the email instead of an attribute
        return '{}.{}@email.com'.format(self.first, self.last)
     
    @property # This changes the below method to a property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter # Here we define a setter by using @settername.setter format, this allows us to set attributes of a class
    def fullname(self, name): # name val is the val we are trying to set
        first, last = name.split(' ') # Since we have the fullname as name we can parse the arg using split to get first and last as vars
        self.first = first # We simply then set the first name arg as the attribute first 
        self.last = last # Then set the last name arg as the attribute last
     
    @fullname.deleter # Decorator specifying class operator
    def fullname(self):
        print('Delete Name!')
        self.first = None # Set the first name attribute equal to None, deleting the attr
        self.last = None# Set the last name attribute equal to None, deleting the attr
        
emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Tucker Celestine' # Throws the error can't set attribute while setter is not being used.
# emp_1.first = 'Tucker'

print(emp_1.first)
print(emp_1.last)
print(emp_1.email) # Adding the email method above automatically updates the email adr now
print(emp_1.fullname)# but we have to now use a method () call to create emails using our class now. Not what we want because it breaks the code for others.
                        # Instead we can use a put in place a @property decorator above the email method so that we can now call the email as an attribute in the print statement.
                        # So the @property decorator allows us to retain the attribute call functionality of our code while changing the attribute to a method.
del emp_1.fullname # Here we test that are deleter works, when we call del on the fullname property we now step into the @fullname.deleter. This then revaluates the instance to and sets the values of first and last to None                     