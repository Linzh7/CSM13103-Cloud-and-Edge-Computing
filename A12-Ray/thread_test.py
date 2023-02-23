import threading
import time
import numpy as np

maxN = 1000
numArray = np.random.randint(1, maxN, 10000)


def sum_thread(numbers, n):
    start_time = time.time()
    result = sum(numbers[:n])
    end_time = time.time()
    return end_time - start_time


def stat(results):
    avg_exec_time = sum(results) / len(results)
    print(
        f"Avg: {avg_exec_time:.5f} seconds.\nMin: {min(results):.5f} seconds.\nMax: {max(results):.5f} seconds.\nStd: {np.std(results):.5f} seconds."
    )


if __name__ == "__main__":
    # Create a list of random numbers
    numbers = [i for i in range(1000)]
    # Create a empty list to store the results
    results = []
    # Repeat thread creation and destruction 1000 times
    num_repeats = 1000
    t1 = time.time()
    for i in range(num_repeats):
        # Choose a random number of elements to add
        n = np.random.randint(1, maxN)

        # Create a new thread
        start_time = time.time()
        t = threading.Thread(target=sum_thread, args=(numbers, n))
        t.start()

        # Wait for the thread to finish
        t.join()

        # Print the total time for thread creation, execution, and destruction
        end_time = time.time()
        results.append(end_time - start_time)
    print("Results for 1000 threads:")
    print(f"Total time: {time.time() - t1:.5f} seconds.")
    stat(results)

    results = []
    # Repeat thread creation and destruction 1000 times
    num_repeats = 1000
    t1 = time.time()
    for i in range(num_repeats):
        # Choose a random number of elements to add
        n = np.random.randint(1, maxN)

        # just sum, not a thread
        start_time = time.time()
        sum_thread(numbers, n)
        end_time = time.time()
        results.append(end_time - start_time)
    print("Results for 1000 sum:")
    print(f"Total time: {time.time() - t1:.5f} seconds.")
    stat(results)