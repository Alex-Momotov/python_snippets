def memory_time(func):
    """Intended as decorator function. Displays time taken
    and memory consumed by the function that it decorates"""
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


def memory(func):
    """Intended as decorator function. Displays memory
    consumed by the function that it decorates"""
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


def timer(func):
    """Intended as decorator function. Displays time
        taken by the function that it decorates"""
    from time import time
    def inner(*args, **kwargs):
        t_before = time()
        result = func(*args, *kwargs)
        t_after = time()
        t_elapsed = round(t_after-t_before, 2)
        print(f'\"{func.__name__}\" finished, took: {t_elapsed} sec')
        return result
    return inner