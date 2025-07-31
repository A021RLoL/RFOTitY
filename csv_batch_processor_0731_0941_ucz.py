# 代码生成时间: 2025-07-31 09:41:20
import numpy as np
import pandas as pd
import os
from glob import glob

"""
CSV文件批量处理器
该程序用于批量处理CSV文件，例如读取、转换和保存。

功能：
- 读取指定目录下的所有CSV文件
- 可选地应用一些转换（例如：数值列标准化）
- 将处理后的CSV文件保存到指定目录
"""

def process_csv_file(file_path, output_dir, transformation=None):
    """
    处理单个CSV文件

    :param file_path: CSV文件路径
    :param output_dir: 输出目录
    :param transformation: 可选的转换函数
    :return: None
    """
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
        
        # 应用转换函数
        if transformation:
            df = transformation(df)
        
        # 构建输出文件路径
        output_file_path = os.path.join(output_dir, os.path.basename(file_path))
        
        # 保存处理后的CSV文件
        df.to_csv(output_file_path, index=False)
        print(f"Processed and saved: {output_file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def batch_process_csv_files(directory, output_dir, transformation=None):
    """
    批量处理指定目录下的所有CSV文件

    :param directory: 包含CSV文件的目录
    :param output_dir: 输出目录
    :param transformation: 可选的转换函数
    :return: None
    """
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取目录下所有CSV文件路径
    csv_file_paths = glob(os.path.join(directory, "*.csv"))
    
    # 批量处理CSV文件
    for file_path in csv_file_paths:
        process_csv_file(file_path, output_dir, transformation)

# 示例：标准化数值列
def standardize_numerical_columns(df):
    """
    标准化数值列

    :param df: pandas DataFrame
    :return: 标准化后的DataFrame
    """
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    df[numerical_cols] = (df[numerical_cols] - df[numerical_cols].mean()) / df[numerical_cols].std()
    return df

# 主函数
if __name__ == "__main__":
    # 指定CSV文件目录和输出目录
    csv_directory = "./csv_files"
    output_directory = "./processed_files"
    
    # 批量处理CSV文件
    batch_process_csv_files(csv_directory, output_directory, standardize_numerical_columns)