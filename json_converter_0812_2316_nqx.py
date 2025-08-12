# 代码生成时间: 2025-08-12 23:16:55
import json
import numpy as np

"""
JSON数据格式转换器

该程序用于将JSON数据转换为NumPy数组，并支持反向转换。
"""

class JsonConverter:
    """
    JsonConverter类提供JSON数据与NumPy数组之间的转换功能。
    """
    def __init__(self):
        """
        初始化JsonConverter实例。
        """
        pass

    def json_to_numpy(self, json_data):
        """
        将JSON数据转换为NumPy数组。
        
        参数:
            json_data (str): JSON格式的字符串。
        
        返回:
            np.ndarray: NumPy数组。
        
        异常:
            json.JSONDecodeError: 如果json_data不是有效的JSON格式。
        """
        try:
            data = json.loads(json_data)
            if isinstance(data, list):
                return np.array(data)
            else:
                raise ValueError("JSON数据必须是列表格式。")
        except json.JSONDecodeError as e:
            raise ValueError("无效的JSON格式。") from e
        except ValueError as e:
            raise ValueError(e)

    def numpy_to_json(self, numpy_array):
        """
        将NumPy数组转换为JSON数据。
        
        参数:
            numpy_array (np.ndarray): NumPy数组。
        
        返回:
            str: JSON格式的字符串。
        
        异常:
            TypeError: 如果numpy_array不是NumPy数组。
        """
        try:
            if not isinstance(numpy_array, np.ndarray):
                raise TypeError("输入必须是NumPy数组。")
            return json.dumps(numpy_array.tolist())
        except TypeError as e:
            raise TypeError(e)

# 示例用法
if __name__ == '__main__':
    converter = JsonConverter()
    try:
        # 将JSON数据转换为NumPy数组
        json_data = '[1, 2, 3, 4, 5]'
        numpy_array = converter.json_to_numpy(json_data)
        print("NumPy数组:", numpy_array)

        # 将NumPy数组转换为JSON数据
        numpy_array = np.array([6, 7, 8, 9, 10])
        json_data = converter.numpy_to_json(numpy_array)
        print("JSON数据:", json_data)
    except Exception as e:
        print("错误:", str(e))