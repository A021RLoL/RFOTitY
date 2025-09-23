# 代码生成时间: 2025-09-23 12:48:04
import numpy as np
import os
import pickle
import shutil
from datetime import datetime


# Constants
BACKUP_DIRECTORY = "backups/"
FILE_EXTENSION = ".npy"
LOG_FILE = "backup_log.txt"


class DataBackupRestore:
    def __init__(self):
        # Ensure backup directory exists
        os.makedirs(BACKUP_DIRECTORY, exist_ok=True)
        self.backup_log = open(LOG_FILE, "a")

    def backup(self, data):
        """
        Backs up the given data to a numpy file.
        :param data: Data to be backed up, expected to be a numpy array.
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"backup_{timestamp}{FILE_EXTENSION}"
            filepath = os.path.join(BACKUP_DIRECTORY, filename)
            np.save(filepath, data)
            self.log_backup(filename)
            print(f"Backup successful: {filename}")
        except Exception as e:
            print(f"Error during backup: {e}")

    def restore(self, filename):
        """
        Restores data from a numpy file.
        :param filename: The filename of the backup file.
        :return: The restored data.
        """
        try:
            filepath = os.path.join(BACKUP_DIRECTORY, filename)
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Backup file not found: {filename}")
            data = np.load(filepath, allow_pickle=True)
            print(f"Restore successful: {filename}")
            return data
        except Exception as e:
            print(f"Error during restore: {e}")
            return None

    def log_backup(self, filename):
        "