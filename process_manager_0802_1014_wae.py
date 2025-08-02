# 代码生成时间: 2025-08-02 10:14:33
import psutil
import sys
import signal
import time

"""
Process Manager: A simple program to manage system processes using Python and psutil.

Features:
- List all current processes.
- Kill a process by its PID.
- Gracefully handle errors and exceptions.
"""

class ProcessManager:
    """Manage system processes."""

    def __init__(self):
        pass

    def list_processes(self):
        """List all current system processes."""
        try:
            for proc in psutil.process_iter(['pid', 'name', 'status']):
                yield proc.info
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error listing processes: {e}")

    def kill_process(self, pid):
        """Kill a process by its PID."""
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait(timeout=5)
        except psutil.NoSuchProcess:
            print(f"No process found with PID {pid}")
        except psutil.AccessDenied:
            print(f"Permission denied to terminate process with PID {pid}")
        except psutil.TimeoutExpired:
            print(f"Process with PID {pid} did not terminate within the timeout period")
        except Exception as e:
            print(f"An error occurred: {e}")

    def signal_handler(self, signal, frame):
        """Handle signals for graceful shutdown."""
        print("Graceful shutdown initiated...")
        sys.exit(0)

if __name__ == '__main__':
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, ProcessManager().signal_handler)
    signal.signal(signal.SIGTERM, ProcessManager().signal_handler)

    manager = ProcessManager()
    while True:
        # Display menu
        print("
Process Manager Menu:")
        print("1. List all processes")
        print("2. Kill a process")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("
Listing all processes...")
            for proc in manager.list_processes():
                print(f"PID: {proc['pid']}, Name: {proc['name']}, Status: {proc['status']}")
        elif choice == '2':
            pid = input("Enter the PID of the process to kill: ")
            try:
                pid = int(pid)
                manager.kill_process(pid)
            except ValueError:
                print("Invalid PID. Please enter a numerical value.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        time.sleep(1)  # Pause for 1 second before displaying the menu again