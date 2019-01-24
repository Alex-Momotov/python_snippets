#%% This is how we would usually import the zip file reader module
from zipfile import ZipFile
import pickle
import os
os.chdir(r'C:\Users\Sasha\Coding\Python\0. Learning Python\3. Working with Files')

#%% Context manager for opening a zip file
#   myzip becomes the zip file object
with ZipFile(r'data/testing.zip', 'r') as myzip:
    print(type(myzip))

#%% myzip.infolist()
#   Returns an information list about all files contained in a zipped file.
#   Use attribute .filename to access the filename of each element in the list. But there is an easier way
with ZipFile(r'data/testing.zip', 'r') as myzip:
    inf_list = myzip.infolist()

print(inf_list[1], '\n')
for file in inf_list: print(file.filename)

#%% myzip.namelist()
#   Returns a list of names of all files contained in the zip file.
with ZipFile(r'data/testing.zip', 'r') as myzip:
    name_list = myzip.namelist()

for name in name_list: print(name)

#%% myzip.open(filename, mode)
#   Returns an external file object which then can be opened using pickle
with ZipFile(r'data/testing.zip', 'r') as myzip:
    with myzip.open(r'1.pickle', 'r') as myzip_data:
        data = pickle.load(myzip_data)
print(data)

#%% Iterate through the names in .namelist() to load each file with pickle
with ZipFile(r'data/testing.zip', 'r') as myzip:
    name_list = myzip.namelist()
    for name in name_list:
        with myzip.open(name, 'r') as myzip_data:
            data = pickle.load(myzip_data)
            print(data['title'])












