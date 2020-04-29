# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res_list = list()
        res = list()
        candidates.sort()

        def core_func(res):
            for item in candidates:
                if sum(res)+item < target:
                    core_func(res + [item])
                elif sum(res) + item == target:
                    temp = res + [item]
                    temp.sort()
                    if temp not in res_list:
                        res_list.append(temp)
                else:
                    return

        core_func(res)
        return res_list


if __name__ == '__main__':
    S = Solution()
    candidates = [8, 7, 4, 3]
    target = 11
    res = S.combinationSum(candidates, target)
    print(res)
