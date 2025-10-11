# 代码生成时间: 2025-10-11 19:38:24
import numpy as np

"""
A voting system implemented using Python and NumPy.

This script provides a simple command-line interface for casting votes and
retrieving vote results. It stores votes in a NumPy array for efficient
manipulation and retrieval.
"""

# Define the maximum number of candidates
MAX_CANDIDATES = 10

class VotingSystem:
    def __init__(self):
        """Initialize the voting system with a NumPy array."""
        self.votes = np.zeros(MAX_CANDIDATES)

    def cast_vote(self, candidate_index):
        """Cast a vote for a candidate at the given index."""
        if not 0 <= candidate_index < MAX_CANDIDATES:
            raise ValueError("Candidate index out of range.")
        self.votes[candidate_index] += 1

    def get_results(self):
        """Return the results of the votes in a sorted list."""
        sorted_indices = np.argsort(self.votes)[::-1]
        results = [(index, self.votes[index]) for index in sorted_indices]
        return results

    def display_results(self):
        "