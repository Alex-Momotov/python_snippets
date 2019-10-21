#%% List comprehensions.py
L1 = [n**2 for n in range(1,11)]
print(L1, '\n')

L2 = [n for n in range(1,11) if n%2 == 0]
print(L2, '\n')

L3 = [(letter, num) for letter in 'ab' for num in range(1,3)]
print(L3, '\n')

L4 = [letter+str(num) for letter,num in zip('abc',range(1,4))]
print(L4, '\n')

L5 = [x%2==0 for x in range(1,9)]
print(L5)

#%% Dictionary comprehensions.py
#   Notice the curly brackets.
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

D1 = {name: hero for name, hero in zip(names, heros)}
print(D1, '\n')

D2 = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(D2, '\n')

#%% Set comprehensions.py.
#   Difference to dictionary comprehensions.py is that there are no colon.
S1 = {x**2 for x in range(1,11)}
print(S1, '\n')

S2 = {x**2 for x in range(1,22) if x%3==0}
print(S2, '\n')

#%% Generator expressions.
G = (x**2 for x in range(1,11))

for x in G:
    print(x)

#%%



