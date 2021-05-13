import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'sleeping {seconds} sec ...')
    time.sleep(seconds)
    print('done sleeping ...')


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)

for t in threads:
    t.join()


print(f'script finished, took {round(time.perf_counter() - start, 3)} sec')