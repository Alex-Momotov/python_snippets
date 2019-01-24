import os
os.chdir('C:\\Users\Sasha\Coding\Python\\0. Learning Python\\3. Working with Files')

#%% To pickle a Python object
#   Step 1 - Import pickle
#   Step 2 - Open a .pickle file in a binary writing mode 'wb'
#   Step 3 - Call pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
data = [1,2,3]
import pickle
with open('test.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

#%% To load Python object from pickle file
#   Step 1 - Open the .pickle file in binary reading mode 'rb'
#   Step 2 - Call pickle.load(f) which returns the Python object
with open('test.pickle', 'rb') as f:
    data = pickle.load(f)





