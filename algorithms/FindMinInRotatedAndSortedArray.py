"""
Find the Minimum Value in a Sorted, Rotated Array

author: adambechtold
link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/7zfRrgA1LpO
difficulty: medium

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""


"""
Runtime: Beats 58%
Memory: Beats 59%
"""
def findMinAdam(nums):
    left_i = 0
    right_i = len(nums) - 1
    curr_min = float("inf")

    while right_i - left_i > 1:
        mid_i = int(((right_i - left_i) / 2) + left_i)
        curr_min = min(nums[left_i], nums[right_i], nums[mid_i], curr_min)

        if nums[mid_i] > nums[0]:
            # move right
            left_i = mid_i
        else:
            # move left
            right_i = mid_i

    return min(curr_min, nums[left_i], nums[right_i])

"""
Runtime: Beats 52%
Memory: Beats 69%
From Neetcode
"""
def findMinNeet(nums):
    start , end = 0, len(nums) - 1 
    curr_min = float("inf")
    
    while start  <  end :
        mid = start + (end - start ) // 2
        curr_min = min(curr_min,nums[mid])
        
        # right has the min 
        if nums[mid] > nums[end]:
            start = mid + 1
            
        # left has the  min 
        else:
            end = mid - 1 
            
    return min(curr_min,nums[start])

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return findMinAdam(nums)