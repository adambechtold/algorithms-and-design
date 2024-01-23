from collections import defaultdict
from typing import List

"""
K Most Frequent Items

link: https://leetcode.com/problems/top-k-frequent-elements/
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/2NcOmJytqtl
author: adambechtold
date: 2024.01.23
"""

PRINT_TESTS = False

"""
Approach - Count Elements, Order elements in an array based on their frequency
Runtime: beats 63%
Memory: beats 20%
"""
def k_most_frequent_items_placement(nums: List[int], k: int) -> List[int]:
    # 1 - count elements
    num_count = defaultdict(int)
    for num in nums:
        num_count[num] += 1

    nums_by_count = [[] for i in range(len(nums) + 1)]
    for num, count in num_count.items():
        nums_by_count[count].append(num)

    most_frequent_nums = []

    for i in range(len(nums_by_count) - 1, 0, -1):
        if len(nums_by_count[i]) > 0:
            for num in nums_by_count[i]:
                most_frequent_nums.append(num)
        if len(most_frequent_nums) >= k:
            break

    return most_frequent_nums

"""
Approach - Count Elements, Return Highest Counts by Sorting

Runtime: beats 75%
    - O(n*log(n) * k)
Memory: beats 95%
    - O(n)
"""
def k_most_frequent_items_sort(nums: List[int], k: int) -> List[int]:
    # 1 - count elements
    num_count = defaultdict(int) 
    for num in nums: # R: O(n)   S: O(n)
        num_count[num] += 1
    
    # 2 - find k highest value counts0
    k_highest = [[num, count] for num, count in num_count.items()] # R: O(n) S: O(n)
    k_highest.sort(key=lambda x: x[1], reverse=True) # R: O(n log(n))

    return [x[0] for x in k_highest[:k]] # R: O(k)


"""
Approach - Count Element, Return the highest element by scanning through, tracking the highest k elements
Runtime: beats 5%
    - I thought this was O(n + k), but it runs very slow. It does iterate through n 3 times
Memory: beats 70%
"""
class NumCount:
    # count: int
    # num: int

    def __init__(self, num: int, count: int):
        self.count = count
        self.num = num

    def __eq__(self, other):
        if isinstance(other, NumCount):
            return self.count == other.count
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, NumCount):
            return self.count > other.count
        return False

    def __ge__(self, other):
        if isinstance(other, NumCount):
            return self.count >= other.count
        return False
    
    def __lt__(self, other):
        if isinstance(other, NumCount):
            return self.count < other.count
        return False

    def __le__(self, other):
        if isinstance(other, NumCount):
            return self.count <= other.count
        return False

    def __str__(self):
        return f"({self.num}: {self.count})"
    
    def __repr__(self):
        return self.__str__()

if PRINT_TESTS:
    print(f"My num count {NumCount(0, 1)}")
    print(f"My list of num counts {[NumCount(1,1), NumCount(1,2)]}")


def insert_if_greater(sorted_counts: List[NumCount], new_count: NumCount):
    min_count = sorted_counts[-1]
    if new_count <= min_count:
        return None

    # replace min with the new count
    sorted_counts[-1] = new_count

    # insert num into sorted_counts
    new_count_index = len(sorted_counts) - 1
    while new_count_index > 0:
        next_value = sorted_counts[new_count_index - 1]
        if next_value < new_count:
            # swap
            sorted_counts[new_count_index] = next_value
            sorted_counts[new_count_index - 1] = new_count
            new_count_index -= 1
        else:
            break
    
    return None

if PRINT_TESTS:
    sorted_counts = [NumCount(n, c) for [n, c] in [[1,5],[2,3]]]
    insert_if_greater(sorted_counts, NumCount(4,1))
    print(sorted_counts)
    insert_if_greater(sorted_counts, NumCount(10,10))
    print(sorted_counts)


def k_most_frequent_items_scan(nums: List[int], k: int) -> List[int]:
    # 1 - count element
    num_count = defaultdict(int)
    for num in nums:
        num_count[num] += 1

    # 2 - Find the k highest counts
    num_counts = [NumCount(value, count) for value, count in num_count.items()]
    k_highest_counts = [NumCount(0, 0)] * k

    for num_count in num_counts:
        insert_if_greater(k_highest_counts, num_count)

    return [num_count.num for num_count in k_highest_counts]

if PRINT_TESTS:
    items = [1]
    print(k_most_frequent_items_scan(items, 1))
    items = [1, 1, 2]
    print(k_most_frequent_items_scan(items, 1))
    items = [2, 2, 1]
    print(k_most_frequent_items_scan(items, 1))
    items = [1,1,1,2,2,3]
    print(k_most_frequent_items_scan(items, 2))


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return k_most_frequent_items_placement(nums, k)
    
