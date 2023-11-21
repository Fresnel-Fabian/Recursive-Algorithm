from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp
import concurrent.futures as future


# def runner():
#     print("Performing a costly function")
#     pause(1)
#     print("Function complete")
def runner(n):
    print(f"Performing costly function {n}")
    pause(n)
    return f"Function {n} has completed"


if __name__ == "__main__":
    # multiprocessing using multiprocessing module
    # start = pc()
    # processes = []
    # for _ in range(10):
    #     p = mp.Process(target=runner)
    #     processes.append(p)
    # for p in processes:
    #     p.start()
    # for p in processes:
    #     p.join()
    # end = pc()
    # print(f"Process took {round(end-start, 2)} seconds")

    # multiprocessing using concurrent.futures

    # with future.ProcessPoolExecutor() as ex:
    #     p1 = ex.submit(runner)
    #     p2 = ex.submit(runner)
    #     r1 = p1.result()
    #     r2 = p2.result()

    start = pc()
    with future.ProcessPoolExecutor() as ex:
        p = [5, 4, 3, 2, 1]
        results = ex.map(runner, p)

        for r in results:
            print(r)
    end = pc()
    print(f"Process took {round(end - start, 2)} seconds")

    # Multithreading
    start = pc()
    with future.ThreadPoolExecutor() as ex:
        p = [5, 4, 3, 2, 1]
        results = ex.map(runner, p)
        for r in results:
            print(r)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
