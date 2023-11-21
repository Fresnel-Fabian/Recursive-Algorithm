#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt


def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n - 1) + fib_py(n - 2)


@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n - 1) + fib_numba(n - 2)


def main():
    f = Person(5)
    print(f.get())
    f.set(7)
    print(f.get())
    print("-"*20)

    # fib method in py, numba, cpp with n values from 30-45
    # n_ = []
    # fib_py_time = []
    # fib_numba_time = []
    # fib_cpp_time = []
    #
    # for n in range(30, 46):
    #     n_.append(n)
    #
    #     start = pc()
    #     print(fib_py(n))
    #     end = pc()
    #     fib_py_time.append(round(end-start, 2))
    #
    #     start = pc()
    #     print(fib_numba(n))
    #     end = pc()
    #     fib_numba_time.append(round(end-start, 2))
    #
    #     start = pc()
    #     f = Person(n)
    #     print(f.fib())
    #     end = pc()
    #     fib_cpp_time.append(round(end-start, 2))
    # print(n_)
    # print(fib_py_time)
    # print(fib_numba_time)
    # print(fib_cpp_time)
    # # plot of time
    # plt.plot(n_, fib_py_time, label="fib_py")
    # plt.plot(n_, fib_numba_time, label="fib_numba")
    # plt.plot(n_, fib_cpp_time, label="fib_cpp")
    # plt.xlabel("n")
    # plt.ylabel("Time (seconds)")
    # plt.legend()
    # plt.savefig("fib(py&numba&cpp, 30-45).png")
    # # plt.show()
    #
    # # fib method in py and numba with n values from 20-30
    # n_ = []
    # fib_py_time = []
    # fib_numba_time = []
    # for n in range(20, 30):
    #     n_.append(n)
    #
    #     start = pc()
    #     print(fib_py(n))
    #     end = pc()
    #     fib_py_time.append(round(end-start, 2))
    #
    #     start = pc()
    #     print(fib_numba(n))
    #     end = pc()
    #     fib_numba_time.append(round(end-start, 2))
    #
    # # Plotting
    # plt.plot(n_, fib_py_time, label="fib_py")
    # plt.plot(n_, fib_numba_time, label="fib_numba")
    # plt.xlabel("n")
    # plt.ylabel("Time (seconds)")
    # plt.legend()
    # plt.savefig("fib(py&numba, 20-30).png")
    # # plt.show()

    # fib method in numba and cpp with n value 47
    n = 47
    start = pc()
    print(fib_numba(n))
    end = pc()
    print(f"fib_numba execution time for n=47: {round(end-start, 2)}")

    start = pc()
    f = Person(n)
    print(f.fib())
    end = pc()
    print(f"fib_cpp execution time for n=47: {round(end-start, 2)}")

if __name__ == '__main__':
    main()
