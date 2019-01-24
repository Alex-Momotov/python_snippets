#   Dunder methods are also known as 'special' methods, or 'magic' methods.
#   They have double underscpre '__' on each side of the method name.
#   Word 'dunder' literally means the double underscore '__' hence the name dunder methods.
#   Dunder methods influence how an object behaves in many situations.
#   The most common example of a dunder method is the __init__ constructor method.

#%% __repr__ and __str__
#   Those two dunder methods are also very common.
#   __repr__ determines what is printed when we call the repr() method on the object.
#   __str__ determines what is printed when we call the str() method on the object.

#   Quick note about their difference: repr() is really meant for developers and debugging puproses while str() is meant
#   for end users.

#   At the very minimum we should define the __repr__ method because when __str__ is not defined the execution falls
#   back onto the __repr__ method.

#   A rule of thumb is to make __repr__ return something that we can can copy and paste back into Python code in order
#   to recreate that exact object.

class Employee:
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

emp1 = Employee('Corey', 'Schafer', 50000)

print(emp1)

print(str(emp1))
print(emp1.__str__())

print(repr(emp1))
print(emp1.__repr__())

#%% __add__
#   Determines what is returned when we add two objects with addition operator '+'
#   In this example we make it return the added salary of two employees.
class Employee:
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"
        Employee.num_of_emps += 1

    def __add__(self, other):
        return self.pay + other.pay

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('James', 'Smith', 50000)
print(emp1 + emp2)

#%% __len__
#   Determines what is returned when we call the len() method on the object.
#   In this example we decide to make it return number of characters in the full name of an employee.
class Employee:
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Corey', 'Schafer', 50000)
print(len(emp1))

