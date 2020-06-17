# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_score = 0
        pre_max = A[0]+0
        for i in range(1, len(A)):
            max_score = max(max_score, pre_max+A[i]-i)
            pre_max = max(pre_max, A[i]+i)

        return max_score
