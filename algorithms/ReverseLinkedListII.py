"""
Reversed Linked List II

date: 2024.02.20
link: https://leetcode.com/problems/reverse-linked-list-ii
difficulty: medium
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/1Ctg7M4p4b8
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Runtime - beats 80%
    # Memory - beats 80%
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head


        l_i, l_node, l_trail = 1, head, None

        # 1) advance to the left node
        while (l_i < left):
            l_i += 1
            l_trail = l_node
            l_node = l_node.next

        # 2) build the reversed section
        reversed_tail = l_node
        reversed_head = l_node
        curr_i, curr_node = l_i, l_node
        next_node = curr_node.next

        while (curr_i < right):
            # keep track of the previous node
            prev_node = curr_node 

            # advance the current node and the next node by one
            curr_i += 1
            curr_node, next_node = next_node, next_node.next

            # the current node points to the previous node
            curr_node.next = prev_node

            # the current node is the start of the reversed portion
            reversed_head = curr_node

        # 3) "insert" the reversed portion in to the list
        reversed_tail.next = next_node

        if l_trail:
            l_trail.next = reversed_head
        else:
            head = reversed_head

        return head
    