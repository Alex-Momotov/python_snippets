#%% Class methods
#   Class methods are created by putting decorator @classmethod above the method declaration.
#   By convention their first argument is named 'cls' and automatically becomes the reference for the class when the
#   class method is called. In order to use the class method, call it from the class name itself
#   e.g. class_name.class_method   ->   Employee.set_raise_amt(1.05)

#   Within class methods we are working with the class instead of the instance, meaning we can change class variables
#   by using cls.variable = new_value

#   Calling class methods on the class name is equivalent to changing class variables manually e.g.
#   "cls.raise_amt = amount" within class method is equivalent to "Employee.raise_amt = amount" outside the class code.

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp_1 = Employee('Alex', 'Momotov', 50000)
emp_2 = Employee('Corey', 'Schafer', 60000)

Employee.set_raise_amt(1.05)

print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.raise_amt)

#%% The above class method is equivalent to the following line. They do exactly the same thing.
Employee.raise_amt = 1.05

#%% Some people use class methods as alternative constructors.
#   In the example below we write class method which returns newly created instance of a class created from a string.
#   By convention these alternative constructors are named beginning with 'from_'.
#   cls acts as a full name of the class e.g. 'Employee' and therefore can be used to construct and return new instances
#   of the class.
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"

    def fullname(self):
        return f'{self.first} {self.last}'

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_3 = Employee.from_string('John-Doe-60000')
print(emp_3.email)
print(emp_3.pay)
print(emp_3.fullname())

#%% Static methods
#   Static methods behave just like normal functions.
#   They do not take instance or the class as the first argument.
#   To create a static method we need add decorator @staticmethod above the method.

#   Static methods could be standalone functions defined outside class body, but sometimes it makes sense to keep them
#   together with the class.

#   A hint that an instance method or a class method should really be a static method is when you don't use 'self'
#   or 'cls' within the method body.

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"

    def fullname(self):
        return f'{self.first} {self.last}'

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False

import datetime
my_date = datetime.date(2018,6,16)
print(Employee.is_workday(my_date))





