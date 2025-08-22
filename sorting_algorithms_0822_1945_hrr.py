# 代码生成时间: 2025-08-22 19:45:53
import numpy as np
"""
Sorting Algorithms Implementation using Python and NumPy.
This module provides several sorting algorithms:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
"""

# Bubble Sort
def bubble_sort(a):
    """
    This function implements the bubble sort algorithm.
    It repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    
    Parameters:
    a (numpy.ndarray): The input array to be sorted.
    
    Returns:
    numpy.ndarray: The sorted array.
    """
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                # Swap the elements
                a[j], a[j+1] = a[j+1], a[j]
    return a

# Selection Sort
def selection_sort(a):
    """
    This function implements the selection sort algorithm.
    It divides the input list into two parts: the sorted part and the unsorted part.
    It repeatedly selects the smallest (or largest, depending on sorting order) element from
    the unsorted part and moves it to the sorted part.
    
    Parameters:
    a (numpy.ndarray): The input array to be sorted.
    
    Returns:
    numpy.ndarray: The sorted array.
    """
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# Insertion Sort
def insertion_sort(a):
    """
    This function implements the insertion sort algorithm.
    It builds the final sorted array one item at a time.
    It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
    
    Parameters:
    a (numpy.ndarray): The input array to be sorted.
    
    Returns:
    numpy.ndarray: The sorted array.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# Merge Sort
def merge_sort(a):
    """
    This function implements the merge sort algorithm.
    It uses the divide and conquer approach to sort the input array.
    
    Parameters:
    a (numpy.ndarray): The input array to be sorted.
    
    Returns:
    numpy.ndarray: The sorted array.
    """
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]
        
        # Recursive call on each half
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        
        # Check if any element was left
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
    return a

# Quick Sort
def quick_sort(a):
    """
    This function implements the quick sort algorithm.
    It is a divide and conquer algorithm.
    It works by selecting a 'pivot' element from the array and partitioning the other elements
    into two sub-arrays, according to whether they are less than or greater than the pivot.
    The sub-arrays are then recursively sorted.
    
    Parameters:
    a (numpy.ndarray): The input array to be sorted.
    
    Returns:
    numpy.ndarray: The sorted array.
    """
    def partition(low, high):
        i = low - 1
        pivot = a[high]
        for j in range(low, high):
            if a[j] <= pivot:
                i = i + 1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[high] = a[high], a[i+1]
        return i+1
    
    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi-1)
            quick_sort_recursive(pi+1, high)
    
    quick_sort_recursive(0, len(a)-1)
    return a

# Main function to test the sorting algorithms
def main():
    print("Testing sorting algorithms with NumPy arrays.")
    test_array = np.array([64, 34, 25, 12, 22, 11, 90])
    
    print("Original array: ", test_array)
    
    print("Bubble Sort: ", bubble_sort(test_array.copy()))
    print("Selection Sort: ", selection_sort(test_array.copy()))
    print("Insertion Sort: ", insertion_sort(test_array.copy()))
    print("Merge Sort: ", merge_sort(test_array.copy()))
    print("Quick Sort: ", quick_sort(test_array.copy()))

if __name__ == '__main__':
    main()