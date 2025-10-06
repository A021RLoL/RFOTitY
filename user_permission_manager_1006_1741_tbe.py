# 代码生成时间: 2025-10-06 17:41:49
import numpy as np

"""
User Permission Manager

This module implements a user permission management system.
It allows for user creation, permission assignment, and permission checks.
"""

class UserPermissionManager:
    """Manages user permissions."""

    def __init__(self):
        """Initializes the permission manager with an empty user permissions dictionary."""
        self.user_permissions = {}

    def create_user(self, username):
        """Creates a new user with no permissions.

        Args:
            username (str): The name of the user to create.

        Raises:
            ValueError: If the username already exists.
        """
        if username in self.user_permissions:
            raise ValueError(f"User '{username}' already exists.")
        self.user_permissions[username] = set()  # Empty set of permissions

    def assign_permission(self, username, permission):
        """Assigns a permission to a user.

        Args:
            username (str): The name of the user.
            permission (str): The permission to assign.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.user_permissions:
            raise ValueError(f"User '{username}' does not exist.")
        self.user_permissions[username].add(permission)

    def remove_permission(self, username, permission):
        """Removes a permission from a user.

        Args:
            username (str): The name of the user.
            permission (str): The permission to remove.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.user_permissions:
            raise ValueError(f"User '{username}' does not exist.")
        self.user_permissions[username].discard(permission)  # Discard does not raise an error if the permission is not found

    def check_permission(self, username, permission):
        """Checks if a user has a specific permission.

        Args:
            username (str): The name of the user.
            permission (str): The permission to check.

        Returns:
            bool: True if the user has the permission, False otherwise.

        Raises:
            ValueError: If the user does not exist.        
        """
        if username not in self.user_permissions:
            raise ValueError(f"User '{username}' does not exist.")
        return permission in self.user_permissions[username]

    def list_permissions(self, username):
        """Lists all permissions of a user.

        Args:
            username (str): The name of the user.

        Returns:
            set: A set of permissions.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.user_permissions:
            raise ValueError(f"User '{username}' does not exist.")
        return self.user_permissions[username].copy()

# Example usage:
if __name__ == '__main__':
    manager = UserPermissionManager()
    try:
        manager.create_user('alice')
        manager.assign_permission('alice', 'read')
        manager.assign_permission('alice', 'write')
        print(manager.check_permission('alice', 'read'))  # Should output True
        print(manager.list_permissions('alice'))         # Should output {'read', 'write'}
        manager.remove_permission('alice', 'write')
        print(manager.list_permissions('alice'))         # Should output {'read'}
    except ValueError as e:
        print(e)