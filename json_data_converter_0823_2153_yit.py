# 代码生成时间: 2025-08-23 21:53:45
import json
import numpy as np

"""
JSON数据格式转换器

功能：将JSON格式的数据转换为NumPy数组格式
"""


def json_to_numpy(json_data):
    """
    将JSON格式的数据转换为NumPy数组格式

    参数：
    json_data (str): JSON格式的字符串数据

    返回：
    numpy.ndarray: NumPy数组格式的数据

    异常：
    ValueError: JSON数据格式不正确
    """
    try:
        # 尝试将JSON数据解析为Python字典
        data_dict = json.loads(json_data)
    except json.JSONDecodeError as e:
        # 如果JSON解析失败，则抛出ValueError异常
        raise ValueError("JSON数据格式不正确：" + str(e))

    # 将Python字典转换为NumPy数组
    numpy_array = np.array(data_dict)
    return numpy_array


def main():
    """主函数"""
    # 示例JSON数据
    json_data = "{"data":[1,2,3,4,5]}"

    try:
        # 将JSON数据转换为NumPy数组
        numpy_array = json_to_numpy(json_data)
        print("NumPy数组格式的数据：")
        print(numpy_array)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()