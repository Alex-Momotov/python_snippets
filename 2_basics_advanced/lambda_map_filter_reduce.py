#%% Lambda expressions.
#   They return function objects.
func = lambda x : x**2
print(func(5))
print(func)

#%%
nums = [1,2,3,4,5,6,7,8,9]
func = lambda x: x > 5
print([x for x in nums if func(x)])

#%%
func = lambda x, y: x/y
print(func(10, 3))

#%%
max_func = lambda x,y: x if x > y else y
print(max_func(5,10))

#%% map(function, sequence)
#   map() filter() and reduce() now all return iterables. If you really need a list, use list() around them.
#   We could use map(lambda_expression, sequence) but this type of work is done
#   much easier with comprehensions.py. Instead we want to use map() when the function
#   that we are mapping is very big (takes many lines) and it would be troublesome
#   to write that function as a comprehension.
def STD(args):
    """This function returns standard deviation"""
    sum1 = sum(args)
    mean = sum1/len(args)
    zero_cent = [num - mean for num in args]
    squares = [x**2 for x in zero_cent]
    sum2 =sum(squares)/len(args)
    return round(sum2**0.5, 4)


L = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
result = list(map(STD, L))
print(result)

#%% filter(condition, sequence)
#   map() filter() and reduce() now all return iterables. If you really need a list, use list() around them.
#   Filter returns only the elements of the specified sequence for which the condition function evaluated True.
#   This would be useful only when the function which calculates boolean condition is very long (many lines).
#   If the condition function is short it would be better to use a comprehension.
nums = [4,3,2,1]
func = lambda x: x > 2
print(list(filter(func, nums)))

#%% functools.reduce(comulative_function, sequence)
#   map() filter() and reduce() now all return iterables. If you really need a list, use list() around them.
#   reduce() was removed from standard library and was put into functools.reduce()
#   This is because 99% of the time it is better to use for loops which is more readable.
import functools
nums = [1,2,3,4,5,6,7]
func = lambda x, y: x * y
print(functools.reduce(func, nums))
