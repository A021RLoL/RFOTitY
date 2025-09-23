# 代码生成时间: 2025-09-24 00:43:43
import numpy as np
import zipfile
import tarfile
import os

"""
File Decompression Tool
========================

This tool is designed to decompress files from various formats such as .zip and .tar.gz.
"""

class DecompressionTool:
    """
    This class provides functionality to decompress different types of files.
    """
    def __init__(self, source_path):
        """
        Initializes the DecompressionTool with the path to the source file.
        :param source_path: The path to the source file to be decompressed.
        """
        self.source_path = source_path

    def decompress_zip(self, destination_path):
        """
        Decompresses a .zip file to a specified destination.
        :param destination_path: The directory to decompress the zip file into.
        """
        try:
            with zipfile.ZipFile(self.source_path, 'r') as zip_ref:
                zip_ref.extractall(destination_path)
                print(f'Decompressed {self.source_path} to {destination_path}')
        except zipfile.BadZipFile:
            print(f'Error: {self.source_path} is not a zip file or is corrupted.')
        except Exception as e:
            print(f'An error occurred: {e}')

    def decompress_tar_gz(self, destination_path):
        """
        Decompresses a .tar.gz file to a specified destination.
        :param destination_path: The directory to decompress the tar.gz file into.
        """
        try:
            with tarfile.open(self.source_path, 'r:gz') as tar_ref:
                tar_ref.extractall(destination_path)
                print(f'Decompressed {self.source_path} to {destination_path}')
        except tarfile.TarError:
            print(f'Error: {self.source_path} is not a .tar.gz file or is corrupted.')
        except Exception as e:
            print(f'An error occurred: {e}')

    def decompress_file(self, destination_path):
        """
        Decompresses the source file to the specified destination based on its extension.
        :param destination_path: The directory to decompress the file into.
        """
        file_extension = os.path.splitext(self.source_path)[1].lower()
        if file_extension == '.zip':
            self.decompress_zip(destination_path)
        elif file_extension == '.tar.gz':
            self.decompress_tar_gz(destination_path)
        else:
            print(f'Unsupported file extension: {file_extension}')

# Example usage:
if __name__ == '__main__':
    source_file_path = 'path_to_your_file.zip'  # Change this to your file path
    destination_directory = 'decompressed_folder'  # Change this to your desired destination
    
    decompressor = DecompressionTool(source_file_path)
    decompressor.decompress_file(destination_directory)