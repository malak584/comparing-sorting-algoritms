import random
import time

def bubble_sort(arr):
    n = len(arr)
    l = n 
    p = 1 
    
    while p <= n - 1:
        E = 0 
        for i in range(l - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                E += 1
        
        if E == 0:
            break  
        
        l -= 1  
        p += 1  
    
    return arr  

def selection_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        smallest = j  
        for i in range(j + 1, n):
            if arr[i] < arr[smallest]:
                smallest = i  
        if smallest != j:
            arr[j], arr[smallest] = arr[smallest], arr[j] 
    return arr

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

def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data[:])  # Use a copy to keep original data intact
    return time.time() - start_time

# Generate datasets
small_dataset = [random.randint(1, 1000) for _ in range(50)]
large_dataset = [random.randint(1, 1000) for _ in range(1000)]
extra_large_dataset = [random.randint(1, 1000) for _ in range(10000)]

# Measure performance
print(" Small Dataset (50 product weights):")
print(f" Bubble Sort took {measure_time(bubble_sort, small_dataset):.6f} seconds.")
print(f" Selection Sort took {measure_time(selection_sort, small_dataset):.6f} seconds.")
print(f" Insertion Sort took {measure_time(insertion_sort, small_dataset):.6f} seconds.")
print(f" Python Built-in Sort took {measure_time(sorted, small_dataset):.6f} seconds.")

print("\n Large Dataset (1000 product weights):")
print(f" Bubble Sort took {measure_time(bubble_sort, large_dataset):.6f} seconds.")
print(f" Selection Sort took {measure_time(selection_sort, large_dataset):.6f} seconds.")
print(f" Insertion Sort took {measure_time(insertion_sort, large_dataset):.6f} seconds.")
print(f" Python Built-in Sort took {measure_time(sorted, large_dataset):.6f} seconds.")

print("\n Extra Large Dataset (10000 product weights):")
print(f" Bubble Sort took {measure_time(bubble_sort, extra_large_dataset):.6f} seconds.")
print(f" Selection Sort took {measure_time(selection_sort, extra_large_dataset):.6f} seconds.")
print(f" Insertion Sort took {measure_time(insertion_sort, extra_large_dataset):.6f} seconds.")
print(f" Python Built-in Sort took {measure_time(sorted, extra_large_dataset):.6f} seconds.")