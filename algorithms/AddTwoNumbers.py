import math
from typing import Optional

"""
Add Two Numbers

author: adambechtold
date: 2024.02.08
difficulty: medium
link: https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add_two_numbers_recursive(l1, l2, 0)

    """
    Approach - Iterative

    - Runtime: beats 50%
    - Memory: beats 50%
    """
    def add_two_nums_recursive(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        l1_pointer, l2_pointer = l1, l2
        result, result_tail = None, None

        def get_ones_place(num: int) -> int:
            return num % 10

        def get_tens_place(num: int) -> int:
            return 1 if num > 0 and math.log10(num) >= 1 else 0

        def append_to_list(tail: ListNode, new_node: ListNode):
            tail.next = new_node
            tail = new_node

        carry = 0
        while l1_pointer and l2_pointer:
            curr_sum = l1_pointer.val + l2_pointer.val + carry
            ones_place = get_ones_place(curr_sum)
            carry = get_tens_place(curr_sum)

            new_node = ListNode(ones_place)

            if not result:
                result, result_tail = new_node, new_node
            else:
                append_to_list(result_tail, new_node)

        while l1_pointer:
            curr_sum = l1_pointer.val + carry
            new_node = ListNode(get_ones_place(curr_sum))
            carry = get_tens_place(curr_sum)
            append_to_list(result_tail, new_node)

        while l2_pointer:
            curr_sum = l2_pointer.val + carry
            new_node = ListNode(get_ones_place(curr_sum))
            carry = get_tens_place(curr_sum)
            append_to_list(result_tail, new_node)

        return result



    """
    Approach - Recursive: Pass Carry Forward

    - Runtime: beats 25%
    - Memory: beats 65%
    """
    def add_two_numbers_recursive(self, l1: Optional[ListNode], l2: Optional[ListNode], carry_val: int) -> Optional[ListNode]:
        if not l1 and not l2:
            return ListNode(1) if carry_val > 0 else None

        value = None
        next_l1 = None
        next_l2 = None
        if not l1:
            value = l2.val + carry_val
            next_l2 = l2.next
        elif not l2:
            value = l1.val + carry_val
            next_l1 = l1.next
        else:
            value = l1.val + l2.val + carry_val
            next_l1 = l1.next
            next_l2 = l2.next

        ones_place = value % 10
        tens_place = 1 if value != 0 and math.log10(value) >= 1 else 0

        this_node = ListNode(ones_place)
        this_node.next = self.add_two_numbers_recursive(next_l1, next_l2, tens_place)
        return this_node
