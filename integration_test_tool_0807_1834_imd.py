# 代码生成时间: 2025-08-07 18:34:34
import numpy as np
import unittest

"""
Integration Test Tool using Python and Numpy.
This tool provides a framework to test numerical operations and ensures
that the implementation adheres to expected behavior.
"""

class NumericalOperation:
    """Class containing the numerical operations to be tested."""
    def add(self, a, b):
        """Adds two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers."""
        return a * b

    def divide(self, a, b):
        """Divides two numbers.
        Will raise an error if division by zero is attempted."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        """Raises a to the power of b."""
        return np.power(a, b)

class TestNumericalOperations(unittest.TestCase):
    """Test suite for NumericalOperation class."""
    def setUp(self):
        """Setup method to create an instance of NumericalOperation."""
        self.num_op = NumericalOperation()

    def test_add(self):
        """Test add method."""
        result = self.num_op.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        """Test subtract method."""
        result = self.num_op.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        """Test multiply method."""
        result = self.num_op.multiply(7, 2)
        self.assertEqual(result, 14)

    def test_divide(self):
        """Test divide method."""
        with self.assertRaises(ValueError):
            self.num_op.divide(10, 0)
        result = self.num_op.divide(15, 3)
        self.assertEqual(result, 5)

    def test_power(self):
        """Test power method."""
        result = self.num_op.power(2, 3)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    """Run the tests if this script is executed."""
    unittest.main()
