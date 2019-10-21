# Json module can be used to convert Python objects into strings and visa versa.

# json.loads(string)
# Returns original Python object from a string.
# The string did not have to come from Python, json uses conversion from other languages too.
import json

string = '[1,2,3,4,5]'
data = json.loads(string)

print(data)
print(type(data))

#%% json.dumps(object)
#   Returns a string, which can be later converted back into Python object.
#   The indent parameter adds indentation to every level of the string to help presentability.

numbers = [1,2,3,4,5,6,7]
string = json.dumps(numbers, indent=3)

print(string)
print(type(string))

#%% Save and load a list to a string using Json.
L = [x**3 for x in range(40)]
string = json.dumps(L)
print(string)
print(type(string))

data = json.loads(string)
print(data)
print(type(data))

#%% json.dump(data, file)
#   Saves an object to a json file. Data is any serializable Python object. File is a .json file opened using context
#   manager. Optional parameter is indent=3 to make the file more readable in a text editor.
import json
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\3_working_with_files")

articles = [
    {'title' : "Linux/Mac Terminal Tutorial: The Grep Command – Search Files and Directories for Patterns of Text",
     'body': "In this Linux/Mac terminal tutorial, we will be learning how to use the grep command. The grep command allows us to search files and directories for patterns of text.",
     'time': 'March 19, 2018'},
    {'title' : "How to Run Linux/Bash on Windows 10 Using the Built-In Windows Subsystem for Linux",
     'body': "In this video, we will be learning how to run Linux on Windows using the new Windows Subsystem for Linux that comes with Windows 10. This is an excellent way to run Bash on a Windows machine. It allows you to use all of the Bash commands we are used to using on Linux within a Windows system. We will be showing how to enable and install Linux on Windows and also go over a quick overview to see how this works. Let’s get started…",
     'time': 'March 15, 2018'},
    {'title': "Python Tutorial: Calculate Number of Days, Weeks, or Months to Reach Specific Goals",
     'body': "In this Python Programming Tutorial, we will be writing three different scripts to estimate how long it will take to reach certain goals. Our first script will calculate how many months it will take us to pay off a credit card. Our second script will calculate how many weeks it will take to lose a certain amount of weight. And our third script will estimate how long it will take to reach a certain number of subscribers. Let’s get started…",
     'time': 'March 12, 2018'},
]

with open('test.json', 'w') as f:
    json.dump(articles, f, indent=5)

#%% json.load(file)
#   Returns a deserialized object from a json file. First the .json file is opened using context manager.
import json
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\3_working_with_files")

with open('test.json', 'r') as f:
    articles = json.load(f)

print(articles)

#%% This script uses Yahoo Finance API to get data and transform it to json files
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/"
             "allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

# print(len(data['list']['resources']))
# print(data['list']['resources'][0]['resource'])

usd_rates = {}

for item in data['list']['resources'][0:150]:
    try:
        name = item['resource']['fields']['name']
        price = item['resource']['fields']['price']
    except Exception:
        name = None
        price = None
    print(name, price)
    usd_rates[name] = price

print(usd_rates['USD/EUR'])





