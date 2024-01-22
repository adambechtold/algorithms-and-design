"""
Palindrome Number
LeetCode No. 9

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

link: https://leetcode.com/problems/palindrome-number/description/
date: 2024.01.21
author: adambechtold
difficulty: easy
"""

run_tests = False

# With String Conversion
# Both of these beat ~60% runtime and 54% memor
def isPalindromeToStringTwoPointer(x):
    str_x = str(x)
    l, r = 0, len(str_x) - 1

    while l < r:
        if str_x[l] != str_x[r]:
            return False
        l += 1
        r -= 1
    
    return True

def isPalindromeToStringReverse(x):
    str_x = str(x)
    str_x_reversed = [c for c in reversed(str_x)]

    for i in range(len(str_x)):
        if str_x[i] != str_x_reversed[i]:
            return False

    return True

from math import floor
from math import log10
# Without String Conversion
# Beats 7% run time
# Beats 53% memory
def isPalindromeNoConversion(x):
    if x < 0:
        return False

    l, r = 0, num_length(x) - 1
    digits_of_x = [digit_at_index(x, i) for i in range(r + 1)]
    
    while l < r:
        if digits_of_x[l] != digits_of_x[r]:
            return False
        l += 1
        r -= 1

    return True
    

def num_length(x: int) -> int:
    if x == 0:
        return 1
    else:
        return 1 + floor(log10(abs(x)))

if run_tests == True:
    print("Test Num Length")
    print(num_length(0),1)
    print(num_length(-1), 1)
    print(num_length(100), 3)

def digit_at_index(x: int, i: int) -> int:
    x = abs(x)
    length_x = num_length(x)

    if i >= length_x:
        raise ValueError

    if x == 0:
        return 0
    
    divide_by = pow(10, (length_x - i - 1))
    ones_place_shift = floor(x / divide_by)
    ones_place_value = ones_place_shift % 10
    return ones_place_value 

if run_tests == True:
    print("Test Digit at Number")
    print(digit_at_index(0, 0), 0)
    print(digit_at_index(10,0), 1)
    print(digit_at_index(10,1), 0)
    print(digit_at_index(100, 0),1)
    print(digit_at_index(-100, 0),1)
    print(digit_at_index(-200, 0), 2)
    print(digit_at_index(-123, 2), 3)
    print(digit_at_index(987654321, 0), 9)
    print(digit_at_index(987654321, 5), 4)
    print(digit_at_index(987654321, 8), 1)

# R: beats 93%
# M: Beats 53%
# Solution from another user
def isPalindromeNoConversionReverseHalf(x: int) -> bool:
    print(f"{x}...")
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False

    reversed_x = 0
    while (x > reversed_x):
        reversed_x = floor(reversed_x * 10 + x % 10)
        x = floor(x / 10)

    print(f"...x:{x}, r:{reversed_x}")
    
    return x == reversed_x or x == floor(reversed_x / 10)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return isPalindromeNoConversionReverseHalf(x)

