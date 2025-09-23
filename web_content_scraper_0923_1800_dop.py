# 代码生成时间: 2025-09-23 18:00:37
import requests
from bs4 import BeautifulSoup
import numpy as np

class WebContentScraper:
    """
    A simple web content scraper using Python and NumPy.
    """

    def __init__(self, url):
        """
        Initializes the scraper with a URL to scrape content from.
        :param url: The URL of the webpage to scrape.
        """
        self.url = url
        self.session = requests.Session()

    def fetch_content(self):
        """
        Fetches the content of the webpage.
        :returns: The content of the webpage as a BeautifulSoup object.
        :raises: requests.RequestException if the request fails.
        """
        try:
            response = self.session.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"An error occurred while fetching content: {e}")
            return None

    def extract_text(self, content):
        """
        Extracts text from the BeautifulSoup object.
        :param content: The BeautifulSoup object to extract text from.
        :returns: A NumPy array containing the text.
        """
        if content is None:
            return np.array([])

        text = content.get_text(separator=' ')
        return np.array([*text.split()])

# Example usage:
if __name__ == '__main__':
    url = "http://example.com"
    scraper = WebContentScraper(url)
    content = scraper.fetch_content()
    if content is not None:
        text_array = scraper.extract_text(content)
        print(text_array)