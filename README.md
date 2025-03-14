# Sorting Product Weights

## Description
This project implements **Bubble Sort, Selection Sort, and Insertion Sort** to sort a list of product weights for a logistics company. The performance of these sorting algorithms is measured and compared with Python's built-in `sorted()` function.

## Features
- **Bubble Sort**: A simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order.
- **Selection Sort**: An algorithm that selects the smallest element and moves it to its correct position.
- **Insertion Sort**: A sorting algorithm that builds the sorted array one item at a time, inserting each new element into its correct position.
- **Performance Measurement**: Execution time comparison for **small (50 elements), large (1000 elements), and extra-large (10,000 elements) datasets**.
- **Analysis**: Insights into algorithm efficiency and real-world implications.

## Implementation

### Bubble Sort
The algorithm repeatedly swaps adjacent elements if they are out of order until the entire list is sorted.

```python
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
```

### Selection Sort
This algorithm selects the smallest element in the remaining list and swaps it with the first unsorted element.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### Insertion Sort
Insertion Sort builds the sorted list one element at a time, placing each new element in its correct position.

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

## Performance Measurement
A function is used to measure execution time:

```python
def measure_time(sort_function, data):
    import time
    start_time = time.time()
    sort_function(data[:])  # Use a copy to keep original data intact
    return time.time() - start_time
```

## Performance Comparison

### Small Dataset (100 product weights)
- **Bubble Sort**: 0.001004 seconds
- **Selection Sort**: ~0.00000 seconds
- **Insertion Sort**: ~0.00000 seconds
- **Python Built-in Sort**: ~0.000000 seconds

### Large Dataset (1000 product weights)
- **Bubble Sort**: ~0.11 seconds
- **Selection Sort**: ~0.05 seconds
- **Insertion Sort**: ~0.04 seconds
- **Python Built-in Sort**: ~0.00000 seconds

### Extra-Large Dataset (10,000 product weights)
- **Bubble Sort**:  Too slow (exceeds reasonable time limits) (11s)
- **Selection Sort**:  Too slow (4s)
- **Insertion Sort**: ~4-5 seconds
- **Python Built-in Sort**: ~0.0003 seconds

## Conclusions
- **Bubble Sort** is inefficient for large datasets due to its O(n²) complexity.
- **Selection Sort** is slightly better but still O(n²), making it slow for large inputs.
- **Insertion Sort** performs better than Bubble and Selection Sort, but remains O(n²).
- **Python's built-in sort (Timsort)** is significantly faster with O(n log n) complexity and is the best choice for large datasets.

## Recommendations
For practical applications, avoid using **Bubble Sort, Selection Sort, and Insertion Sort** for large datasets. Instead, use **Python's built-in sorting functions** or more efficient algorithms like **Merge Sort or Quick Sort**.
