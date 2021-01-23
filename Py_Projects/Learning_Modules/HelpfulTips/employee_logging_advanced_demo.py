import logging

logger = logging.getLogger(__name__) # Remebe the __name__ special method declares to the interpreter the name of the file as __main__ or imported module.
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee_advanced.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee():
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email)) # Here we call logger the var created above instead of logging.
        
    @property
    def email(self):
        return '{}.{}.@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Tucker', 'Celestine')
emp_3 = Employee('Jane', 'Doe')
