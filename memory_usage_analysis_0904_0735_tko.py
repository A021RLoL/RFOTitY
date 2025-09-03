# 代码生成时间: 2025-09-04 07:35:51
import numpy as np
import psutil
import os
from collections import defaultdict

"""
A program to analyze memory usage of numpy arrays.

Features:
- Displays memory usage of numpy arrays in bytes and human-readable format.
- Provides options to analyze memory usage of specific arrays or all arrays in memory.
- Includes error handling for invalid inputs and exceptions.

Usage:
- Run the program to see memory usage analysis of numpy arrays.
"""

class MemoryUsageAnalyzer:
    def __init__(self):
        self.memory_info = defaultdict(int)

    def get_memory_usage(self, array_name):
        """
        Returns memory usage of the specified numpy array in bytes and human-readable format.
        """
        try:
            array = globals()[array_name]
            if not isinstance(array, np.ndarray):
                raise ValueError(f"'{array_name}' is not a numpy array")
            bytes_used = array.nbytes
            readable_format = self.human_readable(bytes_used)
            self.memory_info[array_name] = bytes_used
            return bytes_used, readable_format
        except KeyError:
            raise ValueError(f"'{array_name}' not found in global scope")
        except Exception as e:
            raise Exception(f"Error getting memory usage: {str(e)}")

    def human_readable(self, bytes_used):
        """
        Converts bytes to a human-readable format (e.g., KB, MB, GB).
        """
        if bytes_used < 1024:
            return f"{bytes_used} bytes"
        elif bytes_used < 1024 ** 2:
            return f"{bytes_used / 1024:.2f} KB"
        elif bytes_used < 1024 ** 3:
            return f"{bytes_used / 1024 ** 2:.2f} MB"
        else:
            return f"{bytes_used / 1024 ** 3:.2f} GB"

    def get_total_memory_usage(self):
        """
        Returns total memory usage of all numpy arrays in bytes and human-readable format.
        """
        total_bytes = sum(self.memory_info.values())
        readable_format = self.human_readable(total_bytes)
        return total_bytes, readable_format

    def analyze_memory_usage(self, array_name=None):
        """
        Analyzes memory usage of the specified array or all arrays if no name is provided.
        """
        if array_name:
            bytes_used, readable_format = self.get_memory_usage(array_name)
            print(f"Memory usage of '{array_name}': {readable_format}")
        else:
            total_bytes, readable_format = self.get_total_memory_usage()
            print(f"Total memory usage of all arrays: {readable_format}")

# Example usage:
if __name__ == "__main__":
    # Create a sample numpy array
    sample_array = np.random.rand(1000, 1000)

    # Analyze memory usage of the sample array
    analyzer = MemoryUsageAnalyzer()
    analyzer.analyze_memory_usage("sample_array")

    # Analyze total memory usage of all arrays
    analyzer.analyze_memory_usage()
