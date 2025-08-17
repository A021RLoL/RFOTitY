# 代码生成时间: 2025-08-18 04:09:16
import numpy as np
import requests
from urllib.parse import urlparse
import json

"""URL链接有效性验证程序。

功能：验证URL是否有效，包括协议、域名等。
注：该程序使用requests库进行网络请求，需要安装requests库。"""

class URLValidator:
    def __init__(self):
        """初始化URLValidator类。"""
        pass

    def is_valid_url(self, url):
        """检查URL是否有效。

        Args:
            url (str): 待验证的URL。

        Returns:
            bool: URL是否有效。
        """
        try:
            result = urlparse(url)
            if all([result.scheme, result.netloc]):
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_url(self, url):
        """验证URL的有效性，并执行HTTP请求。

        Args:
            url (str): 待验证的URL。

        Returns:
            dict: 包含URL有效性结果和HTTP响应状态码的字典。
        """
        if self.is_valid_url(url):
            try:
                response = requests.head(url, allow_redirects=True, timeout=5)
                result = {
                    'is_valid': True,
                    'status_code': response.status_code
                }
                return result
            except requests.RequestException as e:
                result = {
                    'is_valid': True,
                    'error': str(e)
                }
                return result
        else:
            result = {
                'is_valid': False,
                'error': 'Invalid URL'
            }
            return result

# 示例用法
if __name__ == '__main__':
    url_validator = URLValidator()
    test_urls = [
        'http://www.example.com',
        'https://www.google.com',
        'ftp://example.com',
        'invalid_url'
    ]

    for url in test_urls:
        result = url_validator.validate_url(url)
        print(f'URL: {url}
Result: {json.dumps(result, indent=4)}
')
