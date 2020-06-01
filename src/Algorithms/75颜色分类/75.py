# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_list = [0] * 3
        for num in nums:
            count_list[num] += 1
        print(count_list)
        for index, count in enumerate(count_list):
            for i in range(count):
                nums[sum(count_list[:index])+i] = index
