# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in T]
        stack = list()
        for index, item in enumerate(T):
            while stack and item > T[stack[-1]]:
                temp = stack.pop()
                res[temp] = index - temp
            stack.append(index)

        return res
