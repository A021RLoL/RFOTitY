# 代码生成时间: 2025-09-03 03:27:36
import numpy as np
def load_data(file_path):
    """
    Load data from a file.

    Parameters:
    file_path (str): The path to the data file.

    Returns:
    numpy.ndarray: The loaded data as a NumPy array.
    """
    try:
        data = np.loadtxt(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def calculate_mean(data):
    """
    Calculate the mean of the data.

    Parameters:
    data (numpy.ndarray): The data to calculate the mean for.

    Returns:
    float: The mean of the data.
    """
    if data is None:
        return None
    return np.mean(data)
def calculate_median(data):
    """
    Calculate the median of the data.

    Parameters:
    data (numpy.ndarray): The data to calculate the median for.

    Returns:
    float: The median of the data.
    """
    if data is None:
        return None
    return np.median(data)
def calculate_standard_deviation(data):
    """
    Calculate the standard deviation of the data.

    Parameters:
    data (numpy.ndarray): The data to calculate the standard deviation for.

    Returns:
    float: The standard deviation of the data.
    """
    if data is None:
        return None
    return np.std(data)
def main():
    # Replace 'data.csv' with your actual data file path
    file_path = 'data.csv'
    data = load_data(file_path)

    if data is not None:
        mean = calculate_mean(data)
        median = calculate_median(data)
        std_dev = calculate_standard_deviation(data)

        print(f'Mean: {mean}')
        print(f'Median: {median}')
        print(f'Standard Deviation: {std_dev}')
    else:
        print("No data to analyze.")

if __name__ == '__main__':
    main()