# 代码生成时间: 2025-08-26 02:41:22
import numpy as np
import socket
import requests

"""
Network Connection Checker using Python and Numpy.
This program checks the connection status of a given URL.
"""

def check_connection(host, port=80):
    """
    Checks if the server at the specified host is reachable.
    
    Parameters:
        host (str): The URL to check.
        port (int): The port number to check. Defaults to 80.
    
    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the socket
        sock.settimeout(10)
        # Try to connect to the host
        result = sock.connect_ex((host, port))
        # Close the socket
        sock.close()
        # If the result is 0, the connection is successful
        return result == 0
    except socket.error as err:
        # Print the error message
        print(f"Socket error: {err}")
        return False

def check_url_connection(url):
    """
    Checks if the specified URL is reachable.
    
    Parameters:
        url (str): The URL to check.
    
    Returns:
        bool: True if the URL is reachable, False otherwise.
    """
    try:
        # Use requests to try to get the URL
        response = requests.get(url)
        # If the response status code is 200, the URL is reachable
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        # Print the error message
        print(f"Request error: {e}")
        return False

if __name__ == "__main__":
    # Define the URL to check
    url_to_check = "http://www.google.com"
    # Check the connection status of the URL
    if check_url_connection(url_to_check):
        print(f"The URL {url_to_check} is reachable.")
    else:
        print(f"The URL {url_to_check} is not reachable.")