# 代码生成时间: 2025-09-01 07:01:58
import os
import numpy as np
from PIL import Image
import shutil

"""
Image Resizer - A program to batch resize images to a specified size.

Attributes:
    None

Methods:
    resize_images: Resizes all images in a given directory to a specified size.
"""

class ImageResizer:
    def __init__(self, source_dir, target_dir, output_size):
        """Initialize the ImageResizer with source, target directories and output size."""
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.output_size = output_size

    def resize_images(self):
        """Resizes all images in the source directory to the output size and saves them in the target directory."""
        # Check if source and target directories exist
        if not os.path.exists(self.source_dir):
            raise FileNotFoundError(f"The source directory {self.source_dir} does not exist.")
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

        # Loop through all files in the source directory
        for filename in os.listdir(self.source_dir):
            # Ignore directories, only process files
            if os.path.isfile(os.path.join(self.source_dir, filename)):
                try:
                    # Open the image file
                    with Image.open(os.path.join(self.source_dir, filename)) as img:
                        # Resize the image
                        img = img.resize(self.output_size, Image.ANTIALIAS)
                        # Save the resized image to the target directory
                        img.save(os.path.join(self.target_dir, filename))
                except IOError:
                    print(f"Error resizing {filename}. Skipping file.")

# Example usage:
if __name__ == '__main__':
    # Define the source and target directories
    source_dir = 'path_to_source_directory'
    target_dir = 'path_to_target_directory'
    # Define the output size as a tuple (width, height)
    output_size = (800, 600)

    # Create an instance of ImageResizer
    resizer = ImageResizer(source_dir, target_dir, output_size)
    # Resize images
    try:
        resizer.resize_images()
    except Exception as e:
        print(f'An error occurred: {e}')
