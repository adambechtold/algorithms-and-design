import sys

"""
Jump Game II

author: adambechtold
difficulty: medium
link: https://leetcode.com/problems/jump-game-ii/
date: 2024.02.03
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.jump_track_min(nums)

    # Runtime - beats 34%
    # Memory - beats 61%
    def jump_track_min(self, nums: List[int]) -> int:
        """
        1) Start at the end
            min_num_jumps = [...0]
        2) Take one step away from the end
            min_num_jumps[here] = 1 + min(min_num_jumps[here:])
        3) repeat step 2
            TODO: can we store the min jump number so we don't have to look at all previous steps?
        4) return min_num_jumps[0]
        """
        min_num_jumps = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            max_jump_distance = nums[i]
            jumpable_locations = min_num_jumps[(i + 1):(i + max_jump_distance + 1)]

            if len(jumpable_locations) != 0:
                min_num_jumps[i] = 1 + min(jumpable_locations)
            else:
                min_num_jumps[i] = sys.maxsize

        return min_num_jumps[0]