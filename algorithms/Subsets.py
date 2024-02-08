from typing import List

"""
Subsets

author: adambechtold
date: 2024.02.08
link: https://leetcode.com/problems/subsets/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/7CAwYPGqiu5
difficulty: medium
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets_recursive(nums)
        #return self.subsets_neet(nums)

    """
    Approach - Recursive

    - Runtime: beats: 80%
    - Memory: beats 78%
    """
    def subsets_recursive(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        subsets_rest = self.subsets_recursive(nums[1:])
        for i in range(len(subsets_rest)):
            subset = subsets_rest[i]
            subset_copy = list(subset)
            subset_copy.append(nums[0])
            subsets_rest.append(subset_copy)

        return subsets_rest

    """
    Approach - DFS approach from Neetcode

    - Runtime: beats 83%
    - Memory: beats 79%
    """
    def subsets_neet(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
