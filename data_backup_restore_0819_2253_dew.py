# 代码生成时间: 2025-08-19 22:53:45
import numpy as np
import os
import pickle
import shutil
from datetime import datetime

# 数据备份恢复程序
class DataBackupRestore:
    """
    用于数据备份和恢复的类。
    """
    def __init__(self, source_path, backup_path):
        """
        构造函数
        :param source_path: 原始数据文件路径
        :param backup_path: 备份数据文件存放路径
        """
        self.source_path = source_path
        self.backup_path = backup_path

    def backup_data(self):
        """
        备份数据文件
        :return: 备份成功返回True，否则返回False
        """
        try:
            if not os.path.exists(self.source_path):
                raise FileNotFoundError(f"源文件{self.source_path}不存在")
            if not os.path.exists(self.backup_path):
                os.makedirs(self.backup_path)
            backup_filename = datetime.now().strftime('%Y%m%d%H%M%S') + '.npy'
            backup_file_path = os.path.join(self.backup_path, backup_filename)
            np.save(backup_file_path, np.load(self.source_path))
            print(f"数据备份成功，备份文件保存在{backup_file_path}")
            return True
        except Exception as e:
            print(f"数据备份失败：{e}")
            return False

    def restore_data(self, backup_filename):
        """
        恢复数据文件
        :param backup_filename: 要恢复的备份文件名
        :return: 恢复成功返回True，否则返回False
        """
        try:
            if not os.path.exists(self.backup_path):
                raise FileNotFoundError(f"备份文件路径{self.backup_path}不存在")
            backup_file_path = os.path.join(self.backup_path, backup_filename)
            if not os.path.exists(backup_file_path):
                raise FileNotFoundError(f"备份文件{backup_filename}不存在")
            np.save(self.source_path, np.load(backup_file_path))
            print(f"数据恢复成功，恢复文件保存在{self.source_path}")
            return True
        except Exception as e:
            print(f"数据恢复失败：{e}")
            return False

# 示例代码
if __name__ == '__main__':
    source_path = 'data.npy'
    backup_path = 'backup'
    backup_restore = DataBackupRestore(source_path, backup_path)
    backup_success = backup_restore.backup_data()
    if backup_success:
        backup_filename = datetime.now().strftime('%Y%m%d%H%M%S') + '.npy'
        restore_success = backup_restore.restore_data(backup_filename)
        if restore_success:
            print("数据恢复成功")
        else:
            print("数据恢复失败")
    else:
        print("数据备份失败")