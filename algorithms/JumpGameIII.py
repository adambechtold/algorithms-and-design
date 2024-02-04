"""
Jump Game III

author: adambechtold
difficulty: medium
link: https://leetcode.com/problems/jump-game-iii/
date: 2024.02.03
"""

class Solution:
    def __init__(self):
        self.visited = set([])

    def canReach(self, arr: List[int], start: int) -> bool:
        return self.can_reach_recurisive(arr, start)

    def can_reach_recursive(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        elif start in self.visited:
            return False
        else:
            self.visited.add(start)
            jump_back = start - arr[start]
            jump_ahead = start + arr[start]

            valid_jump_locations = []
            if jump_back >= 0:
                valid_jump_locations.append(jump_back)
            if jump_ahead < len(arr):
                valid_jump_locations.append(jump_ahead)

            return any([self.can_reach_recursive(arr, jl) for jl in valid_jump_locations])

    def can_reach_dfs(self, arr: List[int], start: int) -> bool:
        visited = set()
        n = len(arr)

        def dfs(i):
            if i in visited:
                return False
            if i < 0 or i >=n:
                return False

            if arr[i] == 0:
                return True

            visited.add(i)

            return dfs(i+arr[i]) or dfs(i-arr[i])

            # h = i + arr[i]
            # if h not in visited:
            #     if 0 <= h < n:
            #         return dfs(h)
            
            # l = i - arr[i]
            # if l not in visited:
            #     if 0 <= l < n:
            #         return dfs(l)

        if dfs(start):
            return True

        return False

"""
Approach - Backtrack from Zero

1) Find zero index
2) scan all nums
    can they reach 0?
    mark as true
3) repeat until your reach the start index or all ar marked true 

Approach - Follow links and track seen

1) start at the start
2) if start is 0
    # mark position in array as true (or 0)
    #   ❓ Question - can we modify the array 
    return true
3) Find all valid jump locations
    return true if any of these locations can reach 0
"""