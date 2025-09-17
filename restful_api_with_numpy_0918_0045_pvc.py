# 代码生成时间: 2025-09-18 00:45:47
import numpy as np
from flask import Flask, jsonify, request

# 初始化Flask应用
app = Flask(__name__)

# 定义一个示例数据集
data = np.array([[1, 2], [3, 4], [5, 6]])

# API端点 /get_data，返回JSON格式的numpy数组数据
@app.route('/get_data', methods=['GET'])
def get_data():
    # 将numpy数组转换为列表
    result = data.tolist()
    # 返回JSON响应
    return jsonify(result)

# API端点 /add_data，接受POST请求，添加数据到numpy数组
@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        # 解析JSON请求数据
        json_data = request.get_json()
        # 将JSON数据转换为numpy数组
        new_data = np.array(json_data)
        # 将新数据添加到原始数据集
        data = np.vstack((data, new_data))
        # 返回添加后的数据集
        result = data.tolist()
        return jsonify(result), 201
    except Exception as e:
        # 返回错误信息
        return jsonify({'error': str(e)}), 400

# 运行Flask应用
if __name__ == '__main__':
    app.run(debug=True)
