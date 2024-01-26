"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


author: adambechtold
date: 2024.01.26 
link: https://leetcode.com/problems/valid-palindrome/

Result:
    Runtime: 36 - beats 97
    Memory: 18 - beats 18
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1

        while left_index < right_index:
            left_val = s[left_index]
            right_val = s[right_index]
            if not left_val.isalpha() and not left_val.isdigit():
                left_index += 1
            elif not right_val.isalpha() and not right_val.isdigit():
                right_index -= 1
            elif right_val.lower() != left_val.lower():
                return False
            else:
                right_index -= 1
                left_index += 1

        return True


