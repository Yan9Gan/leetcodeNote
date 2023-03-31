# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i, num in enumerate(nums):
            if target - num in hash:
                return [hash[target-num], i]
            hash[num] = i
        return []


if __name__ == '__main__':
    S = Solution()
    nums = [3, 2, 4]
    target = 6
    res = S.twoSum(nums, target)
    print(res)
