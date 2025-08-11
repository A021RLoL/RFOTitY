# 代码生成时间: 2025-08-12 07:17:14
import psutil
import time
import json

"""
System Performance Monitor using Python and NumPy

This tool provides a way to monitor system performance metrics such as CPU, Memory, and Disk usage.

How to use this tool:
- Install required packages: psutil
- Run the script and it will start monitoring the system performance.
"""

class SystemPerformanceMonitor:
    """
    A class used to monitor system performance metrics like CPU, Memory, and Disk usage.
    """

    def __init__(self):
        # Initialize the monitor
        self.cpu_usage = 0
        self.memory_usage = 0
        self.disk_usage = 0

    def get_cpu_usage(self):
        """
        Get the current CPU usage as a percentage.
        """
        try:
            self.cpu_usage = psutil.cpu_percent()
        except Exception as e:
            print(f"Failed to get CPU usage: {e}")

    def get_memory_usage(self):
        """
        Get the current memory usage as a percentage.
        """
        try:
            memory = psutil.virtual_memory()
            self.memory_usage = memory.percent
        except Exception as e:
            print(f"Failed to get memory usage: {e}")

    def get_disk_usage(self):
        """
        Get the current disk usage as a percentage.
        """
        try:
            disk = psutil.disk_usage('/')
            self.disk_usage = disk.percent
        except Exception as e:
            print(f"Failed to get disk usage: {e}")

    def get_system_performance(self):
        """
        Get the system performance metrics.
        """
        self.get_cpu_usage()
        self.get_memory_usage()
        self.get_disk_usage()

    def print_performance(self):
        """
        Print the system performance metrics.
        """
        print("System Performance Metrics:")
        print(f"CPU Usage: {self.cpu_usage}%")
        print(f"Memory Usage: {self.memory_usage}%")
        print(f"Disk Usage: {self.disk_usage}%")

    def to_json(self):
        """
        Convert the system performance metrics to JSON format.
        """
        metrics = {
            "CPU Usage": self.cpu_usage,
            "Memory Usage": self.memory_usage,
            "Disk Usage": self.disk_usage
        }
        return json.dumps(metrics, indent=4)

# Main function
def main():
    monitor = SystemPerformanceMonitor()
    monitor.get_system_performance()
    print(monitor.to_json())

if __name__ == "__main__":
    main()