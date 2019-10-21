#%% Closure.

def outer(msg):
    def inner():
        return(msg)
    return inner

hi_func = outer('hi')
bye_func = outer('bye')

print(hi_func())
print(bye_func())

#%% This decorator function prints out elapsed time of its inner function and the name of the function
#   that it was used to decorate. This might be useful for timing/logging purposes

def timer(func):
    from time import time
    def inner(*args, **kwargs):
        t_before = time()
        result = func(*args, *kwargs)
        t_after = time()
        t_elapsed = round(t_after-t_before, 2)
        print(f'\"{func.__name__}\" finished, took: {t_elapsed} sec')
        return result
    return inner


#%% This decorator function prints out memory consumed by the function that it decorates, as well as the final
#   memory usage.

def memory(func):
    from memory_profiler import memory_usage
    def inner(*args, **kwargs):
        mem_before = memory_usage()[0]
        result = func(*args, **kwargs)
        mem_after = memory_usage()[0]
        m_consumed = round(mem_after - mem_before, 2)
        print(f'\"{func.__name__}\" finished, consumed: {m_consumed} Mb')
        print(f'current memory: {memory_usage()[0]} Mb')
        return result
    return inner

#%% This decorator function prints out both time taken and memory consumed by the function that it decorates.

def memory_time(func):
    from memory_profiler import memory_usage
    from time import time
    def inner(*args, **kwargs):
        t_before = time()
        mem_before = memory_usage()[0]
        result = func(*args, *kwargs)
        t_after = time()
        mem_after = memory_usage()[0]
        t_elapsed = round(t_after - t_before, 2)
        m_consumed = round(mem_after - mem_before, 2)
        print(f'\"{func.__name__}\" finished, took: {t_elapsed} sec, consumed: {m_consumed} Mb')
        print(f'\tcurrent memory: {memory_usage()[0]} Mb')
        return result
    return inner

#%% This is a test case which we know will consume around 270Mb of memory and take 1.71 sec.
#   Try decorating it with different functions above.
import random
import time
names = ['John', 'Alisa', 'Stephen', 'Priya', 'Michael', 'Eddie']
majors = ['Maths', 'CompSci', 'Physics', 'Biology', 'Chemistry', 'History']

@memory_time
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

people = people_list(1000000)



