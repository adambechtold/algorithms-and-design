"""
Middle of a Linked List

author: adambechtold
date: 2024.01.21
difficulty: easy
link: https://leetcode.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow_runner, fast_runner = head.next, head.next.next

        while fast_runner and fast_runner.next:
            slow_runner, fast_runner = slow_runner.next, fast_runner.next.next

        return slow_runner
