from typing import Optional
from collections import namedtuple, deque

"""
Maximum Depth of Binary Tree

link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth_iter_bfs_slow(root)


    """
    Approach - Recursive

    - Runtime: beats 36%
    - Memory: beats 79%
    """
    def max_depth_recursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.max_depth_recursive(root.left), self.max_depth_recursive(root.right))

    """
    Approach - Iterative DFS

    - Runtime - beats 20%
    - Memory - beats 94%
    """
    def max_depth_iter_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        DepthNode = namedtuple("DepthNode", ["left", "right", "depth"])
        stack = [DepthNode(root.left, root.right, 1)]
        max_depth = 1

        while len(stack) > 0:
            node = stack.pop()
            depth = node.depth
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append(
                    DepthNode(
                        node.left.left,
                        node.left.right,
                        depth + 1
                    )
                )
            if node.right:
                stack.append(
                    DepthNode(
                        node.right.left,
                        node.right.right,
                        depth + 1
                    )
                )

        return max_depth

    """
    Approach - Iterative BFS with Depth Node

    - Runtime: beats 66%
    - Memory: beats 63%
    """
    def max_depth_iter_bfs_depth_node(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        DepthNode = namedtuple("DepthNode", ["left", "right", "depth"])
        queue = deque()
        queue.append(DepthNode(root.left, root.right, 1))
        max_depth = 0

        while len(queue) > 0:
            node = queue.popleft()
            depth = node.depth
            max_depth = max(max_depth, depth)

            if node.left:
                queue.append(
                    DepthNode(
                        node.left.left,
                        node.left.right,
                        depth + 1
                    )
                )
            if node.right:
                queue.append(
                    DepthNode(
                        node.right.left,
                        node.right.right,
                        depth + 1
                    )
                )

        return max_depth

    """
    Approach - Iterative BFS tracking depth

    - Runtime: beats 98%
    - Memory: beats 94%
    """
    def max_depth_iter_bfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        curr_depth = 0

        while len(queue) > 0:
            curr_depth += 1

            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return curr_depth