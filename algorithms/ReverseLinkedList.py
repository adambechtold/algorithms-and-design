"""
Reverse Linked List

author: adambechtold
date: 2024.02.07
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/LZoRQUB9Ke
link: https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse_list_recursive(head)

    """
    Approach - Iterative
    - Runtime: beats 70%
    - Memory: beats 93%
    """
    def reverse_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None

        while head:
            # save next node
            next_node = head.next

            # make head point back to its previous
            head.next = previous

            # advance previous
            previous = head

            # advance head
            if next_node == None:
                break
            else:
                head = next_node

        return head
    
    """
    Approach - Recursive
    - Runtime: Beats 28%
    - Memory: Beats 58%
    """
    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head, _ = self.reverse_list_recursive_helper(head)
        return reversed_head

    def reverse_list_recursive_helper(self, head: Optional[ListNode]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        if not head or not head.next:
            return head, head

        head_of_reversed_list, end_of_reversed_list = self.reverse_list_recursive_helper(head.next)
        end_of_reversed_list.next = ListNode(head.val)

        return head_of_reversed_list, end_of_reversed_list.next
