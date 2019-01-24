#%% Making an empty function that does nothing but gives no error.
#   Usually 'pass' is used when we want to make function but
#   fill it out later.
def do_nothing():
    pass

#%% Making simple functions
def hello_function():
    print('Hello function!')

hello_function()
hello_function()

#%% Simple function that returns something
def hello_function():
    return 'Hello function!'

print(hello_function())

#%% Parameters and default parameters.
#   Default parameters should always come after non-default parameters
#   Positional arguments (non-defalut ones) should always come first
def greeting(name, greering='Welcome'):
    return f'{greering}, {name}!'

print(greeting('Liam'))
print(greeting('Liam', 'Hi'))
print(greeting('Liam', greering='Hi'))

#%% Function with arbitrary number of positional and keyword arguments.
#   *args becomes a tuple
#   **kwargs becomes a dictionary
def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(1,2,3,4, key = 123, name = 'John')

#%% Unpacking into a function
def fun(*args, **kwargs):
    print(args)
    print(kwargs)

L = [1,2,3,4,5]
D = {'Jack':1234, 'Amy':23094, 'Emily':2394}
fun(L, D)
fun(*L, **D)

#%% Using docstring to document what a function does
def STD(*args):
    """This function returns standard deviation"""
    sum1 = sum(args)
    mean = sum1/len(args)
    zero_cent = [num - mean for num in args]
    squares = [x**2 for x in zero_cent]
    sum2 =sum(squares)/len(args)
    return sum2**0.5

L = [1,2,3,4,5]
print(STD(*L))

