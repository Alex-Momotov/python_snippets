#%% Creating a tuple
courses = ('History', 'Math', 'Physics', 'CompSci')

#%% Create an empty tuple - both ways are fine
empty_tuple = ()
empty_tuple = tuple()

#%% Accessing elements of a tuple
print(courses)
print(courses[0])
print(courses[-1])
print(courses[:2])
print(type(courses[:2]))

#%% Convert tuple or slice of tuple into a list
courses = ('History', 'Math', 'Physics', 'CompSci')
list_courses = list(courses)
print(courses)
print(list_courses)

#%% Convert list into a tuple
courses = ['History', 'Math', 'Physics', 'CompSci']
tuple_courses = tuple(courses)
print(courses)
print(tuple_courses)

#%% Common methods to a list
nums = (1,2,3,4,5)
print(
    max(nums),
    min(nums),
    sum(nums),
    len(nums),
    nums.count(2),
    nums.index(5)
)

#%% sorted(tuple) Return a sorted list from a tuple
nums = (3,5,4,7,2,1)
sorted_nums = sorted(nums)
print(sorted_nums)
