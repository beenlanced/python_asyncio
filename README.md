- `Asyncio` -
- `Coroutine` - special Python function that enables asynchronous programming
- `CPU-bound processes`, processes
- `IO-bound processes`,
- `Python`

#### Synchronous Function

Start to finish no interuptions like a complete block of time

#### Asynchronous Function

A coroutine in Python is a special type of function that can pause its execution and allow other functions to run, enabling asynchronous programming. They are defined using the **async def** syntax and can be executed using the **await** keyword, making them useful for tasks that involve waiting for input/output (I/O) operations like network access or database queries (e.g., process your programming is waiting on that is external) without blocking the entire program.

**Coroutine vs Threads**

Now you might be thinking how coroutine is different from threads, both seem to do the same job.
In the case of threads, it’s an operating system (or run time environment) that switches between threads according to the scheduler. While in the case of a coroutine, it’s the programmer and programming language which decides when to switch coroutines. Coroutines work cooperatively multitask by suspending and resuming at set points by the programmer. The idea is that coroutines voluntarily give up control. You can pause them.

For CPU intensive computations, we would use processes instead of coroutines or asynchronous processes.

`asyncio` is single threaded and runs on a single process that excels at I/O based tasks. You can do other actions while waiting for and I/O task to complete.

`asyncio.run` is the engine that runs and manages asynchronous. It functions like a scheduler. It keeps track of all the tasks. when a tasks is suspended because it is waiting for something else. Control returns to the event loop which then finds another task to start or resume. So, we have to be running an event loop for any of the synchronous code to work.

Three kinds of `awatiable objects` in Python:

- Coroutines - created when you call a function with the **async def** keyword.

  - coroutine objects (e.g. coroutine_obj = async_function()) are the **awaitables** that get returned whe you call that coroutine functions.
    - Syntax `await coroutine_obj`

- Futures - low-level objects representing eventual results. A future's job is to hold a certain state and result.

- Tasks - wrappers around coroutines that are scheduled on the event loop that can be executed independently

  - task are how we actually rung coroutines concurrently.
  - when you wrap a coroutine in a task (e.g., `task = asyncio.create_task(async_function("Test"))`) it's handed over to the event loop and scheduled to run whenever it gets a chance. The task keeps track of the whether the coroutine finished successfully, raised an exception, or got cancelled just like a **future** would. In fact, **tasks** are **futures** under the hood, but with no extra logic to run the coroutine and to do the work of the function. That is why **tasks** are generally used in preference over **futures**.
  - You can queue up multiple tasks at once and the event loop will be able to run them whenever it's ready. Let's tasks take turns whil waiting on IO.
  -

-

#### Python Script descriptions

- **terms.py**

  Python scripts to highlight asyncio terminology in action. Simply uncomment and comment out pieces of code to show results.

- **example1.py**

  Python script that does not use asyncio at all. It is all synchronous code. No event loops at all. Notice here that there is a few seconds where we are waiting for the synchronous functions to complete. Asyncio would allow us to take run other processes during this down time.

- **example2.py**

  Python Script that is a first attempt at converting the synchronous code to asynchonous. I introduce the **asyncio** library. There is a mistake in this script. I call task1 and task2 like I am calling functions as in the synchronous case. It runs in the same amount of time as example1.py's synchronous code -- still not getting concurrency benefits here. Why? Answer: The code is written such that one might suspect that calling the **coroutine** function `fetch_data()` creates a taske and a schedule. Well, it does not. Code like

  ```bash
  task1 = fetch_data(1)
  ```

  just creates coroutine objects! So, when task1, a coroutine object, is awaited (ala `await task1`) the object is getting **scheduled** and **ran to completion** at the same time. As a result, we get no concurrency and no benefit of using **asyncio**. Just having asyncio is not a guarantee of concurrency.

- **example3.py**

  Python Script to show one way of correctly using asyncio to gain concurrency by using `tasks`. The key points in this script are using:

  ```bash
  task1 = asyncio.create_task(fetch_data(1))
  task2 = asyncio.create_task(fetch_data(2))
  ```

  `asyncio.create_task()` creates tasks from the coroutine: `async def fetch_data(param)`. Creating tasks **schedule** a coroutine to run on the event loop, which was the key part missing example2.py.

Stop 9:30
https://www.youtube.com/watch?v=oAkLSJNr5zY
