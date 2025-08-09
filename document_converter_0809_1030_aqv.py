# 代码生成时间: 2025-08-09 10:30:51
import numpy as np
import json
import os
from docx import Document

"""
Document Converter
Converts documents from .docx to .txt format using Python and Numpy.

Attributes:
    None

Methods:
    convert_docx_to_txt(docx_file_path, txt_file_path): Converts a .docx file to a .txt file.
"""

class DocumentConverter:
    """
    A class for converting documents.
    """

    @staticmethod
    def convert_docx_to_txt(docx_file_path, txt_file_path):
        """
        Converts a .docx file to a .txt file.

        Parameters:
            docx_file_path (str): The path to the .docx file.
            txt_file_path (str): The path to the output .txt file.

        Returns:
            bool: True if the conversion is successful, False otherwise.
        """
        try:
            # Check if the input file exists
            if not os.path.exists(docx_file_path):
                print(f"Error: The file {docx_file_path} does not exist.")
                return False

            # Load the .docx file
            document = Document(docx_file_path)

            # Extract text from the document
            text = []
            for para in document.paragraphs:
                text.append(para.text)

            # Save the text to a .txt file
            with open(txt_file_path, 'w') as file:
                file.write('
'.join(text))

            print(f"Document converted successfully: {txt_file_path}")
            return True
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

# Example usage
if __name__ == '__main__':
    docx_file_path = 'example.docx'
    txt_file_path = 'example.txt'
    DocumentConverter.convert_docx_to_txt(docx_file_path, txt_file_path)