from memory_profiler import memory_usage
import numpy as np
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\2_basics_advanced")

#%% 1st way to create Numpy array.
#   np.array(list, dtype=)      Converts list or tuple structure into numpy array.
L1 = [1,2,3,4,5]
L2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
A1 = np.array(L1, dtype=float)
A2 = np.array(L2)
A3 = np.array([i**2 for i in range(100)]).reshape(10,10)
print(A1, A2, A3, sep='\n')

#%% 2nd way to create Numpy array.
#   np.zeros(shape, dtype)      Creates matrix of zeros. Default dtype is float64
#   np.ones(shape, dtype)       Creates matrix of ones.
N1 = np.zeros([10,10])
N2 = np.zeros([5,5], dtype=np.float16)
N3 = np.ones([4,4], int)
print(N1, N2, N3, sep='\n\n')

#%% 3rd way to create Numpy array.
#   np.arange([start,] stop[, step,], dtype=None) Your usual range() method, but generates Numpy array instead.
#   np.linspace(start, stop, num=50)    Return num evenly spaced numbers over a specified interval.
#   If step is a float we should use linspace() instead of arange()
A1 = np.arange(10, dtype=float)
A2 = np.arange(5,11)
A3 = np.arange(0,21,2)
A4 = np.linspace(0.1,1,10, dtype=float)
A5 = np.linspace(1,10,19)
print(A1, A2, A3, A4, A5, sep='\n\n')

#%% np.arange(num).reshape(shape)
#   A common way to create a numpy array.
A1 = np.arange(1,101).reshape(10,10)
print(A1)

#%% 4th way to create Numpy array.
#   np.random.rand(size)    Array of uniformly distributed values 0 to 1 of given size.
#   np.random.randint(low[, high, size, dtype]) Array of random integers between set values and of given size.
A1 = np.random.rand(10,10)
A2 = np.random.randint(0,100,[10,10], dtype=int)
A3 = np.random.randint(0,10,[10,10])/10
print(A1, A2, A3, sep='\n\n')

#%% 5th way to create Numpy array.
#   Is to read in a Numpy array from disk. Can either use np.save() and np.load() or external h5py library.
#   np.save('file.npy', data)               Data must be single numpy array. Saves data to a npy file.
#   np.load('file.npy', mmap_mode=None)     A memory-mapped array is kept on disk. However, it can be accessed and
#   sliced like any ndarray. Memory mapping is especially useful for accessing small fragments of large files without
#   reading the entire file into memory. Memory mapped modes are 'r+' or 'r'. If using memory map, need to remember to
#   delete memory map objects, else it is considered as an open file.

arr = np.random.randint(0,100, [10,10])
np.save("arr.npy", arr)
del arr
arr = np.load("arr.npy")
print(arr)

#%% Memory-mapped loading vs normal loading. As we can see, memory usage is zero when we load using memory mapping
data = np.random.randint(0,100,[1000,1000])
np.save('huge.npy',data)
del data
print(memory_usage())
data = np.load('huge.npy')
print(memory_usage())
del data
print(memory_usage())
data = np.load('huge.npy', mmap_mode='r')
print(memory_usage())
del data

#%% Main NumPy array attributes
#   NumPy arrays are of data type 'numpy.ndarray'
#   .ndim   Number of matrix dimensions 2D -> 2, 3D -> 3
#   .shape  Returns tuple which is number of rows and columns within array (rows,cols) for 2D array
#   .size   Total number of elements within the array
#   .dtype  Type of the elements in the array. Can be Python types or NumPy types
arr = np.random.randint(0,10,[10,5], int)
print(type(arr))
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

#%% np.set_printoptions(threshold=np.nan)
#   This command makes sure NumPy arrays are printed entirely, instead of being truncated.
np.set_printoptions(threshold=np.nan)
print(np.arange(10000).reshape(100,100))

#%% Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
a = np.zeros([4,4]) + 5
b = np.ones([4,4]) * 100
print(a)
print(b)
print(a+b)

