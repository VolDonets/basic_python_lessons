import time
import asyncio


def brew_coffee():
    print("Start Brewing Coffee")
    time.sleep(3)
    print("Stop Brewing Coffee")
    return "Coffee ready"


def toast_bagel():
    print("Start Toast Bagel")
    time.sleep(2)
    print("Stop Toast Bagel")
    return "Bagel toasted"


# this is coroutine function which returns a coroutine object
async def async_brew_coffee():
    print("Start Brewing Coffee")
    await asyncio.sleep(3)
    print("Stop Brewing Coffee")
    return "Coffee ready"


async def async_toast_bagel():
    print("Start Toast Bagel")
    await asyncio.sleep(2)
    print("Stop Toast Bagel")
    return "Bagel toasted"


def sync_test():
    start = time.time()

    result_coffee = brew_coffee()
    result_toast = toast_bagel()

    end = time.time()
    elapsed_time = end - start

    print(f"Result of Brewing Coffee is {result_coffee}")
    print(f"Result of Toast Bagel is {result_toast}")
    print(f"Elapsed Time is {elapsed_time:.2f} seconds\n\n")


async def async_test():
    start = time.time()

    batch = asyncio.gather(async_brew_coffee(), async_toast_bagel())
    result_coffee, result_toast = await batch

    end = time.time()
    elapsed_time = end - start

    print(f"Result of Brewing Coffee is {result_coffee}")
    print(f"Result of Toast Bagel is {result_toast}")
    print(f"Elapsed Time is {elapsed_time:.2f} seconds\n\n")


async def async_test_v2():
    start = time.time()

    coffee_task = asyncio.create_task(async_brew_coffee())
    toast_task = asyncio.create_task(async_toast_bagel())

    result_coffee = await coffee_task
    result_toast = await toast_task

    end = time.time()
    elapsed_time = end - start

    print(f"Result of Brewing Coffee is {result_coffee}")
    print(f"Result of Toast Bagel is {result_toast}")
    print(f"Elapsed Time is {elapsed_time:.2f} seconds\n\n")


if __name__ == "__main__":
    print("*> Sync Test")
    sync_test()

    print("*> Async Test")
    asyncio.run(async_test())

    print("*> Async Test V2")
    asyncio.run(async_test_v2())
