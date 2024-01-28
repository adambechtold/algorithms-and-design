"""
Longest Substring without Repeating Characters

author: adambechtold
difficulty: Medium
link: https://leetcode.com/problems/longest-substring-without-repeating-characters/


Given a string s, find the length of the longest 
substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


"""
Approach - Copy the current substring

Runtime: Beats 24%
Memory: Beats 55%
"""
def lengthOfLongestSubstringCopy(s: str) -> int:
    longest_substring = ""
    char_position_lookup = {}

    left_i, right_i = 0, 0
    curr_substring = ""

    while right_i < len(s):
        c = s[right_i]

        if c in char_position_lookup:
            if len(curr_substring) > len(longest_substring):
                longest_substring = curr_substring

            previous_i_of_c = char_position_lookup[c]

            while left_i <= previous_i_of_c:
                char_position_lookup.pop(s[left_i])
                left_i += 1
            left_i = previous_i_of_c + 1

            curr_substring = s[left_i : right_i + 1]
        else:
            curr_substring = s[left_i : right_i + 1]
            if len(curr_substring) > len(longest_substring):
                longest_substring = curr_substring

        char_position_lookup[c] = right_i
        right_i += 1

    return len(longest_substring)

"""
Track the indices of the longest substring
- Rationale - This avoids the overhead of string copies

Runtime: Beats 24%
Memory: Beats 55%

Lesson - Consider the amount of time actually spend on operation to update the current substring.

I thought that this would be faster because it removes the operations to copy the string. However,
the overall amount of time does not change.

# Explanatation from ChatGPT
However, this does not necessarily mean that the overall time complexity of the function is worse than O(n), where n is the length of the input string s.
The reason is that while the substring operations are O(k),
the sum of all k's over the course of the entire function is bounded by n, the length of the original string.
In each iteration of the while loop, a substring of length k is created,
but each character from the original string is part of such a substring at most once.

Therefore, while these operations are not constant time and depend on the size of the substring,
the total time spent on substring operations across all iterations of the loop is still O(n).
As a result, the overall time complexity of the lengthOfLongestSubstringCopy function remains O(n).
"""
def lengthOfLongestSubstringTrackIndicies(s: str) -> int:
    if len(s) == 0:
        return 0

    longest_left_i, longest_right_i = 0, 0
    left_i, right_i = 0, 0

    def length_of_longest_substring():
        return (longest_right_i - longest_left_i) + 1

    def length_of_curr_substring():
        return (right_i - left_i) + 1

    char_position_lookup = {}

    while right_i < len(s):
        c = s[right_i]

        if c in char_position_lookup:
            if length_of_curr_substring() > length_of_longest_substring():
                longest_left_i = left_i
                longest_right_i = right_i - 1

            previous_i_of_c = char_position_lookup[c]

            while left_i <= previous_i_of_c:
                char_position_lookup.pop(s[left_i])
                left_i += 1
            left_i = previous_i_of_c + 1

        else:
            if length_of_curr_substring() > length_of_longest_substring():
                longest_left_i = left_i
                longest_right_i = right_i

        char_position_lookup[c] = right_i
        right_i += 1

    return length_of_longest_substring()


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return lengthOfLongestSubstringTrackIndicies(s)
