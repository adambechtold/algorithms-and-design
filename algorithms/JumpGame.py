"""
Jump Game

author: adambechtold
link: https://leetcode.com/problems/jump-game/
difficulty: medium

Runtime - Beats 85%
Memory - beats 69%
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        1) start at the end
        2) closest point that can reach end, is the end
        3) Step one step away from the end, 
            can that point reach the closest point that can reach the end?
            if yes, this is the new closest point that can reach the end
            else, do not update the closet point
        Repeat step 3 until you reach the start
        """
        closest_point_that_can_reach_end = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            max_i_from_here = i + nums[i]

            if max_i_from_here >= closest_point_that_can_reach_end:
                closest_point_that_can_reach_end = i

        return closest_point_that_can_reach_end == 0