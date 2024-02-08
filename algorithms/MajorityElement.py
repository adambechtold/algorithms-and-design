from typing import List
from collections import defaultdict

"""
Find Majority Element

whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/2k0b1tuiSxx
link: https://leetcode.com/problems/majority-element/
author: adambechtold
date: 2024.02.07
difficulty: easy
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.majority_element_counter(nums)

    """
    Approach - Count All Numbers

    - Runtime: beats 49%
    - Memory: beats 62%
    """
    def majority_element_hash(self, nums: List[int]) -> int:
        count_lookup = defaultdict(int)
        majority_threshold = len(nums) / 2

        for num in nums:
            count_lookup[num] += 1
            if count_lookup[num] > majority_threshold:
                return num

        raise ValueError('No majority element found.')

    """
    Approach - Keep a counter of the current majority element

    - Runtime: beats 56%
    - Memory: beats 80%
    """
    def majority_element_counter(self, nums: List[int]) -> int:
        # 1) Initialize Counter
        counter = 0
        curr_majority_num = -1

        # 2) Walk through each value in the array...
        for num in nums:
            if counter == 0:
                curr_majority_num = num

            if num == curr_majority_num:
                counter += 1
            else:
                counter -= 1

        # The majority number will have survived.
        return curr_majority_num

"""
Problem:


Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
