# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        temp_list = [[0 for j in i] for i in obstacleGrid]

        for row_index in range(len(obstacleGrid)):
            for column_index, item in enumerate(obstacleGrid[row_index]):
                if item == 1:
                    temp_list[row_index][column_index] = 0
                else:
                    if row_index == 0:
                        if column_index > 0 and temp_list[row_index][column_index-1] == 0:
                            temp_list[row_index][column_index] = 0
                        else:
                            temp_list[row_index][column_index] = 1
                    if column_index == 0:
                        if row_index > 0 and temp_list[row_index-1][column_index] == 0:
                            temp_list[row_index][column_index] = 0
                        else:
                            temp_list[row_index][column_index] = 1
                    if row_index != 0 and column_index != 0:
                        temp_list[row_index][column_index] = temp_list[row_index-1][column_index] + temp_list[row_index][column_index-1]

        return temp_list[-1][-1]


if __name__ == '__main__':
    S = Solution()
    obstacleGrid = [[1, 0]]
    res = S.uniquePathsWithObstacles(obstacleGrid)
    print(res)
