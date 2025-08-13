# 代码生成时间: 2025-08-13 11:20:27
import requests
from urllib.parse import urlparse

"""
URL链接有效性验证程序

功能：
- 使用requests库验证URL链接是否有效
- 检查URL是否能够成功访问（返回状态码200）
- 解析URL并检查协议、域名等是否合法
"""

def is_valid_url(url: str) -> bool:
    """
    验证URL链接是否有效

    参数：
    url (str): 待验证的URL字符串

    返回：
    bool: URL是否有效
    """
    try:
        # 解析URL
        result = urlparse(url)
        # 检查协议、域名等是否合法
        if all([result.scheme, result.netloc]):
            # 发送HTTP请求，检查URL是否能够成功访问
            response = requests.head(url, allow_redirects=True)
            # 检查返回状态码是否为200
            return response.status_code == 200
        else:
            print(f"无效的URL：{url}，协议或域名不合法")
            return False
    except Exception as e:
        print(f"URL验证失败：{e}")
        return False


def main():
    """
    main函数
    """
    # 测试URL
    test_urls = [
        "https://www.google.com",
        "https://www.google.com/abc",
        "https://www.google.com:81",
        "invalid_url"
    ]
    for url in test_urls:
        print(f"验证URL：{url} - {is_valid_url(url)}")

if __name__ == '__main__':
    main()