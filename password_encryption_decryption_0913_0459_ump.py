# 代码生成时间: 2025-09-13 04:59:01
import numpy as np
import os
"""
A simple password encryption and decryption tool using numpy and a random salt.
This tool generates a random salt for each password and stores the salt along with the encrypted password.
"""

# Function to generate a random salt
def generate_salt():
    return os.urandom(16)
"""Generate a 16-byte random salt using os.urandom()"""

# Function to encrypt the password
def encrypt_password(password, salt):
    """Encrypt the password using the salt and numpy's bitwise operations."""
    # Convert the password and salt to numpy arrays of characters
    password_array = np.fromiter(password, dtype='U1')
    salt_array = np.fromiter(salt, dtype='U1')
    
    # XOR the password with the salt
    encrypted = np.bitwise_xor(password_array, salt_array)
    return encrypted.tobytes()

# Function to decrypt the password
def decrypt_password(encrypted, salt):
    """Decrypt the encrypted password using the salt and numpy's bitwise operations."""
    # Convert the encrypted data and salt to numpy arrays of characters
    encrypted_array = np.fromiter(encrypted, dtype='U1')
    salt_array = np.fromiter(salt, dtype='U1')
    
    # XOR the encrypted data with the salt to get the original password
    decrypted = np.bitwise_xor(encrypted_array, salt_array)
    return decrypted.tobytes()

# Main function to handle encryption and decryption
def main():
    try:
        # Input the password from the user
        password = input("Enter password to encrypt: ")
        salt = generate_salt()
        
        # Encrypt the password
        encrypted_password = encrypt_password(password, salt)
        print(f"Encrypted password: {encrypted_password}")
        
        # Display the salt (for decryption purposes)
        print(f"Salt: {salt}")
        
        # Ask for the encrypted password and the salt to decrypt
        encrypted_input = input("Enter encrypted password to decrypt: ")
        salt_input = input("Enter salt for decryption: ")
        
        # Decrypt the password
        decrypted_password = decrypt_password(encrypted_input.encode(), salt_input.encode())
        print(f"Decrypted password: {decrypted_password}")
    except Exception as e:
        print(f"An error occurred: {e}")
"""Handle encryption and decryption process with error handling."""

if __name__ == '__main__':
    main()
