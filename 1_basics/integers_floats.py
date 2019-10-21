#%% type() method checks difference between int and float
print(type(3))
print(type(3.4))



#%% abs() returns absolute value of a number. Not an in-place method.
print(abs(-3))
print(abs(-3.14))

#%% round() rounds to nearest integer. If we pass second argument, it rounds
#   to that number of decimal places
print(round(3.490))
print(round(3.500))
print(round(3.510))
print()
print(round(3.512, 2))  # Here it rounds to 2 decimal place
print(round(3.512, 1))  # Here it rounds to 1 decimal place

#%% Casting with int() and str()
num1 = '10'
num2 = '20'
print(num1 + num2)

num1 = int(num1)
num2 = int(num2)
print(num1 + num2)

num1 = str(num1)
num2 = str(num2)
print(num1 + num2)
