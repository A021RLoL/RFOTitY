# 代码生成时间: 2025-10-03 20:51:52
import os
import zipfile
import tarfile
import shutil

"""
A utility program for decompressing files using Python and NumPy."""

class Decompressor:
    """
    A class for decompressing compressed files.
    """
    def __init__(self, archive_path, output_folder):
        """Initialize the Decompressor with the path of the archive and destination folder."""
        self.archive_path = archive_path
        self.output_folder = output_folder

    def decompress_zip(self):
        """Decompress a ZIP file."""
        try:
            # Check if the file is a ZIP file
            if not self.archive_path.endswith('.zip'):
                raise ValueError("File is not a ZIP archive.")
            
            # Ensure the output directory exists
            os.makedirs(self.output_folder, exist_ok=True)
            
            # Decompress the ZIP file
            with zipfile.ZipFile(self.archive_path, 'r') as zip_ref:
                zip_ref.extractall(self.output_folder)
            print(f"Decompressed {self.archive_path} into {self.output_folder}")
        except zipfile.BadZipFile:
            print("Error: The file is not a ZIP archive or it is corrupted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def decompress_tar(self):
        """Decompress a TAR file."""
        try:
            # Check if the file is a TAR file
            if not self.archive_path.endswith(('.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2')):
                raise ValueError("File is not a TAR archive.")
                
            # Ensure the output directory exists
            os.makedirs(self.output_folder, exist_ok=True)
            
            # Handle different types of TAR files
            if self.archive_path.endswith(('.tar.gz', '.tgz')):
                mode = 'r:gz'
            elif self.archive_path.endswith(('.tar.bz2', '.tbz2')):
                mode = 'r:bz2'
            else:
                mode = 'r'
            
            # Decompress the TAR file
            with tarfile.open(self.archive_path, mode) as tar_ref:
                tar_ref.extractall(self.output_folder)
            print(f"Decompressed {self.archive_path} into {self.output_folder}")
        except tarfile.TarError:
            print("Error: The file is not a TAR archive or it is corrupted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def decompress(self):
        """Determine the type of compression and decompress."""
        if self.archive_path.endswith('.zip'):
            self.decompress_zip()
        elif self.archive_path.endswith(('.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2')):
            self.decompress_tar()
        else:
            print("Unsupported file format.")

# Example usage
if __name__ == '__main__':
    archive_path = 'example.zip'  # Replace with the path to your archive file
    output_folder = 'decompressed'  # Replace with the desired output folder
    decompressor = Decompressor(archive_path, output_folder)
    decompressor.decompress()