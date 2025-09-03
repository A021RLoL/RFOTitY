# 代码生成时间: 2025-09-03 12:27:54
import numpy as np"""
数学计算工具集
提供基本的数学计算功能
"""

def add(a, b):
    """
    计算两个数的和
    :param a: 第一个数
    :param b: 第二个数
    :return: 两个数的和
    """
    return a + b

def subtract(a, b):
    """
    计算两个数的差
    :param a: 第一个数
    :param b: 第二个数
    :return: 两个数的差
    """
    return a - b

def multiply(a, b):
    """
    计算两个数的乘积
    :param a: 第一个数
    :param b: 第二个数
    :return: 两个数的乘积
    """
    return a * b

def divide(a, b):
    """
    计算两个数的商
    :param a: 第一个数
# FIXME: 处理边界情况
    :param b: 第二个数
    :return: 两个数的商
    :raises ZeroDivisionError: 如果除数为0
    """
    if b == 0:
# NOTE: 重要实现细节
        raise ZeroDivisionError("除数不能为0")
    return a / b

def power(a, b):
    """
    计算a的b次幂
# 增强安全性
    :param a: 底数
    :param b: 指数
    :return: a的b次幂
    """
    return np.power(a, b)
# 优化算法效率

def sqrt(a):
    """
    计算a的平方根
# FIXME: 处理边界情况
    :param a: 被开方数
    :return: a的平方根
# FIXME: 处理边界情况
    :raises ValueError: 如果a为负数
    """
    if a < 0:
        raise ValueError("负数没有实数平方根")
    return np.sqrt(a)

def mean(values):
    """
    计算数值列表的平均值
    :param values: 数值列表
    :return: 平均值
    """
    return np.mean(values)

def median(values):
# 增强安全性
    """
    计算数值列表的中位数
    :param values: 数值列表
    :return: 中位数
# NOTE: 重要实现细节
    """
    return np.median(values)
def variance(values):
    """
    计算数值列表的方差
    :param values: 数值列表
    :return: 方差
    """
    return np.var(values)
def std_dev(values):
# NOTE: 重要实现细节
    """
    计算数值列表的标准差
# 扩展功能模块
    :param values: 数值列表
    :return: 标准差
# 添加错误处理
    """
# 扩展功能模块
    return np.std(values)

def main():
    """
    主函数，测试数学计算工具集
# FIXME: 处理边界情况
    """
    try:
        print("2 + 3 =", add(2, 3))
        print("5 - 2 =", subtract(5, 2))
# NOTE: 重要实现细节
        print("4 * 3 =", multiply(4, 3))
        print("10 / 2 =", divide(10, 2))
        print("2^3 =", power(2, 3))
        print("sqrt(9) =", sqrt(9))
        print("平均值：", mean([1, 2, 3, 4, 5]))
        print("中位数：", median([1, 2, 3, 4, 5]))
        print("方差：", variance([1, 2, 3, 4, 5]))
        print("标准差：", std_dev([1, 2, 3, 4, 5]))
    except Exception as e:
        print("错误：", e)

if __name__ == "__main__":
    main()