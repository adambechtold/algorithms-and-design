from typing import Optional

"""
I misunderstood the reverse linked list II problem and thought it was just a swap nodes problem. 
This worked for that, so I figured I'll keep it.

date: 2024.02.20
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/1Ctg7M4p4b8
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        l_i, l_node, l_trail = 1, head, None
        r_i, r_node, r_trail = 2, head.next, head

        while (l_i < left):
            l_i += 1
            l_trail = l_node
            l_node = l_node.next

        while (r_i < right):
            r_i += 1
            r_trail = r_node
            r_node = r_node.next

        # Swap position of l_node and r_node
        ## 1) get reference for the next values of both nodes
        l_node_next = l_node.next
        r_node_next = r_node.next

        ## 2) update the next node for each node
        ### the left node now points towards whatever is after the right node
        l_node.next = r_node_next 
        ### the right node points towards whatever is after the left
        ### unless that was the right node, in which case, the next node is the left node
        r_node.next = l_node_next if not (right - left) == 1 else l_node

        ## 3) update the nodes before the left and right target nodes
        if l_trail:
            ### if we have advanced the l_trail, it now points to the right node
            l_trail.next = r_node
        else:
            ### update the head. l_node was the head, so now r_node is
            head = r_node

        if not (right - left) == 1:
            ### the node that was before r_node now points to l_node, 
            ### since this replaced r_node
            r_trail.next = l_node

        return head

