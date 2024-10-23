import asyncio


async def fetch_data(id_num, sleep_time):
    print(f"Coroutine {id_num} starting to fetch data")
    await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
    return {"id": id_num, "data": f"Sample data from coroutine {id_num}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for inx, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(inx, sleep_time))
            tasks.append(task)

    # After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")


asyncio.run(main())
