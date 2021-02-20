import asyncio
import time


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world!')


asyncio.run(main())
print(type(main))


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(2, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


# Execute concurrently
async def main():

    task1 = asyncio.create_task(say_after(2, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    # Wait until both tasks are completed - should take 2 seconds because they are executed in parallel
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

