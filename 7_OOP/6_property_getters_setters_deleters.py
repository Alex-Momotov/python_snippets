#%% @property
#   @property decorator turns a method into a property object which can be accessed just like an attribute.
#   It becomes accessible without parenthesis.
#   This may be useful when we want to turn an existing attribute into a method, but don't want the client code to break
#   because they would have to go and change all their code and include parenthesis at the end of each attribute call.
class Employee:
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return self.first.lower() + self.last.lower() + "@company.com"

emp1 = Employee('Corey', 'Schafer', 50000)
print(emp1.fullname)
print(emp1.email)

#%% But using the @property decorator in this way may introduce a problem. That is, even though the method technically
#   becomes an attribute, when we try to set it to a new value outside the class we will get an 'AttributeError'.
emp1.fullname = 'hi'

#%% In order to remedy this we can add setter to the method which is decorated with @property.
#   To add a setter method we should put a decorator in a format @att_method.setter where 'att_method' is the method
#   which we are turning into the attribute to begin with. The setter method is triggered whenever we use assignment
#   operator '=' with the object's attribute created with @property decorator.
class Employee:
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, new_name):
        first, last = new_name.split(' ')
        self.first = first
        self.last = last

#   Similarly, deleter method get executed whenever we delete a property like an attribute e.g. del instance.att
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

emp1 = Employee('Corey', 'Schafer', 50000)
print(emp1.fullname)
emp1.fullname = 'Cori Schaf'
print(emp1.fullname)
print(emp1.first)
print(emp1.last)
del emp1.fullname
print(emp1.fullname)

#%% In summary, properties exist so that we can turn an existing attribute into methods which define setting, getting,
#   and deleting behaviour without breaking client code.

#%% Another example:
class Temperature():

    def __init__(self, a):
        self.temperature = a

    @property
    def temperature(self):
        print('@property')
        return self.__temperature

    @temperature.getter
    def temperature(self):
        print('@temperature.getter')
        return self.__temperature

    @temperature.setter
    def temperature(self, new_temp):
        print('@temperature.setter')
        self.__temperature = new_temp

    @temperature.deleter
    def temperature(self):
        print('@temperature.deleter')
        self.__temperature = None

#%%
T = Temperature(24)
#%%
T.temperature
#%%
del T.temperature
#%%
T.temperature = 5

#%% Note about encapsulation in Python.
"""
In Java, if we make an attribute public, clients would start writing the code with direct calls to the public attributes
via the instance e.g. instance.att but when the programmer decides to make this attribute into a function, there would
be no way to do that without breaking the client code. For this reason, Java programmers are told to make things private
and use getters and setters from the beginning, even if all they do is set and return values with no extra checks.

In Python, however, we can allow ourselves to make attributes public in order to be able to conveniently get and set
instance values without extra syntax. This is because, if we later decide to turn the attribute into a function in order
to add some functionality, we can easily do this with the @property decorator, getters and setters.

In short, there is no need to make everything encaplulated in Python. But if we really wanted to make some attributes 
or methods private we could do that by prepending attribute or method name with double underscore __foo(self) or 
self.__bar.  
"""

#%% These two classes are absolutely equivalent.
class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

class P:

    def __init__(self,x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__get_x, __set_x)

#%% A lot of the times we want to make attributes or methods private just to avoid overwhelming the user developer with
#   the multitude of unnecessary attributes. In this case, the use of private attributes and methods is totally
#   justified and is pythonic. See example below, where condition of the robot is calculated using private variables,
#   yet they are hidden from the user since they are private.
class Robot:

    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"


if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)

#%% Finally, there is a way to access private variables (even though they are private) from the client code.
#   To do this we need to prepend the private attribute name with double underscore and a classname.
#   But this is a really bad practice because it breaks the convention and we should never do this.
class Cat:

    def __init__(self, name):
        self.name = name
        self.__secret = 'this should never be known'

C = Cat('Kate')
print(C.name)
print(C.__dict__)
print(C._Cat__secret)

#%% Python allows us to start with the simplest implementation imaginable, and you are free to later migrate to a
#   property version without having to change the interface.

#   We could start with simple code like follows:
class OurClass:

    def __init__(self, a):
        self.OurAtt = a

x = OurClass(10)
print(x.OurAtt)

#   Then, if later we need to introduce additional checks we will use @property functionality to change our code.
class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)
