# 代码生成时间: 2025-09-17 20:48:22
import numpy as np
import sqlite3
from sqlite3 import Error

"""
A Python script to demonstrate SQL injection prevention using parameterized queries with SQLite and NumPy.

Attributes:
    None

Methods:
    - create_connection: Establishes a connection to the SQLite database.
    - prevent_sql_injection: Demonstrates how to use parameterized queries to prevent SQL injection.
"""

def create_connection(db_file):
    """
    Creates a database connection to the SQLite database specified by db_file.
    
    Args:
        db_file (str): The database file name.
    
    Returns:
        conn (sqlite3.Connection): Connection object or None.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def prevent_sql_injection(conn, user_id):
    """
    Demonstrates the use of parameterized queries to prevent SQL injection.
    
    Args:
        conn (sqlite3.Connection): Connection object to the SQLite database.
        user_id (int): The ID of the user to fetch data for.
    
    Returns:
        user_data (list): A list of user data if found, otherwise None.
    """
    cursor = conn.cursor()
    # Using parameterized queries to prevent SQL injection
    sql = """SELECT * FROM users WHERE user_id = ?"""
    try:
        cursor.execute(sql, (user_id,))
        user_data = cursor.fetchall()
        return user_data
    except Error as e:
        print(e)
    finally:
        cursor.close()

# Example usage
if __name__ == '__main__':
    # Database file path
    db_file = 'example.db'
    # User ID to fetch data for
    user_id = 1
    
    # Establish a database connection
    connection = create_connection(db_file)
    if connection:
        user_data = prevent_sql_injection(connection, user_id)
        if user_data:
            for row in user_data:
                print(row)
        else:
            print("No user found with the given ID.")
        
        # Close database connection
        connection.close()
    else:
        print("Error! Cannot establish a database connection.")