# 代码生成时间: 2025-08-01 02:31:25
import json
import numpy as np
import os

"""
ConfigManager is a class responsible for managing configuration files.
It provides methods to load, save, and get configurations from a JSON file.
"""
class ConfigManager:
    def __init__(self, filename):
        """Initialize the ConfigManager with a file path."""
        self.filename = filename
        self.config = {}
        self.load_config()

    def load_config(self):
        """Load the configuration from the specified JSON file."""
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"The file {self.filename} does not exist.")
        with open(self.filename, 'r') as file:
            self.config = json.load(file)

    def save_config(self):
        """Save the current configuration to the specified JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get_config(self, key):
        """Get the value of a specific configuration key."""
        if key in self.config:
            return self.config[key]
        else:
            raise KeyError(f"The key {key} does not exist in the configuration.")

    def set_config(self, key, value):
        """Set the value of a specific configuration key."""
        self.config[key] = value
        self.save_config()

    def remove_config(self, key):
        """Remove a specific configuration key."""
        if key in self.config:
            del self.config[key]
            self.save_config()
        else:
            raise KeyError(f"The key {key} does not exist in the configuration.")

# Example usage:
if __name__ == '__main__':
    config_filename = 'config.json'
    manager = ConfigManager(config_filename)
    try:
        # Load configuration
        manager.load_config()

        # Get configuration value
        print(manager.get_config('example_key'))

        # Set configuration value
        manager.set_config('example_key', 'example_value')

        # Remove configuration key
        manager.remove_config('example_key')

    except (FileNotFoundError, KeyError) as e:
        print(f"Error: {e}")