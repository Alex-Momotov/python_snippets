#%% To create an empty class write 'pass' statement.
class Employee:
    pass

#%% Printing out instances of a class results in printing their memory address
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

#%% Instance variables are unique attributes to each class instance.
#   We can add instance variables even to an empty class as follows:
#   This is a manual method, normally we wouldn't want to be doing that.
class Cat:
    pass

cat1 = Cat()
cat1.weight = 100
cat1.email = 'cat@gmail.com'

print(cat1)
print(cat1.weight)
print(cat1.email)

#%% The __init__ method runs automatically, every time we create a new instance of a class.
#   We can think of the __init__ method as 'initialise' or as a constructor. When we create methods within a class they
#   receive the instance as the first argument automatically. By convention we should call the instance 'self' (we could
#   call it whatever we want but its a good idea to stick to the convention.
#   After 'self' we can specify which other arguments we want to accept.
#   "self.first = first" is equivalent of setting instance variables manually, as in the second cell (see above) but
#   instead this is done automatically. In example below, 'first', 'last', 'pay', 'email' are attributes, or instance
#   variables of class Employee.
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

# When we call an instance method from an instance, the 'self' is passed automatically, no need to specity it.
emp_1 = Employee('Alex', 'Momotov', 24000)  # emp_1 will be passed as 'self' variabe
emp_2 = Employee('Corey', 'Schafer', 50000)  # emp_2 will be passed as 'self' variabe

print(emp_1)
print(emp_1.email)

#%% Example of creating an instance method.
#   All instance methods must take the self parameter. This is required. Else an error will occur.
#   There are two ways of running an instance method: from instance of a class, or from the class itself.
#   From instance of a class looks like this:   instance.method()           ->      emp_1.fullname()
#   From class inself looks like this:          class.method(instance)      ->      Employee.fullname(emp_1)
#   Both ways do the exact same thing. When calling from instance of a class, 'self' is passed automatically.
#   When calling from class itself, the class doesn't know which instance to call the method on, so we need to tell it.
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Alex', 'Momotov', 24000)
emp_2 = Employee('Corey', 'Schafer', 50000)

print(emp_1.fullname())
print(Employee.fullname(emp_1))

#%% My first attempt to implement linked list. This is probably wrong.
class Node:

    def __init__(self, data):
        self.data = data
        self.next_ = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next_):
        self.next_ = next_

    def getNext(self):
        return self.next_

class LinkedList:

    def __init__(self, newNode):
        self.head = newNode

    def addStart(self, newData):
        newNode = Node(newData)
        newNode.setNext(self.head)
        self.head = newNode
        return self

    def printout(self):
        tmpNode = self.head
        while tmpNode != None:
            print(tmpNode.getData())
            tmpNode = tmpNode.getNext()

L1 = LinkedList(Node(999))
L1.addStart(5)
L1.addStart(6)
L1.printout()










































