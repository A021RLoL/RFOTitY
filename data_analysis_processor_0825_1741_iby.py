# 代码生成时间: 2025-08-25 17:41:21
import numpy as np

"""
Data Analysis Processor

This program is designed to analyze data statistics using the numpy library.
It includes error handling, comments, and follows best practices for Python development.
"""

class DataAnalysisProcessor:
    def __init__(self, data):
        """
        Initializes the DataAnalysisProcessor with the given data.
        
        Parameters:
        data (numpy.ndarray): The dataset to be analyzed.
        
        Raises:
        ValueError: If the input data is not a numpy array.
        """
        if not isinstance(data, np.ndarray):
            raise ValueError("Input data must be a numpy array.")
        self.data = data

    def calculate_mean(self):
        """
        Calculates the mean of the dataset.
        
        Returns:
        float: The mean of the dataset.
        """
        return np.mean(self.data)

    def calculate_median(self):
        """
        Calculates the median of the dataset.
        
        Returns:
        float: The median of the dataset.
        """
        return np.median(self.data)

    def calculate_std_deviation(self):
        """
        Calculates the standard deviation of the dataset.
        
        Returns:
        float: The standard deviation of the dataset.
        """
        return np.std(self.data, ddof=0)  # ddof=0 for population standard deviation

    def calculate_variance(self):
        """
        Calculates the variance of the dataset.
        
        Returns:
        float: The variance of the dataset.
        """
        return np.var(self.data, ddof=0)  # ddof=0 for population variance

    def display_statistics(self):
        """
        Displays the calculated statistics of the dataset.
        """
        mean = self.calculate_mean()
        median = self.calculate_median()
        std_dev = self.calculate_std_deviation()
        variance = self.calculate_variance()

        print("Dataset Statistics:")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Standard Deviation: {std_dev}")
        print(f"Variance: {variance}")

# Example usage:
if __name__ == '__main__':
    try:
        # Sample data
        data = np.array([1, 2, 3, 4, 5])

        # Create a DataAnalysisProcessor instance
        processor = DataAnalysisProcessor(data)

        # Display the statistics of the dataset
        processor.display_statistics()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")