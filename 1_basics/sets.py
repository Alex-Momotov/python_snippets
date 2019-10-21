#%% 1st way to create a set
#   Write it out by hand within curly braces
courses = {'History', 'Math', 'Physics', 'CompSci'}
print(courses)
print(type(courses))

#%% 2nd way to create a set
#   Use set function on a sequence
S = set([1,1,2,3,4,4,5,6,7])
print(S)

#%% 3rd way to create a set
#   Set Comprehension
s = {x**2 for x in range(10)}
print(s)

#%% Create an empty set using set()
empty_set_wrong = {}      # This is wrong, it creates empty dictionary
empty_set = set()         # This is the right way to create an empty set

#%% len(set)
#   Returns number of elements in the set
S = {1,2,3,4,5}
print(len(S))

#%% 'in' operator checks if element is in a set. Sets perform this operation
#   much faster than lists or tuples. To check membership for a list is O(n), for set it is O(1)
courses = {'History', 'Math', 'Physics', 'CompSci'}
print('Math' in courses)
print('Chemistry' in courses)

#%% set.add(element) Adds new element to the set. In-place method.
#   If it already has this element nothing happens.
numbers = {1,2,3,4,5}
numbers.add(5)
numbers.add(6)
print(numbers)

#%% set.update({elements}) Adds many new elements to the set. In-place method.
#   If set already has all or some of the elements then it adds only the ones
#   which it doesn't have. We can pass a list or another set.
numbers = {1,2,3,4,5}
numbers.update({1,2,3,6,7})
numbers.update(['a', 'b', 'c'])
another_set = {7,8,9}
numbers.update(another_set)
numbers.update([1,2,3], another_set) # also possible
print(numbers)

#%% set.remove(elem) Removes a given element from set. In-place method.
#   Error if element is not in set.
numbers = {1,2,3,4,5}
numbers.remove(2)
print(numbers)

#%% set.discard(elem) Removes a given element from set, but if element is not
#   in the set then no error will be raised
numbers = {1,2,3,4,5}
numbers.discard(2)
numbers.discard(10)
print(numbers)

#%% set.pop() Removes an arbitrary element from the set and returns it.
numbers = {1,2,3,4,5}
while len(numbers) > 0:
    numbers.pop()
    print(numbers)

#%% set.clear() Removes all elements from the set
numbers = {1,2,3,4,5}
numbers.clear()
print(numbers)

#%% set1.intersection(set2)
#   Returns a set of elements that two sets have in common. set2 can be a list also.
#   We can pass multiple sets to the parenthesis and it will return intersection of all the sets.
s1 = {1, 2, 3}
s2 = [2, 3, 4]
s3 = {3, 4, 5}
print(s1.intersection(s2))
print(s1.intersection(s2, s3))

#%% set1.difference(set2)
#   Returns set of elements which are in set1 but not in set2. set2 can be a list also.
#   We can pass multiple sets to the parenthesis and they will both 'eat away' elements from set1
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = [3, 4, 5]
print(s1.difference(s2))
print(s1.difference(s3))
print(s2.difference(s1, s3))

#%% set1.symmetric_difference(set2)
#   Returns all elements from each set, except for the ones they share in common.
#   The set in parenthesis can also be list
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = [3, 4, 5]
print(s1.symmetric_difference(s2))
print(s1.symmetric_difference(s3))

#%% set1.union(set2)
#   Returns a joined set of all elements
#   The set in parenthesis can also be a list
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = [3, 4, 5]
print(s1.union(s2))
print(s1.union(s3))

#%% Practical example 1:
#   Remove duplicate values from a list.
#   First cast to a set, then cast back to the list.
L = [1,1,2,3,3,3,4,5,6,6,7]
L = list(set(L))
print(L)

#%% Practical example 2:
employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven' ,'Jane', 'April']
#   To see all employees who are both gym members and developers:
result = set(gym_members).intersection(developers)
print(result)
#   To see employees who are neither gym members nor developers:
result = set(employees).difference(gym_members, developers)
print(result)













