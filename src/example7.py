import asyncio
import time


async def fetch_data(param: int) -> str:
    """_summary_

    Args:
        param (int): Integer counter for fetches used as a dummy parameter

    Returns:
        str: Return simple string result
    """
    await asyncio.sleep(param)
    return f"Result of {param}"


async def main():
    # Create Tasks Manually
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    result2 = await task2
    print(f"Task 1 and 2 awaited results: {[result1, result2]}")

    # Gather Coroutines
    # passing coroutines directly gives you the results, but remember using tasks will add extra
    # functionality: like monitor and interact with tasks before completion
    coroutines = [fetch_data(i) for i in range(1, 3)] # create a list of coroutine objects via list comprehension
    results = await asyncio.gather(*coroutines, return_exceptions=True) 
    print(f"Coroutine Results: {results}")

    # Gather Tasks
    # using tasks will add extra
    # functionality: like monitor and interact with tasks before completion
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)] # create a list of task objects via list comprehension
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Task Results: {results}")

    # Task Group
    # Here we use a async context manager. 
    # async with asyncio.TaskGroup() context manager does
    #   - IO operations like tracking tasks, waiting for completions, handles cancellations, handles errors, etc.
    #   - Notice, we are not awaiting anything with the task group. It awaits all tasks created for the group during exit
    async with asyncio.TaskGroup() as tg:
        results = [tg.create_task(fetch_data(i)) for i in range(1, 3)] # create a list of task objects via list comprehension
        # All tasks are awaited when the context manager exits.
    print(f"Task Group Results: {[result.result() for result in results]}")

    return "Main Coroutine Done"

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")