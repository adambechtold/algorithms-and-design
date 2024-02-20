"""
Max Island Size

date: 2024.02.20
difficulty: medium
link: https://leetcode.com/problems/max-area-of-island/
whiteboard: None
"""
from typing import List

ISLAND_VALUE = 1
SEA_VALUE = 0
VISITED_VALUE = -1

class Solution:
    """
    Approach - Recursive Count

    # Runtime - beats 85%
    # Memory - beats 85%
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_size = 0

        for row_i in range(len(grid)):
            for col_i in range(len(grid[row_i])):
                if grid[row_i][col_i] == ISLAND_VALUE:
                    max_island_size = max(
                        max_island_size,
                        self.get_island_size(grid, row_i, col_i)
                    )

        return max_island_size

    def get_island_size(self, grid: List[List[int]], row: int, col: int) -> int:
        if row < 0 or col < 0:
            return 0
        if row >= len(grid) or col >= len(grid[0]):
            return 0

        if grid[row][col] != ISLAND_VALUE:
            return 0
        
        grid[row][col] = VISITED_VALUE

        return 1 + sum([
            self.get_island_size(grid, row - 1, col),
            self.get_island_size(grid, row + 1, col),
            self.get_island_size(grid, row, col - 1),
            self.get_island_size(grid, row, col + 1)
        ])
        