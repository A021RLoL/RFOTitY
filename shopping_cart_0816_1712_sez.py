# 代码生成时间: 2025-08-16 17:12:19
import numpy as np

"""
Shopping Cart Implementation using Python and NumPy.
This program simulates a basic shopping cart where items can be added, removed, and
the total cost can be calculated.

Attributes:
- items (numpy array): Stores the items in the cart with their prices.
- total_cost (float): Tracks the total cost of items in the cart.

Methods:
- add_item(item_name, price): Adds an item to the cart.
- remove_item(item_name): Removes an item from the cart.
- calculate_total_cost(): Calculates the total cost of items in the cart.
"""

class ShoppingCart:
    def __init__(self):
        """Initializes the shopping cart with an empty list of items and total cost."""
        self.items = np.array([])  # Store items as a numpy array for efficient operations
        self.total_cost = 0.0

    def add_item(self, item_name, price):
        """Adds an item to the cart.

        Args:
        item_name (str): The name of the item to add.
        price (float): The price of the item.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.items = np.append(self.items, [(item_name, price)])

    def remove_item(self, item_name):
        """Removes an item from the cart.

        Args:
        item_name (str): The name of the item to remove.
        """
        mask = self.items[:, 0] != item_name  # Create a mask to filter out the item
        self.items = self.items[mask]

    def calculate_total_cost(self):
        """Calculates the total cost of items in the cart.

        Returns:
        float: The total cost of items in the cart.
        """
        prices = self.items[:, 1]  # Extract prices from the items array
        self.total_cost = np.sum(prices)
        return self.total_cost

    def __str__(self):
        """Returns a string representation of the shopping cart."""
        items_str = ", ".join([f"{item[0]}: ${item[1]:.2f}" for item in self.items])
        return f"Shopping Cart: {{Items: [ {items_str} ], Total Cost: ${self.total_cost:.2f}}}"

# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Apple", 1.0)
    cart.add_item("Banana", 0.5)
    cart.add_item("Orange", 1.5)
    print(cart)
    print(f"Total Cost: ${cart.calculate_total_cost():.2f}")
    cart.remove_item("Banana")
    print(cart)
    print(f"Total Cost: ${cart.calculate_total_cost():.2f}")
