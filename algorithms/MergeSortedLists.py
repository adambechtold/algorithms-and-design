from typing import Optional
"""
Merge Sorted Lists

author: adambechtold
date: 2024.02.07
difficulty: easy
link: https://leetcode.com/problems/merge-two-sorted-lists/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/LZoRQUB9Ke
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_lists_recursive(list1, list2)

    """
    Approach - Recursive
    - Runtime: beats 70%
    - Memory: beats 70%
    """
    def merge_lists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            sorted_rest = self.merge_lists_recursive(list1.next, list2)
            list1.next = sorted_rest
            return list1
        else:
            sorted_rest = self.merge_lists_recursive(list1, list2.next)
            list2.next = sorted_rest
            return list2


    """
    Approach - Iterative
    - Runtime: beats 38%
    - Memory: beats 70%
    """
    def merge_lists_iterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create two pointers
        pointer_1, pointer_2 = list1, list2

        # if either is empty, we can simply return the other
        if not pointer_1:
            return pointer_2
        if not pointer_2:
            return pointer_1

        # choose which has our starting node
        head, end = None, None
        if pointer_1.val < pointer_2.val:
            # pointer_1 is lower, so its first node will be our head
            head = pointer_1
            pointer_1 = pointer_1.next
        else:
            # pointer_2 is lower, so its first node will be our head
            head = pointer_2
            pointer_2 = pointer_2.next
        end = head # our list is just one element long
        head.next = end


        # while both pointers are nodes...
        while pointer_1 and pointer_2:
            if pointer_1.val < pointer_2.val:
                # ...if pointer_1 is lower, add it onto the end
                end.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                #...if pointer_2 is lower, add it onto the end
                end.next = pointer_2
                pointer_2 = pointer_2.next
            end = end.next

        # one of these pointers has reached its end
        # complete the merged list with the remaining values from the other list
        if not pointer_1:
            end.next = pointer_2
        else:
            end.next = pointer_1

        return head
