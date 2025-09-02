# 代码生成时间: 2025-09-02 14:18:08
import os
import shutil
import hashlib
import numpy as np
from datetime import datetime
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BackupSyncTool:
    """文件备份和同步工具"""

    def __init__(self, source_dir, backup_dir):
        """初始化工具，设置源目录和备份目录"""
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.backup_files = {}
        self.last_backup_time = None

    def _hash_file(self, file_path):
        """计算文件的哈希值"""
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hasher.update(chunk)
        return hasher.hexdigest()

    def _compare_files(self, file_path1, file_path2):
        """比较两个文件是否相同"""
        return self._hash_file(file_path1) == self._hash_file(file_path2)

    def _sync_files(self):
        """同步文件：将源目录的文件同步到备份目录"""
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_file_path, self.source_dir)
                backup_file_path = os.path.join(self.backup_dir, relative_path)

                try:
                    # 创建备份目录
                    os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)
                    # 检查文件是否存在且是否相同
                    if not os.path.exists(backup_file_path) or \
                       not self._compare_files(source_file_path, backup_file_path):
                        shutil.copy2(source_file_path, backup_file_path)
                        logging.info(f'文件已同步：{source_file_path} -> {backup_file_path}')
                except Exception as e:
                    logging.error(f'同步文件出错：{source_file_path} -> {backup_file_path}')
                    logging.error(str(e))

    def backup(self):
        """执行备份操作"""
        logging.info('开始备份...')
        self._sync_files()
        current_time = datetime.now()
        self.last_backup_time = current_time
        logging.info(f'备份完成。上次备份时间：{self.last_backup_time}')

    def schedule_backup(self, interval):
        """定时备份，interval为秒数"""
        from time import sleep
        while True:
            self.backup()
            sleep(interval)

# 示例用法
if __name__ == '__main__':
    source_directory = '/path/to/source'
    backup_directory = '/path/to/backup'
    backup_tool = BackupSyncTool(source_directory, backup_directory)
    backup_tool.schedule_backup(3600)  # 每小时备份一次