# 代码生成时间: 2025-09-07 02:57:02
import numpy as np
import unittest

"""
自动化测试套件，使用Python和NumPy框架。

该程序包含一个测试类，用于自动化测试NumPy的核心功能。
"""

class TestNumPyFunctions(unittest.TestCase):
    """测试NumPy函数的类"""

    def test_array_creation(self):
        """测试NumPy数组创建功能"""
        # 创建一个NumPy数组
        array = np.array([1, 2, 3, 4, 5])
        # 验证数组类型
        self.assertIsInstance(array, np.ndarray)
        # 验证数组内容
        self.assertEqual(array.tolist(), [1, 2, 3, 4, 5])

    def test_array_arithmetic(self):
        """测试NumPy数组算术运算"""
        # 创建两个NumPy数组
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        # 验证数组加法
        result = array1 + array2
        self.assertEqual(result.tolist(), [5, 7, 9])
        # 验证数组减法
        result = array1 - array2
        self.assertEqual(result.tolist(), [-3, -3, -3])

    def test_matrix_operations(self):
        """测试矩阵运算功能"""
        # 创建两个2x2矩阵
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[5, 6], [7, 8]])
        # 验证矩阵乘法
        result = np.dot(matrix1, matrix2)
        self.assertEqual(result.tolist(), [[19, 22], [43, 50]])

    def test_statistics_functions(self):
        """测试统计函数"""
        # 创建一个NumPy数组
        array = np.array([1, 2, 3, 4, 5])
        # 验证平均值计算
        mean = np.mean(array)
        self.assertAlmostEqual(mean, 3.0)
        # 验证标准差计算
        std_dev = np.std(array)
        self.assertAlmostEqual(std_dev, np.sqrt(2.0))

    def test_errors(self):
        """测试错误处理"""
        # 故意引发一个除零错误
        with self.assertRaises(ZeroDivisionError):
            np.divide(1, 0)

if __name__ == '__main__':
    """运行测试套件"""
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
