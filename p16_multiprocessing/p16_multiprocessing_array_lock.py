import time
from multiprocessing import Process, Value, Array, Lock
import os


def add_100(array, lock):
    for i in range(100):
        time.sleep(0.01)
        for inx in range(len(array)):
            with lock:
                array[inx] += 1.0


if __name__ == "__main__":
    shared_array = Array("d", [0.0, 100.0, 200.0])
    print(f"Number at the beginning is {shared_array[:]}")

    lock = Lock()
    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Number at the end is {shared_array[:]}")
