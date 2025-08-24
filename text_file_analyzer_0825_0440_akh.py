# 代码生成时间: 2025-08-25 04:40:49
import numpy as np
import os

"""
Text File Analyzer

This program analyzes the contents of a text file and
provides various statistics such as word frequencies,
character counts, and line statistics.

Attributes:
    - None

Methods:
    - analyze_text_file(file_path): Analyzes the contents of a text file.

"""

def analyze_text_file(file_path):
    """
    Analyzes the contents of a text file.

    Args:
        file_path (str): The path to the text file to analyze.

    Returns:
        dict: A dictionary containing the analysis results.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        raise IOError(f"Failed to read the file {file_path}: {e}")

    # Calculate word frequencies
    word_frequencies = {}
    words = text.split()
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Calculate character counts
    character_counts = {}
    for char in text:
        character_counts[char] = character_counts.get(char, 0) + 1

    # Calculate line statistics
    lines = text.splitlines()
    line_stats = {
        'total_lines': len(lines),
        'average_line_length': np.mean([len(line) for line in lines])
    }

    return {
        'word_frequencies': word_frequencies,
        'character_counts': character_counts,
        'line_stats': line_stats
    }

# Example usage
if __name__ == '__main__':
    file_path = 'example.txt'
    try:
        analysis_results = analyze_text_file(file_path)
        print('Analysis Results:')
        print(analysis_results)
    except Exception as e:
        print(f'Error: {e}')