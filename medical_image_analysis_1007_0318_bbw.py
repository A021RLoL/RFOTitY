# 代码生成时间: 2025-10-07 03:18:27
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from skimage import exposure
from skimage import filters
from skimage import io
from scipy import ndimage

"""
Medical Image Analysis using Python and NumPy.
This program performs basic analysis on medical images, including loading,
displaying, and filtering.
"""

class MedicalImageAnalyzer:
    def __init__(self, image_path):
        """
        Initializes the MedicalImageAnalyzer with an image path.
        :param image_path: Path to the medical image file.
        """
# NOTE: 重要实现细节
        if not self._is_image_file(image_path):
            raise ValueError("Invalid image file.")
# NOTE: 重要实现细节
        self.image_path = image_path
        self.image = self._load_image(image_path)

    def _is_image_file(self, file_path):
        """
        Checks if the file is a valid image file based on extension.
        :param file_path: Path to the file.
# 改进用户体验
        :return: True if valid image file, False otherwise.
# TODO: 优化性能
        """
        return file_path.endswith(('.nii', '.nii.gz', '.png', '.jpg', '.jpeg'))
# FIXME: 处理边界情况

    def _load_image(self, image_path):
        """
        Loads the medical image using nibabel (for NIfTI files) or skimage (for other files).
        :param image_path: Path to the medical image file.
# 优化算法效率
        :return: The loaded image data.
        """
        try:
            if self._is_image_file(image_path):
                return nib.load(image_path).get_fdata()
            else:
                return io.imread(image_path)
        except Exception as e:
            raise ValueError("Failed to load image: " + str(e))
# NOTE: 重要实现细节

    def display_image(self):
        """
        Displays the loaded medical image using matplotlib.
        """
        try:
            plt.imshow(self.image, cmap='gray')
# 扩展功能模块
            plt.colorbar()
            plt.show()
        except Exception as e:
# 改进用户体验
            raise ValueError("Failed to display image: " + str(e))

    def apply_filter(self, filter_type):
        """
        Applies a specified filter to the medical image.
# 添加错误处理
        :param filter_type: Type of filter to apply (e.g., 'gaussian', 'median', 'laplacian').
        :return: Filtered image data.
# 增强安全性
        """
        if filter_type == 'gaussian':
            return ndimage.gaussian_filter(self.image, sigma=1)
        elif filter_type == 'median':
# 添加错误处理
            return filters.median(self.image)
        elif filter_type == 'laplacian':
# TODO: 优化性能
            return filters.laplacian(self.image)
        else:
            raise ValueError("Invalid filter type.")

    def adjust_contrast(self, clip_limit=0.01):
        """
        Adjusts the contrast of the medical image.
        :param clip_limit: Fraction of pixels to clip at the low and high end.
        :return: Contrast-adjusted image data.
        """
        return exposure.rescale_intensity(self.image, in_range=(clip_limit, 1 - clip_limit))

# Example usage
if __name__ == '__main__':
    image_path = 'example_image.nii'
    analyzer = MedicalImageAnalyzer(image_path)
    try:
        analyzer.display_image()
# 添加错误处理
        filtered_image = analyzer.apply_filter('gaussian')
        plt.imshow(filtered_image, cmap='gray')
        plt.colorbar()
        plt.show()
        contrast_adjusted_image = analyzer.adjust_contrast()
        plt.imshow(contrast_adjusted_image, cmap='gray')
# FIXME: 处理边界情况
        plt.colorbar()
        plt.show()
# NOTE: 重要实现细节
    except Exception as e:
        print("Error: ", str(e))