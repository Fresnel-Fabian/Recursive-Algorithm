import random
import time
import concurrent.futures


def generate_point(d):
    return [random.uniform(-1, 1) for _ in range(d)]  # Generate a random point in the hypercube


def is_inside_hypersphere(point):
    return sum(x ** 2 for x in point) <= 1


def monte_carlo_hypersphere_volume_parallel(n, d, n_process):

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_process) as executor:
        points = list(executor.map(generate_point, [d] * n))
        points_inside = sum(executor.map(is_inside_hypersphere, points))

    volume_approximation = (points_inside / n) * (2 ** d)
    return volume_approximation


n = 1000000  # Total number of samplings for both experiments
d = 11  # Number of dimensions


# Time the parallel version with 10 processes
n_process = 10
n_parallel = n // n_process  # Distribute total samplings evenly
start = time.perf_counter()
volume_estimate = monte_carlo_hypersphere_volume_parallel(n_parallel, d, n_process)
end = time.perf_counter()
print(f"Parallel execution time with {n_process} processes: {round(start-end, 2)} seconds")
