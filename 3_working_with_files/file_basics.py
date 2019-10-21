#%% f = open(path, 'r')
#   This way is not recommended to read and write files from.
#   Not specifying second argument means reading a file, by default 'r'
#   'r'     reading
#   'w'     writing - overwrites original file
#   'a'     appending - adds new strings to the end of file
#   'r+'    reading and writing
#   'rb'    reading binary files
#   'wb'    writing binary files
#   f.close() Closes the file. We must always close the file.
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\3_working_with_files")


f = open('test.txt', 'r')
print(f.name)
print(f.mode)
f.close()

#%% f.closed()
#   Returns a boolean, which is true is file is closed.
f = open('test.txt', 'r')
print(f.closed)
f.close()
print(f.closed)

#%% with open('test.txt', 'r') as f:
#   This is the proper way to open a file. This is called context manager.
#   This is because we don't have to worry about forgetting to close the file.
#   This way is the best practice way.
with open('test.txt', 'r') as f:
    pass

#%% f.read()
#   Returns all text in a file as a single string.
with open('test.txt', 'r') as f:
    contents = f.read()
print(contents)

#%% f.read(num_characters)
#   Returns specified number of characters in a file as a single string.
#   If you call f.read again in the same context manager, then f.read(num) picks up where it left off.
#   When end of file is reached, it will return an empty string
with open('test.txt', 'r') as f:
    contents = f.read(72)
    print(contents)
    contents = f.read(30)
    print(contents)
    contents = f.read()
    print(contents)

#%% f.tell()
#   Returns position of an imaginary caret when using f.read(number)
with open('test.txt', 'r') as f:
    print(f.tell())
    contents = f.read(72)
    print(contents)
    print(f.tell())
    contents = f.read(30)
    print(contents)
    print(f.tell())

#%% f.seek(position)
#   Moves imaginary caret to a specified position when using f.read(number)
with open('test.txt', 'r') as f:
    contents = f.read(14)
    print(contents)
    f.seek(0)
    contents = f.read(14)
    print(contents)

#%% f.readlines(num)
#   Returns all text in a file as a list of all lines.
#   If num is specified the method stops after this number of read characters.
with open('test.txt', 'r') as f:
    contents = f.readlines()
print(contents)

#%% f.readline()
#   Returns a single line from file as a string.
#   Each time we run f.readline() it goes to next line.
#   Could put it in a for loop.
with open('test.txt', 'r') as f:
    contents = f.readline()
    print(contents, end='')
    contents = f.readline()
    print(contents, end='')

#%% for line in f:
#   This for loop is a nice way to iterate through lines in a file
#   Variable line becomes string of each line, sequentially.
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

#%% with open('test2.txt', 'w') as f:
#   Opens the file for writing.
#   If file does not exist, it will create it.
#   If file does exist, it will override it.
#   To create an empty file, just write 'pass' into the context manager.
#   Having multiple f.write statements within same context manager will make it continue writing where it left off.
#   You can use f.seek() to move the imaginary caret, and it will start overriting what it has already written, even
#   within the same context manager.
with open('test2.txt', 'w') as f:
    f.write('This is a test string \n')
    f.write('Having multiple f.write statements will make it continue writing where it left off')

#%% How to open two files at once and copy contents of one file to another.
#   We can achieve the same result by nesting one content managers into another.
with open('test.txt', 'r') as rf, open('test_copy.txt', 'w') as wf:
    for line in rf:
        wf.write(line)

#%% Open two binary files (images) and copy contents of one into another.
#   We need to use binary mode for reading 'rb' and binary mode for writing 'wb' to accomplish this.
with open('test.jpg', 'rb') as rf, open('test_copy.jpg', 'wb') as wf:
    for line in rf:
        wf.write(line)

#%% Make list of lists of words in each line from a text
with open('test.txt', 'r') as f:
    all_words = [(line).split(' ') for line in f]
print(all_words)