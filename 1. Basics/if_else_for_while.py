#%% If-elif-else statements
x = 3
if x < 3:
    print('yes')
elif x > 3:
    print('no')
else:
    print('x is 3')

#%% Another way of using if statements
a = 0
a += 5 + 5 if True else 3
print(a)


#%% Some more if-elif-else statements
condition1 = False
condition2 = True
if not condition1:
    print('yay')

if condition2 and 2 <= 3:
    print('both conditions satisfied')

if condition1 or condition2:
    print('either of conditions satisfied')

#%% Situations which evaluate to false in Python
print(
    bool('text'),   # True
    bool(''),       # False
    bool(25),       # True
    bool(-25),      # True
    bool(0),        # False
    bool(None),     # False
    bool([]),           # False
    bool([1, 2, 3]),    # True
    bool(()),           # False
    bool({}),           # False
)

#%% For loop iterating through list
#   If you want to use enumerate() and zip() - see 'lists.py'
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)


#%% Use of break statement
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 4:
        print('Found!')
        break
    print(num)

#%% Use of continue statement
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    if num % 2 == 1:
        continue
    print(num)

#%% Nested for loop
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    for letter in 'abc':
        print(num, letter)

#%% range(number) Is a handy way to iterate a certain number of times
for i in range(10):
    print(i)

#%% range(begin, end, step) Specifies beginning, end, and step of range
for i in range(0,21,2):
    print(i)

#%% While loop
x = 0
while x < 10:
    print(x)
    x += 1

#%% Infinite while loop
x = 0
while True:
    if x == 10:
        break
    print(x)
    x += 1
