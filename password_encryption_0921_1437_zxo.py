# 代码生成时间: 2025-09-21 14:37:38
import numpy as np
import os

"""
A simple password encryption and decryption tool using Python and NumPy.
This tool uses a simple XOR operation for encryption and decryption.
"""

def generate_key(length=8):
    """Generate a random key for encryption/decryption."""
    return os.urandom(length)


def encrypt(password, key):
    """Encrypt the given password using XOR operation with the provided key."""
    # Convert password and key to NumPy arrays for efficient computation
    password_array = np.frombuffer(password.encode(), dtype=np.uint8)
    key_array = np.frombuffer(key, dtype=np.uint8)
    
    # Ensure the key's length matches the password's length
    key_array = np.tile(key_array, (len(password) // len(key) + 1))[:len(password)]
    
    # Perform XOR operation
    encrypted = np.bitwise_xor(password_array, key_array).astype(np.uint8)
    return encrypted.tobytes()


def decrypt(encrypted, key):
    """Decrypt the given encrypted data using XOR operation with the provided key."""
    # Convert encrypted data and key to NumPy arrays
    encrypted_array = np.frombuffer(encrypted, dtype=np.uint8)
    key_array = np.frombuffer(key, dtype=np.uint8)
    
    # Ensure the key's length matches the encrypted data's length
    key_array = np.tile(key_array, (len(encrypted) // len(key) + 1))[:len(encrypted)]
    
    # Perform XOR operation
    decrypted = np.bitwise_xor(encrypted_array, key_array).astype(np.uint8)
    return decrypted.tobytes()


def main():
    # Generate a random key
    key = generate_key()
    
    # Get password from the user
    password = input("Enter the password to encrypt: ")
    
    try:
        # Encrypt the password
        encrypted = encrypt(password, key)
        print("Encrypted password: ", encrypted)
        
        # Decrypt the encrypted password
        decrypted = decrypt(encrypted, key)
        print("Decrypted password: ", decrypted)
    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    main()