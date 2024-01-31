from typing import List

"""
Fair Candy Swap

link: https://leetcode.com/problems/fair-candy-swap/
difficulty: easy
author: adambechtold
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/2gV0BQ48Szj

Runtime: Beats 99%
Memory: Beats 45%
"""

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # 1) Find the average number of candies
        bobSum = sum(bobSizes)
        aliceSum = sum(aliceSizes)
        fairTotalFloat = (bobSum + aliceSum) / 2
        fairTotal = int(fairTotalFloat)
        
        if fairTotalFloat != fairTotal:
            raise ValueError(f'A fair exchange is not possible. The average number, {fairTotalFloat}, is not an integer.')

        # 2) Determine the target difference
        netChangeAlice = fairTotal - aliceSum

        # 3) Create a set of bob's candy sizes
        bobSizesLookup = set(bobSizes)

        # 4) For each of alice's boxes...
        for aliceSize in aliceSizes:
            # ... use the set to see if bob has a box that will result in the desired net change
            sizeNeededForFairExchange = aliceSize + netChangeAlice
            if sizeNeededForFairExchange in bobSizesLookup:
                return [aliceSize, sizeNeededForFairExchange]

        raise ValueError(f'A fair exchange was not possible. We needed a net change of {netChangeAlice} for Alice, and {-netChangeAlice} for Bob. This could not be found in their sizes.')


"""
# Problem Description

Alice and Bob have a different total number of candies. 
You are given two integer arrays aliceSizes and bobSizes 
where aliceSizes[i] is the number of candies of the 
ith box of candy that Alice has and bobSizes[j] is the 
number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each 
so that after the exchange, they both have the same total amount of candy. 
The total amount of candy a person has is the sum of the number of candies 
in each box they have.

Return an integer array answer where answer[0] is the number of candies 
in the box that Alice must exchange, and answer[1] is the number of candies 
in the box that Bob must exchange. If there are multiple answers, you may 
return any one of them. It is guaranteed that at least one answer exists.


Example 1:

Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]
Example 2:

Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]
Example 3:

Input: aliceSizes = [2], bobSizes = [1,3]
Output: [2,3]
"""