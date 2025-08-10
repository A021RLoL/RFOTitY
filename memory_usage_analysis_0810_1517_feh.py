# 代码生成时间: 2025-08-10 15:17:23
import numpy as np
import psutil
import os
import sys

"""
Memory Usage Analysis Tool

This tool is designed to analyze the memory usage of a Python program.
It uses the psutil library to gather memory usage information and numpy to handle data.
"""

# Function to get the current memory usage of the system
def get_system_memory_usage():
    try:
        # Get the current process
        process = psutil.Process(os.getpid())
        # Get the memory usage information
        mem_info = process.memory_info()
        # Return the memory usage in bytes
        return mem_info.rss  # Resident Set Size
    except Exception as e:
        # Handle any exceptions that may occur
        print(f"An error occurred: {e}")
        sys.exit(1)

# Function to get the peak memory usage of the system
def get_peak_memory_usage():
    try:
        # Get the current process
        process = psutil.Process(os.getpid())
        # Get the peak memory usage information
        mem_info = process.memory_info(peak=True)
        # Return the peak memory usage in bytes
        return mem_info.rss  # Resident Set Size
    except Exception as e:
        # Handle any exceptions that may occur
        print(f"An error occurred: {e}")
        sys.exit(1)

# Function to calculate the total memory usage of numpy arrays
def get_numpy_array_memory_usage():
    try:
        # Get the memory usage of all numpy arrays
        total_usage = 0
        for arr in np._NDArrayArray.__array__():
            total_usage += arr.nbytes
        # Return the total memory usage in bytes
        return total_usage
    except Exception as e:
        # Handle any exceptions that may occur
        print(f"An error occurred: {e}")
        sys.exit(1)

# Main function to analyze memory usage
def main():
    # Print the current memory usage
    current_usage = get_system_memory_usage()
    print(f"Current memory usage: {current_usage / (1024 * 1024):.2f} MB")

    # Print the peak memory usage
    peak_usage = get_peak_memory_usage()
    print(f"Peak memory usage: {peak_usage / (1024 * 1024):.2f} MB")

    # Print the total memory usage of numpy arrays
    numpy_usage = get_numpy_array_memory_usage()
    print(f"Total memory usage of numpy arrays: {numpy_usage / (1024 * 1024):.2f} MB")

if __name__ == 