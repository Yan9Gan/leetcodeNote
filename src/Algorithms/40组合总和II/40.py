# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def core_func(candidate_list, res, res_list):
            for index, item in enumerate(candidate_list):
                if item > target:
                    continue

                if sum(res)+item == target:
                    if res+[item] not in res_list:
                        res_list.append(res+[item])
                    return

                if sum(res)+item < target:
                    core_func(candidate_list[index+1:], res+[item], res_list)
                else:
                    return

        res_list = list()
        res = list()
        core_func(candidates, res, res_list)
        return res_list


if __name__ == '__main__':
    S = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = S.combinationSum2(candidates, target)
    print(res)
