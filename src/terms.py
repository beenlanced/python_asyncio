import asyncio
import time

def sync_function(test_param: str) -> str:
    """Function to demonstrate synchronous operations

    Args:
        test_param (str): test parameter 

    Returns:
        str: Time delayed print of the test parameter to simulate a process that took specific amount of time
    """

    print("This is a synchronous function")

    time.sleep(0.1)

    return f"Sync Result: {test_param}"

# Also known as a COROUTINE function
async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function.")

    await asyncio.sleep(0.1)

    return f"Async Results: {test_param}"


async def main():
    # # example code showing synchronous code operation
    # sync_result = sync_function("Test")
    # print(sync_result)

    # # example code showing concurrency - i.e., awaitable code uses `await` 
    # # awaitables are objects that implement the `__await__()` method under the hood
    # # await says pause execution and yield 
    # loop = asyncio.get_running_loop()
    # future = loop.create_future() 
    # print(f"Empty Future: {future}")

    # future.set_result("Future Result: Test")
    # future_result = await future
    # print(future_result)

    # # Coroutine Example
    # # coroutines are functions defined with the `async def` keyword
    # coroutine_obj = async_function("Test")
    # print(coroutine_obj)

    # coroutine_result = await coroutine_obj
    # print(coroutine_result)

    # Tasks Example
    # tasks 
    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task
    print(task_result)


if __name__ == "__main__":
    asyncio.run(main()) # Starts the event loop - engine that runs and manages asynchronous functions
