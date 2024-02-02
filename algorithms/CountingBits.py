"""
Count Number of Bits

author: adambechtold
date: 2024.02.01
difficulty: easy
link: https://leetcode.com/problems/counting-bits/
"""

"""
Approach from Adam
- Runtime: Beats 54%
- Memory: Beats 67%
"""
def count_bits_adams(n):
    if n < 2:
        return [0] if n == 0  else [0,1]
    
    answer = [0,1]
    group = 1
    items_remaining = 2

    for i in range(2, n + 1):
        result = answer[i - pow(2, group)] + 1
        answer.append(result)
        items_remaining -= 1
        if items_remaining == 0:
            group += 1
            items_remaining = pow(2, group)

    return answer

class Solution:
    def countBits(self, n: int) -> List[int]:
        return count_bits_adams(n)

"""
Approach from Neetcode
- Runtime: beats 52%
- Memory: beats 80%
"""
def neetcode(n):
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp


"""
Scratchpad

# Problem


## Example 
Input: n = 8
Output: [0,1,1,2,1,2,2,3,1]
Explanation:
0 --> 0 
1 --> 1 
2 --> 10 
3 --> 11 
4 --> 100
5 --> 101
6 --> 110
7 --> 111
8 --> 1000
      1001
      1010
      1011
      1100
      1101
      1110
      1111
      1000

# Approaches
## Approach - Count 1s in each number

for i in range(n): # O(n)
    countBinary1s(i) # O(log(n))
"""