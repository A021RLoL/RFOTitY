# 代码生成时间: 2025-09-22 22:51:09
import numpy as np
import pandas as pd
# 扩展功能模块
import os
from glob import glob

"""
CSV文件批量处理器

这个程序会处理一个目录下所有的CSV文件，并将结果存储为新的CSV文件。
每个文件的内容将被转换为NumPy数组，然后每个数组被转换成一个Pandas DataFrame，并保存。
"""
# 扩展功能模块

def process_csv_file(file_path):
    """
    处理单个CSV文件

    参数：
    file_path: 要处理的CSV文件路径
    """
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
# NOTE: 重要实现细节
        # 将Pandas DataFrame转换为NumPy数组
        numpy_array = df.to_numpy()
        # 处理数组（例如：简单的数据清洗或转换）
        # 在这里可以添加更多的数据处理逻辑
        # 将处理后的NumPy数组转换回Pandas DataFrame
        processed_df = pd.DataFrame(numpy_array, columns=df.columns)
        # 保存处理后的DataFrame为新的CSV文件
        processed_df.to_csv(file_path.replace('.csv', '_processed.csv'), index=False)
        print(f'文件 {file_path} 已成功处理。')
    except Exception as e:
        print(f'处理文件 {file_path} 时发生错误：{e}')


def batch_process_csv_files(directory):
    """
    批量处理指定目录下的所有CSV文件

    参数：
    directory: 包含CSV文件的目录路径
    """
    try:
# 添加错误处理
        # 获取目录下所有的CSV文件路径
        csv_files = glob(os.path.join(directory, '*.csv'))
        # 遍历文件并处理
# 增强安全性
        for file_path in csv_files:
            process_csv_file(file_path)
# 改进用户体验
    except Exception as e:
        print(f'批量处理CSV文件时发生错误：{e}')

# 主函数，用于运行程序
if __name__ == '__main__':
# TODO: 优化性能
    directory_path = input('请输入包含CSV文件的目录路径：')
    batch_process_csv_files(directory_path)