# 代码生成时间: 2025-08-05 20:46:58
import os
import re
from pathlib import Path


def rename_files(directory, pattern, replacement):
    '''
    批量重命名指定目录下的文件。
    
    参数:
    directory (str): 要重命名文件的目录路径。
    pattern (str): 正则表达式模式，用于匹配要替换的字符串。
    replacement (str): 替换匹配模式的字符串。
    '''
    # 确保目录路径存在
    if not os.path.isdir(directory):
        raise ValueError(f"The directory {directory} does not exist.")
    
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 构建文件的完整路径
        file_path = os.path.join(directory, filename)
        
        # 检查是否为文件
        if os.path.isfile(file_path):
            # 使用正则表达式重命名文件
            new_filename = re.sub(pattern, replacement, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # 检查新文件名是否已存在
            if os.path.exists(new_file_path):
                raise FileExistsError(f"The file {new_file_path} already exists.")
            
            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
        else:
            print(f"Skipping directory '{filename}'")


if __name__ == '__main__':
    # 示例用法
    directory = 'path/to/your/directory'
    pattern = r'old_pattern'  # 要替换的正则表达式模式
    replacement = 'new_pattern'  # 替换的新字符串
    
    try:
        rename_files(directory, pattern, replacement)
    except Exception as e:
        print(f"Error: {e}")