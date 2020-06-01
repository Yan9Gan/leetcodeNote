# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if not candies:
            return []

        flag_list = list()
        max_candies = max(candies)
        for item in candies:
            if item+extraCandies >= max_candies:
                flag_list.append(True)
            else:
                flag_list.append(False)

        return flag_list
