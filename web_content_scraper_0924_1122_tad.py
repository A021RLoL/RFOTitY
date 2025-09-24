# 代码生成时间: 2025-09-24 11:22:24
import requests
from bs4 import BeautifulSoup
import numpy as np

class WebContentScraper:
    """
    A simple web content scraper using Python and NumPy.
    """

    def __init__(self, url):
        """
        Initialize the scraper with a URL.
        :param url: The URL of the webpage to scrape.
        """
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})

    def fetch_content(self):
        """
        Fetch the webpage content.
        :raises Exception: If the webpage cannot be fetched.
        :return: The fetched content of the webpage.
        """
        try:
            response = self.session.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch webpage: {e}")

    def parse_content(self, content):
        """
        Parse the fetched content using BeautifulSoup.
        :param content: The HTML content of the webpage.
        :return: The parsed content.
        """
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def extract_data(self, soup, data_type, selector):
        """
        Extract specific data from the parsed content.
        :param soup: The parsed soup object.
        :param data_type: The type of data to extract (e.g., 'text', 'href').
        :param selector: The CSS selector for the data.
        :return: A NumPy array of extracted data.
        """
        elements = soup.select(selector)
        if data_type == 'text':
            data = np.array([element.get_text() for element in elements])
        elif data_type == 'href':
            data = np.array([element.get('href') for element in elements])
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
        return data

    def scrape(self, data_type, selector):
        """
        Scrape the webpage and extract the specified data.
        :param data_type: The type of data to extract (e.g., 'text', 'href').
        :param selector: The CSS selector for the data.
        :return: A NumPy array of extracted data.
        """
        content = self.fetch_content()
        soup = self.parse_content(content)
        return self.extract_data(soup, data_type, selector)

# Example usage:
if __name__ == '__main__':
    scraper = WebContentScraper('https://example.com')
    try:
        text_data = scraper.scrape('text', 'p')
        print(text_data)
    except Exception as e:
        print(f"An error occurred: {e}")