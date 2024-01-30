"""
Valid Parentheses

link: https://leetcode.com/problems/valid-parentheses/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/8y3JDb5sMZw
author: adambechtold
difficulty: easy


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


Runtime: beats 92
Memory: beats 92
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    pending_opens = []
    matching_char_lookup = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    open_chars = set([value for key, value in matching_char_lookup.items()])

    for c in s:
        if c in open_chars:
            pending_opens.append(c)
        else:
            if len(pending_opens) < 1:
                return False

            pending_open = pending_opens[-1]
            if matching_char_lookup[c] != pending_open:
                return False

            pending_opens.pop()

    return len(pending_opens) == 0

print(isValid('()[]{}'), True)
print(isValid('[(()])'), False)
print(isValid('[()]'), True)



