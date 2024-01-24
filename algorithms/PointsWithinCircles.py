from typing import List

"""
author: adambechtold
interviewer: badr
date: 2024.01.24
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/5gnVVnTm4oU


# Problem
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.

## Example
Input: 
	- points = [[1,3],[3,3],[5,3],[2,2]]
  - queries = [[2,3,1],[4,3,1],[1,1,2]]
Output: [3,2,2]

Explanation: The points and circles are shown above.

queries[0] is the green circle
queries[1] is the red circle
and queries[2] is the blue circle.
"""

from math import sqrt

def get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
  diff_x = x2 - x1
  diff_y = y2 - y1
  distance = sqrt(pow(diff_x, 2), pow(diff_y, 2))
  return distance 

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
      
      output = []
      
      for query in queries:
        num_points_within_circle = 0
        center_x, center_y, radius = query
        
        for point in points:
          point_x, point_y = point
          distance = get_distance(point_x, point_y, center_x, center_y)
          if distance <= radius:
            num_points_within_circle += 1
          
        output.append(num_points_within_circle)
        
      return output
