#%% When we import another module with 'import' Python automatically runs all code in the module.
#   So all code in the module will be executed, including print() statements.
import sys
sys.path.append(r"C:\Users\Sasha\Coding\Python\0. Learning Python\1. Basics")
import imp_testing
import imp_testing as tst

L = [1,2,3,4]
print(imp_testing.find_index(L,3))
print(tst.find_index(L,3))


#%% from module import method Means we don't have to prepend function names with module name each time.
#   Using * is frowned upon because then it makes debugging harder
from imp_testing import *
from imp_testing import L
from imp_testing import find_index
from imp_testing import find_index as find

print(L)
K = [1,2,3,4]
print(find_index(K,3))
print(find(K,3))

#%% sys.path is a list of all paths where Python looks for, when it is trying to import a module
#   You can append a path to sys.path by using sys.path.append to import a module from a separate folder
import sys
print(sys.path)
sys.path.append('C:\\Users\\Sasha\\Coding\\Python\\0.0 Learning Python\\1_basics\\imp_testing.py')
print(sys.path)

#%% Random library
from random import choice
for x in range(10): print(choice(range(1,1000)))
rand_list = [choice(range(1,1000)) for x in range(1000)]
print(sum(rand_list)/len(rand_list))

#%% Datetime library
import datetime
today = datetime.datetime.today()
print(today)

#%% Antigravity module
import antigravity
