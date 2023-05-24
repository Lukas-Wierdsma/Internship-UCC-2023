from multiprocessing import Pool
import time

def process(x):
    time.sleep(3)
    return x/1000000

if __name__ == "__main__":
    # Create a Pool with the desired number of processes
    num_processes = 4
    pool = Pool(processes=num_processes)
    results = []
    t0 = time.time()
    # Define a list of numbers
    for i in range(5000000):
        if (i % 1000000) == 0:
            results.append(pool.apply_async(process, [i]))
            t1 = time.time()
            print ("Elapsed time trigger:", t1 - t0)
    t1 = time.time()
    print("Total elapsed time:", t1 - t0)
    
    results = [result.get() for result in results]

    # Close the pool to prevent any more tasks from being submitted
    pool.close()

    # Wait for all the processes to complete
    pool.join()
    t1 = time.time()
    print("Total elapsed time (including pool join):", t1 - t0)

    # Print the results
    print(results)