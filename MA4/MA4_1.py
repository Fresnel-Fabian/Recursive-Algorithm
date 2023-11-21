import functools
import math
import random
import matplotlib.pyplot as plt
import concurrent.futures as future
from time import perf_counter as pc


def estimate_pi(n):
    nc = 0
    x_circle, y_circle = [], []
    x_square, y_square = [], []

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            nc += 1
            x_circle.append(x)
            y_circle.append(y)
        else:
            x_square.append(x)
            y_square.append(y)
    pi_estimate = (nc / n) * 4
    print(f"Number of points inside the circle: {nc}")
    print(f"Approximation of pi: {pi_estimate}")
    print(f"Pi: {math.pi}")
    plt.figure(figsize=(6, 6))
    plt.scatter(x_circle, y_circle, color='blue', s=2)
    plt.scatter(x_square, y_square, color="red", s=2)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title(f"Monte Carlo estimation of {n}: {pi_estimate:.5f}")
    # Save the plot as a PNG file
    # plt.savefig(f"monte_carlo_pi_estimate: {n}.png", dpi=300)
    # plt.show()


def monte_carlo_hypersphere_volume(n, d):
    # List Comprehension
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    # Check if a point is inside the hypersphere (x1**2+x2**2.....xd**2 <= 1)
    # filter function
    points_inside = filter(lambda point: sum(x ** 2 for x in point) <= 1, points)
    # reduce
    points_inside_count = functools.reduce(lambda x, _: x + 1, points_inside, 0)
    volume_approximation = (points_inside_count / n) * 2 ** d
    # v = (math.pi ** d/2) / math.gamma((d/2)+1)
    # print(v)
    return volume_approximation


# Generate a random point in the hypercube
def generate_point(d):
    return [random.uniform(-1, 1) for _ in range(d)]


# Check if the point is inside the hypersphere
def is_inside_hypersphere(point):
    return sum(x ** 2 for x in point) <= 1


def monte_carlo_hypersphere_volume_parallel(n, d, n_process):
    with future.ProcessPoolExecutor(max_workers=n_process) as executor:
        points = list(executor.map(generate_point, [d] * n))
        points_inside = sum(executor.map(is_inside_hypersphere, points))

    volume_approximation = (points_inside / n) * (2 ** d)
    return volume_approximation


def main():
    print("MA4 1.1")
    print("-" * 10)
    ns = [1000, 10000, 100000]
    for n in ns:
        estimate_pi(n)
        print("-----------------------------------------")
    print()

    print("MA4 1.2")
    print("-" * 15)
    v = monte_carlo_hypersphere_volume(100000, 2)
    print("Volume of Hypersphere using Monte Carlo Algorithm")
    print(f"dimension: 2 \npoints: 100000 \nvolume: {v}")
    print("-" * 15)
    v = monte_carlo_hypersphere_volume(100000, 11)
    print(f"dimension: 11 \npoints: 100000 \nvolume: {v}")
    print("-" * 15)
    print()

    print("MA$ 1.3")
    print("-" * 10)
    n = 1000000
    d = 11
    start = pc()
    print(monte_carlo_hypersphere_volume(n, d))
    end = pc()
    print(f"Time taken by Non-parallel execution: {round(end - start, 2)} seconds")
    print("-" * 20)

    n_process = 10
    n_parallel = n // n_process
    start = pc()
    print(monte_carlo_hypersphere_volume_parallel(n_parallel, d, n_process))
    end = pc()
    print(f"Time taken by parallel execution with 10 processes: {round(end - start, 2)} seconds")


if __name__ == "__main__":
    main()
