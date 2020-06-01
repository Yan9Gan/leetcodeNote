# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [0 for _ in prices]
        min_price = None
        for index, item in enumerate(prices):
            if index == 0:
                min_price = item
                continue

            dp[index] = max(item-min_price, item-prices[index])

            if item < min_price:
                min_price = item

        return max(dp)
