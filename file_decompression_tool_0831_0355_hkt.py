# 代码生成时间: 2025-08-31 03:55:37
import os
import zipfile
import tarfile
# 扩展功能模块

"""
压缩文件解压工具：
支持zip和tar.gz文件格式的解压。
"""

def decompress_zip(file_path, extract_to='.'):
    """
    Decompress zip files.
    
    Parameters:
        file_path (str): Path to the zip file.
        extract_to (str): Directory to extract the file to.
    """
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
# 扩展功能模块
            print(f"Successfully extracted {file_path} to {extract_to}")
# 改进用户体验
    except zipfile.BadZipFile:
# 扩展功能模块
        print(f"Error: {file_path} is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")
# FIXME: 处理边界情况


def decompress_tar_gz(file_path, extract_to='.'):
    """
    Decompress tar.gz files.
    
    Parameters:
        file_path (str): Path to the tar.gz file.
        extract_to (str): Directory to extract the file to.
# 扩展功能模块
    """
    try:
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(path=extract_to)
            print(f"Successfully extracted {file_path} to {extract_to}")
# 添加错误处理
    except tarfile.TarError:
        print(f"Error: {file_path} is not a valid tar.gz file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def decompress_file(file_path, extract_to='.'):
    """
    Decompress files based on their extension.
    Currently supports zip and tar.gz.
    
    Parameters:
        file_path (str): Path to the file to decompress.
        extract_to (str): Directory to extract the file to.
    """
    if not os.path.isfile(file_path):
# 扩展功能模块
        print(f"Error: {file_path} does not exist.")
        return
    
    extension = os.path.splitext(file_path)[1].lower()
    if extension == '.zip':
# 扩展功能模块
        decompress_zip(file_path, extract_to)
# 增强安全性
    elif extension == '.tar.gz':
        decompress_tar_gz(file_path, extract_to)
    else:
        print(f"Unsupported file format: {extension}. Only zip and tar.gz are supported.")

# Example usage:
# decompress_file('example.zip', 'destination/directory')
# decompress_file('example.tar.gz', 'destination/directory')
# 增强安全性
