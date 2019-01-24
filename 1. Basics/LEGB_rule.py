#%%     LEGB Rule:
#       Local -> Enclosing -> Global -> Bultin
#   Local        -  Variables declared within a function. Also function's parameter variables.
#   Enclosing    -  Variables declared outside current function, but within enclosing function (nested functions).
#   Global       -  Variables declared within the main body of the Python file.
#   Bultin       -  Variables that are in builtin list.
#   When execution flow cannot find a certain variable in Local scope, it goes out to search in Enclosing scope. When
#   that fails, it goes out again, and searches within the Global scope. If that fails, then it will go to search within
#   the Builtin variables list. If that fails too, an error will be raised.

#%% Way to list builtin variables.
import builtins
built_in_vars = list(dir(builtins))
for x in built_in_vars: print(x)

#%% Comment out different print() statements to understand how LEGB rule works.

x = 'global x'

def enclosing():
    x = 'enclosing x'
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)

enclosing()
print(x)

del x

#%%