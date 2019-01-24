import os

#%% os.getcwd() Returns current working directory as string.
print(os.getcwd())

#%% os.chdir(path) Changes current working directory to a given path
os.chdir("C:\\Users\Sasha\Pictures\Wallpapers")
print(os.getcwd())

#%% os.listdir() Shows all files and folders in current working directory
#   os.listdir(path) Shows all file and folders in a specified path
print(os.listdir(), "\n")
print(os.listdir("C:\\Users\Sasha\Pictures\Deawings"))

#%% os.mkdir('FolderName') Makes a new directory in current path.
os.mkdir('Puppy')

#%% os.makedirs('FolderStructure') Can make a deep directory structure
os.makedirs('Fish/Cat')

#%% os.rmdir('Folder') Removes a single directory.
os.rmdir('Puppy')

#%% os.removedirs('Folder/Folder') Removes one or more deep directories.
os.removedirs('Fish/Cat')

#%% os.rename('original_name', 'new_name') Renames file or folder to new name.
os.rename('Coding', 'Code Wallpapers')

#%% os.stat('file') Returns a string with info about that file.
print(os.stat("London_from_above.jpg"))

#%% os.stat('file').st_mtime Returns las modification time of file as a timestamp
#   We can convert the timestamp using the datetime module
from datetime import datetime
modification_time = os.stat("London_from_above.jpg").st_mtime
print(datetime.fromtimestamp(modification_time))

#%% os.walk() or os.walk(path) Traverses through all files and folders within
#   the current or specified path and returns them as an iteratable triple.
for dirpath, dirnames, filenames in os.walk("C:\\Users\Sasha\Pictures"):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#%% os.environ Prints out all environment variables
print(os.environ.get('USERDOMAIN'))

#%% os.path.join(path1, path2) Returns a string of two paths joined.
#   It doesn't necessarily mean the path will exist, it just concatenates two paths.
#   In other words it makes sure you don't have to mess with slashes "\"
print(os.path.join("C:\\Users\Sasha\Pictures", "Sasha\Pictures\Wallpapers\London_from_above.jpg"))

#%% os.path.basename(path) Returns the file name on the end of the path.
#   The file or directory doesn't necessarily have to exist.
print(os.path.basename("C:\\Users\Sasha\Pictures\Wallpapers\London.jpg"))

#%% os.path.dirname(path) Returns name of directory the file on the end of the path is in.
print(os.path.dirname("C:\\Users\Sasha\Pictures\Wallpapers\London.jpg"))

#%% os.path.exists(path) Returns a boolean indicating whether the given path actually exists in the system.
print(os.path.exists("C:\\Users\Sasha\Pictures\Wallpapers\London.jpg"))
print(os.path.exists("C:\\Users\Sasha\Pictures\Wallpapers\London_from_above.jpg"))

#%% os.path.isdir(path) Returns a boolean indicating whether end file on this path is a directory
#   os.path.isfile(path) Returns a boolean indicating whether end file on this path is a file
print(os.path.isdir("C:\\Users\Sasha\Pictures\Wallpapers\London_from_above.jpg"))
print(os.path.isfile("C:\\Users\Sasha\Pictures\Wallpapers\London_from_above.jpg"))

#%% os.path.splitext(path) Returns a tuple with path and extension split apart
print(os.path.splitext("C:\\Users\Sasha\Pictures\Wallpapers\London_from_above.jpg"))
