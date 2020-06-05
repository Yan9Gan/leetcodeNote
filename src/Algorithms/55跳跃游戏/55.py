# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True

        flag = False
        jump_count = nums[0]
        for index, num in enumerate(nums[:-1]):
            if jump_count <= 0 and num <= 0:
                break

            if len(nums)-1-index <= num:
                flag = True
                break

            if num > jump_count:
                jump_count = num

            jump_count -= 1

        return flag


if __name__ == '__main__':
    S = Solution()
    nums = [5, 4, 0, 2, 0, 1, 0, 1, 0]
    flag = S.canJump(nums)
    print(flag)
