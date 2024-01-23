"""
Longest Common Prefix

author: adambechtold
date: 2024.01.23
link: https://leetcode.com/problems/longest-common-prefix/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/8UZTjQCc7dg
difficulty: easy
"""

"""
Runtime: beats 85%
 - O(n * l)
    - n = number of strings
    - l = length of the strings
Memory: beats 60%
O(n*l)
"""
def longest_prefix(strs):
    if len(strs) < 1:
        return ""
    
    common_prefix = strs[0]

    for i in range(1, len(strs)):
        next_str = strs[i]
        j = 0

        # count how many chars in this string are the same
        # as the common prefix
        while (j < len(next_str) and j < len(common_prefix)): 
            if next_str[j] == common_prefix[j]:
                j += 1
            else:
                break
        
        # shorten the common prefix if neccessary
        if j > 0:
            common_prefix = common_prefix[:j]
        else:
            # if there are no common characters
            return ""

    # all strings have been checked
    return common_prefix

"""
Runtime: beats 60%
    - O(l * nlog(n))
        - n = number of strings
        - l = length of strings
Memory: beats 56%
"""
def longest_prefix_sort(strs):
    strs = strs.sorted()

    first = strs[0]
    last = strs[len(strs) - 1]

    common_prefix = ""
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            break
        common_prefix += first[i]

    return common_prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return longest_prefix(strs)
        