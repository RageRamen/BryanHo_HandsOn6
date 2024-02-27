import random
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def quicksort_random_pivot(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_random_pivot(left) + middle + quicksort_random_pivot(right)

def generate_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(size))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def time_quicksort(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

def benchmark(sort_func, size, trials):
    times = []
    for _ in range(trials):
        arr = generate_array(size)
        times.append(time_quicksort(sort_func, arr))
    return sum(times) / trials

def plot_benchmarks():
    sizes = [10, 100, 1000, 10000]
    trials = 10

    best_case_times = []
    worst_case_times = []
    average_case_times = []

    for size in sizes:
        best_case_times.append(benchmark(quicksort, size, trials))
        worst_case_times.append(benchmark(quicksort, size, trials))
        average_case_times.append(benchmark(quicksort, size, trials))

    plt.plot(sizes, best_case_times, label='Best Case')
    plt.plot(sizes, worst_case_times, label='Worst Case')
    plt.plot(sizes, average_case_times, label='Average Case')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.title('Quicksort Benchmarks')
    plt.legend()
    plt.show()


plot_benchmarks()
