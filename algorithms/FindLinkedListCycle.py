"""
Find Linked List Cycle

link: https://leetcode.com/problems/linked-list-cycle/
author: adambechtold
date: 2024.02.03
difficulty: easy
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: Beats 97%
# Memory: Beats 83%
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer, fast_pointer = head, head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True

        return False

