# 代码生成时间: 2025-08-12 11:59:52
import os
import shutil
import numpy as np

"""
文件备份和同步工具
提供将指定目录下的所有文件备份到另一个目录的功能，并支持同步更新。
"""


class FileBackupSync:
    def __init__(self, source_dir, backup_dir, sync_dir=None):
        """
        初始化文件备份和同步工具。
        :param source_dir: 源目录路径，需要备份的文件所在的目录
        :param backup_dir: 备份目录路径，备份文件存放的目录
        :param sync_dir: 同步目录路径，需要同步更新的目录（可选）
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.sync_dir = sync_dir

    def backup_files(self):
        """
        备份源目录下的所有文件到备份目录。
        """
        try:
            # 确保备份目录存在
            os.makedirs(self.backup_dir, exist_ok=True)

            # 遍历源目录下的所有文件
            for filename in os.listdir(self.source_dir):
                file_path = os.path.join(self.source_dir, filename)
                # 确保是文件而非目录
                if os.path.isfile(file_path):
                    # 备份文件
                    shutil.copy2(file_path, self.backup_dir)
                    print(f'文件 {filename} 已备份到 {self.backup_dir}')

        except Exception as e:
            print(f'备份文件时发生错误：{e}')

    def sync_files(self):
        """
        同步备份目录和同步目录。
        """
        try:
            if self.sync_dir is None:
                print('同步目录未指定，跳过同步操作。')
                return

            # 确保同步目录存在
            os.makedirs(self.sync_dir, exist_ok=True)

            # 遍历备份目录下的所有文件
            for filename in os.listdir(self.backup_dir):
                file_path = os.path.join(self.backup_dir, filename)
                # 确保是文件而非目录
                if os.path.isfile(file_path):
                    # 同步文件到同步目录
                    shutil.copy2(file_path, self.sync_dir)
                    print(f'文件 {filename} 已同步到 {self.sync_dir}')

        except Exception as e:
            print(f'同步文件时发生错误：{e}')

    def run(self):
        """
        运行备份和同步过程。
        """
        print('开始备份和同步文件...')
        self.backup_files()
        if self.sync_dir is not None:
            self.sync_files()
        print('文件备份和同步完成。')


def main():
    # 源目录、备份目录和同步目录
    source_dir = 'path/to/source/directory'
    backup_dir = 'path/to/backup/directory'
    sync_dir = 'path/to/sync/directory'

    # 创建文件备份和同步工具实例
    backup_sync_tool = FileBackupSync(source_dir, backup_dir, sync_dir)

    # 运行备份和同步过程
    backup_sync_tool.run()

if __name__ == '__main__':
    main()