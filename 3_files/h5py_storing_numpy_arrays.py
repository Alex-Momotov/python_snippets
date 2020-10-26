import h5py
import numpy as np
import os
from memory_profiler import memory_usage as memory
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\3_files")

#%% An HDF5 file is a container for two kinds of objects: datasets, which are array-like collections of data, and
#   groups, which are folder-like containers that hold datasets and other groups. Groups work like dictionaries, and
#   datasets work like NumPy arrays.

#%% Let's create a 10,000 by 10,000 nparray of random numbers to practise saving and loading it.
data1 = np.random.randint(0,100, [1000,1000])
data2 = np.ones([10,10])

#%% To save a Numpy array into .hdf5 file:
#   Step 1 - Create an empty file and open it for writing using context manager e.g. with h5py.File(filename, 'w') as f:
#   Step 2 - Save our numpy array into the file e.g.    f.create_dataset(dataset_name, data=array)
#   chunks=True sets automatic chunking, so that when reading from large file only the indexed chunk will be read.
with h5py.File("numpy_array.hdf5", 'w') as f:
    f.create_dataset("Random numbers", data=data1, chunks=True)
    f.create_dataset("Ones", data=data2)
del data1
del data2

#%% To load a Numpy array from .hdf5 file:
#   Step 1 - (optional) Iterate through file object and see which datasets are stored in it.
#   Step 2 - Retrieve the needed dataset (as a dataset object) by indexing file object like a dictionary e.g. f['nums']
#   Step 3 - Index dataset object like a numpy array to retrieve all or a portion of it as a numpy array.
with h5py.File("numpy_array.hdf5", 'r') as f:
    for ds in f: print(ds)    # Iterating through file object prints out all datasets in it.
    DS1 = f['Ones']
    A1 = DS1[...]
    A2 = f['Random numbers'][...]
    A3 = f['Random numbers'][:10,:10]

#%% Example of how to write a gigantic numpy dataset to a disk without ever storing it in the memory.
print(memory())
with h5py.File("numpy_array.hdf5", 'w') as f:
    f.create_dataset("Random numbers", data=np.random.randint(0,100, [10000,10000]))
print(memory())

#%% Create a blank dataset with zeros, then write to it one number at a time.
with h5py.File("np_data.hdf5", 'a') as f:
    ds1 = f.create_dataset("blank3", data=np.zeros([10,10], int))
    ds1[0,0] = 5
    A1 = ds1[:]
    print(A1)

#%% File mode considerations and deletion.
#   'w' mode will override all existing datasets in the file.
#   'r' mode will only read.
#   'a' mode can add new datasets to the file, without overriding anything.
#   'r+' useful for deleting dataset from a file.
#   To delete a dataset: del f['dataset']
with h5py.File("np_data.hdf5", 'r+') as f:
    for x in f: print(x)
    print()
    del f['blank2']
    for x in f: print(x)

#%% Dataset objects support attributes .shape .size .dtype
with h5py.File("numpy_array.hdf5", 'r') as f:
    ds1 = f['Ones']
    ds2 = f['Random numbers']
    print(ds1.shape, ds1.size, ds1.dtype, sep='\n', end='\n\n')
    print(ds2.shape, ds2.size, ds2.dtype, sep='\n', end='\n\n')

#%% Sometimes we want to create an empty dataset and populate it later. To do that:
with h5py.File("test_np.hdf5", 'w') as f:
    f.create_dataset("data", shape=[10,10], dtype='i8')
    f.create_dataset("data2", shape=[10,10], dtype='i8', chunks=True, data=np.random.randint(0,2,[10,10]))
    print(f['data'])
    print(f['data'][...], end='\n\n')
    print(f['data2'][...])

#%% A much simpler way is to save and load numpy arrays using np.save and np.load().
#   See notes on numpy for more details.
import numpy as np

arr = np.random.randint(0,100, [10,10])
np.save("arr.npy", arr)
del arr
arr2 = np.load("arr.npy")[:, :]
print(arr2)

