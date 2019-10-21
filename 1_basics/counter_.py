from collections import Counter

#%% Create new empty counter
c = Counter()
print(c)

#%% Create new counter, counting characters in a string
c = Counter('this is a test string')
print(c)

#%% Create new counter from a mapping
c = Counter({'red': 4, 'blue': 2})
print(c)

#%% Create new counter from keyword args
c = Counter(cats=4, dogs=3)
print(c)

#%% Create new counter from a list of items. Items can be anything hashable.
c = Counter(['a','a','b','b','b','c'])
print(c)

#%% Index counter using keywords, just like dictionary
#   Indexing with non-existant keys returns 0 instead of raising error
c = Counter(['a','a','b','b','b','c'])
print(c['b'])
print(c['something'])

#%% Can add keys to counter manually like this
c = Counter()
c['something'] = 4
print(c)

#%% Delete entry from counter with 'del'
c = Counter(['nothing'])
print(c)
del c['nothing']
print(c)

#%% c.elements()
#   Return an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary order.
#   If an element’s count is less than one, elements() will ignore it.
c = Counter(cat=4, dog=2)
print(c.elements())
L = list(c.elements())
print(L)

#%% c.most_common()
#   Return a list of the n most common elements and their counts from the most common to the least. If n is omitted
#   or None, most_common() returns all elements in the counter.
c = Counter('abracadabra')
print(c.most_common(3))
print(c.most_common())

#%% c.most_common()[:-n-1:-1]
#   Return n least common elements
c = Counter([1,1,1,1,2,2,2,3,4,4,4,5,5,5,6,6,7,8,9,11,12,13,14,15])
print(c.most_common()[:-3-1:-1])


#%% c.subtract(iterable-or-mapping)
#   Subtracts elements in an iterable (e.g. list) or another mapping or another counter from the current counter.
#   Both inputs and outputs may be zero or negative.
c = Counter(a=3, b=3, c=3)
print(c)
sub = ['a', 'b', 'b', 'c']
c.subtract(sub)
print(c)

#%% c.update(iterable-or-mapping)
#   Elements are added in to the current counter entries from an iterable (e.g. list) or mapping or another counter.
c = Counter(a=3, b=3, c=3)
print(c)
c.update(['a','a',25])
print(c)
c.update({'a':12, 's':1})
print(c)

#%% Common patterns when working with counters:
c = Counter(a=3, b=3, c=3, d=-1)
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
+c                              # return copy of counter with only zero and negative counts

#%% Counter is a subclass from dictionary and supports all dictionary methods (except .fromkeys())
c = Counter(a=3, b=3, c=3, d=-1)
print(c.keys())
print(c.values())


