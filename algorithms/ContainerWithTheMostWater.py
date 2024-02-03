"""
Container with the Most Water

author: adambechtold
link: https://leetcode.com/problems/container-with-most-water/
difficulty: medium
"""

# Approach - Outside→In
# Runtime: beats 36%
# Memory: beats 63%
def max_area_outside_in(height: List[int]) -> int:
    left_i, right_i = 0, len(height) - 1
    max_area = 0

    while left_i < right_i:
        max_area = max(max_area, calc_area(left_i, right_i, height))

        if height[left_i] > height[right_i]:
            right_i -= 1
        else:
            left_i += 1
    
    return max_area

# Approach - View all valid areas
# Runtime: Timeout
def max_area_all_areas(height: List[int]) -> int:
    max_area = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)

    return max_area

def calc_area(left_wall_index: int, right_wall_index: int, height: List[int]) -> int:
        distance = right_wall_index - left_wall_index
        left_wall_height = height[left_wall_index]
        right_wall_height = height[right_wall_index]
        if distance < 0:
            raise ValueError('Distance between walls must be positive.')
        return min(left_wall_height, right_wall_height) * distance

# Walk from left to right, keeping the largest bucket sides
# ▼ Con - This does not keep track of large bucket walls in between
def max_area_left_to_right(height: List[int]) -> int:
    if len(height) < 2:
        raise ValueError("Provide at least two heights")

    max_left_wall = 0
    max_right_wall = 1
    max_area = calc_area(max_left_wall, max_right_wall, height)

    for i in range(1, len(height)):
        area_with_left = calc_area(max_left_wall, i, height)
        area_with_right = calc_area(max_right_wall, i, height)
        #print(f"i {i}, left_wall {max_left_wall}, right_wall: {max_right_wall}, l_a: {area_with_left}, r_a: {area_with_right}")

        if area_with_left > max_area:
            max_wall_right = i
        elif area_with_right > max_area:
            max_wall_left = max_wall_right
            max_wall_right = i
        else:
            continue
        max_area = max(max_area, area_with_left, area_with_right)
       # print(f"Max area after this check {max_area}")
        
    
    return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return max_area_outside_in(height)
