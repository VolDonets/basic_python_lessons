import time
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Pool
import os


def cube(number):
    return number * number * number


if __name__ == "__main__":
    pool = Pool()
    numbers = range(10)

    # map, apply, join, close
    result = pool.map(cube, numbers)

    # apply function to one element
    # result = pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)
