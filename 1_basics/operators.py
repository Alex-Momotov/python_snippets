#%% Arithmetic Operators:
print(3 + 2)    # Addition
print(3 - 2)    # Subtraction
print(3 * 2)    # Multiplication
print(3 / 2)    # Division - will return 1.5
print(3 // 2)   # Floor Division - will return 1
print(3 ** 2)   # Exponent
print(3 % 2)    # Modulus - can be used to check if number is odd or even

#%% Incrementing Operators
num = 5

num += 1    # Increment by
num -= 1    # Decrement by
num /= 2    # Divide itself by
num *= 2    # Multiply itself by
num //= 2   # Floor-divide itself by
num **= 2   # Raise itself to a power
num %= 2    # Modulus of itself

#%% Boolean Operators
print(3 == 2)
print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)

print()

print('cat' is 'cat')   # 'is' operator checks for identity - if two objects have same ID
print('dog' is not 'cat')
print('c' in 'cat')
print('d' not in 'cat')

print()

print(True and True)    # Same as && in Java
print(True or False)    # Same as || in Java
print(not False)        # Same as ! in Java
