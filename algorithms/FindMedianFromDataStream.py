from heapq import heappush, heappop

"""
Find Median from Data Stream

author: adambechtold
difficulty: hard
date: 2024.01.30
link: https://leetcode.com/problems/find-median-from-data-stream/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/A2xhCqbevm6

"""

"""
Approach - High heap and low heap

Runtime: beats 77%
Memory: beats 81%
"""
class MedianFinder:
    def __init__(self):
        self.low_heap = [] # smaller half of numbers
        self.high_heap = [] # larger half of numbers. 
        #  len(low_heap) == len(high_heap) <= len(low_heap) + 1

    def addNum(self, num: int) -> None:
        if len(self.high_heap) > len(self.low_heap):
            # high_heap is larger, add to low_heap
            heappush(self.low_heap, -num)
        else:
            # high_heap is equal size or smaller
            heappush(self.high_heap, num)

        # rebalance heaps
        if len(self.low_heap) > 0 and len(self.high_heap) > 0:
            largest_of_small_numbers = -self.low_heap[0]
            smallest_of_large_numbers = self.high_heap[0]

            if largest_of_small_numbers > smallest_of_large_numbers:
                heappop(self.high_heap)
                heappop(self.low_heap)
                heappush(self.low_heap, -smallest_of_large_numbers)
                heappush(self.high_heap, largest_of_small_numbers)


    def findMedian(self) -> float:
        #print(f"find median: state of vals: {self.vals}")
        if len(self.high_heap) > len(self.low_heap):
            return self.high_heap[0]
        else:
            return (self.high_heap[0] + -self.low_heap[0]) / 2

"""
Approach - Track in Array

Runtime: Timeout

class MedianFinder:
    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        self.vals.append(num)

        for i in range(len(self.vals) - 1, 0, -1):
            #print(f'i: {i}')
            if self.vals[i] > self.vals[i - 1]:
                tmp = self.vals[i-1]
                self.vals[i-1] = self.vals[i]
                self.vals[i] = tmp
            else:
                break
        

    def findMedian(self) -> float:
        #print(f"find median: state of vals: {self.vals}")
        if len(self.vals) % 2 == 1:
            return self.vals[int(len(self.vals) / 2)]
        else:
            high_median_i = int(len(self.vals) / 2)
            low_median_i = high_median_i - 1
            total = self.vals[high_median_i] + self.vals[low_median_i]
            return total / 2
"""


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()