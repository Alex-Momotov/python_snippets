#   threading.current_thread() returns current thread.
#   When runninng a function from the main body of a script it will print MainThread

import threading

def my_task():
    print(f"Hello, world: {threading.current_thread()}")

my_task()

#%% threading.Thread(name='thr_name', target=func)
#   A function that creates a new thread. Name parameter is the name of the thread.
#   Target parameter is the name of the function from which the thread will be created.
#   When running function wsing created thread, threading.current_thread() will print name of the running thread.
def my_task():
    print(f"Hello, world: {threading.current_thread()}")

new_thr = threading.Thread(name='test_1', target=my_task)
new_thr.start()


#%% ThreadPoolExecutor(max_workers=3)
#   Provides an abstraction for using multiple threads in a concurrent fashion.
#   The recommendation is to use the context manager where we specify the number of workers (free CPU cores)
#   Then, using executor.submit(task) we can start a given task. They will run simultaneously.
from concurrent.futures import ThreadPoolExecutor
import threading
from time import sleep

def task1():
    for i in range(10):
        print('I am task 1')
        sleep(1.1)

def task2():
    for i in range(10):
        print('I am task 2')
        sleep(1.2)

def task3():
    for i in range(10):
        print('I am task 3')
        sleep(1.3)

with ThreadPoolExecutor(max_workers=3) as executor:
    task1 = executor.submit(task1)
    task1 = executor.submit(task2)
    task1 = executor.submit(task3)

#%%
import asyncio

async def myCoRoutine():
    print("Simple coroutine example")

loop = asyncio.get_event_loop()
loop.run_until_complete(myCoRoutine())
loop.close()

#%%
import asyncio
import random

async def myCoRoutine(id):
    process_time = random.randint(3,5)
    await asyncio.sleep(process_time)
    print(f'{id} finished after {process_time} seconds.')

async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(myCoRoutine(i)))
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

#%%
import threading

account_balance = 100
L = threading.Lock()

def withdraw(amount=10):
    global account_balance
    L.acquire()
    account_balance -= amount
    L.release()

thread_1 = threading.Thread(target=withdraw)
thread_2 = threading.Thread(target=withdraw)

print(account_balance)
thread_1.start()
thread_2.start()
print(account_balance)








