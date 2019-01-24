#   Class variables are variables that are shared across all instances of a class.
#   Class variables are declared outside all methods in a class, usually declared straight after class declaration.
#   We can access class variables either through instances of a class (emp_1.raise_amount) or through the class itself
#   (Employee.raise_amount). When using class variables within an instance method, we can access it via 'self' e.g.
#   (self.raise_amount) or via class itself (Employee.raise_amount) and there is an important difference between the two.
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee('Alex', 'Momotov', 50000)
emp_2 = Employee('Corey', 'Schafer', 50000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay, '\n')

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

#%% .__dict__
#   Prints out namespace of an instance or a class (all named attributes and their values)
#   When we try to access an attribute of an instance, Python will first check if this instance contains this attribute,
#   and if it doesn't then it will go and look if its class or any class it iherits from contains that attribute.
#   When accessing class variables through instances of a class (e.g. emp.raise_amount) they don't actually have that
#   attribute themselves, so they go and look if the class has this attribute.

print(emp_1.__dict__)   # There is no raise_amount it the list
print(Employee.__dict__)    # The class itself contains the raise_amount class variable

#%% When we change a class variable from a class (e.g. Employee.raise_amount) it changes for all instances as well as
#   the class. However when we change class variable from an instance (e.g. emp_1.raise_amount) it copies the variable
#   into the namespace of that particular instance and changes it there. This might be unexpected and is an important
#   concept to understand.
class Employee:
    raise_amount = 1.04

emp_1 = Employee()
emp_2 = Employee()

Employee.raise_amount = 1.05    # Changes class variable for all instances.
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount, '\n')

#%%
class Employee:
    raise_amount = 1.04

emp_1 = Employee()
emp_2 = Employee()

emp_1.raise_amount = 1.05   # Copies class variable into namespace of that instance and changes it there.
print(emp_1.raise_amount)
print(emp_2.raise_amount)   # Therefore all other instances have the old value of the class variable.
print(Employee.raise_amount, '\n')

#%%
class Employee:
    raise_amount = 1.04

emp_1 = Employee()
emp_2 = Employee()

print(emp_1.__dict__)
Employee.raise_amount = 1.05
print(emp_1.__dict__)   # Namespace of an instance is unaffected.

#%%
class Employee:
    raise_amount = 1.04

emp_1 = Employee()
emp_2 = Employee()

print(emp_1.__dict__)
emp_1.raise_amount = 1.05
print(emp_1.__dict__)   # Namespace of the instance now has an additional arrtibute

#%% It is important to understand when you want to use self. or class_name. when accessing class variables within an
#   instance method of a class. If it is important for any particular instance to be able to override the value of the
#   class variable then use self. Otherwise, if we want the method to access the class variable which is not overriden
#   by a particular instance, then use class_name.class_variable
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)    # Here we would be able to override raise_amount for any
                                                        # particular instance and the method would refer to that.

emp_1 = Employee('Alex', 'Momotov', 50000)
emp_2 = Employee('Corey', 'Schafer', 50000)

emp_1.raise_amount = 1.05   # We overriden class variable for this particular instance and the method works as expected.
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)

#%% If we wanted to keep track of number of instances created (number of employees) it wouldn't make sense to use self.,
#   instead we should prepend the assignment of new class variable with the name of the class class_name.class_variable
#   (e.g. Employee.num_of_employees += 1)
class Employee:

    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + last.lower() + "@company.com"
        Employee.num_of_employees += 1

print(Employee.num_of_employees)

emp_1 = Employee('Alex', 'Momotov', 50000)
emp_2 = Employee('Corey', 'Schafer', 50000)

print(Employee.num_of_employees)


#%% Run the remaining cells in any order to gain full understanding of this.
class Marble:
    colour = 'black'

    def __init__(self, size):
        self.size = size

    def change_colour(self, new_colour):
        Marble.colour = new_colour


# %%
m1 = Marble(5)
m2 = Marble(10)

# %%
print(m1.__dict__)
print(m2.__dict__)
print(Marble.__dict__)

# %%
print(m1.colour)
print(m2.colour)
print(Marble.colour)

# %%
m1.change_colour('green')

# %%
Marble.colour = 'blue'

# %%
m1.colour = 'violet'































