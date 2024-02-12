from typing import Optional

"""
Invert Binary Tree

link: https://leetcode.com/problems/invert-binary-tree/
author: adambechtold
date: 2024.02.12
difficulty: easy
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)

        root.left = inverted_right
        root.right = inverted_left

        return root

"""
Approach - Recursive

- Runtime: beats 50%   O(n)
- Memory: beats 65%    O(n)

- Base Case - Empty
    return Empty

1) Invert the left tree and invert the right tree
2) Add the inverted left to the right and the inverted right to the left
return this node
"""
        