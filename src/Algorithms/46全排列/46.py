# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = list()
        res = list()
        self.core(nums, curr, res)

        return res

    def core(self, nums, curr, res):
        if len(nums) == 0:
            if curr not in res:
                res.append(curr)
            return

        for i in range(len(nums)):
            self.core(nums[:i]+nums[i+1:], curr+[nums[i]], res)


if __name__ == '__main__':
    S = Solution()
    nums = [1, 2, 3]
    res = S.permute(nums)
    print(res)

