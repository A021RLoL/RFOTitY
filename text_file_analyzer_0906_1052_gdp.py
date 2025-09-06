# 代码生成时间: 2025-09-06 10:52:05
import numpy as np

"""
Text File Analyzer using Python and NumPy.
This program reads a text file and provides basic analysis such as word frequency.

Attributes:
    None

Methods:
    analyze_text_file(file_path): Analyzes the text file and returns word frequency.
"""

def analyze_text_file(file_path):
    """
    Analyzes the text file and returns word frequency.

    Args:
        file_path (str): Path to the text file to be analyzed.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    try:
        # Attempt to open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Convert text to lowercase to ensure uniformity
            text = text.lower()
            # Use NumPy to count the frequency of each word
            words = text.split()
            word_counts = np.array(words)
            unique_words, counts = np.unique(word_counts, return_counts=True)
            # Create a dictionary with words and their frequencies
            word_freq = dict(zip(unique_words, counts))
            return word_freq
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == '__main__':
    file_path = 'example.txt'  # Replace with your actual file path
    word_frequencies = analyze_text_file(file_path)
    if word_frequencies:
        print("Word Frequencies:")
        for word, freq in word_frequencies.items():
            print(f"{word}: {freq}")
    else:
        print("No valid data found.")