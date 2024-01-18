"""
Two Sum
link: https://leetcode.com/problems/two-sum/
date: 2024.01.18
author: @adambechtold
"""

from collections import defaultdict

# Initial solution
## O(n) time, O(n) space
## ▼ Con - the lookup logic is complex
def twoSumLookup(nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(set)
        for i, num in enumerate(nums):
            lookup[num].add(i)

        
        for i, num in enumerate(nums):
            complement_val = target - num

            is_complement_in_list = complement_val in lookup
            is_complement_equal_to_num = complement_val == num
            copies_of_num = len(lookup[num])

            use_this_complement = \
                is_complement_in_list \
                and (
                    not is_complement_equal_to_num \
                    or copies_of_num > 1
                )

            if use_this_complement:
                return [
                    lookup[num].pop(),
                    lookup[complement_val].pop()
                ]

        return []

# Brute force solution
# Used this to further understand the problem, hoping it would surface optimizations
def twoSumBrute(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i,j]

# Optimal solution
# O(n) time, O(n) space
# ▼ Pro - lookup logic is simple
# I did't come up with this solution, but I understand it
def twoSumTrackSeen(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement_val = target - num
        if complement_val in lookup:
            return [i, lookup[complement_val]]
        lookup[num] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return twoSumTrackSeen(nums, target)