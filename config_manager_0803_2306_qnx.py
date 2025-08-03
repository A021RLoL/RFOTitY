# 代码生成时间: 2025-08-03 23:06:05
import json
import numpy as np
import os

class ConfigManager:
    """
    A configuration manager that handles reading, updating, and saving of configuration files.
    """

    def __init__(self, config_path):
        """
        Initialize the ConfigManager with a path to the configuration file.
        """
        self.config_path = config_path
        self.config = {}
        self.load_config()

    def load_config(self):
        """
        Load the configuration from the file. If the file does not exist, initialize an empty dictionary.
        """
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as file:
                    self.config = json.load(file)
            except json.JSONDecodeError:
                raise ValueError("Configuration file is not in valid JSON format.")
        else:
            self.config = {}

    def save_config(self):
        """
        Save the current configuration to the file.
        """
        try:
            with open(self.config_path, 'w') as file:
                json.dump(self.config, file, indent=4)
        except IOError:
            raise IOError("Failed to write to the configuration file.")

    def update_config(self, key, value):
        """
        Update the configuration with a new key-value pair.
        """
        if key in self.config:
            self.config[key] = value
        else:
            raise KeyError(f"Key '{key}' does not exist in the configuration.")

    def get_config(self, key):
        """
        Retrieve the value for a given key from the configuration.
        """
        if key in self.config:
            return self.config[key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the configuration.")

    def list_configs(self):
        """
        Return a list of all configuration keys.
        """
        return list(self.config.keys())

# Example usage:
if __name__ == '__main__':
    config_manager = ConfigManager('config.json')
    try:
        config_manager.update_config('resolution', '1920x1080')
        print(config_manager.get_config('resolution'))
        config_manager.save_config()
    except (KeyError, ValueError, IOError) as e:
        print(f"An error occurred: {e}")
