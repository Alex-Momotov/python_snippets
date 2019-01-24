#%% A sample class to work with.
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#%% Inheritance allows us to inherit attributes and methods from the parent class.
#   We specify in parenthesis which class we want to inherit from. In this case we are inheriting from Employee class.
#   We create an empty subclass Developer just to show that it has all methods and attributes of the parent.
#   Play around with different methods and attributes of this empty subclass in the next cell.
class Developer(Employee):
    pass

#%%
emp1 = Employee('Test', 'Employee', 70000)
dev1 = Developer('Corey', 'Schafer', 50000)
dev2 = Developer('James', 'Hills', 50000)

print(dev1.pay)
print(dev1.email)
print(Developer.num_of_emps)    # As we can see they share the value of class variable after we change it for parent.

#%% We can freely change subclass code without breaking parent class code.
#   In example below we change raise_amt for developers, but that value for employees is the same.
class Developer(Employee):
    raise_amt = 1.08

emp1 = Employee('Test', 'Employee', 50000)
dev1 = Developer('Corey', 'Schafer', 50000)

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

print('\n')
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

#%% What happens under the hood when we call attribute or a method from a subclass is that Python looks for that
#   method or attribute in the subclass, then if doesn't find it, goes up the chain and looks at parent class and so on.
#   This chain of subclasses is called method resulution order. help(class_name) prints out the resolution order.
print(help(Developer))

#   This is what we look for. First it looks for attributes/methods in Developer class, then goes to look in Employee,
#   then looks at the built-in object class that all classes inherit from.
"""
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object"""

#   This section shows methods inherited from the parent class.
"""
 |  Methods inherited from Employee:
 |  
 |  __init__(self, first, last, pay)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  apply_raise(self)
 |  
 |  fullname(self)"""

#   This senction shows data and attributes inherited from parent class.
"""
 |  Data and other attributes inherited from Employee:
 |  
 |  num_of_emps = 24
 |  
 |  raise_amt = 1.04"""

#%% Redefine our sample class so its closer to look at.
class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#%% Perhaps we want to initialise subclass with more information than our superclass. To achieve this, we might be
#   tempted to copy the contents of our __init__ method into our subclass, but we should avoid doing this. Instead,
#   it is enough to only copy the __init__ declaration line, then pass into the body the following line:
#   super().__init__(params)            Where params are the original parameters as per the parent class.

#   There is another way of accomplishing this, we could pass this line into __init__ body instead:
#   parent_class.__init__(self, params)
#   But this way is a little less maintainable and it is recommended to stick to the first way.

#   Once we done that, we can initialise our additional instance variable in a regular fashion via self.param = param
class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)          # Good way of doing this.
        self.prog_lang = prog_lang

class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)   # Alternative way, but we should stick to the one above.
        self.prog_lang = prog_lang

dev1 = Developer('Corey', 'Shafer', 50000, 'Python')
dev2 = Developer('James', 'Smith', 50000, 'Java')
print(dev1.email)
print(dev1.prog_lang)
print(dev2.prog_lang)

#%% A full example of a subclass
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
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

dev1 = Developer('Corey', 'Shafer', 50000, 'Python')
dev2 = Developer('James', 'Smith', 50000, 'Java')

mng1 = Manager('Sue','Stephen', 90000, [dev1])
print(mng1.email)
mng1.print_emps()

print()
mng1.add_emp(dev2)
mng1.print_emps()

print()
mng1.remove_emp(dev1)
mng1.print_emps()

#%% isinstance(instance, class)
#   Returns True if a given class instance is an instance of the specified class.
#   In the example below, mng1 is an instance of both Manager and Employee classes (because Manager inherits from
#   Employee) but is not an instance of the Developer class.
print(isinstance(mng1, Manager))
print(isinstance(mng1, Employee))
print(isinstance(mng1, Developer))

#%% issubclass(class1, class2)
#   Returns True is class1 is a subclass of class2 and False otherwise.
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))













