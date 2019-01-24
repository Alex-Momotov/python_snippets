#    Methods .__iter__() and iter() both return an iterator object
L = [1,2,3]
print(L.__iter__())
print(iter(L))

#%% Unlike a list, an iterator object has a __next__() dunder method that allows us to call next() upon it.
#   Iterators are objects which remember their iteration state - the state where the iteration currently is.
L = [1,2,3]
i_L = iter(L)
print(dir(L))
print(dir(i_L))

#%% When we call next() on an iterator that run out of values, we get a StopIteration error.
L = iter([1,2,3])
next(L)
next(L)
next(L)
next(L)

#%% Under the hood the basic for loop first obtains an iterator out of the object we are iterating through and then
#   it is obtaining next() values until it hits the StopIteration exception. We can recreate a for loop as follows:
obj_to_loop = [1, 2, 3, 4]
iterator = iter(obj_to_loop)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

#%% Another property of iterators is that they only go forward, there is no going backward, resetting it or making copy.
#   All you can do is call next(). If you need to start over, you need to create iterator again from original object.

#%% Here is an example of recreating the range class in using iterators.
#   Since it is possible to call iter() on iterator objects themselves, we need to include __iter__() that simply
#   returns the instance of the object back. It doesn't really add any functionality.

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,10)
for n in nums:
    print(n)

#%% Generators are also iterators and you can create your own iterator using them.
#   An example of a range function that is created using generators is as follows.

def my_range(start, end):
    curr = start
    while curr < end:
        yield curr
        curr += 1

nums = my_range(1,10)
for i in nums:
    print(i)

#%% What is cool about iterators and generators is that you can loop forever, if you specify so.

def my_range(start):
    curr = start
    while True:
        yield curr
        curr += 1

nums = my_range(1)
for i in nums:
    print(i)

#%%

class Sentence:

    def __init__(self, string):
        s_list = string.strip().split(' ')
        self.s_list = s_list
        self.curr = 0
        self.length = len(s_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr >= self.length:
            raise StopIteration
        output = self.s_list[self.curr]
        self.curr += 1
        return output

def gen_sent(sentence):
    sentence += ' '
    curr = ''
    for char in sentence:
        if char != ' ':
            curr += char
        else:
            yield curr
            curr = ''

#%%

my_sentence = Sentence('This is test')
for word in my_sentence:
    print(word)

test_string = 'This is test'
sent_gen = gen_sent(test_string)
for word in sent_gen:
    print(word)


