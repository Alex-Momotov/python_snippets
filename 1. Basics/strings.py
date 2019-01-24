#%% Quotes, multi-line comments
message = "Hello' Word!"
message = 'Hello" Word!'
message = "Hello\" Word!"
message = 'Hello\' Word!'

#%% Multi-line string using triple quotes ''' or """
message = '''This is a
multi-line string
'''
print(message)

#%% Multi-line comment using triple quotes ''' or """
'''
that's
multi-line
comment
'''

#%% len() prints length of string
len("hello")

#%% Index and slice a string
h = "hello"
print(h[0])
print("hello"[0])
print(h[-1])
print(h[0:3])
print(h[:3])

#%% .lower() makes string lowercase. Not an in-place method.
string = "Hello World!"
print(string.lower())
print(string)

#%% .upper() makes string uppercase. Not an in-place method.
string = "Hello World!"
print(string.upper())
print(string)

#%% .count() counts characters or substrings in a string
string = "she and he and they and me"
print(string.count("and"))
print(string.count("m"))
print(string.count("she"))

#%% .find() finds character or substring in a string and returns its index;
#    if not found returns -1
string = "she and he and they and me"
print(string.find("she"))
print(string.find("and"))
print(string.find("y"))
print(string.find("hello"))

#%% .replace() replaces a substring or character in a string with another string
#    Not an in-place method.
string = "she and he and they and me"
print(string)
print(string.replace("they and ", "") + "\n")  # original string is unchanged

string = string.replace("she", "Sarah")
print(string)

string = string.replace("and", "+")
print(string + "\n")

string = "she and he and they and me"
print(string)
print(string.replace(" ", ""))

#%% Concatenating strings
greeting = 'Hello'
name = 'Michael'
message = greeting + ", " + name + '. Welcome!'
print(message)

#%% separator.join(list) Joins elements in the list over the given separator
#   and returns it.
courses = ['History', 'Math', 'Physics', 'CompSci']
result = '__'.join(courses)
print(result)

#%% text.split(', ') Splits a given string using given separator and returns list
text = 'History, Math, Physics, CompSci'
courses = text.split(', ')
print(courses)

#%% "{}".format() Is string formatting
greeting = 'Hello'
name = 'Michael'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#%% f'{string}' Is same as "{}".format() but you can write code in placeholders {}
greeting = 'Hello'
name = 'Michael'
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

#%% dir() returns a list of all methods available to that object
string = "test string"
print(dir(string))
print(dir(2))

#%% help() prints out all methods of an object and their descriptions.
#   Can also print out a specific method.
help(int)
help(5)
help(str)
help("test")
help(str.join)

#%% Iterate through string
string = 'Hello World!'
for letter in string:
    print(letter)

#%% string.strip() Removes trailing and leading whitespace from a string.
#   string.strip('!.,# ') Removes specified trailing and leading characters from a string.
string = "  e! example,!#  "
print(string)
print(string.strip())
print(string.strip(' ,!#'))

#%% re.sub('.|,|#', '', string)
#   Replaces or removes all occurrences of specified characters in a string.
import re
string = '@#! , text!312,>..'
print(re.sub('>|\.|@|#|,|1|2|3|!','',string))
