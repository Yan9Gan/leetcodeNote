# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        out_list = [matrix[0][0]]
        idx_list = [(0, 0)]
        row = 0
        column = 0
        turn = 'right'
        count = 0

        while 1:
            if count >= 2:
                break

            if turn == 'right':
                if column != len(matrix[row]) - 1 and (row, column + 1) not in idx_list:
                    out_list.append(matrix[row][column + 1])
                    idx_list.append((row, column + 1))
                    column += 1
                    count = 0
                else:
                    turn = 'down'
                    count += 1

            if turn == 'down':
                if row != len(matrix) - 1 and (row + 1, column) not in idx_list:
                    out_list.append(matrix[row + 1][column])
                    idx_list.append((row + 1, column))
                    row += 1
                    count = 0
                else:
                    turn = 'left'
                    count += 1

            if turn == 'left':
                if column != 0 and (row, column - 1) not in idx_list:
                    out_list.append(matrix[row][column - 1])
                    idx_list.append((row, column - 1))
                    column -= 1
                    count = 0
                else:
                    turn = 'up'
                    count += 1

            if turn == 'up':
                if row != 0 and (row - 1, column) not in idx_list:
                    out_list.append(matrix[row - 1][column])
                    idx_list.append((row - 1, column))
                    row -= 1
                    count = 0
                else:
                    turn = 'right'
                    count += 1

        return out_list
