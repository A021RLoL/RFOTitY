# 代码生成时间: 2025-10-08 20:52:56
import requests
import numpy as np
from urllib.parse import urlparse

class URLValidator:
    """
    Class for validating the validity of a URL.
    It checks if the URL is well-formed and accessible via HTTP(S).
    """
    def __init__(self):
        """
        Initialize the URLValidator class.
        """
        self.session = requests.Session()  # Create a session for making HTTP requests
    
    def is_valid(self, url):
        """
        Check if the URL is valid and accessible.
        :param url: The URL to validate.
        :return: Tuple with a boolean indicating validity and an error message if applicable.
        """
        try:
            # Check if the URL is well-formed using urlparse
            result = urlparse(url)
            if all([result.scheme, result.netloc]):
                # Make a HEAD request to check if the URL is accessible
                response = self.session.head(url, timeout=5)
                if response.status_code == 200:  # OK status code
                    return True, ""
                else:  # Not OK status code
                    return False, f"HTTP error: {response.status_code}
"
            else:  # URL is not well-formed
                return False, "URL is not well-formed.
"        
        except requests.RequestException as e:  # Handle request exceptions
            return False, f"Request exception: {e}
"
    
    def validate(self, urls):
        """
        Validate a list of URLs.
        :param urls: List of URLs to validate.
        :return: A list of tuples, each containing the URL and its validity.
        """
        validation_results = []
        for url in urls:  # Loop through the list of URLs
            validity, error_message = self.is_valid(url)
            validation_results.append((url, validity, error_message))  # Append the result to the list
        return validation_results
    
# Example usage
if __name__ == '__main__':
    validator = URLValidator()
    urls_to_test = ['http://www.example.com', 'https://www.google.com', 'invalid-url']
    results = validator.validate(urls_to_test)
    for url, valid, message in results:  # Print the validation results
        print(f"URL: {url}
Valid: {valid}
Message: {message}
")