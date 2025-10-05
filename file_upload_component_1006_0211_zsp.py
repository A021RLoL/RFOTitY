# 代码生成时间: 2025-10-06 02:11:21
import os
from flask import Flask, request, jsonify
import numpy as np

# 创建 Flask 应用
app = Flask(__name__)

# 定义允许上传文件的最大字节数
MAX_FILE_SIZE = 1024 * 1024 * 10  # 10 MB

# 定义文件保存的目录
UPLOAD_FOLDER = 'uploaded_files'

# 确保上传目录存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 定义文件上传的路由
@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查是否有文件在请求中
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    # 如果没有选择文件，浏览器也会提交一个空的部分，无需保存
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 检查文件大小
    if file.content_length > MAX_FILE_SIZE:
        return jsonify({'error': 'File size exceeds limit'}), 413

    # 检查文件扩展名
    if not file_allowed(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    # 保存文件
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # 返回成功消息
    return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200

# 检查文件扩展名是否允许
def file_allowed(filename):
    allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

# 确保文件名安全，避免路径遍历攻击
from werkzeug.utils import secure_filename

if __name__ == '__main__':
    app.run(debug=True)