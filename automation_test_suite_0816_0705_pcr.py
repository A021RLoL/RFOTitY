# 代码生成时间: 2025-08-16 07:05:38
import numpy as np
import unittest

"""
自动化测试套件
这个程序包含了使用Python和NumPy框架的自动化测试案例。
每个测试用例都将验证NumPy操作的正确性。"""

class TestNumPyOperations(unittest.TestCase):
    """测试NumPy操作"""
    def setUp(self):
        """设置测试环境"""
        self.array1 = np.array([1, 2, 3])
        self.array2 = np.array([4, 5, 6])

    def test_addition(self):
        """测试NumPy数组加法"""
        result = np.add(self.array1, self.array2)
        expected_result = np.array([5, 7, 9])
        self.assertTrue(np.array_equal(result, expected_result), "加法测试失败")

    def test_subtraction(self):
        """测试NumPy数组减法"""
        result = np.subtract(self.array1, self.array2)
        expected_result = np.array([-3, -3, -3])
        self.assertTrue(np.array_equal(result, expected_result), "减法测试失败")

    def test_multiplication(self):
        """测试NumPy数组乘法"""
        result = np.multiply(self.array1, self.array2)
        expected_result = np.array([4, 10, 18])
        self.assertTrue(np.array_equal(result, expected_result), "乘法测试失败")

    def test_division(self):
        """测试NumPy数组除法"""
        result = np.divide(self.array1, self.array2)
        expected_result = np.array([0.25, 0.4, 0.5])
        self.assertTrue(np.allclose(result, expected_result), "除法测试失败")

    def test_power(self):
        """测试NumPy数组幂运算"""
        result = np.power(self.array1, 2)
        expected_result = np.array([1, 4, 9])
        self.assertTrue(np.array_equal(result, expected_result), "幂运算测试失败")

    def test_logarithm(self):
        """测试NumPy数组对数运算"""
        result = np.log(self.array1)
        expected_result = np.log(self.array1)
        self.assertTrue(np.allclose(result, expected_result), "对数运算测试失败")

    def test_mean(self):
        """测试NumPy数组均值计算"""
        result = np.mean(self.array1)
        expected_result = np.sum(self.array1) / len(self.array1)
        self.assertTrue(np.isclose(result, expected_result), "均值计算测试失败")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
