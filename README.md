# Python AsyncIO - How to Write Asynchronous Python Code

<div align="center">
    <img alt="ASYNCIO image" src="./imgs/asyncio.jpeg" width="50%" height="200">
</div>

[img source: Python's asynci: Hands-On Walkthrough](https://realpython.com/async-io-python/)
<br>

---

## Project Description

This is guide to understanding AsyncIO in Python. It describes how to write asynchonous code using the async/await syntax and explores how AsyncIO works using coroutines, tasks, and event loops. The project includes scripts that convert existing synchronous code to asynchronous code using AsyncIO as well as other standard asynchronous Python Libraries. It involves a discussiong of how to determine IObound and CPUbound process so that you can know where to apply asynchronous code and where to apply process related code to speed up code execution.

The project is heavily based on the on-line tutorial given by [Cory Schaffer: Python Tutorial: AsyncIO - Complete Guide to Asynchronous Programming with Animations](https://www.youtube.com/watch?v=oAkLSJNr5zY).

---

## Objective

The project uses the well-known `source (SRC)` layout structure. It contains the key elements:

- `Asyncio` library enables you to write concurrent code using the async and await keywords,
- `Coroutine` , special Python function that enables asynchronous programming,
- `CPU-bound processes`, processes whose execution speed is primarily limited by the speed of the central processing unit (CPU) rather than any other system resources, such as memory or input/output (I/O) operations,
- `HTTPX` the fully featured HTTP client for Python 3, which provides sync and async APIs,
- `IO-bound processes` computing task that primarily spends its time waiting for input/output (I/O) operations to complete,
- `Pillow`, the de facto image processing package for Python,
- `Python` script coding language
- `requests` Python module that simplifies the process of making HTTP requests in Python,
- `ruff` , Python linter and formatter to help check asyncio errors
- `Scalene` a high-performance CPU, GPU and memory profiler for Python,
- `Semaphore` control access to a shared resource by limiting the number of concurrent tasks that can access it
- `uv` package management including use of `ruff` for linting and formatting.

---

## Tech Stack

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?logo=html5&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

---

## Getting Started

Here are some instructions to help you set up this project locally.

---

## Installation Steps

### Installation from Github with UV (recommended)

Here are the steps to install and set up a Github repository as a package/project directly from a `GitHub` repository using `uv`:

1. **Install uv**

   - If you haven't already, install uv. Several installation methods are available, including using a standalone installer or installing from PyPI with pipx or pip.

     - Using the standalone installer (example for macOS/Linux)

       ` curl -fsSL https://astral.sh/uv/install.sh | s`

   - Install from GitHub: Use `uv pip install` with the GitHub repository URL. The format is.

     `uv pip install git+https://github.com//<repo>.git`

   - To install a specific branch, tag, or commit, add `@<reference>` to the URL.

`uv pip install git+https://github.com/beenlanced/python_asyncio.git@<branch_name>`

- Editable installs: For local development where you want changes in the repository to be immediately reflected, use the `-e` flag.

`uv pip install -e git+https://github.com/beenlanced/python_asyncio.git`

2. **Install Dependencies- with `uv` it is already done for you**

   - All dependencies should be specified in the **pyproject.toml** file, so you should not have to add any additional dependencies.
   - To update your projects virtual environment simply run  
      `uv pip sync`
     This will also activate your virtual environment (e.g., .venv folder) without requiring manual activation of the environment on your part with all the required packages as specified in the **pyproject.toml** file.

3. **Run the Source Code Scripts**

Have a look at the various directories, modules, and other files for examples of how to perform asynchronous ooperations.

- Start the project by running the appropriate command at the root directory
  ```
  uv run src/<script_file_name>.py
  ```

4. **Special Instructions**

I have added the `ruff` linter and code formatter to help assist in discovering possible asyncio issues.

To add `ruff` for development perposes using `uv` simply type the following

```bash
uv add --dev ruff
```

Then to run a check of all of the code

```bash
uv run ruff check
```

## Additional Information and Background Material

### Synchronous Function

Start to finish no interuptions like a complete block of time

### Asynchronous Function

A coroutine in Python is a special type of function that can pause its execution and allow other functions to run, enabling asynchronous programming. They are defined using the **async def** syntax and can be executed using the **await** keyword, making them useful for tasks that involve waiting for input/output (I/O) operations like network access or database queries (e.g., process your programming is waiting on that is external) without blocking the entire program.

**Coroutine vs Threads**

Now you might be thinking how is a coroutine is different from threads, both seem to do the same job.
In the case of threads, it’s an operating system (or run time environment) that switches between threads according to the scheduler. While in the case of a coroutine, it’s the programmer and programming language which decides when to switch coroutines. Coroutines work cooperatively multitask by suspending and resuming at set points by the programmer. The idea is that coroutines voluntarily give up control. You can pause them.

For CPU intensive computations, we would use processes instead of coroutines or asynchronous processes.

`asyncio` is single threaded and runs on a single process that excels at I/O based tasks. You can do other actions while waiting for an I/O task to complete.

`asyncio.run` is the engine that runs and manages asynchronous. It functions like a scheduler. It keeps track of all the tasks. when a tasks is suspended because it is waiting for something else. Control returns to the event loop which then finds another task to start or resume. So, we have to be running an event loop for any of the synchronous code to work.

Three kinds of `awaitable objects` in Python:

- Coroutines - created when you call a function with the **async def** keyword.

  - coroutine objects (e.g., coroutine_obj = async_function()) are the **awaitables** that get returned when you call that coroutine functions.
    - Syntax `await coroutine_obj`

- Futures - low-level objects representing eventual results. A future's job is to hold a certain state and result.

- Tasks - wrappers around coroutines that are scheduled on the event loop that can be executed independently.

  - **tasks** are how we actually run coroutines concurrently.
  - when you wrap a coroutine in a task (e.g., `task = asyncio.create_task(async_function("Test"))`) it's handed over to the event loop and scheduled to run whenever it gets a chance. The task keeps track of whether the coroutine finished successfully, raised an exception, or got cancelled just like a **future** would. In fact, **tasks** are **futures** under the hood, but with no extra logic to run the coroutine and to do the work of the function, that is why **tasks** are generally used in preference over **futures**.

  - You can queue up multiple tasks at once and the event loop will be able to run them whenever it's ready.

### Python Script Descriptions

- **terms.py**

  Python scripts to highlight asyncio terminology in action. Simply uncomment and comment out pieces of code to show results.

- **example1.py**

  Python script that does not use asyncio at all. It is all synchronous code. No event loops at all. Notice here that there is a few seconds where we are waiting for the synchronous functions to complete. Asyncio would allow us to take run other processes during this down time.

- **example2.py**

  Python Script that is a first attempt at converting the synchronous code to asynchonous. I introduce the **asyncio** library. There is a mistake in this script. I call task1 and task2 like I am calling functions as in the synchronous case. It runs in the same amount of time as example1.py's synchronous code -- still not getting concurrency benefits here. Why? Answer: The code is written such that one might suspect that calling the **coroutine** function `fetch_data()` creates a task and a schedule. Well, it does not.

  ```bash
  task1 = fetch_data(1)
  ```

  just creates coroutine objects! So, when task1, a coroutine object, is awaited (ala `await task1`) the object is getting **scheduled** and **runs to completion** at the same time. As a result, we get no concurrency and no benefit of using **asyncio**. Just having asyncio is not a guarantee of concurrency.

- **example3.py**

  Python Script to show one way of correctly using asyncio to gain concurrency by using `tasks`. The key points in this script are using:

  ```bash
  task1 = asyncio.create_task(fetch_data(1))
  task2 = asyncio.create_task(fetch_data(2))
  ```

  `asyncio.create_task()` creates tasks from the coroutine: `async def fetch_data(param)`. Creating tasks **schedules** a coroutine to run on the event loop, which was the key part missing in example2.py.

- **example4.py**

  Python Script to show one way of correctly using asyncio to gain concurrency by using `tasks` from example3.py. Except, some key changes were made to the code:

  ```bash
  result2 = await task2 #<---- Here
    print("Task 2 fully completed")
    result1 = await task1 #<---- Here
    print("Task 1 fully completed")
  ```

  `asyncio.create_task()` creates tasks from the coroutine: `async def fetch_data(param)`. Creating tasks **schedules** a coroutine to run on the event loop, which was the key part missing example2.py.

  The differences between example4 and example3 are to show how events occur on the event loop. We await task2 first then task1 in example4.

  Notice the `await` runs whatever is ready, so the results of 4 are very similar to example 3.

- **example5.py**

  Python Script to show what happens when the event loop get blocked with synchronous blocking code. This script creates tasks as before in the examples 3&4, but now we add :

  ```bash
  time.sleep(param)
  ```

  Instead of using asyncio.sleep

  ```bash
  await asyncio.sleep(param)
  ```

  time.sleep() IS NOT _awaitable_, so I can't say `await time.sleep(param)` as that will raise an exception. Plus, time.sleep() does not know how to suspend itself, therefore it blocks the event loop!

- **example6.py**

  Python Script to show what happens when the event loop get blocked with synchronous blocking code, but we mitigate using some asynchronous methods. In this example, `async def fetch_data()` coroutine has been converted into a normal Python method `fetch_data()`. In the script, this function is passed to asyncio to pass this regular function to a thread, which is an example of how to pass this thread to a process. This passing is accomplished by wrapping the `fetch_data` function in `asyncio.to_thread()`. The function is awaitable and essentially a `future`.

  Note, `flush=true` in the print statements is used to print out items in the order expected since I am using threads and processes. Also, notice because I am using threads to spawn new processes, I have to use

  `if __name__ == "__main__":`

  to make sure that the code runs correctly for each new process.

  The time to run this script is greater than all of the previous examples because I ran it in two batches: as tasks and threads and then as two processes within the `with` block of code.

- **example7.py**

  Python Script to show how we can schedule and await `tasks`. Here, I show how to run multiple tasks at once using either of the following:

  - `asyncio.gather(*tasks)` # gather
    - Note `*tasks` used here **unpacks** the list. Unpacking is like entering all of the items of the list individually. Essentially, I am using programmatic methods to do that versus listing each individual item from the list. Similar `*coroutines` unpacking was also done.
  - `asyncio.TaskGroup()` # taskgroups

    - In this section using TaskGroup, I apply a `context manager` that is async because I anticipate IO operations during set-up or teardowns. Recall, a context manager in Python is an object that defines a temporary context for a block of code, ensuring that resources are properly set up at the beginning of the block and torn down (cleaned up) at the end, even if errors occur. A good example is the file handler:

    ```bash
    with open("my_file.txt", "w") as f:
    f.write("Hello, world!")
    # The file 'f' is automatically closed here, even if an error occurred during writing.
    ```

    - Notice, I am not `awaiting` anything with the task group. It `awaits` all tasks created for the group during exit of the context manager.

  The key determination of whether to use `gather` or `task groups` might be based on how you want to handle errors/exceptions. With `asyncio.gather`, if you use the default of `return_exception=False`, then if one task fails it will raise the exception for that task, and not continue with the other tasks. As a result, there is the risk of orphaning tasks. With `return_exception=True`, if one task fails it will raise the exception for that task, but will continue with the other tasks. The results will point out which task did not succeed via an exception result.

  In contrast, `task groups` will fail on a task and cancels all other tasks. It raises an exception group containing all exceptions from the failed tasks. It gives better errors and handles cleaning up the orphan task issue better. Used when you expect all tasks to run successfully.

- **real_world_example_sync1.py**

  Python Script that synchronously downloads and processes a bunch of image files. The idea is to get a baseline set of download, processing, and execution times arrived at through synchronous file operations such that I want to show improvements using asynchronous techniques.

  To determine where to apply the asynchronous operations it is important to determine what is IObound operations and what are CPUbound operations.

  - CPUbound operations - These are operations where compute, calculate, process occur.

  - IObound operations - These are operations where we have to wait for external events to complete like HTTP requests.

  Using `Scalene` is a Python way of determining operations. **Scalene** is a high-performance, high-precision profiler for Python, designed to help developers identify and optimize performance bottlenecks in their code. It offers a comprehensive view of how a Python program utilizes system resources, including CPU, GPU, and memory.

  A sample of the command in action using `uv`

  ```bash
  uv run -m scalene --html --outfile profile_report.html real_world_example_sync1.py
  ```

  results in two files: `profile_report.html` and `profile_report.json`. Both give you an idea of where asynchronous operations or threads can help.

  Looking at the html file in a browser indicates that `system time` is a lot of waiting on IObound operation time. The bulk of that system time occurs in the `dowload_single_image()` function. CPU based time is indciated by the higher **Python** related times which indicates areas for processes incorporation.

  In the next scripts, I will attempt to make improvements.

- **real_world_example_async1.py**

  Python Script that asynchronously downloads and processes a bunch of image files used in exampl_sync1. Here, I am using asyncio only and not other libraries. Notice, I am using `requests` which is not an asynchronous library (i.e., awaitable), so I will need to use `threads` and use `asyncio` to manage those threads.

  I use task groups as well to manage the threads.

  Results show that download time improved. Processe time did not improve. Overall time descreased. Yay!

- **real_world_example_async2.py**

  Python Script that asynchronously downloads and processes a bunch of image files used in exampl_sync1. Here, I am using asyncio other Python libraries that help with asynchronous tasks. I use `HTTPX` for HTTP requests and `aiofiles` package for file processing.

  Additionally, I am going to speed up CPUbound tasks using processes.

  After running the script, I observed a significant reduction in both IObound and CPUbound processes. Total overall execution decreased significantly.

- **real_world_example_async3.py**

  Python Script that asynchronously downloads and processes a bunch of image files used in exampl_sync1. Here, I am using asyncio other Python libraries that speed up IObound and CPUbound tasks similar to the async2 example. However, I am improving on that former script by including code, asyncio's `Semafore`, to manage resources. The general idea is to show how to not overwhelm a system by restricting the number of processes at a time. Imagine if you tried performing 1000's of operations at a time, it may overwhelm some systems.

  An asyncio semaphore in Python is a synchronization primitive that controls access to a shared resource by limiting the number of concurrent tasks that can access it. It is useful for managing resources like database connections or API requests to avoid overwhelming the system.

  After running the script, I observed a significant reduction in both IObound and CPUbound processes. Total overall execution decreased significantly, but not as much as in async2. The differences here is that we limit processes to four at one time and I can see that I execute four processes and as a process finishes I am able to start a new process. In short, providing a more managed approach to processing versus the "shotgun, everything all at once" approach.

---

### Final Words

Thanks for visiting.

Give the project a star (⭐) if you liked it or if it was helpful to you!

You've `beenlanced`! 😉

---

## Acknowledgements

I would like to extend my gratitude to all the individuals and organizations who helped in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, have been invaluable. Thank you.

Specifically, I would like to acknowledge:

- Cory Schaffer for his [Cory Schaffer: Python Tutorial: AsyncIO - Complete Guide to Asynchronous Programming with Animations](https://www.youtube.com/watch?v=oAkLSJNr5zY)

- The folks at **Real Python** for helping to put terminology in the proper context [Real Python](https://realpython.com/async-io-python/)

- [Hema Kalyan Murapaka](https://www.linkedin.com/in/hemakalyan) and [Benito Martin](https://martindatasol.com/blog) for sharing their README.md templates upon which I have derived my README.md.

- The folks at Astral for their UV [documentation](https://docs.astral.sh/uv/)

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details
