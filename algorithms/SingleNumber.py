"""
Single Number

author: adambechtold
difficulty: easy
date: 2024.02.01
link: https://leetcode.com/problems/single-number/

Runtime: 103 - beats 97.44%
Memory: 19.8 - beats 42.93%
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer = answer ^ num
        return answer




"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""

"""
Scratch Pad
[2,2,1]
1

[4,1,2,1,2]
4

# Check each for duplicate. If none, found, return
O(N^2)

# Store count. Return count of 2
T: O(N)
- once over each to build
- once over each to find count of 1
S: O(N)

# XOR ...  
000

2 - 010
2 - 010
1 - 001
XOR → 001 → 4



4 - 100
1 - 001
2 - 010
1 - 001
2 - 010
XOR → 100 → 4

[5,5,6,6,7]
5 101
6 110
5 101
7 111
6 110
XOR → 000 or 111?

[5,5,6,7,7]
101
101
110
111
111

110


Insight - Odd number of elements

# Approach - Add and Subtract Values
Item | Count
5
6
7
5
6

❓ Question - How do you know whether to add or subtract?
You don't...

"""