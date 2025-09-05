# 代码生成时间: 2025-09-05 13:39:32
import json
import numpy as np


# JSON数据格式转换器类
class JsonConverter:
    def __init__(self):
        '''
        初始化JSON数据格式转换器
        '''
        pass

    def load_json(self, json_str):
        '''
        加载JSON字符串并返回JSON对象

        参数：
            json_str (str)：JSON字符串

        返回：
            dict：JSON对象
        '''
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f'无效的JSON字符串：{e}')

    def convert_to_numpy(self, json_obj):
        '''
        将JSON对象转换为NumPy数组

        参数：
            json_obj (dict)：JSON对象

        返回：
            np.ndarray：NumPy数组
        '''
        try:
            return np.array(json_obj)
        except TypeError as e:
            raise ValueError(f'无法转换为NumPy数组：{e}')

    def convert_to_json(self, np_array):
        '''
        将NumPy数组转换为JSON对象

        参数：
            np_array (np.ndarray)：NumPy数组

        返回：
            dict：JSON对象
        '''
        try:
            return np_array.tolist()
        except Exception as e:
            raise ValueError(f'无法转换为JSON对象：{e}')

    def save_json(self, json_obj, file_path):
        '''
        将JSON对象保存到文件

        参数：
            json_obj (dict)：JSON对象
            file_path (str)：文件路径

        返回：
            None
        '''
        try:
            with open(file_path, 'w') as f:
                json.dump(json_obj, f, indent=4)
        except IOError as e:
            raise ValueError(f'无法保存到文件：{e}')


# 示例用法
if __name__ == '__main__':
    # 创建JSON数据格式转换器实例
    converter = JsonConverter()

    # 加载JSON字符串
    json_str = '{
        "array" : [1, 2, 3, 4, 5]
    }
    json_obj = converter.load_json(json_str)

    # 将JSON对象转换为NumPy数组
    np_array = converter.convert_to_numpy(json_obj)
    print(f'NumPy数组：{np_array}')

    # 将NumPy数组转换为JSON对象
    new_json_obj = converter.convert_to_json(np_array)
    print(f'新的JSON对象：{new_json_obj}')

    # 将JSON对象保存到文件
    file_path = 'output.json'
    converter.save_json(new_json_obj, file_path)
    print(f'JSON对象已保存到文件：{file_path}')