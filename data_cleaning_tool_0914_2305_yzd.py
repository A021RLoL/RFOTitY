# 代码生成时间: 2025-09-14 23:05:21
import numpy as np
import pandas as pd

"""
Data Cleaning and Preprocessing Tool
This tool is designed to clean and preprocess data by handling missing values,
# FIXME: 处理边界情况
normalizing data, and encoding categorical variables.
"""

class DataCleaningTool:
    def __init__(self, data):
        """
        Initializes the DataCleaningTool with the input data.
        :param data: A pandas DataFrame containing the raw data.
        """
        self.data = data

    def handle_missing_values(self, strategy='mean'):
        """
        Handles missing values in the dataset.
        :param strategy: The strategy to use for handling missing values.
            Options are 'mean', 'median', 'mode', or 'drop'.
        """
        if strategy == 'mean':
# 增强安全性
            self.data = self.data.fillna(self.data.mean())
        elif strategy == 'median':
            self.data = self.data.fillna(self.data.median())
        elif strategy == 'mode':
            self.data = self.data.fillna(self.data.mode().iloc[0])
        elif strategy == 'drop':
            self.data = self.data.dropna()
        else:
            raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', or 'drop'.")

    def normalize_data(self):
        """
        Normalizes the numerical columns in the dataset.
        """
        numerical_cols = self.data.select_dtypes(include=[np.number]).columns
        self.data[numerical_cols] = (self.data[numerical_cols] - 
                                 self.data[numerical_cols].mean()) / \
                                 (self.data[numerical_cols].std())

    def encode_categorical_variables(self, encoding='onehot'):
        """
        Encodes categorical variables in the dataset.
# 增强安全性
        :param encoding: The type of encoding to use. Options are 'onehot' or 'label'.
        """
        if encoding == 'onehot':
            self.data = pd.get_dummies(self.data, drop_first=True)
        elif encoding == 'label':
            self.data = self.data.apply(lambda x: \
                             LabelEncoder().fit_transform(x) if x.dtype == 'object' else x)
        else:
            raise ValueError("Invalid encoding type. Choose from 'onehot' or 'label'.")

    def preprocess_data(self, missing_strategy='mean', normalize=True, encoding='onehot'):
        """
# FIXME: 处理边界情况
        Performs data preprocessing by handling missing values, normalizing data, and encoding categorical variables.
        :param missing_strategy: The strategy to use for handling missing values.
# 添加错误处理
        :param normalize: A boolean indicating whether to normalize the data.
        :param encoding: The type of encoding to use for categorical variables.
# NOTE: 重要实现细节
        """
        try:
            self.handle_missing_values(missing_strategy)
            if normalize:
                self.normalize_data()
            self.encode_categorical_variables(encoding)
        except Exception as e:
            print(f"An error occurred during data preprocessing: {e}")

# Example usage:
if __name__ == '__main__':
    # Load your dataset here
    data = pd.DataFrame(...)

    # Create an instance of DataCleaningTool
# 改进用户体验
    cleaner = DataCleaningTool(data)

    # Preprocess the data
    cleaner.preprocess_data(missing_strategy='mean', normalize=True, encoding='onehot')

    # The preprocessed data is now stored in cleaner.data
# 扩展功能模块
    print(cleaner.data)