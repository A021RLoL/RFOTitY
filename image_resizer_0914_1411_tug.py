# 代码生成时间: 2025-09-14 14:11:43
import numpy as np
from PIL import Image
import os
import sys

"""
Image Resizer

This program is designed to batch resize images to a specified size.
It uses the PIL library for image manipulation and NumPy for numerical operations.
"""

class ImageResizer:
    def __init__(self, input_folder, output_folder, target_size):
        """Initialize the ImageResizer with input and output folders and target size."""
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.target_size = target_size

    def resize_images(self):
        "