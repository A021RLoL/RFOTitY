# 代码生成时间: 2025-09-11 05:13:58
import numpy as np
import re
from collections import Counter
import os

"""
Text File Analyzer

This module analyzes the content of a given text file and provides
statistics such as word frequency, common phrases, and character count.
"""

class TextFileAnalyzer:
    def __init__(self, file_path):
        """
        Initialize the TextFileAnalyzer with the path to the text file.
        Args:
            file_path (str): The path to the text file to analyze.
        """
        self.file_path = file_path
        self.content = ""
        
    def read_file(self):
        """
        Read the content of the text file.
        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If an I/O error occurs.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            raise
        except IOError as e:
            print(f"IO error: {e}")
            raise
        
    def word_frequency(self):
        """
        Calculate the frequency of each word in the text file content.
        Returns:
            Counter: A dictionary-like object with word counts.
        """
        words = re.findall(r'\b\w+\b', self.content.lower())
        return Counter(words)
    
    def character_count(self):
        """
        Calculate the count of each character in the text file content.
        Returns:
            Counter: A dictionary-like object with character counts.
        """
        return Counter(self.content)
    
    def common_phrases(self, phrase_length=2):
        """
        Identify common phrases of a given length in the text file content.
        Args:
            phrase_length (int): The length of the phrases to identify.
        Returns:
            list: A list of common phrases.
        """
        if phrase_length < 2:
            return []
        words = re.findall(r'\b\w+\b', self.content.lower())
        phrases = [' '.join(words[i:i+phrase_length]) for i in range(len(words) - phrase_length + 1)]
        phrase_counts = Counter(phrases)
        return [phrase for phrase, count in phrase_counts.items() if count > 1]

    def analyze(self, phrase_length=2):
        """
        Analyze the text file content and print the results.
        Args:
            phrase_length (int): The length of the phrases to identify.
        """
        self.read_file()
        word_freq = self.word_frequency()
        char_count = self.character_count()
        common_phrases = self.common_phrases(phrase_length)
        print("Word Frequency:")
        for word, count in word_freq.items():
            print(f"{word}: {count}")
        print("Character Count:")
        for char, count in char_count.items():
            print(f"{char}: {count}")
        print("Common Phrases:")
        for phrase in common_phrases:
            print(phrase)

if __name__ == '__main__':
    analyzer = TextFileAnalyzer('example.txt')
    analyzer.analyze()
