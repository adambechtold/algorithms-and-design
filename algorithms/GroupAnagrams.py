"""
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

author: adambechtold
link: https://leetcode.com/problems/group-anagrams/
date: 2024.01.23
"""

from collections import defaultdict

RUN_TESTS = False

def count_chars(s):
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1

    return count

if RUN_TESTS:
    print(count_chars("a"))
    print(count_chars("abc"))
    print(count_chars("aabbcd"))

def group_anagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        char_count = count_chars(s)
        groups[tuple(char_count)].append(s)

    return [group for key, group in groups.items()]


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        return group_anagrams(strs)
