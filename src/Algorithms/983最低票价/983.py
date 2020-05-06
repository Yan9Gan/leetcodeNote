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
