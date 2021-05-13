import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} sec ...')
    time.sleep(seconds)
    raise RuntimeError
    return f'done sleeping ... for {seconds}'

with ThreadPoolExecutor() as executor:          # its good practice to use context manager with thread pool (executor) so we don't forget to close it
    f_1 = executor.submit(do_something, 2)      # name of function (do_something) is followed by unpacked list of arguments for that function
    f_2 = executor.submit(do_something, 1)

    res_1 = f_1.result()    # get result of the future - blocking operation
    res_2 = f_2.result()    # If thread throws an exception, result() is where the exception will be raised in the main thread

    print(res_1)
    print(res_2)





print(f'script finished, took {round(time.perf_counter() - start, 3)} sec')
