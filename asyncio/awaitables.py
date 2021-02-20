import asyncio

# an object is awaitable if it can be used in an await expression

# coroutines


async def nested():
    return 42


async def main():
    # Nothing happens
    # nested()

    print(await nested())


asyncio.run(main())

# tasks - used to schedule coroutines concurrently


async def main():
    # when a coroutine is wrapped to a task, it is marked to be executed soon
    task = asyncio.create_task(nested())

    await task


asyncio.run(main())


# future - represents an eventual result of an asynchronous operation


async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)


async def main():

    loop = asyncio.get_running_loop()

    fut = loop.create_future()

    loop.create_task(set_after(fut, 1, '...world'))

    print('hello...')

    print(await fut)


asyncio.run(main())
