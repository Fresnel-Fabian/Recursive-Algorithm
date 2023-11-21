import multiprocessing as mp

# max no of process that can be run is limited by the no of processes
print("Number of processors: ", mp.cpu_count())
# Synchronous execution
# The processes are completed in the same order in which it was started.
# This is achieved by locking the main program until the respective
# processes are finished

# Asynchronous execution
# Doesn't involve locking
# The order of the results can get mixed up but usually gets done quicker

# There are 2 main objects in multiprocessing to implement parallel execution
# Pool class and Process class

# 1. Pool class
# Synchronous execution
# Pool.map() and Pool.starmap()
# Pool.apply()
# Asynchronous execution
# Pool.map_async() and Pool.starmap_async()
# Pool.apply_async()

# Count how many numbers exist between a given range in each row

import numpy as np
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
print(data[:5])


def how_many_within_range(row, minimum, maximum):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count += 1
        return count


# results = []
# for row in data:
#     results.append(how_many_within_range(row, minimum=4, maximum=8))
# print(results[:10])
# Init multiprocessing.Pool()
# pool = mp.Pool(mp.cpu_count())
#
# # pool.apply the 'how_many_within_range()'
# results = [pool.apply(how_many_within_range, args=(row, 4, 8)) for row in data]
#
# pool.close()
# print(results[:10])

# Parallel processing with Pool.apply_async()


pool = mp.Pool(mp.cpu_count())

results = []


# Step 1: Redefine, to accept `i`, the iteration number
def howmany_within_range2(i, row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)


# Step 2: Define callback function to collect the output in `results`
# def collect_result(result):
#     global results
#     results.append(result)
#
#
# # Step 3: Use loop to parallelize
# for i, row in enumerate(data):
#     pool.apply_async(howmany_within_range2, args=(i, row, 4, 8), callback=collect_result)
#
# # Step 4: Close Pool and let all the processes complete
# pool.close()
# pool.join()  # postpones the execution of next line of code until all processes in the queue are done.
#
# # Step 5: Sort results [OPTIONAL]
# results.sort(key=lambda x: x[0])
# results_final = [r for i, r in results]
#
# print(results_final[:10])

# pool = mp.Pool(mp.cpu_count())
#
# results = []
#
# # call apply_async() without callback
# result_objects = [pool.apply_async(howmany_within_range2, args=(i, row, 4, 8)) for i, row in enumerate(data)]
#
# # result_objects is a list of pool.ApplyResult objects
# results = [r.get()[1] for r in result_objects]
#
# pool.close()
# pool.join()
# print(results[:10])
print()
import pandas as pd

df = pd.DataFrame(np.random.randint(3, 10, size=[5, 2]))
print(df)
print(df.shape)


# def hypotenuse(row):
#     return round(row[1]**2 + row[2]**2, 2)**0.5
#
# with mp.Pool(4) as pool:
#     result = pool.imap(hypotenuse, df.itertuples(name=False), chunksize=10)
#     output = [round(x, 2) for x in result]
#
# print(output)

# Column wise Operation
def sum_of_squares(column):
    return sum([i**2 for i in column[1]])

with mp.Pool(2) as pool:
    result = pool.imap(sum_of_squares, df.iteritems(), chunksize=10)
    output = [x for x in result]

print(output)