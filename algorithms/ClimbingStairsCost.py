from collections import defaultdict
from typing import List

"""
Climbing Stairs Cost

author: adambechtold
date: 2024.02.01
link: https://leetcode.com/problems/min-cost-climbing-stairs/
difficulty: easy
"""


"""
Approach - Memoized DP
- Runtime: 131ms - beats 5%
- Memory: 21 - beats 5%
"""
def minCostMemo(costs, costs_lookup):
    n = len(costs)
    if n in costs_lookup:
        return costs_lookup[n]

    if n <= 1:
        return 0
    if n == 2:
        return min(costs[0], costs[1])

    cost_1_step = costs[0] + minCostMemo(costs[1:], costs_lookup)
    cost_2_step = costs[1] + minCostMemo(costs[2:], costs_lookup)
    answer = min(cost_1_step, cost_2_step)
    costs_lookup[n] = answer
    return answer

"""
Approach - Iterative
- Runtime: 112 - beats 5%
- Memory: 21 - beats 5%
"""
def minCostIter(costs):
    l = len(costs)
    if l <= 1:
        return 0
    if l == 2:
        return min(costs[0], costs[1])

    c1 = costs[l - 1]
    c2 = costs[l - 2]

    # Example
    for i in reversed(range(0, l - 2)):
        tmp = min(costs[i] + c1, c2, costs[i] + c2)
        c1 = c2
        c2 = tmp

    return c2

"""
Approach - Neetcode's approach
- Runtime: 53 - 87%
- Memory: 17.6 - 17%
"""
def minCostNeet(cost):
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return minCostIter(cost)
