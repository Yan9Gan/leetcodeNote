# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] >= target:
                return idx
            else:
                idx += 1

        return len(nums)
