"""
Unlike threading, mulitprocessing can assist in speeding up cpu bound tasks. However, multiprocessing can help speed up
both CPU and IO bound tasks. I/O bound tasks include file system and networking tasks i.e. https requests, file output/input,
and more...
"""
import time
import multiprocessing
import concurrent.futures

# calc start time
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {round(seconds, 2)} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, secs) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


# pass the actual value of the function not the return value which is denoted by ()
# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# In order to run the code use .start() to run the initialized variables p1 & p2
# p1.start()
# p2.start()

# In order to actually run the process before moving down in the script we use the join() method.
# p1.join()
# p2.join()

# Instead of entering each value manually for to loop over a range of processes
# Underscore is a throw away variable.
# nterms = int(input('Please input and integer range to loop over:'))
#
# processes = []
#
# for _ in range(nterms):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)
#
# for process in processes:
#     process.join()


# Check that you understand synchronous code call the do_something() func twice
# do_something()
# do_something()

# calc finish time
finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
