# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        max_area = 0
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                curr_index = stack.pop()
                max_area = max(max_area, (index-stack[-1]-1)*heights[curr_index])
            stack.append(index)

        return max_area
