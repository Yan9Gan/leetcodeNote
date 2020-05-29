# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for j in i] for i in grid]
        for row, i in enumerate(grid):
            for column, j in enumerate(i):
                if row == 0:
                    dp[row][column] = sum(grid[row][:column+1])
                if column == 0 and row != 0:
                    dp[row][column] = grid[row][column] + dp[row-1][column]

        for row in range(1, len(grid)):
            for column in range(1, len(grid[row])):
                dp[row][column] = grid[row][column] + min(dp[row-1][column], dp[row][column-1])

        return dp[-1][-1]
