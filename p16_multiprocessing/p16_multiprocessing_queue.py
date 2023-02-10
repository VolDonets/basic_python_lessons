import time
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import os


def square(numbers, q, lock):
    for i in numbers:
        q.put(i * i)


def make_negative(numbers, q, lock):
    for i in numbers:
        q.put(-1 * i)


if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    numbers = range(1, 6)

    p1 = Process(target=square, args=(numbers, q, lock))
    p2 = Process(target=make_negative, args=(numbers, q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
