"""
Number of Island

link: https://leetcode.com/problems/number-of-islands/submissions/1181244058/
date: 2024.02.20
difficulty: medium
"""
from typing import List

ISLAND_VALUE = "1"
SEA_VALUE = "0"
VISITED_VALUE  = "-1"

class Solution:
    """
    Approach - Recursive Traversal

    # Runtime - beats 67%
    # Memory - beats 91%
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0

        for row_i in range(len(grid)):
            for col_i in range(len(grid[row_i])):
                if grid[row_i][col_i] == ISLAND_VALUE:
                    counter += 1
                    self.traverse_and_mark_island(row_i, col_i, grid)
        
        return counter

    def traverse_and_mark_island(self, row: int, col: int, grid: List[List[str]]) -> int:
        # ignore if this the input values are invalid
        if row < 0 or col < 0:
            return
        if row >= len(grid) or col >= len(grid[0]):
            return

        # check if this location is an island
        this_location = grid[row][col]
        if this_location != ISLAND_VALUE:
            return

        # mark as visited
        grid[row][col] = VISITED_VALUE

        # traverse all neighbors
        self.traverse_and_mark_island(row - 1, col, grid)
        self.traverse_and_mark_island(row + 1, col, grid)
        self.traverse_and_mark_island(row, col - 1, grid)
        self.traverse_and_mark_island(row, col + 1, grid)

