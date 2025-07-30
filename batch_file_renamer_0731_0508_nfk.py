# 代码生成时间: 2025-07-31 05:08:50
import os
import re
from pathlib import Path

"""
A batch file renamer tool using Python and NumPy framework.
This script provides a simple way to rename multiple files in a directory
with a specific naming pattern.
"""

def rename_files(directory, pattern, replacement):
    """
    Rename files in a directory based on a given pattern and replacement.

    Parameters:
    directory (str): The directory containing the files to be renamed.
    pattern (str): The regular expression pattern to match in the filenames.
    replacement (str): The string to replace the matched pattern with.

    Returns:
    None
    """
    # Check if the directory exists
    if not Path(directory).is_dir():
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Compile the regular expression pattern
    regex_pattern = re.compile(pattern)

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the current item is a file
        if os.path.isfile(os.path.join(directory, filename)):
            # Apply the regex pattern to the filename
            new_filename = regex_pattern.sub(replacement, filename)
            # Construct the full path for the old and new filenames
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # Check if the new filename is different from the old one
            if new_filename != filename:
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                # No changes needed
                print(f"No changes needed for '{filename}'")

# Example usage
if __name__ == '__main__':
    # Define the directory containing the files
    directory = 'path/to/your/files'
    # Define the regex pattern to match in filenames
    pattern = r'[0-9]+'  # Example pattern to replace numbers with '_'
    # Define the replacement string
    replacement = '_'
    
    # Call the function with the specified parameters
    rename_files(directory, pattern, replacement)