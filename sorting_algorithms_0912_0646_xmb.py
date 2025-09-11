# 代码生成时间: 2025-09-12 06:46:58
import numpy as np

"""
A Python module providing various sorting algorithms implemented using numpy arrays.

This module includes implementations of several sorting algorithms such as:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
Each algorithm is implemented as a function that takes a numpy array as input and returns the sorted array.
"""


def bubble_sort(arr):
    """
    Bubble Sort implementation using numpy arrays.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
# 增强安全性
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# TODO: 优化性能
    return arr


def selection_sort(arr):
    """
    Selection Sort implementation using numpy arrays.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
    n = len(arr)
# NOTE: 重要实现细节
    for i in range(n):
        min_idx = np.argmin(arr[i:])
        arr[i], arr[min_idx + i] = arr[min_idx + i], arr[i]
    return arr


def insertion_sort(arr):
    """
    Insertion Sort implementation using numpy arrays.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
# TODO: 优化性能
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
# 改进用户体验
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Merge Sort implementation using numpy arrays.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
    if len(arr) > 1:
# 优化算法效率
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
# FIXME: 处理边界情况
            k += 1
        while j < len(R):
# TODO: 优化性能
            arr[k] = R[j]
# 改进用户体验
            j += 1
            k += 1
    return arr


def sort_array(arr, algorithm='bubble_sort'):
# 扩展功能模块
    """
    Sorts the array using the specified algorithm.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.
    algorithm (str): The name of the sorting algorithm to use.
        Options are 'bubble_sort', 'selection_sort', 'insertion_sort', 'merge_sort'.

    Returns:
# 改进用户体验
    numpy.ndarray: The sorted array.
    """
    if algorithm == 'bubble_sort':
        return bubble_sort(np.copy(arr))
    elif algorithm == 'selection_sort':
        return selection_sort(np.copy(arr))
# NOTE: 重要实现细节
    elif algorithm == 'insertion_sort':
        return insertion_sort(np.copy(arr))
    elif algorithm == 'merge_sort':
        return merge_sort(np.copy(arr))
    else:
# 改进用户体验
        raise ValueError("Invalid sorting algorithm specified")

# Example usage:
if __name__ == '__main__':
    arr = np.array([64, 34, 25, 12, 22, 11, 90])
    sorted_arr = sort_array(arr, algorithm='merge_sort')
    print("Sorted array: ", sorted_arr)