#%%
a = np.arange(0,100).reshape(10,10)
print(a**2)

#%%
a = np.random.randint(-10,10,[10,10])
c = a>0
print(a)
print(np.abs(a))
print(c)

#%% The * operator performs elementwise mupliplication.
#   If we want dot product, we need to use A.dot(B)
a = np.arange(4).reshape(2,2)
b = np.ones([2,2])*2
print(a*b)
print(b.dot(a))

#%% Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.
a = np.ones([2,3], dtype=int)
b = np.random.rand(2,3)
a*=3
print(a)
b += a
print(b)
# a += b   # Will raise error because we cant cast float onto int array

#%% When operating with arrays of different types, the type of the resulting array corresponds to the more general
#   or precise one (a behavior known as upcasting).
a = np.ones([3,3], dtype=np.int8)
b = np.ones([3,3], dtype=np.int16)
c = a + b
print(c.dtype)

#%% np.round(arr, dec)
#   arr.round(dec)
#   Both return new array with all values in arr rounded to dec decimal places
a = np.random.rand(10,10)
a = np.round(a, 1)
print(a)

#%% arr.T
#   Returns a copy of transposed array.
a = np.arange(20).reshape(2,10)
print(a)
print(a.T)

#%% Common unary operations are methods of ndarray class. By default, these operations apply to the array as though it
#   were a shapeless list of numbers. To apply along specific axis we need to specify axis keyword.
#                             (axis=0) columns        (axis=1) rows
#   arr.min(axis=)              Min
#   arr.max(axis=)              Max
#   arr.sum(axis=)              Sum
#   arr.mean(axis=)             Returns new array of mean values along given axis
#   np.median(arr, axis=)       Returns new array of median values along given axis
arr = np.arange(1,16).reshape(3,5)
print(arr, end='\n\n')
print('median', np.median(arr,axis=0))
print('min', arr.min(axis=0))
print('max',arr.max(axis=0))
print('mean axis=0',arr.mean(axis=0))
print('sum axis=1',arr.sum(axis=1))

#%% np.std(arr, axis=)
#   Returns new array of Standard Deviation values along given axis
arr = np.random.randint(-10,10,[10,10])
std = np.std(arr, axis=0)
print(std.round(2))

#%% np.var(arr, axis=)
#   Returns new array of Variance values computed along given axis
arr = np.random.randint(-10,10,[10,10])
var = np.var(arr, axis=0)
std = np.std(arr, axis=0)
print(var)
print(std**2)

#%% Universal functions.
#   Mathematical functions provided by NumPy. They operate elementwise on an array and produce a new array as an output.
#   np.all(axis=)   Logical AND along given axis
#   np.any(axis=)   Logical OR along given axis
#   np.sqrt()       Square root, elementwise
a = np.arange(4)
print(np.sqrt(a))
b = np.array([[True, False], [False, False]])
print(b)
print(np.any(b, axis=0), '\n')

#%% np.apply_along_axis(func, axis, arr, *args, **kwargs)
#   Applies a function that operates on a 1D array (or list) on a specified axis.
#   The *args, **kwargs in the above signature are for the function that is applied along axis (func)
def rounding(L):
    L2 = [round(i, 2) for i in L]
    return L2

def min_(L):
    min = 9999999
    for i in L:
        if i < min: min = i
    return min

a = np.random.rand(10,10)
b = np.apply_along_axis(rounding, 0, a)
c = np.apply_along_axis(min_, 0, b)
print(b)
print(c)

#%% np.logical_and(arr1, arr2)
#   np.logical_or(arr1, arr2)
#   Take two boolean arrays of same shape and return new array of their logical AND/OR operations.
arr = np.random.randint(1,100,[10,10])
bool_arr1 = arr[:,0] > 50   # Rows where first column value is bigger than 50
bool_arr2 = arr[:,1] > 50   # Rows where second column value is bigger than 50
cond_and = np.logical_and(bool_arr1, bool_arr2)     # Rows where first AND second column values are bigger than 50
cond_or = np.logical_or(bool_arr1, bool_arr2)       # Rows where first OR second column values are bigger than 50
print(cond_and)
print(cond_or)

