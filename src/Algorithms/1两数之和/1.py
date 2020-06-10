# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        while index < len(nums):
            temp = target - nums[index]
            if temp in nums[index+1:]:
                return [index, index+1+nums[index+1:].index(temp)]
            index += 1


if __name__ == '__main__':
    S = Solution()
    nums = [3, 2, 4]
    target = 6
    res = S.twoSum(nums, target)
    print(res)
