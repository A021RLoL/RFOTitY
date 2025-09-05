# 代码生成时间: 2025-09-06 07:08:34
import numpy as np
import matplotlib.pyplot as plt
import os

"""
Text File Analyzer using Python and NumPy.

This program analyzes the content of a text file, calculating basic statistics
such as the number of words, characters, and unique characters. Additionally, it
provides a frequency distribution of the characters using matplotlib."""


def analyze_text_file(file_path):
    """Analyze the content of the text file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return analyze_text_content(content)


def analyze_text_content(text):
    """Analyze the content of the text."""
    words = text.split()
    unique_chars = set(text)
    unique_words = set(words)
    
    num_words = len(words)
    num_chars = len(text)
    num_unique_chars = len(unique_chars)
    num_unique_words = len(unique_words)
    
    # Calculate character frequency
    char_frequency = {char: text.count(char) for char in unique_chars}
    sorted_char_frequency = dict(sorted(char_frequency.items(), key=lambda item: item[1], reverse=True))
    
    return {
        'num_words': num_words,
        'num_chars': num_chars,
        'num_unique_chars': num_unique_chars,
        'num_unique_words': num_unique_words,
        'char_frequency': sorted_char_frequency
    }


def plot_char_frequency(char_frequency):
    """Plot the character frequency distribution using matplotlib."""
    plt.figure(figsize=(10, 6))
    plt.bar(char_frequency.keys(), char_frequency.values())
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.title('Character Frequency Distribution')
    plt.show()


def main():
    # Example usage
    file_path = 'example.txt'
    try:
        analysis_results = analyze_text_file(file_path)
        print("Analysis Results:")
        for key, value in analysis_results.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        # Plot character frequency
        plot_char_frequency(analysis_results['char_frequency'])
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
