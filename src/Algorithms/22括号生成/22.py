# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res_list = list()
        temp_str = ''
        self.core_func(n, n, temp_str, res_list)

        return res_list

    def core_func(self, left, right, res, res_list):
        if left == 0 and right == 0:
            res_list.append(res)
            return

        if right < left:
            return
        if left > 0:
            self.core_func(left-1, right, res+'(', res_list)
        if right > 0:
            self.core_func(left, right-1, res+')', res_list)
