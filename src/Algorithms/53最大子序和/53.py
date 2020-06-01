# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for index, item in enumerate(nums[1:]):
            if item+dp[index] >= item:
                dp[index+1] = item+dp[index]
            else:
                dp[index+1] = item

        return max(dp)
