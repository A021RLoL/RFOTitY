# 代码生成时间: 2025-08-11 18:31:46
import os
import shutil
from datetime import datetime
import numpy as np

"""
Folder Organizer

This script is designed to organize files within a specified directory.
It moves files into respective folders based on the file extension.
"""

class FolderOrganizer:
    def __init__(self, source_dir, target_dir):
        """
        Initialize the folder organizer with source and target directories.
        
        :param source_dir: The directory to organize files from.
        :param target_dir: The directory to organize files to.
        """
        self.source_dir = source_dir
        self.target_dir = target_dir
        
    def create_folder(self, folder_name):
        """
        Creates a new folder if it doesn't exist.
        
        :param folder_name: The name of the folder to create.
        """
        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
        except OSError as e:
            print(f"Error creating folder {folder_name}: {e}")

    def organize_files(self):
        """
        Organize files into folders based on their extensions.
        """
        try:
            for filename in os.listdir(self.source_dir):
                file_path = os.path.join(self.source_dir, filename)
                if os.path.isfile(file_path):
                    self.move_file_to_folder(file_path)
        except Exception as e:
            print(f"An error occurred: {e}")

    def move_file_to_folder(self, file_path):
        """
        Moves a file to a folder based on its extension.
        
        :param file_path: The path to the file to be moved.
        """
        extension = os.path.splitext(file_path)[1]
        if extension:
            folder_name = os.path.join(self.target_dir, extension)
            self.create_folder(folder_name)
            new_path = os.path.join(folder_name, os.path.basename(file_path))
            shutil.move(file_path, new_path)
            print(f"Moved: {file_path} to {new_path}")
        else:
            print(f"No extension found for file {file_path}")

    def run(self):
        "