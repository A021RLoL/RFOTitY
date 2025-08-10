# 代码生成时间: 2025-08-11 07:24:16
import numpy as np
import time
from datetime import datetime

"""
性能测试脚本，用于评估NumPy操作的性能。

本脚本将执行两个主要操作：
1. 创建一个大数组并计算其平方
2. 创建一个大数组并执行元素级加法

每个操作将被执行多次，以获取平均性能数据。
"""

# 定义数组的大小
array_size = 100000000  # 1亿元素

# 定义测试迭代次数
iterations = 10

"""
计算给定数组平方的平均执行时间。
"""
def test_square_performance(array_size, iterations):
    # 创建一个随机数组
    array = np.random.rand(array_size)
    
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        np.square(array)
        end_time = time.time()
        total_time += (end_time - start_time)
    
    average_time = total_time / iterations
    print(f'平均平方操作耗时: {average_time:.6f} 秒')

"""
计算给定数组元素级加法的平均执行时间。
"""
def test_elementwise_add_performance(array_size, iterations):
    # 创建两个随机数组
    array1 = np.random.rand(array_size)
    array2 = np.random.rand(array_size)
    
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        np.add(array1, array2)
        end_time = time.time()
        total_time += (end_time - start_time)
    
    average_time = total_time / iterations
    print(f'平均元素级加法耗时: {average_time:.6f} 秒')


# 主函数
if __name__ == '__main__':
    try:
        # 测试平方操作性能
        test_square_performance(array_size, iterations)
        
        # 测试元素级加法性能
        test_elementwise_add_performance(array_size, iterations)
    except Exception as e:
        print(f'发生错误: {e}')
