# 代码生成时间: 2025-07-31 21:59:53
import numpy as np

"""
Access Control Program using Python and Numpy.
This program implements a simple access control system that checks user permissions.
"""

class PermissionDeniedError(Exception):
    """
    Custom exception to handle permission denied errors.
    """
    def __init__(self, message="Access Denied: You do not have permission to perform this action."):
        super().__init__(message)

class AccessControl:
    """
    AccessControl class to manage user permissions.
    """
    def __init__(self):
        # Initialize a dictionary to store user permissions
        self.permissions = {}

    def add_user(self, username):
        """
        Adds a new user to the permissions dictionary.
        """
        if username in self.permissions:
            raise ValueError(f"User '{username}' already exists.")
        self.permissions[username] = set()

    def remove_user(self, username):
        """
        Removes a user from the permissions dictionary.
        """
        if username not in self.permissions:
            raise ValueError(f"User '{username}' does not exist.")
        del self.permissions[username]

    def assign_permission(self, username, permission):
        "