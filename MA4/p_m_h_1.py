import random
import time
import concurrent.futures


def is_inside_hypersphere(point):
    return sum(x ** 2 for x in point) <= 1


def monte_carlo_hypersphere_volume_parallel(n, d, num_processes):
    points_inside = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        for _ in range(n):
            point = [random.uniform(-1, 1) for _ in range(d)]
            points_inside += executor.submit(is_inside_hypersphere, point).result()

    volume_approximation = (points_inside / n) * (2 ** d)
    return volume_approximation


n = 1000000  # Total number of samplings for both experiments
d = 11  # Number of dimensions

# Time the parallel version with 10 processes
num_processes = 10
n_parallel = n // num_processes  # Distribute total samplings evenly
start_time = time.perf_counter()
volume_estimate = monte_carlo_hypersphere_volume_parallel(n_parallel, d, num_processes)
end_time = time.perf_counter()
print(f"Parallel execution time with {num_processes} processes: {end_time - start_time:.2f} seconds")
