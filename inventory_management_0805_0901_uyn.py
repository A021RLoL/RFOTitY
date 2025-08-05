# 代码生成时间: 2025-08-05 09:01:31
import numpy as np


"""
Inventory Management System using Python and NumPy.
# NOTE: 重要实现细节

This system allows for basic inventory operations such as adding, removing, and
checking the quantity of items in stock.

Attributes:
- inventory (dictionary): stores item names and their quantities.

Methods:
# 扩展功能模块
- add_item(item_name, quantity): Adds a specified quantity of an item to the inventory.
- remove_item(item_name, quantity): Removes a specified quantity of an item from the inventory.
- check_inventory(item_name): Checks the quantity of an item in the inventory.

Example:
>>> inventory_system = InventoryManagement()
>>> inventory_system.add_item("Apples", 10)
>>> inventory_system.check_inventory("Apples")
10
>>> inventory_system.remove_item("Apples", 5)
>>> inventory_system.check_inventory("Apples")
5
"""

class InventoryManagement:
    def __init__(self):
        """Initialize the inventory system with an empty dictionary."""
        self.inventory = {}
# 优化算法效率

    def add_item(self, item_name, quantity):
        """Add a specified quantity of an item to the inventory.

        Args:
# 增强安全性
        item_name (str): The name of the item to add.
        quantity (int): The quantity of the item to add.

        Raises:
        ValueError: If the quantity is not a non-negative integer.
# 扩展功能模块
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity):
        """Remove a specified quantity of an item from the inventory.

        Args:
# NOTE: 重要实现细节
        item_name (str): The name of the item to remove.
        quantity (int): The quantity of the item to remove.

        Raises:
        ValueError: If the quantity is not a non-negative integer or exceeds the inventory quantity.
        KeyError: If the item is not in the inventory.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
# 扩展功能模块

        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
# TODO: 优化性能

        if quantity > self.inventory[item_name]:
            raise ValueError(f"Cannot remove more items than are in stock for '{item_name}'.")

        self.inventory[item_name] -= quantity

        if self.inventory[item_name] == 0:
            del self.inventory[item_name]

    def check_inventory(self, item_name):
        """Check the quantity of an item in the inventory.
# FIXME: 处理边界情况

        Args:
# 增强安全性
        item_name (str): The name of the item to check.

        Returns:
        int: The quantity of the item in the inventory.

        Raises:
        KeyError: If the item is not in the inventory.
        """
        if item_name not in self.inventory:
# 增强安全性
            raise KeyError(f"Item '{item_name}' not found in inventory.")

        return self.inventory[item_name]


# Example usage
if __name__ == "__main__":
    inventory_system = InventoryManagement()
# 添加错误处理
    inventory_system.add_item("Apples", 10)
    print(inventory_system.check_inventory("Apples"))  # Output: 10
    inventory_system.remove_item("Apples", 5)
    print(inventory_system.check_inventory("Apples"))  # Output: 5