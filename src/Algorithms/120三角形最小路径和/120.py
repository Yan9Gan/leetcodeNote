# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for _ in i] for i in triangle]
        dp[0][0] = triangle[0][0]
        for row, row_item in enumerate(triangle):
            if row == 0:
                continue
            for column, item in enumerate(row_item):
                if column == 0:  # 第一个
                    dp[row][column] = dp[row-1][column] + item
                elif column == len(row_item)-1:  # 最后一个
                    dp[row][column] = dp[row-1][column-1] + item
                else:
                    dp[row][column] = min(dp[row-1][column-1], dp[row-1][column]) + item

        return min(dp[-1])

"""
[
    [2],
    [5, 6],
    [11, 10, 13],
    [15, 11, 18, 16]
]
"""
