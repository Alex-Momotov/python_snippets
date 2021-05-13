from concurrent.futures import ThreadPoolExecutor, as_completed
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} sec ...')
    time.sleep(seconds)
    return f'done sleeping ... for {seconds}'

with ThreadPoolExecutor() as executor:
    futures = []
    for sec in [5, 4, 3, 2, 1]:
        futures.append(executor.submit(do_something, sec))

    for f in as_completed(futures):         # as_completed(futures) returns an iterator over futures as they are completed
        print(f.result())                   # futures that are completed first will be returned first - use when order of completion is not relevant

print(f'script finished, took {round(time.perf_counter() - start, 3)} sec')
