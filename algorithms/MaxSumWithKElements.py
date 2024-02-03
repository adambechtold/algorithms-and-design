"""
Maximum Sum with Exactly K Elements

link: https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
difficulty: easy
author: adambechtold
date: 2024.02.03

Runtime: Beats 90%
Memory: Beats 57%
"""

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0
        max_num = max(nums)
        return sum([max_num + i for i in range(0, k)])