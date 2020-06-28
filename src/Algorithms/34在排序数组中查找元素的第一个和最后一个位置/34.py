# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx_list = [-1, -1]
        first = 0
        last = len(nums)-1
        while 1:
            if last < first:
                break

            mid = (first+last)//2
            if nums[mid] == target:
                idx_list = [mid, mid]
                break
            elif nums[mid] < target:
                first = mid+1
            else:
                last = mid-1

        for i in range(idx_list[0]-1, -1, -1):
            if nums[i] == target:
                idx_list[0] -= 1
            else:
                break
        for i in range(idx_list[1]+1, len(nums), 1):
            if nums[i] == target:
                idx_list[1] += 1
            else:
                break

        return idx_list
