"""
Two Sum - Sorted Array

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

author: adambechtold
date: 2024.01.26
difficulty: medium
link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/



Result:
    R: 108 - beats 80
    M: 18 - beats 33
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1

        while left_index < right_index:
            low_value = numbers[left_index]
            high_value = numbers[right_index]
            sum = low_value + high_value

            if sum == target:
                return [left_index + 1, right_index + 1]
            elif sum < target:
                left_index += 1
            else:
                right_index -= 1

        return None


