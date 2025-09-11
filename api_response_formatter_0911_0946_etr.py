# 代码生成时间: 2025-09-11 09:46:25
import json
import numpy as np

"""
API响应格式化工具

该工具用于将API响应数据格式化为JSON字符串。
支持自定义的数据结构和错误处理。
"""

class ApiResponseFormatter:
    def __init__(self, data, status_code, message):
        """
        初始化API响应格式化工具
        
        参数:
        data (object): API响应数据
        status_code (int): 状态码
        message (str): 消息
        """
        self.data = data
        self.status_code = status_code
        self.message = message

    def format_response(self):
        """
        格式化API响应数据
        
        返回值:
        str: 格式化后的JSON字符串
        """
        try:
            # 将数据转换为字典
            if isinstance(self.data, np.ndarray):
                data_dict = self.data.tolist()
            else:
                data_dict = self.data

            # 构建响应字典
            response = {
                "status_code": self.status_code,
                "message": self.message,
                "data": data_dict
            }

            # 将响应字典转换为JSON字符串
            return json.dumps(response, ensure_ascii=False)
        except Exception as e:
            # 处理格式化过程中的异常
            return json.dumps({
                "status_code": 500,
                "message": f"Error formatting response: {str(e)}",
                "data": {}
            }, ensure_ascii=False)

# 示例用法
if __name__ == "__main__":
    # 创建API响应格式化工具实例
    formatter = ApiResponseFormatter(np.array([1, 2, 3]), 200, "Success")

    # 格式化API响应数据
    response = formatter.format_response()
    print(response)