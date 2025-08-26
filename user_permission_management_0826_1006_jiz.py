# 代码生成时间: 2025-08-26 10:06:07
import numpy as np

"""
User Permission Management System

This module provides functionalities to manage user permissions using a
permission matrix. It allows adding, removing, and checking permissions.

Attributes:
    permissions_matrix (numpy array): A 2D array where each row represents a user and
        each column represents a permission. A 1 indicates the user has the permission,
        a 0 indicates they do not.

Methods:
    add_user: Adds a new user with no permissions.
    remove_user: Removes a user and their permissions.
    add_permission: Adds a new permission for all users.
    remove_permission: Removes a permission for all users.
    grant_permission: Grants a permission to a specific user.
    revoke_permission: Revokes a permission from a specific user.
    check_permission: Checks if a user has a specific permission.
"""

# Initialize a 2D numpy array to store permissions_matrix
permissions_matrix = np.array([[]])

# Define the number of permissions
num_permissions = 0

# Function to add a new user with no permissions
def add_user():
    """Adds a new user to the permissions matrix with no permissions."""
    global permissions_matrix, num_permissions
    # Append a new row of zeros to the permissions matrix
    permissions_matrix = np.append(permissions_matrix, np.array([0] * num_permissions), axis=0)

# Function to remove a user and their permissions
def remove_user(user_id):
    """Removes a user from the permissions matrix."""
    global permissions_matrix
    if 0 <= user_id < permissions_matrix.shape[0]:
        permissions_matrix = np.delete(permissions_matrix, user_id, axis=0)
    else:
        raise ValueError("User ID is out of range.")

# Function to add a new permission for all users
def add_permission():
    """Adds a new permission to all users in the permissions matrix."""
    global permissions_matrix, num_permissions
    # Append a new column of zeros to the permissions matrix
    permissions_matrix = np.append(permissions_matrix, np.array([[0] * permissions_matrix.shape[0]]), axis=1)
    num_permissions += 1

# Function to remove a permission for all users
def remove_permission(permission_id):
    """Removes a permission for all users in the permissions matrix."""
    global permissions_matrix
    if 0 <= permission_id < permissions_matrix.shape[1]:
        permissions_matrix = np.delete(permissions_matrix, permission_id, axis=1)
    else:
        raise ValueError("Permission ID is out of range.")

# Function to grant a permission to a specific user
def grant_permission(user_id, permission_id):
    """Grants a permission to a specific user."""
    global permissions_matrix
    if 0 <= user_id < permissions_matrix.shape[0] and 0 <= permission_id < permissions_matrix.shape[1]:
        permissions_matrix[user_id, permission_id] = 1
    else:
        raise ValueError("User ID or Permission ID is out of range.")

# Function to revoke a permission from a specific user
def revoke_permission(user_id, permission_id):
    """Revokes a permission from a specific user."""
    global permissions_matrix
    if 0 <= user_id < permissions_matrix.shape[0] and 0 <= permission_id < permissions_matrix.shape[1]:
        permissions_matrix[user_id, permission_id] = 0
    else:
        raise ValueError("User ID or Permission ID is out of range.")

# Function to check if a user has a specific permission
def check_permission(user_id, permission_id):
    """Checks if a user has a specific permission."""
    global permissions_matrix
    if 0 <= user_id < permissions_matrix.shape[0] and 0 <= permission_id < permissions_matrix.shape[1]:
        return permissions_matrix[user_id, permission_id] == 1
    else:
        raise ValueError("User ID or Permission ID is out of range.")
