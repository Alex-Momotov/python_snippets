#%% Generators are functions which return generator objects.
#   Below, the normal squaring function 'list_func' returns a list.
#   But the equivalent generator function 'gen_func' returns a generator object.
#   This is because generators never hold the entire result in memory.
#   Generators yield one result at a time and wait for the programmer to ask for its next result.
#   At the time you created a generator object with 'res = gen_func(nums)' the generator hasn't actually,
#   computed anything yet. This is because it's waiting for you to ask for its next result.

def list_func(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


nums = [1, 2, 3, 4, 5, 6, 7]
res = list_func(nums)
print('normal function:', res)

def gen_func(nums):
    for i in nums:
        yield i*i


nums = [1, 2, 3, 4, 5, 6, 7]
gen = gen_func(nums)                # Create generator object, at this stage it didn't compute anything yet.
print('generator function:', gen)
nums = [x for x in gen_func(nums)]

#%% A common way of using generators is iterating through generator objects using 'for' loop.
def gen_func(nums):
    for i in nums:
        yield i*i


nums = [1, 2, 3, 4, 5, 6, 7]
gen = gen_func(nums)
for i in gen:
    print(i)


#%% next(generator_obj)
#   Returns the next computation from generator (i.e. from yield).
#   Each time we call next() it goes and gets the next value that's yielded.
#   When we call a next() on a generator that ran out of values, we get StopIteration error.
def gen_func(nums):
    for i in nums:
        yield i*i


nums = [1, 2, 3]
gen = gen_func(nums)    # Create generator object, at this stage it didn't compute anything yet.
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))      # Uncomment this out to see StopIteration error.

#%% Generators won't go infinitely by default.
#   Generators can have multiple 'yield' statements, each next() or iteration of 'for' loop
#   will just go to the next 'yield' statement. In fact this is the only way generators return values. This is because
#   if we put 'for' loop inside generator to yield us values, then, what really happens is that the generator has
#   multiple 'yield' statements, duplicated by the 'for loop'.
#   Therefore, generators can be used to enforce a strict execution sequence.
def gen_func():
    yield 1
    yield 0
    yield 2
    yield 999

gen = gen_func()
for x in gen:
    print(x)

#%% Another example.
def gen_func():
    yield 1
    yield 0
    yield 2
    yield 999

gen = gen_func()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#%% Another example.
#   Here we advance generator by 1 value with next() before iterating through the rest of values with the 'for' loop.
#   Notice that the first value "1" was not printed, because we skipped it with next().
def gen_func(nums):
    for i in nums:
        yield i


nums = [1, 2, 3, 4, 5, 6, 7]
gen = gen_func(nums)    # Create generator object, at this stage it didn't compute anything yet.
next(gen)               # Comment this out to see that generator will skip the first value in the 'for' loop.
for i in gen:
    print(i)

#%% Generator expressions.
#   Generator expressions have similar syntax to list comprehensions.
#   As we can see, generator expressions return generator objects. We still need to iterate through those objects.
gen = (x**2 for x in range(10))     # Generator expression.
lis = [x**2 for x in range(10)]     # List comprehension.
print(gen)
print(lis)

#%% In this example, we make generator object using generator expression, then iterate through it.
gen = (x**2 for x in range(10))     # Generator expression.
lis = [x**2 for x in range(10)]     # List comprehension.
for x in lis: print(x, end=' ')
print()
for x in gen: print(x, end=' ')

#%% Neat illustration using sleep module.
from time import sleep

def gen_func():
    for i in range(8):
        sleep(0.3)
        yield i

def func():
    L = []
    for i in range(8):
        sleep(0.3)
        L.append(i)
    return L

gen = gen_func()
for x in gen: print(x, end=' ')
print()

lis = func()
for x in func(): print(x, end=' ')

#%% Let's illustrate how generators are more memory efficient.
#   Un-comment one block at a time to see performance diffenrence.
#   Don't forget to reset console each time to clear memory.

#   IN SUMMARY:
#   1) Creating huge list takes a lot of time and a lot of memory.
#   2) Creating huge generator object takes 0 time and 0 memory.
#   3) Iterating through huge generator takes a lot of time (same as list) but 0 memory!
import memory_profiler
import random
import time

names = ['John', 'Alisa', 'Stephen', 'Priya', 'Michael', 'Eddie']
majors = ['Maths', 'CompSci', 'Physics', 'Biology', 'Chemistry', 'History']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

# HERE, CREATING LIST TOOK 270 Mb OF MEMORY AND 1.75 SECONDS.
# print(f'Memory (before) {round(memory_profiler.memory_usage()[0],2)} Mb')
# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()
# print(f'Memory (after) {round(memory_profiler.memory_usage()[0],2)} Mb')
# print(f'Took {round(t2-t1, 2)} sec')

# HERE, CREATING GENERATOR OBJECT TOOK 0.00 SECONDS AND 0.00 Mb OF MEMORY.
# print(f'Memory (before) {round(memory_profiler.memory_usage()[0],2)} Mb')
# t1 = time.clock()
# people = people_generator(1000000)
# t2 = time.clock()
# print(f'Memory (after) {round(memory_profiler.memory_usage()[0],2)} Mb')
# print(f'Took {round(t2-t1, 2)} sec')

# HERE, CREATING AND ITERATING THROUGH THE GENERATOR TOOK 1.72 SEC (SAME AS LIST) BUT 0.0Mb OF MEMORY.
print(f'Memory (before) {round(memory_profiler.memory_usage()[0],2)} Mb')
t1 = time.clock()
people = people_generator(1000000)
var = None
for x in people: var = x
t2 = time.clock()
print(f'Memory (after) {round(memory_profiler.memory_usage()[0],2)} Mb')
print(f'Took {round(t2-t1, 2)} sec')

#%%

