# 代码生成时间: 2025-09-30 02:34:24
import numpy as np

"""
This Python program simulates a Lightning Network node using NumPy framework.

It demonstrates the creation of a node, maintaining a balance, and managing transactions.
"""

class LightningNode:
    """
    A class representing a Lightning Network node.
    """
    def __init__(self, node_id, initial_balance=0):
        """
        Initializes a Lightning Node with a unique ID and an optional initial balance.
        :param node_id: Unique identifier for the node
        :param initial_balance: Initial balance of the node
        """
        self.node_id = node_id
        self.balance = initial_balance

    def receive_payment(self, amount):
        """
        Simulates receiving a payment to the node.
        :param amount: Amount to be received
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.balance += amount
        return f"Received {amount}, new balance: {self.balance}"

    def send_payment(self, amount):
        """
        Simulates sending a payment from the node.
        :param amount: Amount to be sent
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return f"Sent {amount}, new balance: {self.balance}"

    def get_balance(self):
        """
        Returns the current balance of the node.
        """
        return self.balance

# Example usage
if __name__ == '__main__':
    # Create a Lightning Node with node_id 1 and initial balance 100
    node1 = LightningNode(node_id=1, initial_balance=100)

    # Receive a payment of 50
    print(node1.receive_payment(50))

    # Send a payment of 30
    print(node1.send_payment(30))

    # Check balance
    print(f"Final balance: {node1.get_balance()}")
