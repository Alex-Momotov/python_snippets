#%% General format of try-except statement
#   If code in try block throws and exception, then control flow moves to the except block.
#   Keyword 'Exception' catches all possible exceptions, but its a bad practice.
try:
    f = open('file.txt', 'r')
except Exception:
    print('File we are trying to open does not exist')

#%% Here we catch a more specific exception - FileNotFoundError. If any other type of
#   errors will occur, an exception will not be handled and an error will occur. To see this
#   behaviour un-comment the bad variable assignment
try:
    # var = bad_var
    f = open('file.txt', 'r')
except FileNotFoundError:
    print('File we are trying to open does not exist')

#%% In this code block we handle a specific type of exception - FileNotFound, but if any other
#   type of exception occurs we also handle it with the general 'except Exception' statement.
try:
    # var = bad_var
    f = open('file.txt', 'r')
except FileNotFoundError:
    print('File we are trying to open does not exist.')
except Exception:
    print('Something else went wrong.')

#%% except Exception as e:
#   One way to print out more meaningful exceptions is to pass exception name into print statement.
try:
    # var = bad_var
    f = open('file.txt', 'r')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

#%% Adding 'else' statement adds an additional logic to 'try' block.
#   The else block only executes if 'try' block executed correctly without raising any errors.
#   'else' block can be viewed as continuation of the 'try' block, which only works if 'try' succeeded.
#   For example, we only want to read a file if it opened successfully.
#   Change 'file.txt' to 'test.txt' to see the difference.
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\1. Basics")
try:
    f = open('file.txt', 'r')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

#%% The 'finally:' block executes no matter if the 'try' block was successful or not.
#   The 'finally' block is always in the end, after 'try', 'except', and 'else' blocks.
#   Use finally, when you want to perform an action no matter what. For example closing an open file or a database.
#   In example below, if 'try' fails after file was opened, then the else block wont be executed and won't close it;
#   therefore, we must close the file in our 'finally' block, no matter if it worked or not. Uncomment var to see this.
try:
    f = open('test.txt', 'r')
    # var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print(f.closed)
    f.close()

#%% raise Exception
#   'raise' is the keyword to throw your own exceptions.
#   Usually, 'raise' is put inside an if-statement which detects a bad situation.
def division(divident, divisor):
    if divisor == 0:
        raise Exception('Division by zero')
    else:
        return divident / divisor

num = 0
try:
    division(10,num)
except Exception as e:
    print(e)

