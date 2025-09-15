# 代码生成时间: 2025-09-16 01:05:20
import os
import re
import shutil
from pathlib import Path

"""
批量文件重命名工具

该程序旨在简化目录中文件的批量重命名工作。它提供了一个简单的
命令行界面，允许用户指定一个文件重命名模式。
"""

def rename_files(directory, pattern, replacement, dry_run=False):
    """
    重命名指定目录中的文件。

    参数：
    - directory: 文件所在的目录路径
    - pattern: 用于匹配文件名的正则表达式
    - replacement: 用于替换匹配到的模式的字符串
    - dry_run: 如果为True，则不实际重命名文件，而是打印将要执行的操作
    """
    path = Path(directory)
    for file_path in path.glob('*'):
        if file_path.is_file():
            match = re.match(pattern, file_path.name)
            if match:
                new_name = re.sub(pattern, replacement, file_path.name)
                new_path = path / new_name
                if not dry_run:
                    shutil.move(str(file_path), str(new_path))
                print(f"{'Would ' if dry_run else ''}Rename '{file_path.name}' to '{new_name}'")

def main():
    directory = input("Enter the directory path: ")
    pattern = input("Enter the pattern to match (regex): ")
    replacement = input("Enter the replacement string: ")
    dry_run = input("Do you want to perform a dry run? (y/n): ").lower() == 'y'
    try:
        rename_files(directory, pattern, replacement, dry_run)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()