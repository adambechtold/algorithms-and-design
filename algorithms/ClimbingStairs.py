from collections import defaultdict
"""
Climbing Stairs

author: adambechtold
date: 2024.02.01
difficulty: easy
link: https://leetcode.com/problems/climbing-stairs/
"""

"""
Approach - Iterative
- Runtime: 30 - beats 92%
- Memory: 17.32 - beats 14%
"""
def climbIter(n):
    if n <= 3:
        return n

    n1, n2 = 2, 3
    for i in range(3, n):
        tmp = n1 + n2
        n1 = n2
        n2 = tmp

    return n2

"""
Approach - Memoized Dynamic Programming
- Runtime: 35: beats 70%
- Memory: 17.21 beats: 17.21
"""
def climbStairsMemo(n: int, solutions) -> int:
    if n in solutions:
        return solutions[n]

    # Base Case
    if n <= 2:
        return n

    answer = climbStairsMemo(n - 1, solutions) + climbStairsMemo(n - 2, solutions)
    solutions[n] = answer
    return answer


class Solution:
    def climbStairs(self, n: int) -> int:
        # return climbStairsMemo(n, defaultdict(int))
        return climbIter(n)

"""
Scratchpad

Base Case
n = 0 → 0
n = 1 → 1

Stairs
1 2
^
"""
