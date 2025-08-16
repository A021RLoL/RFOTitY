# 代码生成时间: 2025-08-17 02:45:50
import numpy as np

"""
A simple cache policy implementation using Least Recently Used (LRU) strategy.
This policy maintains a fixed-size cache and evicts the least recently used items first."""

class LRUCache:
    def __init__(self, capacity: int):
        """Initialize the LRU cache with a given capacity."""
        self.capacity = capacity
        self.cache = {}
        self.usage = {}

    def get(self, key: int) -> int:
        """Retrieve the value associated with the given key.
        If the key is not present, return -1.
        Update the usage of the key to indicate it was recently used."""
        if key not in self.cache:
            return -1
        value = self.cache[key]
        self.mark_recently_used(key)
        return value

    def put(self, key: int, value: int) -> None:
        """Insert or update the value associated with the given key.
        If the cache is full, evict the least recently used item first."""
        if key in self.cache:
            self.mark_recently_used(key)
        elif len(self.cache) == self.capacity:
            self.evict_least_recently_used()
        self.cache[key] = value
        self.mark_recently_used(key)

    def mark_recently_used(self, key: int) -> None:
        """Mark the given key as recently used by updating its usage."""
        if key in self.usage:
            del self.usage[key]
        self.usage[key] = key

    def evict_least_recently_used(self) -> None:
        """Evict the least recently used item from the cache."""
        least_recently_used_key = next(iter(self.usage))
        del self.cache[least_recently_used_key]
        del self.usage[least_recently_used_key]

    def display_cache(self) -> None:
        """Display the current state of the cache."""
        print("Cache content: ", self.cache)
        print("Recently used order: ", self.usage)

# Example usage
if __name__ == "__main__":
    cache = LRUCache(capacity=3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.display_cache()
    print(cache.get(1))  # returns 1
    cache.put(4, 4)    # evicts key 2
    cache.display_cache()
    print(cache.get(2))  # returns -1 (not found)
    print(cache.get(1))  # returns 1
