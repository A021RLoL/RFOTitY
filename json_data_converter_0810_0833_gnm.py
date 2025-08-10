# 代码生成时间: 2025-08-10 08:33:51
import json
import numpy as np

"""
JSON数据格式转换器

这个程序可以将JSON格式的数据转换为numpy数组，或者将numpy数组转换为JSON格式。
它包括错误处理，确保代码的健壮性。
"""

class JSONDataConverter:
    def __init__(self):
        """初始化转换器"""
        pass

    def json_to_numpy(self, json_data):
        """
        将JSON数据转换为numpy数组

        参数:
            json_data (str): JSON格式的字符串数据

        返回:
            numpy.ndarray: 转换后的numpy数组

        异常:
            ValueError: 如果JSON数据无效
        """
        try:
            data = json.loads(json_data)
            return np.array(data)
        except json.JSONDecodeError as e:
            raise ValueError("无效的JSON数据") from e

    def numpy_to_json(self, numpy_array):
        """
        将numpy数组转换为JSON格式

        参数:
            numpy_array (numpy.ndarray): numpy数组

        返回:
            str: JSON格式的字符串数据

        异常:
            TypeError: 如果输入不是numpy数组
        """
        if not isinstance(numpy_array, np.ndarray):
            raise TypeError("输入必须是numpy数组")

        return json.dumps(numpy_array.tolist())

# 示例用法
def main():
    converter = JSONDataConverter()

    # 将JSON数据转换为numpy数组
    json_data = '[1, 2, 3, 4, 5]'
    numpy_array = converter.json_to_numpy(json_data)
    print("转换后的numpy数组:", numpy_array)

    # 将numpy数组转换为JSON数据
    numpy_array = np.array([1, 2, 3, 4, 5])
    json_data = converter.numpy_to_json(numpy_array)
    print("转换后的JSON数据:", json_data)

if __name__ == "__main__":
    main()