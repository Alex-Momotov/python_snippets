import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} sec ...')
    time.sleep(seconds)
    print('done sleeping ...')

t1 = threading.Thread(target=do_something, args=[1])       # target = the function name to run, without parenthesis
t2 = threading.Thread(target=do_something, args=[1])       # args = list of arguments to the function

t1.start()
t2.start()

t1.join()       # If thread throws an exception, join() is where the exception will be raised in the main thread
t2.join()


print(f'script finished, took {round(time.perf_counter() - start, 3)} sec')