# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        stack = [0] * (days[-1]+1)
        for i in range(days[-1]+1):
            if i == 0:
                continue

            if i in days:
                stack[i] = min(stack[max(0, i-1)]+costs[0], stack[max(0, i-7)]+costs[1], stack[max(0, i-30)]+costs[2])
            else:
                stack[i] = stack[i-1]

        return stack[-1]


if __name__ == '__main__':
    S = Solution()
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    res = S.mincostTickets(days, costs)
    print(res)
