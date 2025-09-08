# 代码生成时间: 2025-09-08 20:41:33
import numpy as np
import unittest

"""
A simple unit test framework using Python's unittest module and NumPy for numerical operations.
"""

class NumericalOperationTests(unittest.TestCase):
    def test_addition(self):
        """
        Test addition of two numbers.
        """
        result = np.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtraction(self):
        """
        Test subtraction of two numbers.
        """
        result = np.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        """
        Test multiplication of two numbers.
        """
        result = np.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_division(self):
        """
        Test division of two numbers.
        """
        with self.assertRaises(ZeroDivisionError):
            result = np.divide(10, 0)

    def test_power(self):
        """
        Test raising a number to a power.
        """
        result = np.power(2, 3)
        self.assertEqual(result, 8)

    def test_mean(self):
        """
        Test calculating the mean of a set of numbers.
        """
        numbers = np.array([1, 2, 3, 4, 5])
        result = np.mean(numbers)
        self.assertEqual(result, 3.0)

    def test_sum(self):
        """
        Test calculating the sum of a set of numbers.
        """
        numbers = np.array([1, 2, 3, 4, 5])
        result = np.sum(numbers)
        self.assertEqual(result, 15)

    def test_std_deviation(self):
        """
        Test calculating the standard deviation of a set of numbers.
        """
        numbers = np.array([1, 2, 3, 4, 5])
        result = np.std(numbers)
        self.assertGreaterEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
