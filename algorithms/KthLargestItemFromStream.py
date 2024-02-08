from heapq import heappush, heappop, heapreplace
from typing import List

"""
Kth Largest Element from a Stream

author: adambechtold
date: 2024.02.08
link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/LZoRQUB9Ke
difficulty: easy
"""


"""
Approach - Maintain Min Heap of Large Numbers of Size K

- Runtime: beats 94%
- Memory: beats 78%
"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.max_heap_size = k

        for num in nums:
            if len(self.heap) < self.max_heap_size:
                heappush(self.heap, num)
            else:
                if self.heap[0] < num:
                    heapreplace(self.heap, num)

        return None


    def add(self, val: int) -> int:
        if len(self.heap) < self.max_heap_size:
            heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapreplace(self.heap, val)

        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
