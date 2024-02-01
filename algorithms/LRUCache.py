from typing import Optional

"""
Design LRU Cache

author: adambechtold
link: https://leetcode.com/problems/lru-cache/
difficulty: medium
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/fISzrI9sul
date: 2024.01.31
"""

"""
Approach - Doubly Linked Recency List

Runtime: beats 58%
Memory: beats 55%


Use 3 data structures

- A doubly linked list of keys
- A map of key to their node in the linked list
- A map of keys to their current value

The doubly linked list makes it possible to move any item to the the front and
"shift" the location of all other keys in O(1)
"""

class ListNode:
    def __init__(self, value: int, prevNode: Optional['ListNode'] = None, nextNode: Optional['ListNode'] = None):
        self.value = value
        self.prev = prevNode
        self.next = nextNode

class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.node_map = {}

        self.recency_list_head = None 
        self.recency_list_tail = None

        self.capacity = capacity


    def get(self, key: int) -> int:
        if not key in self.map:
            return -1
        else:
            self.push_to_front(key)
        
        # get value and return it
        return self.map[key]


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            self.push_to_front(key)
            return None
        
        # If at capacity, remove tail key
        if len(self.map) == self.capacity:
            # Remove tail node from linked list
            tail_node = self.recency_list_tail
            if tail_node.prev:
                tail_node.prev.next = None
                self.recency_list_tail = tail_node.prev
            
            # Remove key from node_map and map
            self.node_map.pop(tail_node.value, None)
            self.map.pop(tail_node.value, None)
            
        # Add the new key/value to the cache
        new_node = ListNode(key)

        # Add new node to the head of the list
        new_node.next = self.recency_list_head

        if self.recency_list_head:
            # have the previous head point back to this new node
            self.recency_list_head.prev = new_node
        
        self.recency_list_head = new_node

        # Add as the tail if list is empty
        if len(self.node_map) == 0:
            self.recency_list_tail = new_node

        # Add new node to node map
        self.node_map[key] = new_node

        # Add k and value to map
        self.map[key] = value

    """
    Push to Front

    Move this key to the front of the recency list
    """
    def push_to_front(self, key: int):
        if key not in self.node_map:
            raise ValueError(f"{key} not found in node map")

        # reorder key access recency list
        key_node = self.node_map[key]

        # if head, do nothing
        if not key_node.prev:
            pass
        else:
            key_node.prev.next = key_node.next
            if key_node.next:
                key_node.next.prev = key_node.prev
            else:
                # the key_node is the tail
                if key_node.prev:
                    # make the previous node the tail
                    self.recency_list_tail = key_node.prev
                else:
                    # there is no previous node, so keep the key_node as the tail
                    pass

            # move key_node to the head
            head = self.recency_list_head
            key_node.next = head
            key_node.prev = None
            head.prev = key_node
            self.recency_list_head = key_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Problem

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""