#%% Boolean arrays can be used to index NumPy arrays and return new arrays.
arr = np.random.randint(1,100,[10,10])
A2 = arr[arr[:,0]>50]
print(A2)

#%% Combining the above two functionalities we can create subsets of original arrays based on conditions.
#   For example, this will select rows where values in first OR second columns are above 75.
arr = np.random.randint(1,100,[10,10])
cond = np.logical_or(arr[:,0] > 75, arr[:,0] > 75)
print(arr[cond,:])

#%% For instance, lets select all rows where first column value is even
arr = np.random.randint(1,100,[10,10])
result = arr[arr[:,0]%2==0,:]
print(result)

#%% np.isin(arr, values)
#   Finds indices of elements in arr which are in values.
#   Can use the resultant indices to index the array too.
good_values = [11,21,41]
arr = np.arange(1,101).reshape(10,10)
idx = np.isin(arr[:,0], good_values)
print(arr[idx,:])

#%% Three dots [...] represent as many colons as needed to produce a complete indexing
a = np.random.randint(0,2,[10,10])
print(a[...])
print(a[:,...])
print(a[...,:4])

#%% Iterating through arrays
#   Nexted for loops iterate through rows then through columns
matrix = np.arange(1,26).reshape(5,5)
print(matrix, '\n')
for row in matrix:
    for col in row:
        print(col)

#%% arr.flat
#   The attribute returnes flattened array as an iterator which goes through rows then columns
#   similarly to the nested for loop.
matrix = np.arange(1,26).reshape(5,5)
print(matrix, '\n')
print(matrix.flat, '\n')
for elem in matrix.flat:
    print(elem)

#%% arr.reshape()       Returns reshaped copy of array
#   arr.T               Returns transposed copy of array
#   arr.ravel()         Returns flattened copy of array
#   arr.resize([size])  Reshapes array in place!!!
#   Both return a copy of array, they do not modify array shape in place.

#%% np.vstack([arr1, arr2])       Stacks arr1 on top of arr2 and returns the new stacked array.
#   np.hstack([arr1, arr2])       Stacks arr1 and arr2 together, such that arr1 is on the left and arr2 on the right.
arr1 = np.ones([4,4])
arr2 = np.zeros([4,4])
arr3 = np.ones([4,4])
print(np.vstack([arr1, arr2, arr3]), '\n')
print(np.hstack([arr1, arr2, arr3]), '\n')

#%% np.vsplit(arr, [idx])   Vertically splits array and returns array parts as in a list, idx specifies split index(s)
#   np.hsplit(arr, [idx])   Horisonrally splits array and returns array splinters in a list
arr = np.arange(1,101).reshape(10,10)
print(arr, '\n')
print(np.vsplit(arr, [3])[0], '\n')
print(np.hsplit(arr, [3])[0])

#%% Copies, deep copies and views and distinction (see 3 blocks of code below)
a = np.arange(25).reshape(5,5)
#%% Alias
#   Single assignment does not create a copy, instead it creates alias.
b = a                   # Changing b will change a
print(id(a), id(b))     # Thier object ID is same
print(b is a)
#%% View
#   Slicing an array will return a 'view' of it. Changing data in a view changes original array, but changing
#   shape of view does nothing to the original.
a = np.arange(25).reshape(5,5)
b = a[...]
print(id(a), id(b))     # Thier object ID is different
print(b is a)
b.resize([1,25])
b[0,4] = 999
print(a, b, sep='\n')
#%% Deep Copy
#   arr1 = arr2.copy()  Creates a complete copy of the array and its data
#   Objects are independent, changing one does not change another.
a = np.arange(25).reshape(5,5)
b = a.copy()
print(b is a)
b[0,0] = 999
print(a, b, sep='\n\n')
