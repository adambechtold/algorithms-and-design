from math import floor
"""
Number of 1 Bits

author: adambechtold
difficulty: easy
link: https://leetcode.com/problems/number-of-1-bits/
"""

"""
Approach - Shift
- Runtime: 33 - beats 87%
- Memory: 17.4 - beats 10%
"""
def hamming_weight_shift(n: int) -> int:
    count = 0
    while n > 0:
        count += n % 2
        n = n >> 1
    return count

"""
Approach - Floor
- Runtime: 44 - beats 22
- Memory: 17.4 - beats 10%
"""
def hamming_weight_floor(n: int) -> int:
    count = 0
    while n > 0:
        count += n %2
        n = floor(n / 2)
    return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        return hamming_weight_shift(n)

        
        

"""
Scratchpad

Hamming wieght...

## Examples
001101 → 3
001000 → 1
111110 → 5

# Approach - Count and Shift

count = 0
tmp = copy(n)
while tmp > 0:
    count += tmp % 2
    tmp / 2

return count

1 | 001101 → count++
2 |  00110
3 |   0011 → count++
4 |    001 → count++
5 |     00
6 |      0


### Example
Input: 11 (01011)
1 | 11 % 2 = 1  and 11 / 2 = 5
2 | 5 % 2 = 1 and 5 / 2 = 2
3 | 2 % 2 = 0 and 2 / 2 = 1
4 | 1 % 2 = 1 and 1 / 2 = 0
"""