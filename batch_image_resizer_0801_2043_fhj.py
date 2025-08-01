# 代码生成时间: 2025-08-01 20:43:32
import os
import sys
from PIL import Image
import numpy as np

"""
Batch Image Resizer

This script resizes multiple images to a specified size.
It handles errors and is designed to be easily maintainable and extendable.
"""

# Function to resize a single image
def resize_image(image_path, output_path, size):
    """Resizes an image to the specified size.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to the resized image.
        size (tuple): Desired size of the output image as (width, height).

    Returns:
        None
    """
    try:
        with Image.open(image_path) as img:
            img = img.resize(size, Image.ANTIALIAS)
            img.save(output_path)
            print(f"Image resized successfully: {output_path}")
    except IOError:
        print(f"Error: Unable to open or save image file {image_path}")

# Function to resize multiple images
def resize_images(image_folder, output_folder, size):
    """Resizes multiple images in a folder to the specified size.

    Args:
        image_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder where resized images will be saved.
        size (tuple): Desired size of the output images as (width, height).

    Returns:
        None
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(image_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(image_path, output_path, size)
        else:
            print(f"Skipping non-image file: {filename}")

# Main function to run the batch image resizer
def main():
    if len(sys.argv) != 4:
        print("Usage: python batch_image_resizer.py <image_folder> <output_folder> <width>x<height>")
        sys.exit(1)

    image_folder = sys.argv[1]
    output_folder = sys.argv[2]
    size_str = sys.argv[3]

    try:
        size = tuple(map(int, size_str.split('x')))
    except ValueError:
        print("Error: Invalid size format. Use <width>x<height>")
        sys.exit(1)

    resize_images(image_folder, output_folder, size)

if __name__ == '__main__':
    main()