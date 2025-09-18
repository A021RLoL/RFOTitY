# 代码生成时间: 2025-09-18 23:14:56
import numpy as np
import unittest

"""
Integration Test Tool

This tool provides a basic framework for integrating and testing numerical
calculations using the NumPy library.
"""

class NumericalCalculation:
    """
    A class for encapsulating numerical calculations.

    Attributes:
        None
    """
    def add(self, x, y):
        """
        Adds two numbers.

        Parameters:
        x (float): The first number.
        y (float): The second number.

        Returns:
        float: The sum of x and y.
        """
        return x + y

    def multiply(self, x, y):
        """
        Multiplies two numbers.

        Parameters:
        x (float): The first number.
        y (float): The second number.

        Returns:
        float: The product of x and y.
        """
        return x * y

    def divide(self, x, y):
        """
        Divides two numbers.

        Parameters:
        x (float): The numerator.
        y (float): The denominator.

        Returns:
        float: The quotient of x divided by y.
        
        Raises:
        ValueError: If y is zero.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

class TestNumericalCalculations(unittest.TestCase):
    """
    Test cases for numerical calculations.

    Attributes:
        None
    """
    def setUp(self):
        """
        Initializes the test environment.
        """
        self.calc = NumericalCalculation()

    def test_add(self):
        """
        Tests the add method.
        """
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_multiply(self):
        """
        Tests the multiply method.
        """
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_divide(self):
        """
        Tests the divide method.
        """
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(-10, -2), 5.0)
        
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
