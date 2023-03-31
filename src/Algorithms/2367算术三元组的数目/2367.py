# -*- coding: utf-8 -*-
# @Time: 2023/3/31 15:24
# @Author: yanggan

class Solution:
    @staticmethod
    def arithmetic_triplets(nums: list[int], diff: int) -> int:
        total = 0
        s = set()
        for num in nums:
            if num - diff in s and num - diff * 2 in s:
                total += 1
            s.add(num)
        return total


if __name__ == '__main__':
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    res = Solution.arithmetic_triplets(nums, diff)
    print(res)
