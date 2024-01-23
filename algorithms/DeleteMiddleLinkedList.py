"""
Delete Middle of Linked List

author: adambechtold
link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
difficulty: Medium
date: 2024.01.23
"""


"""
Runtime: beats 97%
Memory: beats 98%
"""
def delete_middle_fast_and_slow(head: Optional[ListNode]):
    if not head:
        return head
    
    if not head.next:
        return None

    if not head.next.next:
        head.next = None
        return head

    slow_trail = head
    slow_runner = head.next
    fast_runner = head.next.next

    while fast_runner.next and fast_runner.next.next:
        slow_trail = slow_runner
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next


    if fast_runner.next:
        # slow_runner is right before the element to remove
        slow_runner.next = slow_runner.next.next
    else:
        #slow runner is the element to remove
        slow_trail.next = slow_runner.next

    return head 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return delete_middle_fast_and_slow(head)