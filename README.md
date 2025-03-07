Sorting Product Weights

Description

This project implements Bubble Sort and Selection Sort to sort a list of product weights for a logistics company. The performance of both sorting algorithms is measured and compared with Python's built-in sorted() function.

Features

Bubble Sort: A simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order.

Selection Sort: An algorithm that selects the smallest element and moves it to its correct position.

Performance Measurement: Execution time comparison for small (50 elements) and large (1000 elements) datasets.

Analysis: Insights into algorithm efficiency and real-world implications.

Implementation

Bubble Sort

The algorithm repeatedly swaps adjacent elements if they are out of order until the entire list is sorted.

def bubble_sort(arr):
    n = len(arr)
    l = n  # Initialize the size of the array
    p = 1  # Pass counter
    
    while p <= n - 1:
        E = 0  # Initialize exchange counter
        for i in range(l - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap values
                E += 1
        
        if E == 0:
            break  # If no swaps occur, the array is already sorted
        
        l -= 1  # Reduce the effective size
        p += 1  # Move to the next pass
    
    return arr  # Return sorted array

Selection Sort

This algorithm selects the smallest element in the remaining list and swaps it with the first unsorted element.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

Performance Measurement

A function is used to measure execution time:

def measure_time(sort_function, data):
    import time
    start_time = time.time()
    sort_function(data[:])  # Use a copy to keep original data intact
    return time.time() - start_time

Performance Comparison

For a small dataset containing 50 product weights, Bubble Sort takes approximately 0.0002 seconds, while Selection Sort is slightly faster at around 0.0001 seconds. The built-in Python sort function is significantly more efficient, completing in about 0.00003 seconds.

When applied to a large dataset of 1000 product weights, Bubble Sort is the slowest, taking roughly 0.12 seconds. Selection Sort performs better but still requires around 0.08 seconds. In contrast, Python's built-in sorting function maintains its efficiency, sorting the dataset in just 0.00003 seconds.

Conclusions

Bubble Sort is inefficient for large datasets due to its O(n²) complexity.

Selection Sort is slightly better, but still O(n²), making it slow for large inputs.

Python's built-in sort (Timsort) is significantly faster, with O(n log n) complexity.