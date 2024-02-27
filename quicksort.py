import random
import timeit
import matplotlib.pyplot as plt


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_random_pivot(arr):
    random.shuffle(arr)
    quicksort(arr, 0, len(arr) - 1)


def quicksort_nonrandom_pivot(arr):
    quicksort(arr, 0, len(arr) - 1)


def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]


def generate_best_case_array(size):
    return list(range(1, size + 1))


def generate_worst_case_array(size):
    return list(range(size, 0, -1))


def generate_average_case_array(size):
    return [random.randint(1, size) for _ in range(size)]


def benchmark(sort_function, input_generator, sizes, repeats=5):
    results = []
    for size in sizes:
        time_taken = timeit.timeit(lambda: sort_function(input_generator(size)), number=repeats)
        results.append(time_taken / repeats)
    return results


test_array = [5, 3, 2, 1, 4]
print("Original array:", test_array)
quicksort_nonrandom_pivot(test_array)
print("Sorted array:", test_array)

test_array = [5, 3, 2, 1, 4]
print("Original array:", test_array)
quicksort_random_pivot(test_array)
print("Sorted array:", test_array)


sizes = [10, 50, 100, 200, 300, 400, 500]
repeats = 5

best_case_results = benchmark(quicksort_nonrandom_pivot, generate_best_case_array, sizes, repeats)
worst_case_results = benchmark(quicksort_nonrandom_pivot, generate_worst_case_array, sizes, repeats)
average_case_results = benchmark(quicksort_nonrandom_pivot, generate_average_case_array, sizes, repeats)


plt.plot(sizes, best_case_results, label="Best Case")
plt.plot(sizes, worst_case_results, label="Worst Case")
plt.plot(sizes, average_case_results, label="Average Case")

plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Non-random Pivot Quicksort Benchmarks')
plt.legend()
plt.show()
