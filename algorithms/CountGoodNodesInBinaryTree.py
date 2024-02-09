from typing import Optional

"""
Count Good Nodes in Binary Tree

whiteboard: https://app.excalidraw.com/s/ATbTqvQ19d9/9fsNrmWz3Dv
link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
difficulty: medium
date: 2024.02.09
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import sys
min_int = sys.maxsize * -1 - 1

"""
Approach - Recurive Walk Through Tree

- Runtime: beats 57%
- Memory: beats 63%
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      return self.good_nodes_helper(root, min_int)

    def good_nodes_helper(self, root: Optional[TreeNode], max_val_seen: int) -> int:
      if not root:
        return 0

      is_node_good = root.val >= max_val_seen
      new_max_val = max(root.val, max_val_seen)

      num_good_nodes_left = self.good_nodes_helper(root.left, new_max_val)
      num_good_nodes_right = self.good_nodes_helper(root.right, new_max_val)

      return num_good_nodes_left + num_good_nodes_right + (1 if is_node_good else 0)
