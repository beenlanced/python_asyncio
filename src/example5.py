import asyncio
import time


async def fetch_data(param: int) -> str:
    """_summary_

    Args:
        param (int): Integer counter for fetches used as a dummy parameter

    Returns:
        str: Return simple string result
    """
    print(f"Do something with {param}...")
    time.sleep(param) #---- this is the synchronous event
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")