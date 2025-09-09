# 代码生成时间: 2025-09-09 17:30:03
import numpy as np

"""
Random Number Generator using NumPy

This program generates random numbers using NumPy's random module.
It provides functionality to generate different types of random numbers,
including integers, floats, and normal distributions.

Attributes:
    None

Methods:
    generate_random_integers(low, high, size): Generates random integers within a given range.
    generate_random_floats(size): Generates random floats between 0 and 1.
    generate_random_normals(mean, std_dev, size): Generates random numbers from a normal distribution.
"""

class RandomNumberGenerator:
    """
    A class to generate random numbers using NumPy.
    """

    def generate_random_integers(self, low, high, size):
        """
        Generates random integers within a given range.
        
        Args:
            low (int): The lower bound of the range (inclusive).
            high (int): The upper bound of the range (exclusive).
            size (int): The number of random integers to generate.
        
        Returns:
            np.ndarray: An array of random integers.
        
        Raises:
            ValueError: If low is greater than high.
        """
        if low >= high:
            raise ValueError("Low must be less than high.")
        return np.random.randint(low, high, size)

    def generate_random_floats(self, size):
        """
        Generates random floats between 0 and 1.
        
        Args:
            size (int): The number of random floats to generate.
        
        Returns:
            np.ndarray: An array of random floats.
        """
        return np.random.rand(size)

    def generate_random_normals(self, mean, std_dev, size):
        """
        Generates random numbers from a normal distribution.
        
        Args:
            mean (float): The mean of the normal distribution.
            std_dev (float): The standard deviation of the normal distribution.
            size (int): The number of random numbers to generate.
        
        Returns:
            np.ndarray: An array of random numbers from the normal distribution.
        
        Raises:
            ValueError: If standard deviation is zero or negative.
        """
        if std_dev <= 0:
            raise ValueError("Standard deviation must be greater than zero.")
        return np.random.normal(mean, std_dev, size)

# Example usage:
if __name__ == "__main__":
    rng = RandomNumberGenerator()
    print("Random Integers: ", rng.generate_random_integers(1, 100, 10))
    print("Random Floats: ", rng.generate_random_floats(10))
    print("Random Normals: ", rng.generate_random_normals(0, 1, 10))