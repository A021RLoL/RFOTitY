# 代码生成时间: 2025-08-31 12:41:08
import numpy as np

"""
# 优化算法效率
Sorting Algorithms Implementation
=================
This module provides implementations of various sorting algorithms.
# 扩展功能模块
It includes Bubble Sort, Selection Sort, Insertion Sort, and Quick Sort.
# NOTE: 重要实现细节

Attributes:
    None

Methods:
    bubble_sort(arr): Sorts an array using Bubble Sort algorithm.
    selection_sort(arr): Sorts an array using Selection Sort algorithm.
# 添加错误处理
    insertion_sort(arr): Sorts an array using Insertion Sort algorithm.
    quick_sort(arr): Sorts an array using Quick Sort algorithm.
"""


def bubble_sort(arr):
    """
    Sorts an array using Bubble Sort algorithm.

    Args:
        arr (numpy array): The input array to be sorted.

    Returns:
        numpy array: The sorted array.
# TODO: 优化性能
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """
    Sorts an array using Selection Sort algorithm.

    Args:
        arr (numpy array): The input array to be sorted.

    Returns:
        numpy array: The sorted array.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
# 扩展功能模块
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """
    Sorts an array using Insertion Sort algorithm.

    Args:
        arr (numpy array): The input array to be sorted.

    Returns:
        numpy array: The sorted array.
    """
# NOTE: 重要实现细节
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
# 添加错误处理
    return arr


def quick_sort(arr):
    """
    Sorts an array using Quick Sort algorithm.

    Args:
        arr (numpy array): The input array to be sorted.

    Returns:
        numpy array: The sorted array.
# TODO: 优化性能
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
# FIXME: 处理边界情况
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = np.array([64, 34, 25, 12, 22, 11, 90])
    print("Original array: ", arr)
    print("Sorted array (Bubble Sort): ", bubble_sort(arr.copy()))
    print("Sorted array (Selection Sort): ", selection_sort(arr.copy()))
    print("Sorted array (Insertion Sort): ", insertion_sort(arr.copy()))
# 增强安全性
    print("Sorted array (Quick Sort): ", quick_sort(arr.copy()))