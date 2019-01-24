#%% Creating a list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

#%% List comprehension
squares = [x**2 for x in range(0,11,2)]

#%% Create an empty list - both methods are fine
empty_list = []
empty_list = list()

#%% Alias considerations
a = [1,2,3]
b = a       # This would create alias
b = a[:]    # This creates a new copy of list and returns it, no alias created

#%% Access elements from front, from back
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0])
print(courses[-1])

#%% List of lists and accessing it
nums = [[1,2,3],[4,5,6],[7,8,9]]
print(nums[0][1])

#%% Change a slice of a list
nums = [1,2,3,4,5]
nums[2:4] = [0,0]
print(nums)

#%% Clear all elements from a list
nums = [1,2,3,4,5]
nums.clear()
print(nums)

#%% len() returns length of list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(len(courses))

#%% list[start:end:step] Slices through a list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0:2])
print(courses[:2])
print(courses[2:])
print(courses[2:4])
print(courses[::-1])
print(courses[::-2])
print(courses[::2])
print(courses[-1:0:-1])

#%% .append Adds an element to the end of list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
courses.append("Art")
print(courses)

#%% .insert(elem, index) Inserts element at a given index in a list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
courses.insert(0, "Art")
print(courses)

#%% list1.extend(list2) adds contents of list2 to the end of list1
#   This is an inplace method. It doesn't return anything
courses = ['History', 'Math']
courses_2 = ['Art', 'Geography']
courses.extend(courses_2)
print(courses)

#%% list1 + list2
#   Returns new list where elements of list2 are added to the end of list1.
#   Same as .extend, but returns new list instead of being an inplace method.
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print(L1)
print(L2)
print(L3)

#%% list.remove(element) removes known element from the list. Inplace method.
#   Gives error if element is not in the list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
courses.remove('Math')
print(courses)

#%% list.pop() removes last element of the list and returns it.
#   list.pop(index) removes element at given index and returns it.
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
a = courses.pop()
print(courses)
b = courses.pop(0)
print(courses)
print()
print(a)
print(b)

#%% list.reverse() Reverses list in place. Does not return anything
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
courses.reverse()
print(courses)

#%% reversed(list) Returns iterator object that goes through reversed list.
#   Original list is not changed.
nums = [1,2,3]
for x in reversed(nums): print(x, end=' ')

#%% list.sort() Sorts a list in place.
#   Can pass argument .sort(reverse = true) to reverse in descending order
numbers = [2,5,2,3,1,3,4]
numbers.sort()
print(numbers)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort(reverse=True)
print(courses)

#%% sorted(list) Returns a copy of sorted list. Does not change original list.
numbers = [2,5,2,3,1,3,4]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

#%% list.index(element) Returns index of a given element in the list.
#   Will create error if the element is not in the list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index("Physics"))

#%% x in list Returns True if item x is in the list, False otherwise
nums = [1,2,3,4,5]
print(10 in nums)

words = ['cat', 'dog', 'fish', 'mouse']
print('cat' in words)
print('bird' in words)

#%% Looping through a list
courses = ['History', 'Math', 'Physics', 'CompSci']

for word in courses:
    print(word)

print()
for word in courses: print(word)

#%% Enumerated looping through a list
#   If we pass optional argument start=N, enumeration will start from N
courses = ['History', 'Math', 'Physics', 'CompSci']

for index, word in enumerate(courses):
    print(index, word)

print()
for index, word in enumerate(courses, start=1):
    print(index, word)

#%% zip()
#   Zips two or more lists which can be looped through at once.
names = ['Eddie', 'Jason', 'Mike', 'Sophia']
professions = ['Researcher', 'Lecturer', 'Teacher', 'Editor']
experience = [3, 5, 4, 2]
for name, prof, exp, in zip(names, professions, experience):
    print(f'{name} is a {prof} with {exp} years of experience')

#%% min(list) Returns minimum element in the list.
numbers = [1,2,3,4,5]
print(min(numbers))

#%% max(list) Returns maximum element in the list.
numbers = [1,2,3,4,5]
print(max(numbers))

#%% sum(list) Returns sum of all elements in the list.
numbers = [1,2,3,4,5]
print(sum(numbers))

#%% Use list as a stack
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.append('Art')   # .push()
courses.pop()           # .pop()
len(courses)            # .size()
len(courses) == 0       # .isEmpty()
courses[-1]             # .top()

