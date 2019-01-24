#%% Four ways to create a dictionary

# [WAY 1] Write out by hand
d1 = {'Jack':1234, 'Amy':23094, 'Emily':2394}

# [WAY 2] Faster way of writing by hand, only works if all keys are strings
d3 = dict(adsifk=23421, sadf=21341, momermf=23412)

# [WAY 3] Dictionary comprehension
d2 = {x:(x-5) for x in range(10)}

# [WAY 4] Using dict() function on a sequence of pairs, e.g. list of lists, tuple of tuples
d4 = dict([['Jack', 1234], ['Amy', 23094], ['Emily', 2394]])

#%% Create an empty dictionary - both methods are fine
d0 = {}
d0 = dict()

#%% Access a value of a given key. If not found will give error.
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
print(phones)
print(phones['Jack'])
print(phones['Sarah']) # Will give error

#%% dictionary.get(value)
#   Is a second way to access a value of a given key.
#   This way is better because when key not found, will not give error, instead will return None.
#   Can pass second parameter dictionary.get(value, 'Not found') which is returned if key not found
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
print(phones)
print(phones.get('Jack'))
print(phones.get('Sarah'))
print(phones.get('Sarah', 'Not found'))

#%% Adding new key-value pairs to dictionary.
#   If the key already exists, the command will update its value
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
print(phones)
phones['Sarah'] = 7777
print(phones)
phones['Jack'] = 9999
print(phones)

#%% dictionary.update({values})
#   Updates multiple values in the dictionary
#   If some key-value pairs don't exist, they will be created
phones = {'Jack': 1234, 'Amy': 23094, 'Emily': 2394}
print(phones)
phones.update({'Jack': 9999, 'Amy': 0000, 'Sarah': 1234})
print(phones)

#%% del dictionary['key']
#   Deletes a key-value pair from a dictionary.
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
print(phones)
del phones['Emily']
print(phones)

#%% dictionary.pop('key')
#   Removes the key-value pair from dictionary and returns its value.
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
print(phones)
Jack_num = phones.pop('Jack')
print(Jack_num)
print(phones)

#%% len(dictionary)
#   Returns number of key-value pairs in a dictionary
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
print(len(phones))

#%% dictionary.keys()
#   Returns all keys from a dictionary as an iterator
#   You cannot index the returned iterator directly, will have to make
#   a list out of it by using L = list(dictionary.keys())
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
print(phones.keys())
for number in phones.keys(): print(number)
list_of_keys = list(phones.keys())
print(list_of_keys)

#%% dictionary.values()
#   Returns all values from a dictionary as an iterator
#   You cannot index the returned iterator directly, will have to make
#   a list out of it by using L = list(dictionary.values())
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
print(phones.values())
for val in phones.values(): print(val)
list_of_values = list(phones.values())
print(list_of_values)

#%% Another way to loop through keys in dictionary
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
for key in phones: print(key)

#%% dictionary.items()
#   Allows to loop through key-value pairs
phones = {'Jack':1234, 'Amy':23094, 'Emily':2394}
for key, value in phones.items(): print(key, value)
