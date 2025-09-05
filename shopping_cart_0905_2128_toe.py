# 代码生成时间: 2025-09-05 21:28:05
import numpy as np

"""
A simple shopping cart implementation using Python and NumPy.
"""

class ShoppingCart:
    """Shopping Cart class to manage items and quantities."""

    def __init__(self):
        # Initialize an empty cart
        self.items = np.array([])

    def add_item(self, item, quantity):
        """Add an item to the cart with a specified quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        # Append the item and quantity to the cart
        self.items = np.append(self.items, np.array([item, quantity]))

    def remove_item(self, item):
        """Remove an item from the cart."""
        # Find the index of the item
        idx = np.where(self.items == item)[0]
        if len(idx) == 0:
            raise ValueError(f"Item '{item}' not found in the cart.")
        # Remove the item and its quantity from the cart
        self.items = np.delete(self.items, idx + 1)
        self.items = np.delete(self.items, idx)

    def get_cart_contents(self):
        """Return the current contents of the cart."""
        return self.items

    def calculate_total(self):
        """Calculate the total price of the items in the cart."""
        # Assuming each item has a fixed price of 10 (for demonstration)
        item_prices = np.ones_like(self.items[1::2]) * 10
        total_price = np.sum(item_prices)
        return total_price

    def __str__(self):
        """String representation of the cart contents."""
        if len(self.items) == 0:
            return "Your cart is empty."
        cart_contents = ", ".join([f"{item} x{quantity}" for item, quantity in self.items[::2], self.items[1::2]])
        return f"Your cart contains: {cart_contents}."

# Example usage
if __name__ == '__main__':
    cart = ShoppingCart()
    try:
        cart.add_item("Apples", 3)
        cart.add_item("Bananas", 5)
        print(cart)  # Print cart contents
        cart.remove_item("Apples")
        print(cart)  # Print cart contents after removal
        print(f"Total price: ${cart.calculate_total():.2f}")  # Calculate total price
    except ValueError as e:
        print(e)