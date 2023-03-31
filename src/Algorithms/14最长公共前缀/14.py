# -*- coding: utf-8 -*-
# @Time: 2023/3/31 15:59
# @Author: yanggan

class Solution:
    @staticmethod
    def longest_common_prefix(strs: list[str]) -> str:
        if not strs:
            return ""
        min_str = min(strs)
        max_str = max(strs)
        for i, s in enumerate(min_str):
            if max_str[i] != s:
                return min_str[:i]
        return min_str


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    res = Solution.longest_common_prefix(strs)
    print(res)
